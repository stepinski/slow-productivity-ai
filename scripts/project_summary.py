import json
import os
import sys
import datetime
import logging
import numpy as np
from llama_index.core import Settings, StorageContext, load_index_from_storage
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core.prompts import PromptTemplate

# Configure logging for detailed error messages
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("llama_index")
logger.setLevel(logging.INFO)

# Load config
with open("config/settings.json", "r") as f:
    config = json.load(f)
INDEX_DIR = config["index_dir"]

def generate_project_summary():
    # Check if index exists
    if not os.path.exists(INDEX_DIR):
        print(f"Error: Index not found at {INDEX_DIR}. Please build it first.")
        sys.exit(1)
        
    print("Generating project summary...")
    
    try:
        # Configure Ollama models with increased timeout values
        embed_model = OllamaEmbedding(
            model_name=config["llm_model"], 
            url=config["llm_url"],
            request_timeout=60.0  # Increase timeout to 60 seconds
        )
        
        llm = Ollama(
            model=config["llm_model"], 
            url=config["llm_url"],
            request_timeout=120.0  # Increase timeout to 120 seconds
        )
        
        # Set global settings
        Settings.embed_model = embed_model
        Settings.llm = llm
        
        # Check if Ollama is responding
        print("Testing connection to Ollama service...")
        try:
            # Try a simple completion to test connection
            test_response = llm.complete("Hello")
            print("Successfully connected to Ollama service!")
        except Exception as e:
            print(f"Error connecting to Ollama service: {e}")
            print("Please check if Ollama is running at the configured URL")
            print(f"Configured URL: {config['llm_url']}")
            print("You may need to start the Ollama service or check network connectivity")
            sys.exit(1)
            
        # Load the index from storage
        print("Loading index from storage...")
        storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
        index = load_index_from_storage(storage_context)
        print("Index loaded successfully!")
        
        # Sample basic document content
        print("Sampling documents from index...")
        nodes = list(index.docstore.docs.values())
        sample_size = min(5, len(nodes))
        sample_nodes = nodes[:sample_size]
        
        # Create a direct prompt with document samples
        prompt = f"""
You are a helpful AI assistant tasked with creating a project status report.
I need you to create a comprehensive project status report based on my notes.
Here's what I need in the report:
1. ACTIVE PROJECTS: List all currently active projects with brief descriptions
2. PRIORITY TASKS: Identify high-priority unfinished tasks across all projects
3. BLOCKED ITEMS: Note any tasks or projects that appear to be blocked or delayed
4. RECENT ACCOMPLISHMENTS: Summarize recently completed milestones or tasks
5. UPCOMING DEADLINES: List any approaching deadlines mentioned in the notes

When creating this report:
- Think step-by-step about the information in my notes
- Only include projects and tasks actually mentioned in my notes
- If item from my notes is a scientific document or definition it's most probably a source document not related to tasks due dates but rather potentaial source to look for solutions so don't include them in projects summary
- Format the report as a clean, well-structured markdown document
- Use headings, bullet points, and emphasis to improve readability

Today's date: {datetime.datetime.now().strftime("%Y-%m-%d")}

Here are some samples from my notes to help you understand my projects:

"""
        
        # Add sample content
        for i, node in enumerate(sample_nodes):
            if hasattr(node, 'text'):
                content = node.text[:1000]  # Take first 1000 chars
            else:
                content = str(node)[:1000]  # Take first 1000 chars
            prompt += f"--- DOCUMENT {i+1} ---\n{content}\n\n"
            
        prompt += "\nCreate the project status report based on the information above:"
        
        # Send direct query to LLM with increased timeout
        print("Sending query to Ollama (this might take some time)...")
        response = llm.complete(prompt)
        
        # Format as markdown
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        markdown_output = f"""# Project Status Summary
Generated: {today}

{str(response)}
"""
        
        # Create directory for summaries if it doesn't exist
        os.makedirs("data/summaries", exist_ok=True)
        
        # Save to file
        output_file = f"data/summaries/project_summary_{today}.md"
        with open(output_file, "w") as f:
            f.write(markdown_output)
        
        print(f"Project summary saved to {output_file}")
        return output_file
        
    except Exception as e:
        print(f"Error generating project summary: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    generate_project_summary()
