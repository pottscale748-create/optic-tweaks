from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running"

@app.route("/download")
def download():
    return send_file("pack.zip", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
        return abort(403)

    if time.time() > valid_tokens[token]:
        return abort(403)

    del valid_tokens[token]

    return send_file("pack.zip", as_attachment=True)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
