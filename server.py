from flask import Flask, send_file, request, abort
import time
import os

app = Flask(__name__)

ADMIN_CODE = "mySecret123"
valid_tokens = {}

@app.route("/")
def home():
    return "Server is running"


# ADMIN: create token
@app.route("/create-token")
def create_token():
    admin = request.args.get("admin")

    if admin != ADMIN_CODE:
        return abort(403)

    token = "test123"
    valid_tokens[token] = time.time() + 60

    return token


# DOWNLOAD
@app.route("/download")
def download():
    token = request.args.get("token")

    if token not in valid_tokens:
        return abort(403)

    if time.time() > valid_tokens[token]:
        return abort(403)

    del valid_tokens[token]

    return send_file("pack.zip", as_attachment=True)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
