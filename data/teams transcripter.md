Display name
:
transcript fetcher
Application (client) ID
:
559e2499-2073-4447-8f65-f38f6aef6de5
Object ID
:
c9d6e375-2a5e-4574-b647-0a2e1fe624e1
Directory (tenant) ID
:
eceb0c3a-4ab0-4897-af2e-b9ae848586b0



secret:

value 
M7e8Q~6vUU3I-6RB2.SNztWWa8RmyrNLcWR7edz0

id
dc041cc6-b4e0-4821-a1a4-1eb6abbbfb66


from ms_graph import generate_access_token, get_transcript CLIENT_ID = '559e2499-2073-4447-8f65-f38f6aef6de5' CLIENT_SECRET = 'M7e8Q~6vUU3I-6RB2.SNztWWa8RmyrNLcWR7edz0' TENANT_ID = 'eceb0c3a-4ab0-4897-af2e-b9ae848586b0' # Authenticate token = generate_access_token(CLIENT_ID, CLIENT_SECRET, TENANT_ID) # Fetch Transcript transcript = get_transcript(token, meeting_id='your-meeting-id') with open("transcript.txt", "w") as file: file.write(transcript)