import openai
import argparse

# Set up command-line arguments
parser = argparse.ArgumentParser(description='Generate a book summary.')
parser.add_argument('input_file', type=str, help='the name of the file containing the book')
parser.add_argument('output_file', type=str, help='the name of the file to save the summary to')
args = parser.parse_args()

# Set up OpenAI API credentials
openai.api_key = ""
# Load the book text from file
with open(args.input_file, 'r') as f:
    book_text = f.read()

# Define the parameters for the API request
model = "text-davinci-003"
parameters = {
    "engine": model,
    "prompt": f"Summarize the following book:\n{book_text}",
    "max_tokens": 50,
    "temperature": 0.5,
    "n": 1,
    "stop": "\n"
}

# Generate the book summary using the OpenAI API
response = openai.Completion.create(**parameters)
summary = response.choices[0].text.strip()

# Save the book summary to a file
with open(args.output_file, 'w') as f:
    f.write(summary)

print(f"Book summary saved to {args.output_file}")
