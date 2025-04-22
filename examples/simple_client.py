"""
A simple example of using the A2A client to interact with an A2A server.
"""
import asyncio
from a2a_commons import A2AClient
from a2a_commons.types import Message, TextPart

async def main():
    # Create a client connected to the echo server
    client = A2AClient(server_url="http://localhost:8000")
    
    # Create a message
    message = Message(
        role="user",
        parts=[
            TextPart(
                type="text",
                text="Hello, A2A server!"
            )
        ]
    )
    
    print("Sending a task to the A2A server...")
    
    # Send the task and get the response
    try:
        response = await client.send_task(message=message)
        print("Response received:")
        
        # Print each text part in the response
        for part in response.status.message.parts:
            if part.type == "text":
                print(f"  {part.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example of streaming response
    print("\nSending a streaming task...")
    try:
        async for update in client.send_task_streaming(message=message):
            if hasattr(update, 'status') and update.status.message:
                for part in update.status.message.parts:
                    if part.type == "text":
                        print(f"  Streaming response: {part.text}")
    except Exception as e:
        print(f"Streaming error: {e}")

if __name__ == "__main__":
    asyncio.run(main()) 