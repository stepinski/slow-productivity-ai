# slow-productivity-ai

Automating Knowledge &amp; Task Management with Offline Hugging Face, n8n &amp; Obsidian

## better keyword extraction

python# In the process_note method, after extracting keywords

# Step 2: Extract top 5 keywords (lightweight, focused query)

keywords = self.extract_keywords_with_llm(main_content, filename)

# Step 3: Determine PARA category (lightweight, focused query)

analysis = self.analyze_para_category(main_content, filename)

# Get Git information

git_info = self.get_git_dates(note_path)

# Extract dates from content

date_entries = self.extract_dates_from_content(main_content)

# Step 4: Create a concise summary (with all elements maintained)

enhanced_content = self.summarize_note(main_content)

# Add timeline information without extra headers

timeline_section = self.generate_timeline_section(git_info, date_entries)
if timeline_section and "## Timeline" not in enhanced_content:
    if "##" in enhanced_content:
        # Insert before the first section heading
        first_heading = re.search(r'\n##\s+', enhanced_content)
        if first_heading:
            insert_pos = first_heading.start()
            enhanced_content = enhanced_content[:insert_pos] + "\n" + timeline_section + enhanced_content[insert_pos:]
        else:
            enhanced_content += "\n" + timeline_section
    else:
        enhanced_content += "\n" + timeline_section

# Ensure source reference is included

source_ref = f"[[{os.path.splitext[filename](0)}]]"
if "## Source" not in enhanced_content and source_ref not in enhanced_content:
    enhanced_content += f"\n\n## Source\n{source_ref}"

# Format and add keywords at the bottom of the note content (instead of in frontmatter)

if keywords:
    keywords_section = self.format_keywords_as_tags(keywords)
    enhanced_content += keywords_section

# Store keywords and tasks for reports

self.all_keywords.update(keywords)
self.all_tasks.extend(tasks)

# Prepare frontmatter

frontmatter = dict(original_frontmatter)  # Copy original frontmatter

# REMOVE this line if it was previously there

# frontmatter['keywords'] = " ".join(hashtag_keywords)

# Keywords will now be at the bottom of the note instead

The second addition is the format_keywords_as_tags method, which you'll need to add to the class:

pythondef format_keywords_as_tags(self, keywords: List[str]) -> str:
    """Format keywords as hashtags for appending to the note."""
    if not keywords:
        return ""

    # Convert keywords to hashtags
    hashtags = []
    for keyword in keywords:
        # Remove spaces and special characters for consistent hashtags
        clean_keyword = re.sub(r'[^\w]', '', keyword.replace(' ', ''))
        if clean_keyword:
            hashtags.append(f"#{clean_keyword.lower()}")
            
    # Return as a single line of hashtags
    return "\n\n" + " ".join(hashtags)
These changes will:

Remove keywords from the YAML frontmatter
Add them as hashtags at the bottom of each note (e.g., #montreal #water #weftec)
