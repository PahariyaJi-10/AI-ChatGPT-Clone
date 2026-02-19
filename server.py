import os
from flask import Flask, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options=types.HttpOptions(api_version="v1")
)

chat = client.chats.create(model="gemini-2.5-flash")


@app.route("/chat", methods=["POST"])
def chat_api():
    data = request.json
    message = data["message"]

    response = chat.send_message(message)

    return jsonify({"reply": response.text})


if __name__ == "__main__":
    print("Starting Flask Server...")
    app.run(debug=True)
