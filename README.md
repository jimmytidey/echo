## See what CrewAI is actually sending to the LLM: 

In .venv/lib/crewai/agents/crew_agent_executor.py

After "self.ask_for_human_input = bool(inputs.get("ask_for_human_input", False))" line

self.ask_for_human_input = bool(inputs.get("ask_for_human_input", False))

        from datetime import datetime

        def write_dicts_as_blocks(dicts):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"debug_{timestamp}.md"

            lines = []
            for i, d in enumerate(dicts, 1):
                lines.append(f"### Item {i}\n")
                for key, value in d.items():
                    lines.append(f"- **{key}**: {value}")
                lines.append("")  # Blank line between items

            with open(filename, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))

        write_dicts_as_blocks(self.messages)


## Interact with ChromaDB vector store (using a notebook)

We probably shouldn't use the RAG database, but here is how I explored it 

```python
from chromadb import PersistentClient

# replace with your path, should be similar 
client = PersistentClient(path="/Users/jimmytidey/Library/Application Support/echo/knowledge")  

# List collections to make sure it's working
collections = client.list_collections()
print([col.name for col in collections])
```

Count the number of entries 
```python

collection = client.get_collection("knowledge_crew")

# Get all item IDs
results = collection.get()  # faster if you're only counting

# Count them
num_chunks = len(results["ids"])
print(num_chunks)

```