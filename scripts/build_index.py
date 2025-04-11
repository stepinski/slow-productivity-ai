# scripts/build_index.py
import json
import os
import sys
# from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
# from llama_index.llms import Ollama

from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_index.embeddings.ollama import OllamaEmbedding

# from tqdm import tqdm
from llama_index.core.callbacks import CallbackManager#, TqdmProgressBarCallback
# from llama_index.core.service_context import ServiceContext
# Initialize progress bar callback
# callback_manager = CallbackManager([TqdmCallbackHandler()])

# Create ServiceContext with callback
# service_context = ServiceContext.from_defaults(callback_manager=callback_manager)

# Load config
with open("config/settings.json", "r") as f:
    config = json.load(f)

embed_model = OllamaEmbedding(model_name=config["llm_model"], url=config["llm_url"])  # Replace with your model
Settings.embed_model = embed_model  # Set the embedding model

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
    
    # Connect to Ollama
    llm = Ollama(model=config["llm_model"], url=config["llm_url"])
    
    Settings.llm = llm
    # Create service context
    # service_context = ServiceContext.from_defaults(llm=llm)
    # Assuming `documents` is a list
    # documents = list(tqdm(documents, desc="Processing Documents"))

    # Create callback manager with TqdmProgressBarCallback for progress tracking
    # callback_manager = CallbackManager([TqdmProgressBarCallback()])
    
    # Create service context with the callback manager
    # service_context = ServiceContext.from_defaults(
        # llm=llm,
        # embed_model=embed_model,
        # callback_manager=callback_manager
    # )
    
    # Create and save index with the service context
    # index = VectorStoreIndex.from_documents(
        # documents,
        # service_context=service_context,
        # show_progress=True  # Explicitly enable progress display
    # )
    
    # Save the index if needed
    # if not os.path.exists(INDEX_DIR):
        # os.makedirs(INDEX_DIR)
    # index.storage_context.persist(persist_dir=INDEX_DIR)

    # Create and save index
    # index = VectorStoreIndex.from_documents(documents,service_context=service_context)
    # Import the base callback handler
    from llama_index.core.callbacks import CallbackManager
    from llama_index.core.callbacks.base import BaseCallbackHandler
    
    # Set up tqdm for batch processing
    from tqdm import tqdm
    
    # Process documents in smaller batches for visible progress
    batch_size = 20
    total_batches = (len(documents) - 1) // batch_size + 1
    
    # Create a progress bar for batch processing
    with tqdm(total=total_batches, desc="Processing document batches") as pbar:
        all_indices = []
        
        # Process documents in batches to show progress
        for i in range(0, len(documents), batch_size):
            batch = documents[i:i+batch_size]
            batch_num = i//batch_size + 1
            
            # Create a sub-index for this batch
            print(f"\nProcessing batch {batch_num} ({i+1}-{min(i+batch_size, len(documents))} of {len(documents)} documents)")
            batch_index = VectorStoreIndex.from_documents(
                batch,
                show_progress=True  # Try to enable any built-in progress reporting
            )
            all_indices.append(batch_index)
            pbar.update(1)
    
    # Combine indices if needed (or just use the last one if it's cumulative)
    if len(all_indices) == 1:
        index = all_indices[0]
    else:
        # If you have multiple indices, you might need to merge them
        # For newer versions:
        from llama_index.core.indices.vector_store import VectorStoreIndex
        index = VectorStoreIndex.from_indices(all_indices)
    
    # class TqdmCallbackHandler(BaseCallbackHandler):
    #     """Callback handler for tqdm progress bar."""
    # Create a custom callback handler with tqdm
    # class TqdmCallbackHandler(BaseCallbackHandler):
    #     """Callback handler for tqdm progress bar."""
    #
    #     def __init__(self):
    #         event_starts_to_ignore = []
    #         event_ends_to_ignore = []
    #         super().__init__(event_starts_to_ignore, event_ends_to_ignore)
    #         self.pbar = None
    #         self.total_embedding_calls = 0
    #         # super().__init__()
    #
    #     def on_event_start(self, event_type, payload=None, event_id=None, **kwargs):
    #         if event_type == "embed":
    #             if self.pbar is None:
    #                 # Initialize progress bar on first embedding call
    #                 self.pbar = tqdm(desc="Embedding documents", unit=" chunks")
    #             self.total_embedding_calls += 1
    #             self.pbar.update(1)
    #
    #     def on_event_end(self, event_type, payload=None, event_id=None, **kwargs):
    #         pass
    #     def start_trace(self, trace_id=None):
    #         # Implement required abstract method
    #         pass
    #
    #     def end_trace(self, trace_id=None, trace_map=None):
    #         # Implement required abstract method
    #         pass           
    #     def close(self):
    #         if self.pbar is not None:
    #             self.pbar.close()
    #
    # # Create callback manager with our custom handler
    # callback_manager = CallbackManager([TqdmCallbackHandler()])
    #
    # # Create service context with the callback manager
    # service_context = ServiceContext.from_defaults(
    #     llm=llm,
    #     embed_model=embed_model,
    #     callback_manager=callback_manager
    # )
    #
    # # Create and save index with the service context
    # print("Starting indexing process...")
    # index = VectorStoreIndex.from_documents(
    #     documents,
    #     service_context=service_context
    # )
    #
    print("testing") 
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(INDEX_DIR), exist_ok=True)
    
    # Save index
    index.storage_context.persist(INDEX_DIR)
    print(f"Index created successfully at {INDEX_DIR}")
    return index

if __name__ == "__main__":
    create_index()
