from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

APP_NAME = "CI/CD Cloud Ops – Rajkumar"
APP_VERSION = "4.0.0"

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
                font-family: 'Poppins', Arial, sans-serif;
                background: radial-gradient(circle at top, #1f1147, #070312);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                color: #e9d5ff;
            }}

            .panel {{
                background: rgba(17, 6, 43, 0.85);
                border-radius: 20px;
                padding: 50px;
                width: 70%;
                box-shadow: 0 0 40px rgba(168, 85, 247, 0.35);
                border: 1px solid rgba(168, 85, 247, 0.4);
                text-align: center;
            }}

            h1 {{
                color: #c084fc;
                margin-bottom: 12px;
                letter-spacing: 1px;
            }}

            .status {{
                display: inline-block;
                padding: 8px 18px;
                border-radius: 30px;
                background: linear-gradient(90deg, #22c55e, #4ade80);
                color: #052e16;
                font-weight: bold;
                margin-bottom: 25px;
                box-shadow: 0 0 15px #22c55e;
            }}

            p {{
                font-size: 18px;
                color: #e9d5ff;
            }}

            .grid {{
                margin-top: 30px;
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 18px;
                text-align: left;
            }}

            .item {{
                background: rgba(255, 255, 255, 0.06);
                padding: 16px;
