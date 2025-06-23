from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__, static_folder="static", template_folder="templates")

with open("asl_dict.json") as f:
    asl_dict = json.load(f)

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.json.get("message", "").strip().lower()
    image_url = asl_dict.get(user_msg)

    if image_url:
        return jsonify({
            "response": f"Here's how to sign '{user_msg}' in ASL:",
            "image_url": image_url
        })
    else:
        return jsonify({
            "response": f"Sorry, I don't have the ASL sign for '{user_msg}'.",
            "image_url": None
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
