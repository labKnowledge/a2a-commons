# A2A Commons

Common utilities for Agent-to-Agent (A2A) communication. This library provides a standardized way for AI agents to communicate with each other using a JSON-RPC protocol over HTTP.

## Features

- **A2A Server**: Create servers that can handle agent-to-agent communication
- **A2A Client**: Connect to other A2A-compatible agents
- **Task Management**: Track and manage tasks between agents
- **Push Notifications**: Support for asynchronous updates
- **Streaming**: Real-time communication between agents
- **Type-Safe Communication**: Pydantic models for all communication data

## Installation

```bash
pip install a2a-commons
```

Or install from source:

```bash
git clone https://github.com/yourusername/a2a-commons.git
cd a2a-commons
pip install -e .
```

## Usage

### Server

```python
from a2a_commons import A2AServer, InMemoryTaskManager
from a2a_commons.types import AgentCard, AgentProvider, AgentCapabilities, AgentAuthentication, AgentSkill

# Create an agent card
agent_card = AgentCard(
    name="My Agent",
    description="An example agent",
    url="http://localhost:5000",
    version="1.0.0",
    provider=AgentProvider(
        organization="My Organization"
    ),
    capabilities=AgentCapabilities(
        streaming=True,
        pushNotifications=True
    ),
    authentication=AgentAuthentication(
        schemes=["none"]
    ),
    skills=[
        AgentSkill(
            id="task1",
            name="Example Task",
            description="Performs an example task"
        )
    ]
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
from a2a_commons import A2AClient
from a2a_commons.types import Message, TextPart

# Create a client
client = A2AClient(server_url="http://localhost:5000")

# Send a task
message = Message(
    role="user",
    parts=[
        TextPart(
            type="text",
            text="Hello, world!"
        )
    ]
)

response = await client.send_task(message=message)
print(response)

# For streaming responses
async for update in client.send_task_streaming(message=message):
    print(update)
```

## Development

### Setup

```bash
# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

## License

Apache License 2.0 