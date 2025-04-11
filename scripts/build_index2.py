import os
import sys
import json
from tqdm import tqdm
import logging
from llama_index.core import Settings
from llama_index.core.indices import VectorStoreIndex
# Import necessary components from llama_index
# from llama_index import VectorStoreIndex, Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
# from llama_index.readers.file import SimpleDirectoryReader

from llama_index.core import SimpleDirectoryReader
# Load configuration
with open("config/settings.json", "r") as f:
    config = json.load(f)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("llama_index")
logger.setLevel(logging.INFO)

# Set paths from configuration
OBSIDIAN_PATH = config["obsidian_vault_path"]
INDEX_DIR = config["index_dir"]

def create_index():
    print("Building index from Obsidian vault...")
    # Check if Obsidian path exists
    if not os.path.exists(OBSIDIAN_PATH):
        print(f"Error: Obsidian vault path {OBSIDIAN_PATH} does not exist")
        sys.exit(1)
        
    # Load documents from Obsidian vault
    documents = SimpleDirectoryReader(OBSIDIAN_PATH, recursive=True).load_data()
    print(f"Loaded {len(documents)} documents")
    
    # Configure Ollama models
    embed_model = OllamaEmbedding(model_name=config["llm_model"], url=config["llm_url"])
    llm = Ollama(model=config["llm_model"], url=config["llm_url"])
    
    # Set global settings
    Settings.embed_model = embed_model
    Settings.llm = llm
    
    # Process documents in batches for better visibility
    batch_size = 20
    total_batches = (len(documents) - 1) // batch_size + 1
    
    # Initialize overall progress bar
    with tqdm(total=total_batches, desc="Overall progress") as pbar:
        indices = []
        
        # Process document batches
        for i in range(0, len(documents), batch_size):
            batch = documents[i:i+batch_size]
            batch_num = i//batch_size + 1
            end_idx = min(i+batch_size, len(documents))
            
            print(f"\nProcessing batch {batch_num}/{total_batches} (documents {i+1}-{end_idx} of {len(documents)})")
            
            # Create mini-index for this batch
            try:
                batch_index = VectorStoreIndex.from_documents(batch)
                indices.append(batch_index)
                print(f"✓ Completed batch {batch_num}")
            except Exception as e:
                print(f"Error processing batch {batch_num}: {e}")
            
            # Update overall progress
            pbar.update(1)
    
    # Combine all mini-indices if we processed in batches
    if len(indices) == 1:
        index = indices[0]
    else:
        print("\nMerging all indices...")
        try:
            # Try different merging approaches based on the llama_index version
            try:
                # Newer versions
                index = VectorStoreIndex.from_indices(indices)
            except (AttributeError, TypeError):
                # If that doesn't work, try concatenating the documents
                all_nodes = []
                for idx in indices:
                    all_nodes.extend(idx.docstore.get_all_nodes())
                index = VectorStoreIndex(all_nodes)
        except Exception as e:
            print(f"Error merging indices: {e}")
            # Just use the first index as a fallback
            index = indices[0]
            print("Using only the first batch as the index")
    
    # Create directory if it doesn't exist
    if not os.path.exists(INDEX_DIR):
        os.makedirs(INDEX_DIR)
    
    # Save the index
    print(f"\nSaving index to {INDEX_DIR}")
    index.storage_context.persist(persist_dir=INDEX_DIR)
    
    print("Indexing completed successfully!")
    return index

if __name__ == "__main__":
    create_index()
