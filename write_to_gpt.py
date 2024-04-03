from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(os.getenv("OPENAI_API_KEY"))

def call_openai_api(prompt):

    # Send the request
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful software tester"},
            {"role": "user", "content": f"Write unit test for the react component with the framework Jest. React component:\n {prompt}"}
        ],
        max_tokens=150,
        temperature=0.1
    )

    # Print the completion
    return response.choices[0].message