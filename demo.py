import chainlit as cl
from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def llm_tool(message: str):
    # Call ChatGPT API with streaming
    try:
        msg = cl.Message(content="")
        await msg.send()

        stream = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ],
            temperature=0.7,
            stream=True
        )

        # Stream the response
        full_response = ""
        async for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                full_response += content
                await msg.stream_token(content)

        await msg.update()
        return full_response
    
    except Exception as e:
        return f"Error calling ChatGPT: {str(e)}"

@cl.on_message
async def main(message: cl.Message):
    """
    This function is called every time a user inputs a message in the UI.
    It streams back the response from ChatGPT token by token.

    Args:
        message: The user's message.

    Returns:
        None.
    """
    
    await llm_tool(message.content)
