from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

APP_NAME = "CI/CD Deployment Rajkumar"
APP_VERSION = "3.0.0"

@app.route("/")
def home():
    hostname = socket.gethostname()

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{APP_NAME}</title>
        <style>
            body {{
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #fdfbfb, #ebedee);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }}

            .card {{
                background: #ffffff;
                padding: 45px;
                border-radius: 16px;
                width: 65%;
                box-shadow: 0 20px 40px rgba(0,0,0,0.15);
                text-align: center;
            }}

            h1 {{
                color: #2563eb;
                margin-bottom: 10px;
            }}

            .badge {{
                display: inline-block;
                background: #dcfce7;
                color: #166534;
                padding: 6px 14px;
                border-radius: 20px;
                font-weight: bold;
                margin-bottom: 20px;
            }}

            p {{
                font-size: 18px;
                color: #374151;
            }}

            .info {{
                margin-top: 25px;
                text-align: left;
                background: #f9fafb;
                padding: 20px;
                border-radius: 12px;
                font-size: 16px;
            }}

            .info span {{
                font-weight: bold;
                color: #111827;
            }}

            .footer {{
                margin-top: 30px;
                font-size: 14px;
                color: #6b7280;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="badge">DEPLOYMENT SUCCESS</div>
            <h1>✅ CI/CD Pipeline Completed</h1>

            <p>Hello Rajkumar 👋</p>
            <p>Your application is live on a new machine.</p>

            <div class="info">
                <p><span>Application:</span> {APP_NAME}</p>
                <p><span>Version:</span> {APP_VERSION}</p>
                <p><span>Host:</span> {hostname}</p>
                <p><span>Deployed At:</span> {datetime.utcnow()} UTC</p>
            </div>

            <div class="footer">
                Powered by Flask • Jenkins • Docker • AWS
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(
        status="UP",
        service=APP_NAME,
        version=APP_VERSION,
        timestamp=datetime.utcnow().isoformat()
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
