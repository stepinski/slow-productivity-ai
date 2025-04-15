# scripts/chroma_query.py
import os
import json
import chromadb
from chromadb.config import Settings
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index import VectorStoreIndex
from llama_index.llms import Ollama
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index import ServiceContext
from llama_index.prompts import PromptTemplate

def load_chroma_index(config):
    """Load the ChromaDB index."""
    db_path = config.get("chroma_db_path", "./indices/chroma_db")
    
    # Initialize ChromaDB
    client = chromadb.PersistentClient(path=db_path, settings=Settings(anonymized_telemetry=False))
    
    # Get collection
    collection_name = "obsidian_notes"
    chroma_collection = client.get_collection(collection_name)
    
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
    
    # Load index
    index = VectorStoreIndex.from_vector_store(
        vector_store,
        service_context=service_context,
    )
    
    return index

def advanced_query(config, query_text, filter_dict=None, top_k=10):
    """Query the ChromaDB index with filters."""
    index = load_chroma_index(config)
    
    # Create metadata filter if specified
    metadata_filter = None
    if filter_dict:
        metadata_filter = lambda meta: all(
            meta.get(k) == v for k, v in filter_dict.items()
        )
    
    # Create PromptTemplate for better responses
    query_prompt = PromptTemplate(
        """You are an assistant helping with knowledge retrieval from a personal notes vault.
        
        The notes are structured with metadata including:
        - para_category: Projects, Areas, Resources, Archives
        - type: project, task, reference, etc.
        - status: active, completed, on-hold, etc.
        - priority: high, medium, low
        - timeline_position: beginning, middle, end, completed
        
        User query: {query_str}
        
        Relevant information from the notes:
        {context_str}
        
        Provide a comprehensive answer that directly addresses the query.
        Organize your response clearly with appropriate headings and structure.
        If the context doesn't contain relevant information, acknowledge this limitation.
        """
    )
    
    # Create query engine
    query_engine = index.as_query_engine(
        text_qa_template=query_prompt,
        similarity_top_k=top_k,
        vector_store_query_mode="default",
        metadata_filter=metadata_filter,
    )
    
    # Execute query
    response = query_engine.query(query_text)
    
    return str(response)

def query_by_category(config, category, query_text="", top_k=10):
    """Query only notes in a specific PARA category."""
    filter_dict = {"para_category": category}
    
    if not query_text:
        if category == "Projects":
            query_text = "Summarize all active projects and their tasks"
        elif category == "Areas":
            query_text = "Summarize the key areas of responsibility and their current status"
        elif category == "Resources":
            query_text = "Provide an overview of the key resources and knowledge"
        elif category == "Archives":
            query_text = "Summarize the completed projects and archived information"
    
    return advanced_query(config, query_text, filter_dict, top_k)

def query_projects_timeline(config):
    """Generate a timeline view of projects."""
    query_text = """
    Create a comprehensive timeline of all projects.
    For each project:
    1. Identify the start date and due date
    2. Determine the current status and phase
    3. List key milestones and tasks
    4. Note any dependencies between projects
    
    Organize the timeline chronologically, grouping related projects together.
    """
    
    return advanced_query(
        config, 
        query_text, 
        filter_dict={"para_category": "Projects"}, 
        top_k=30
    )

def generate_project_summary(config):
    """Generate a comprehensive project summary."""
    query_text = """
    Create a detailed project status report with the following sections:
    
    1. ACTIVE PROJECTS:
       - List each project with status and timeline position
       - Include start dates and deadlines
       - Note the priority level
    
    2. PRIORITY TASKS:
       - List high-priority tasks across all projects
       - Group by project and timeline position
       - Include deadlines for urgent items
    
    3. BLOCKED ITEMS:
       - Identify any tasks or projects that appear to be blocked
       - Note dependencies and potential solutions
    
    4. RECENT ACCOMPLISHMENTS:
       - List recently completed tasks and milestones
       - Organized by project
    
    5. UPCOMING DEADLINES:
       - List deadlines in chronological order
       - Include both project and task deadlines
       - Highlight items due in the next 7 days
    
    Format this as a well-structured markdown document with clear headings and organization.
    """
    
    return advanced_query(config, query_text, top_k=30)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Query ChromaDB indexed notes")
    parser.add_argument("--query", help="Custom query to run")
    parser.add_argument("--category", choices=["Projects", "Areas", "Resources", "Archives"],
                        help="Query only notes in this PARA category")
    parser.add_argument("--timeline", action="store_true", help="Generate project timeline")
    parser.add_argument("--summary", action="store_true", help="Generate project summary")
    parser.add_argument("--config", default="config/settings.json", help="Path to config file")
    parser.add_argument("--top-k", type=int, default=10, help="Number of results to consider")
    args = parser.parse_args()
    
    # Load config
    with open(args.config, "r") as f:
        config = json.load(f)
    
    # Handle command
    if args.timeline:
        result = query_projects_timeline(config)
    elif args.summary:
        result = generate_project_summary(config)
    elif args.category:
        result = query_by_category(config, args.category, args.query, args.top_k)
    elif args.query:
        result = advanced_query(config, args.query, top_k=args.top_k)
    else:
        parser.print_help()
        exit(1)
    
    # Print result
    print(result)
