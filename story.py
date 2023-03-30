import openai
import argparse
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# Set up command-line arguments
parser = argparse.ArgumentParser(description='Generate a story based on a writing prompt.')
parser.add_argument('prompt', type=str, help='the writing prompt for the story')
parser.add_argument('filename', type=str, help='the name of the file to save the story to')
parser.add_argument('--max_tokens', type=int, default=4000, help='the maximum number of tokens to generate per request')
parser.add_argument('--num_chunks', type=int, default=1, help='the number of chunks to generate')
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

# Generate the story in chunks using the OpenAI API
story_chunks = []
for i in range(args.num_chunks):
    response = openai.Completion.create(engine=model, **parameters)
    story_chunk = response.choices[0].text.strip()
    story_chunks.append(story_chunk)

    # Update the prompt to continue the story
    parameters["prompt"] = f"{args.prompt} {''.join(story_chunks)}"

# Combine the story chunks into a single string
story_text = '\n'.join(story_chunks)

# Save the story to a file
with open(args.filename, 'w') as f:
    f.write(story_text)

print(f"Story saved to {args.filename}")



#This script has been modified to generate a story instead of a book, and it takes the 
#generated story chunks and updates the prompt with the previous content to continue the story.