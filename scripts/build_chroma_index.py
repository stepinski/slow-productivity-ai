# scripts/build_chroma_index.py
import os
import json
import glob
from typing import List, Dict, Any
import chromadb
from chromadb.config import Settings
from llama_index import VectorStoreIndex, Document
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.llms import Ollama
from llama_index import ServiceContext

def load_enhanced_notes(vault_path: str) -> List[Document]:
    """Load all enhanced markdown notes from the vault."""
    print(f"Loading notes from {vault_path}...")
    
    notes = []
    for filepath in glob.glob(f"{vault_path}/**/*.md", recursive=True):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse frontmatter
            metadata = {}
            if content.startswith("---"):
                end_idx = content[3:].find("---") + 6
                frontmatter_str = content[3:end_idx-3].strip()
                main_content = content[end_idx:].strip()
                
                # Extract frontmatter as metadata
                for line in frontmatter_str.split("\n"):
                    if ":" in line:
                        key, value = line.split(":", 1)
                        metadata[key.strip()] = value.strip()
            else:
                main_content = content
            
            # Add file path and name to metadata
            metadata["filepath"] = filepath
            metadata["filename"] = os.path.basename(filepath)
            
            # Use relative path to organize notes in PARA structure
            rel_path = os.path.relpath(filepath, vault_path)
            parts = os.path.split(rel_path)
            if len(parts) > 0:
                metadata["folder"] = parts[0]
            
            # Create document with metadata
            doc = Document(
                text=main_content,
                metadata=metadata,
                id=os.path.relpath(filepath, vault_path)
            )
            notes.append(doc)
            
        except Exception as e:
            print(f"Error loading {filepath}: {str(e)}")
    
    print(f"Loaded {len(notes)} notes")
    return notes

def build_chroma_index(config: Dict[str, Any]) -> None:
    """Build a ChromaDB index from the notes."""
    vault_path = config["obsidian_vault_path"]
    db_path = config.get("chroma_db_path", "./indices/chroma_db")
    
    # Create directory if it doesn't exist
    os.makedirs(db_path, exist_ok=True)
    
    # Load documents
    documents = load_enhanced_notes(vault_path)
    
    # Initialize ChromaDB
    print(f"Initializing ChromaDB at {db_path}...")
    client = chromadb.PersistentClient(path=db_path, settings=Settings(anonymized_telemetry=False))
    
    # Get or create collection
    collection_name = "obsidian_notes"
    try:
        chroma_collection = client.get_collection(collection_name)
        print(f"Found existing collection '{collection_name}'")
    except:
        chroma_collection = client.create_collection(collection_name)
        print(f"Created new collection '{collection_name}'")
    
    # Create vector store
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    # Initialize embedding model - using HuggingFace for better quality
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    
    # Initialize LLM
    llm = Ollama(model=config["llm_model"], url=config["llm_url"])
    
    # Create service context
    service_context = ServiceContext.from_defaults(
        llm=llm,
        embed_model=embed_model
    )
    
    print("Building index...")
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        service_context=service_context,
    )
    
    print(f"Index built successfully with {len(documents)} documents")
    
    # Save config for retrieval
    index_config = {
        "chroma_collection": collection_name,
        "chroma_db_path": db_path,
        "document_count": len(documents),
        "build_time": datetime.now().isoformat()
    }
    
    with open(os.path.join(db_path, "index_config.json"), "w") as f:
        json.dump(index_config, f, indent=2)
    
    print("Index configuration saved")
    
if __name__ == "__main__":
    import argparse
    from datetime import datetime
    
    parser = argparse.ArgumentParser(description="Build ChromaDB index for enhanced notes")
    parser.add_argument("--config", default="config/settings.json", help="Path to config file")
    args = parser.parse_args()
    
    # Load config
    with open(args.config, "r") as f:
        config = json.load(f)
    
    # Add ChromaDB path if not present
    if "chroma_db_path" not in config:
        config["chroma_db_path"] = "./indices/chroma_db"
    
    # Build index
    build_chroma_index(config)
