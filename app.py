from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will allow all origins; you can customize as needed

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])
        if not isinstance(data, list):
            raise ValueError("The 'data' field must be a list.")
        numbers = []
        alphabets = []
        highest_lowercase_alphabet = None
        for item in data:
            if not isinstance(item, str):
                raise ValueError("All items in 'data' must be strings.")
            if item.isdigit():
                numbers.append(item)
            elif item.isalpha():
                alphabets.append(item)
                if item.islower():
                    if highest_lowercase_alphabet is None or item > highest_lowercase_alphabet:
                        highest_lowercase_alphabet = item
        response = {
            "is_success": True,
            "user_id": "Shubham_Shaswat_10032002",
            "email": "shubham.shaswat2002@gmail.com",
            "roll_number": "21BCE0097",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }
        return jsonify(response)
    except ValueError as ve:
        return jsonify({"is_success": False, "error": str(ve)}), 400
    except Exception as e:
        return jsonify({"is_success": False, "error": "An unexpected error occurred: " + str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
