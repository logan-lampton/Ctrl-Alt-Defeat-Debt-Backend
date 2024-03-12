from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the .env file. If it's in the same directory as your script, you can call load_dotenv() without any arguments.
load_dotenv()

client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )

# Now you can access the variable
# openai_api_key = os.getenv('OPEN_AI_API_KEY')

# Set the API key
# openai.api_key = openai_api_key


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant that specializes in personal finance. You can analyze a user's financial data, including bank information, expenses, and transactions, to provide budget recommendations. You can also make future projections based on this data. If a user has a specific financial goal, you can suggest strategies to help them save money and reach their goal."
        },
        {
            "role": "user",
            "content": "I'm trying to save for a new car. Can you help me adjust my budget?"
        }
    ],
    temperature=0.5,
    max_tokens=64,
)

print(response.choices[0].message)