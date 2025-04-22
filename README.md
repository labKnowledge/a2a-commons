# A2A Common

Common utilities for Agent-to-Agent (A2A) communication.

## Installation

```bash
pip install a2a-common
```

Or install from source:

```bash
git clone https://github.com/yourusername/A2A.git
cd A2A
pip install -e .
```

## Usage

### Server

```python
from a2a_common import A2AServer, InMemoryTaskManager
from a2a_common.types import AgentCard

# Create an agent card
agent_card = AgentCard(
    name="My Agent",
    description="An example agent",
    version="1.0.0"
)

# Create a task manager
task_manager = InMemoryTaskManager()

# Create and start the server
server = A2AServer(
    host="0.0.0.0",
    port=5000,
    agent_card=agent_card,
    task_manager=task_manager
)
server.start()
```

### Client

```python
from a2a_common import A2AClient

# Create a client
client = A2AClient(server_url="http://localhost:5000")

# Send a task
response = await client.send_task(
    inputs={"message": "Hello, world!"},
    expects={"response": "string"}
)
```

## License

Apache License 2.0 