# file: jwt_api_server.py

from flask import Flask,jsonify
from jwt_generator import JWTGenerator  # We'll separate your existing JWT class into jwt_generator.py
from datetime import timedelta
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Health check
@app.route('/health', methods=['GET'])
def health():
    return "API is alive!", 200

# Main API route to get JWT
@app.route('/generate_jwt', methods=['GET'])  # GET is enough now
def generate_jwt():
    try:
        generator = JWTGenerator(
            account="novonordisk-nni",  # Replace with your actual Snowflake account
            user="SVC_CONNEX_APP_ADMIN_CDW_NPROD",        # Replace with your Snowflake user
            private_key_file_path="private_key.p8",  # Store key in project root or 'keys/' folder
            lifetime=timedelta(minutes=59),
            renewal_delay=timedelta(minutes=54),
        )
        token = generator.get_token()
        return jsonify({"token": token}), 200
    except Exception as e:
        logging.error(f"Error generating JWT: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
