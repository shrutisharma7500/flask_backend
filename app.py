from flask import Flask, request, jsonify
from flask_cors import CORS



app = Flask(__name__)
CORS(app)  # This allows cross-origin requests

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Log incoming data
        print("Incoming request data:", request.get_json())

        # Parse and validate data
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not name or not email or not password:
            return jsonify({"error": "All fields are required"}), 400

        # Log parsed data
        print(f"Received data: Name={name}, Email={email}, Password={password}")

        return jsonify({"message": "Form submitted successfully", "data": data}), 200
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": "Something went wrong"}), 500

            


if __name__ == '__main__':
    app.run(debug=True)
