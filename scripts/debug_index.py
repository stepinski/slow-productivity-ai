# scripts/debug_index.py
import json
import os
import sys
from llama_index.core.readers import SimpleDirectoryReader
# Load config
with open("config/settings.json", "r") as f:
    config = json.load(f)

OBSIDIAN_PATH = config["obsidian_vault_path"]

def debug_index():
    print(f"Checking Obsidian vault at {OBSIDIAN_PATH}...")
    
    # Check if path exists
    if not os.path.exists(OBSIDIAN_PATH):
        print(f"Error: Obsidian vault path {OBSIDIAN_PATH} does not exist")
        sys.exit(1)
    
    # List all markdown files
    md_files = []
    for root, dirs, files in os.walk(OBSIDIAN_PATH):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    print(f"Found {len(md_files)} markdown files")
    
    # Try to load documents
    documents = SimpleDirectoryReader(OBSIDIAN_PATH, recursive=True).load_data()
    print(f"Successfully loaded {len(documents)} documents")
    
    # Print sample content from the first few documents
    for i, doc in enumerate(documents[:3]):
        print(f"\nDocument {i+1} sample:")
        print("-" * 50)
        print(doc.text[:300] + "...")
        print("-" * 50)

if __name__ == "__main__":
    debug_index()
