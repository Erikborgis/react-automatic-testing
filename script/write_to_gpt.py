from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def call_openai_api(prompt):

    # Send the request
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful software tester"},
            {"role": "user", "content": f"Write unit tests for the react component with the framework Jest. React component:\n {prompt}"}
        ],
        max_tokens=300,
        temperature=0.1
    )

    content = response.choices[0].message.content
    code_block = content.split("```jsx")[1].strip()
    return code_block