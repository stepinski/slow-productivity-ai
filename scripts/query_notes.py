import os
import sys
import json
import logging
import argparse
from llama_index.core import Settings, StorageContext, load_index_from_storage
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core.prompts import PromptTemplate

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("llama_index")
logger.setLevel(logging.INFO)

# Load configuration
with open("config/settings.json", "r") as f:
    config = json.load(f)

# Set paths from configuration
INDEX_DIR = config["index_dir"]

def load_index():
    """Load the existing index from storage"""
    print(f"Loading index from {INDEX_DIR}...")
    
    # Check if index directory exists
    if not os.path.exists(INDEX_DIR):
        print(f"Error: Index directory {INDEX_DIR} does not exist. Run the indexing script first.")
        sys.exit(1)
    
    try:
        # Configure Ollama models
        embed_model = OllamaEmbedding(model_name=config["llm_model"], url=config["llm_url"])
        llm = Ollama(model=config["llm_model"], url=config["llm_url"])
        
        # Set global settings (instead of ServiceContext)
        Settings.embed_model = embed_model
        Settings.llm = llm
        
        # Load the index from the storage
        storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
        index = load_index_from_storage(storage_context)
        
        print("Index loaded successfully!")
        return index
    
    except Exception as e:
        print(f"Error loading index: {e}")
        sys.exit(1)

def query_index(index, query_text, top_k=5, show_sources=True):
    """Query the index with the given text"""
    try:
        print(f"Querying index with: '{query_text}'")
        
        # Create custom RAG prompt template
        rag_prompt_tmpl = PromptTemplate(
            """\
You are a helpful AI assistant with access to a knowledge base of personal notes.
Human query: {query_str}
The following context information from the knowledge base might be helpful:
{context_str}
When answering:
1. First consider what the user is asking for
2. Carefully review the provided context
3. Formulate a clear, helpful response based on the context
4. If the context doesn't contain relevant information, acknowledge this limitation
5. Format your response in a clean, readable way
Your response:
"""
        )
        
        # Create query engine with custom prompt
        query_engine = index.as_query_engine(
            text_qa_template=rag_prompt_tmpl,
            similarity_top_k=top_k
        )
        
        # Execute query
        response = query_engine.query(query_text)
        
        print("\n===== RESPONSE =====")
        print(response)
        
        # Only show sources if requested
        if show_sources:
            print("\n===== SOURCE DOCUMENTS =====")
            
            if hasattr(response, "source_nodes"):
                for i, source_node in enumerate(response.source_nodes):
                    print(f"\n--- SOURCE {i+1} ---")
                    print(f"Source: {source_node.node.metadata.get('file_path', 'Unknown')}")
                    print(f"Relevance: {source_node.score:.4f}")
                    print(f"Content: {source_node.node.get_content()[:300]}...")
            else:
                print("No source documents available")
            
        return response
    
    except Exception as e:
        print(f"Error querying index: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Query your Obsidian vault using natural language")
    parser.add_argument("query", nargs="*", help="The query text")
    parser.add_argument("--top-k", type=int, default=5, help="Number of results to return")
    parser.add_argument("--no-sources", action="store_true", help="Hide source documents in output")
    args = parser.parse_args()
    
    # Load the index
    index = load_index()
    
    if not args.query:
        # Interactive mode
        print("Enter your queries (type 'exit' to quit):")
        while True:
            query_text = input("\nQuery: ")
            if query_text.lower() in ("exit", "quit", "q"):
                break
            query_index(index, query_text, args.top_k, not args.no_sources)
    else:
        # Single query mode
        query_text = " ".join(args.query)
        query_index(index, query_text, args.top_k, not args.no_sources)

if __name__ == "__main__":
    main()
