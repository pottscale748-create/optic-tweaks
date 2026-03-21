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