from flask import Flask, send_file, render_template_string
import os

app = Flask(__name__)
download_count = 0

# Landing page with download button
@app.route("/")
def home():
    global download_count
    html = f"""
    <html>
        <head>
            <title>Safe Tweaks Tool</title>
        </head>
        <body style="font-family:sans-serif; text-align:center; margin-top:50px;">
            <h1>Safe Tweaks Tool</h1>
            <p>Downloads so far: {download_count}</p>
            <a href="/download">
                <button style="font-size:20px; padding:10px 20px;">Download Now</button>
            </a>
            <p>After downloading, use 7-Zip with your password to extract the tool.</p>
        </body>
    </html>
    """
    return render_template_string(html)

# Download route
@app.route("/download")
def download():
    global download_count
    download_count += 1

    # Ensure Flask finds the file in the same folder as app.py
    file_path = os.path.join(os.path.dirname(__file__), "SafeTweaks.7z")
    if not os.path.exists(file_path):
        return "File not found!", 404

    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    # On Render, host/port are handled automatically
    app.run(host="0.0.0.0", port=5000, debug=True)
