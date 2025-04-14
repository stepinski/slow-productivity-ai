# scripts/enhance_with_timeline.py
import os
import re
import glob
import shutil
import subprocess
from datetime import datetime
from llama_index.llms import Ollama

class TimelineEnhancer:
    def __init__(self, vault_path, model="llama3:8b"):
        self.vault_path = vault_path
        self.llm = Ollama(model=model)
        self.stats = {
            "processed": 0,
            "enhanced": 0,
            "with_dates": 0,
            "errors": 0
        }
        
        # Ensure PARA folders exist
        self.para_folders = {
            "Projects": os.path.join(vault_path, "Projects"),
            "Areas": os.path.join(vault_path, "Areas"),
            "Resources": os.path.join(vault_path, "Resources"),
            "Archives": os.path.join(vault_path, "Archives")
        }
        
        for folder in self.para_folders.values():
            os.makedirs(folder, exist_ok=True)
    
    def extract_date_from_filename(self, filename):
        """Extract date from filename patterns like YYYY-MM-DD or YYYYMMDD."""
        # Pattern for YYYY-MM-DD
        pattern1 = r'(\d{4}-\d{2}-\d{2})'
        # Pattern for YYYYMMDD
        pattern2 = r'(\d{4})(\d{2})(\d{2})'
        
        match = re.search(pattern1, filename)
        if match:
            return match.group(1)
        
        match = re.search(pattern2, filename)
        if match:
            return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
        
        return None
    
    def get_git_dates(self, filepath):
        """Get git creation and modification dates for a file."""
        git_dates = {
            "git_created": None,
            "git_modified": None
        }
        
        try:
            # Check if file is in a git repository
            result = subprocess.run(
                ["git", "rev-parse", "--is-inside-work-tree"],
                cwd=os.path.dirname(filepath),
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0 or result.stdout.strip() != "true":
                return git_dates
            
            # Get first commit date (creation)
            result = subprocess.run(
                ["git", "log", "--follow", "--format=%ad", "--date=short", "--reverse", filepath],
                cwd=self.vault_path,
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0 and result.stdout.strip():
                git_dates["git_created"] = result.stdout.strip().split('\n')[0]
            
            # Get latest commit date (modification)
            result = subprocess.run(
                ["git", "log", "-1", "--format=%ad", "--date=short", filepath],
                cwd=self.vault_path,
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0 and result.stdout.strip():
                git_dates["git_modified"] = result.stdout.strip()
                
        except Exception as e:
            print(f"Error getting git dates for {filepath}: {str(e)}")
            
        return git_dates
    
    def extract_dates_from_content(self, content):
        """Use LLM to extract dates mentioned in the content."""
        prompt = f"""
        Extract all dates mentioned in this content that could indicate:
        - Creation dates
        - Due dates
        - Milestone dates
        - Meeting dates
        - Deadlines
        
        Note content (excerpt):
        ```
        {content[:3000]}
        ```
        
        For each date found, provide:
        - date: [YYYY-MM-DD format]
        - context: [short description of what this date refers to]
        - confidence: [high, medium, low]
        
        Format as valid YAML list items. If no dates are found, return "No dates found."
        """
        
        response = self.llm.complete(prompt)
        return str(response)
    
    def has_frontmatter(self, content):
        """Check if note already has frontmatter."""
        return content.startswith("---") and "---" in content[3:]
    
    def extract_frontmatter(self, content):
        """Extract existing frontmatter if present."""
        if not self.has_frontmatter(content):
            return {}, content
        
        # Extract frontmatter
        end_idx = content[3:].find("---") + 6
        frontmatter_str = content[3:end_idx-3].strip()
        main_content = content[end_idx:].strip()
        
        # Parse frontmatter
        frontmatter = {}
        for line in frontmatter_str.split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                frontmatter[key.strip()] = value.strip()
        
        return frontmatter, main_content
    
    def analyze_content_with_dates(self, content, filename, dates_info):
        """Analyze content with awareness of dates."""
        prompt = f"""
        Analyze this note considering date information and determine its PARA classification and metadata.
        
        Note filename: {filename}
        
        Date information:
        {dates_info}
        
        Note content:
        ```
        {content[:4000]}
        ```
        
        Please provide a structured response with these fields:
        - para_category: [Projects, Areas, Resources, Archives]
        - type: [project, task, reference, note, etc]
        - status: [active, completed, on-hold, planned]
        - priority: [high, medium, low] (if applicable)
        - projects: [list any projects mentioned]
        - tasks: [list any tasks mentioned or implied]
        - start_date: [when this project/task started, based on dates]
        - due_date: [when this project/task is due, based on dates]
        - timeline_position: [beginning, middle, end, completed] (project phase)
        
        Use the date information to determine status and timeline position.
        
        Format as valid YAML, only these fields, no explanations.
        """
        
        response = self.llm.complete(prompt)
        yaml_response = str(response)
        
        # Convert YAML-like response to dict (simple parsing)
        result = {}
        for line in yaml_response.split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                result[key.strip()] = value.strip()
        
        return result
    
    def enhance_content_with_timeline(self, content, analysis, dates_info):
        """Enhance content with timeline awareness."""
        prompt = f"""
        Enhance this note with timeline awareness by:
        1. Converting implicit tasks to explicit checkbox tasks using "- [ ]" format
        2. Identifying and marking project headings
        3. Adding timeline markers to sections where appropriate
        4. Standardizing any deadline mentions to "Deadline: YYYY-MM-DD" format
        5. Adding a timeline section at the end if appropriate
        6. Never removing or changing factual information
        
        Timeline information:
        {dates_info}
        
        Original content:
        ```
        {content[:4000]}
        ```
        
        Analysis indicates this is a {analysis.get('type', 'note')} in {analysis.get('timeline_position', 'unknown')} phase.
        
        Return ONLY the enhanced content without explanations.
        """
        
        response = self.llm.complete(prompt)
        return str(response)
    
    def process_note_with_timeline(self, filepath):
        """Process a single note with timeline enhancement."""
        try:
            filename = os.path.basename(filepath)
            
            # Skip PDFs - will be handled separately
            if filepath.lower().endswith('.pdf'):
                self.stats["skipped"] += 1
                return True
                
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract existing frontmatter
            frontmatter, main_content = self.extract_frontmatter(content)
            
            # Collect date information
            dates = {
                "filename_date": self.extract_date_from_filename(filename),
                **self.get_git_dates(filepath)
            }
            
            # Extract dates from content
            content_dates = self.extract_dates_from_content(main_content)
            
            # Compile date information for LLM
            dates_info = f"""
            Filename date: {dates['filename_date']}
            Git creation date: {dates['git_created']}
            Git modification date: {dates['git_modified']}
            
            Dates found in content:
            {content_dates}
            """
            
            # Analyze content with dates awareness
            analysis = self.analyze_content_with_dates(main_content, filename, dates_info)
            
            # Add date information to frontmatter
            if dates['filename_date']:
                frontmatter['filename_date'] = dates['filename_date']
            if dates['git_created']:
                frontmatter['git_created'] = dates['git_created']
            if dates['git_modified']:
                frontmatter['git_modified'] = dates['git_modified']
            
            # Add analysis to frontmatter
            for key, value in analysis.items():
                if key not in frontmatter:
                    frontmatter[key] = value
            
            # Generate enhanced content
            enhanced_content = self.enhance_content_with_timeline(main_content, analysis, dates_info)
            
            # Compile new note content
            frontmatter_str = "---\n"
            for key, value in frontmatter.items():
                frontmatter_str += f"{key}: {value}\n"
            frontmatter_str += "---\n\n"
            
            new_content = frontmatter_str + enhanced_content
            
            # Create backup
            backup_path = filepath + ".bak"
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Determine target PARA folder
            para_category = analysis.get('para_category', 'Resources')
            target_folder = self.para_folders.get(para_category, self.para_folders['Resources'])
            target_path = os.path.join(target_folder, filename)
            
            # Create subfolders based on analysis if needed
            if para_category == 'Projects' and 'projects' in analysis:
                project_name = analysis['projects'].split(',')[0].strip()
                if project_name:
                    project_folder = os.path.join(target_folder, project_name)
                    os.makedirs(project_folder, exist_ok=True)
                    target_path = os.path.join(project_folder, filename)
            
            # Write enhanced note to target location
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            # Only delete the original if it's different from the target
            if os.path.abspath(filepath) != os.path.abspath(target_path):
                # Delete original if necessary (but keep the backup)
                if os.path.exists(filepath) and filepath != backup_path:
                    os.remove(filepath)
            
            self.stats["enhanced"] += 1
            if dates['filename_date'] or dates['git_created'] or content_dates != "No dates found.":
                self.stats["with_dates"] += 1
                
            return True
            
        except Exception as e:
            print(f"Error processing {filepath}: {str(e)}")
            self.stats["errors"] += 1
            return False
    
    def enhance_vault_with_timeline(self, max_notes=None):
        """Enhance all notes with timeline information."""
        notes = glob.glob(f"{self.vault_path}/**/*.md", recursive=True)
        print(f"Found {len(notes)} markdown notes in vault")
        
        if max_notes:
            notes = notes[:max_notes]
            print(f"Processing first {max_notes} notes")
        
        for i, note_path in enumerate(notes):
            print(f"Processing note {i+1}/{len(notes)}: {os.path.basename(note_path)}")
            self.process_note_with_timeline(note_path)
            self.stats["processed"] += 1
        
        print(f"\nTimeline enhancement complete:")
        print(f"Processed: {self.stats['processed']}")
        print(f"Enhanced: {self.stats['enhanced']}")
        print(f"With date information: {self.stats['with_dates']}")
        print(f"Errors: {self.stats['errors']}")

    def generate_project_timeline(self):
        """Generate a project timeline based on enhanced notes."""
        # Get all notes in Projects folder
        project_notes = glob.glob(f"{self.para_folders['Projects']}/**/*.md", recursive=True)
        
        if not project_notes:
            print("No project notes found.")
            return
        
        timeline_data = []
        
        for note_path in project_notes:
            try:
                with open(note_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                frontmatter, _ = self.extract_frontmatter(content)
                
                if not frontmatter:
                    continue
                
                # Extract timeline data
                timeline_item = {
                    "file": os.path.basename(note_path),
                    "project": frontmatter.get("projects", "Unknown"),
                    "type": frontmatter.get("type", "Unknown"),
                    "status": frontmatter.get("status", "Unknown"),
                    "start_date": None,
                    "due_date": None,
                    "timeline_position": frontmatter.get("timeline_position", "Unknown")
                }
                
                # Find best start date
                for date_field in ["start_date", "git_created", "filename_date"]:
                    if date_field in frontmatter and frontmatter[date_field]:
                        timeline_item["start_date"] = frontmatter[date_field]
                        break
                
                # Find best due date
                for date_field in ["due_date", "deadline"]:
                    if date_field in frontmatter and frontmatter[date_field]:
                        timeline_item["due_date"] = frontmatter[date_field]
                        break
                
                timeline_data.append(timeline_item)
                
            except Exception as e:
                print(f"Error processing timeline for {note_path}: {str(e)}")
        
        # Sort by start date then due date
        timeline_data.sort(key=lambda x: (x["start_date"] or "9999-99-99", x["due_date"] or "9999-99-99"))
        
        # Generate timeline markdown
        timeline_md = "# Project Timeline\n\n"
        timeline_md += "Generated: " + datetime.now().strftime("%Y-%m-%d") + "\n\n"
        
        # Group by project
        projects = {}
        for item in timeline_data:
            project = item["project"]
            if project not in projects:
                projects[project] = []
            projects[project].append(item)
        
        # Generate timeline per project
        for project, items in projects.items():
            timeline_md += f"## {project}\n\n"
            timeline_md += "| File | Type | Status | Start Date | Due Date | Phase |\n"
            timeline_md += "|------|------|--------|------------|----------|-------|\n"
            
            for item in items:
                timeline_md += f"| {item['file']} | {item['type']} | {item['status']} | "
                timeline_md += f"{item['start_date'] or 'N/A'} | {item['due_date'] or 'N/A'} | "
                timeline_md += f"{item['timeline_position']} |\n"
            
            timeline_md += "\n"
        
        # Save timeline
        os.makedirs("data/timelines", exist_ok=True)
        timeline_path = f"data/timelines/project_timeline_{datetime.now().strftime('%Y-%m-%d')}.md"
        
        with open(timeline_path, 'w', encoding='utf-8') as f:
            f.write(timeline_md)
        
        print(f"Project timeline generated at {timeline_path}")
        return timeline_path
        
if __name__ == "__main__":
    import json
    import argparse
    
    parser = argparse.ArgumentParser(description="Enhance notes with timeline information")
    parser.add_argument("--max", type=int, default=None, help="Maximum number of notes to process")
    parser.add_argument("--timeline-only", action="store_true", help="Only generate timeline, don't enhance notes")
    args = parser.parse_args()
    
    # Load config
    with open("config/settings.json", "r") as f:
        config = json.load(f)
    
    vault_path = config["obsidian_vault_path"]
    model = config["llm_model"]
    
    # Create enhancer
    enhancer = TimelineEnhancer(vault_path, model)
    
    if args.timeline_only:
        enhancer.generate_project_timeline()
    else:
        # Process notes with timeline enhancement
        enhancer.enhance_vault_with_timeline(max_notes=args.max)
        
        # Generate timeline
        enhancer.generate_project_timeline()
