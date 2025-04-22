"""
A simple example of creating an A2A server.
"""
import asyncio
from a2a_commons import A2AServer, InMemoryTaskManager
from a2a_commons.types import (
    AgentCard, 
    AgentProvider, 
    AgentCapabilities, 
    AgentAuthentication, 
    AgentSkill,
    TaskState,
    Message,
    TextPart
)

async def handle_task(task_id, message):
    """Process an incoming task and return a response."""
    # Extract the message text from the parts
    text = ""
    for part in message.parts:
        if part.type == "text":
            text += part.text
    
    # Create a response
    response = Message(
        role="agent",
        parts=[
            TextPart(
                type="text",
                text=f"You said: {text}"
            )
        ]
    )
    
    return response

def main():
    # Create an agent card
    agent_card = AgentCard(
        name="Echo Agent",
        description="An agent that echoes back your messages",
        url="http://localhost:8000",
        version="1.0.0",
        provider=AgentProvider(
            organization="Example Organization"
        ),
        capabilities=AgentCapabilities(
            streaming=True,
            pushNotifications=False
        ),
        authentication=AgentAuthentication(
            schemes=["none"]
        ),
        skills=[
            AgentSkill(
                id="echo",
                name="Echo Task",
                description="Echoes back the message that was sent"
            )
        ]
    )

    # Create a task manager with a custom task handler
    task_manager = InMemoryTaskManager()
    task_manager.register_task_handler(handle_task)

    # Create and start the server
    server = A2AServer(
        host="0.0.0.0",
        port=8000,
        agent_card=agent_card,
        task_manager=task_manager
    )
    
    print(f"Starting A2A server at http://localhost:8000")
    server.start()

if __name__ == "__main__":
    main() 