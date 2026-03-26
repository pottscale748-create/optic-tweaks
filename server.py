from flask import Flask, send_file

app = Flask(__name__)

download_count = 0

@app.route("/")
def home():
    return f"Downloads: {download_count}"

@app.route("/download")
def download():
    global download_count
    download_count += 1
    return send_file("pack.zip", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
