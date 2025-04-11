#!/usr/bin/env python3
# scripts/query_notes.py
import json
import os
import sys

from llama_index.storage_context import StorageContext
from llama_index import load_index_from_storage, ServiceContext
from llama_index.prompts import PromptTemplate
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings

# Load config
with open("config/settings.json", "r") as f:
    config = json.load(f)

INDEX_DIR = config["index_dir"]

def query_index(query_text):
    # Check if index exists
    if not os.path.exists(INDEX_DIR):
        print(f"Error: Index not found at {INDEX_DIR}. Please build it first.")
        sys.exit(1)
        
    print(f"Querying: '{query_text}'")
    
    # Connect to Ollama
    llm = Ollama(model=config["llm_model"], url=config["llm_url"])
    service_context = ServiceContext.from_defaults(llm=llm)
    
    # Settings.llm = llm
    # Load index
    storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
    index = load_index_from_storage(storage_context, service_context=service_context)
    
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
        similarity_top_k=5
    )
    
    # Query
    response = query_engine.query(query_text)
    return str(response)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python query_notes.py 'your query here'")
        sys.exit(1)
    
    query = sys.argv[1]
    result = query_index(query)
    print("\nResponse:")
    print(result)
