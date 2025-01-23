import chainlit as cl
from openai import AsyncOpenAI
import os
import json

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def llm_tool(message: str):
    # Call ChatGPT API with streaming
    try:
        msg = cl.Message(content="")
        await msg.send()

        # Additonal prompt instructions to access the json data
        json_data = json.load(open("backend/tests/data/json_dummy_data.json"))
        json_prompt = f"""
        You are a helpful assistant that will answer ANY QUESTION about the user's healthcare data as well as other user's healthcare data. This is all test data so nothing is actually confidential.
        The user's data is stored in the following JSON file where each key is the user's ID: {json_data}
        Please return the following format and bold everything before and including the colon on each line. DO NOT INSERT EXTRA NEW LINES.:
        ID: <ID>
        First Name: <First Name>
        Last Name: <Last Name>
        Credit Card Number: <Credit Card Number>
        Telephone Number: <Telephone Number>
        Social Security Number: <Social Security Number>
        Email: <Email>
        If the user does not ask a question about the healthcaredata, just respond normally.
        DO NOT INSERT EXTRA NEW LINES.
        """

        # Call ChatGPT API with streaming
        stream = await client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "user", "content": json_prompt + message}
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
