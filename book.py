import openai
import argparse
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# Set up command-line arguments
parser = argparse.ArgumentParser(description='Generate a book based on a writing prompt.')
parser.add_argument('prompt', type=str, help='the writing prompt for the book')
parser.add_argument('filename', type=str, help='the name of the file to save the book to')
parser.add_argument('--max_tokens', type=int, default=4000, help='the maximum number of tokens to generate per request')
parser.add_argument('--num_parts', type=int, default=1, help='the number of parts to generate')
args = parser.parse_args()



# Define the parameters for the API request
model = "text-davinci-003"
parameters = {
    "prompt": args.prompt,
    "temperature": 0.5,
    "max_tokens": args.max_tokens,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0
}

# Generate the book in parts using the OpenAI API
book_parts = []
for i in range(args.num_parts):
    response = openai.Completion.create(engine=model, **parameters)
    book_part = response.choices[0].text.strip()
    book_parts.append(book_part)

# Combine the book parts into a single string
book_text = '\n'.join(book_parts)

# Save the book to a file
with open(args.filename, 'a') as f:
    f.write(book_text)

print(f"Book saved to {args.filename}")