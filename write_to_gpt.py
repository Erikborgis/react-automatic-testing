import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def call_openai_api(prompt):

    # Set your API key
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Send the request
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.1
    )

    # Print the completion
    return response.choices[0].text