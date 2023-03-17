import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import openai

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize the Slack app
app = App()

# Initialize OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Slash command to interact with ChatGPT
@app.command("/chatgpt")
def handle_chatgpt(ack, respond, command):
    ack()
    query = command.get("text")
    response = chatgpt_query(query)
    respond(response)

# Function to interact with ChatGPT API
def chatgpt_query(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

# Start the app
if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
