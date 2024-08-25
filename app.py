from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        # Extract data from the request
        data = request.json.get('data', [])
        
        # Initialize lists for numbers and alphabets
        numbers = []
        alphabets = []
        highest_lowercase_alphabet = []  # Changed to a list
        
        # Iterate through the data and categorize each item
        for item in data:
            if item.isdigit():
                numbers.append(item)
            elif item.isalpha():
                alphabets.append(item)
                # Check if it's a lowercase alphabet and track the highest one
                if item.islower():
                    if not highest_lowercase_alphabet or item > highest_lowercase_alphabet[0]:
                        highest_lowercase_alphabet = [item]
        
        # Create the response object
        response = {
            "is_success": True,
            "user_id": "Shubham_Shaswat_10032002",
            "email": "shubham.shaswat2002@gmail.com",
            "roll_number": "21BCE0097",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
        
        return jsonify(response)
    
    except Exception as e:
        # Handle any errors
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    # Return the hardcoded JSON object
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
