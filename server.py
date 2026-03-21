from flask import Flask, send_file, request, abort
import time
import os

app = Flask(__name__)

# store tokens (temporary storage)
valid_tokens = {}

# create a test token (expires in 60 seconds)
valid_tokens["test123"] = time.time() + 60

@app.route("/")
def home():
    return "Server is running"

@app.route("/download")
def download():
    token = request.args.get("token")

    if token not in valid_tokens:
        return abort(403)

    # check expiration
    if time.time() > valid_tokens[token]:
        del valid_tokens[token]
        return abort(403)

    # one-time use (delete after use)
    del valid_tokens[token]

    return send_file("pack.zip", as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
