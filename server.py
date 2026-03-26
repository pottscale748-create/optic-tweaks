from flask import Flask, send_file

app = Flask(__name__)

# Track downloads for each file
download_counts = {
    "DO_NOT_OPEN": 0,
    "Open": 0,
    "Open_dash": 0
}

@app.route("/")
def home():
    return (
        f"DO_NOT_OPEN.zip downloads: {download_counts['DO_NOT_OPEN']}<br>"
        f"Open.zip downloads: {download_counts['Open']}<br>"
        f"Open-.zip downloads: {download_counts['Open_dash']}"
    )

@app.route("/download/do_not_open")
def download_do_not_open():
    download_counts["DO_NOT_OPEN"] += 1
    return send_file("DO NOT OPEN!!!.zip", as_attachment=True)

@app.route("/download/open")
def download_open():
    download_counts["Open"] += 1
    return send_file("Open.zip", as_attachment=True)

@app.route("/download/open_dash")
def download_open_dash():
    download_counts["Open_dash"] += 1
    return send_file("Open-.zip", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
