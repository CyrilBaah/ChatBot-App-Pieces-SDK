from pieces_copilot_sdk import PiecesClient
import platform

# Use port based on platform
platform_info = platform.platform()
if "Linux" in platform_info:
    port = 5323
else:
    port = 1000

config = {
    "baseUrl": f"http://localhost:{port}",
}

# Initialize the PiecesClient
pieces_client = PiecesClient(config)

# Ask a question
question = "Who is the president of Ghana?"
response = pieces_client.ask_question(question)


print(response)
