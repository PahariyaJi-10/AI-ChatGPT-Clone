import os
from flask_cors import CORS
from flask import Flask, request, jsonify
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("AIzaSyAtXEq9wZPb4u6U6WCEMZyP-AhVvhHJg8s")
client = genai.Client( 
    api_key=api_key
)
app = Flask(__name__)
CORS(app)


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
