from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

APP_NAME = "CI/CD Demo App"
APP_VERSION = "1.0.0"

@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{APP_NAME}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #0f172a;
                color: #e5e7eb;
                text-align: center;
                padding-top: 80px;
            }}
            .box {{
                background: #111827;
                padding: 40px;
                border-radius: 12px;
                width: 60%;
                margin: auto;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            }}
            h1 {{
                color: #38bdf8;
            }}
            p {{
                font-size: 18px;
            }}
            .footer {{
                margin-top: 20px;
                font-size: 14px;
                color: #9ca3af;
            }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 CI/CD Pipeline Successful</h1>
            <p>Hello Rajkumar 👋</p>
            <p>Your Flask application has been deployed successfully via Jenkins & Docker.</p>
            <p><b>Version:</b> {APP_VERSION}</p>
            <div class="footer">
                Deployed at {datetime.utcnow()} UTC
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(
        status="UP",
        app=APP_NAME,
        version=APP_VERSION
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
