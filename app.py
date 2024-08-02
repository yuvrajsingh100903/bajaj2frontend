from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML file

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])
        
        if not data:
            return jsonify({
                "is_success": False,
                "error": "Invalid input data"
            }), 400
        
        # Separate numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]

        # Determine the highest alphabet (case insensitive)
        highest_alphabet = max(alphabets, key=lambda x: x.lower(), default='')

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with your actual user_id logic
            "email": "john@xyz.com",         # Replace with your actual email
            "roll_number": "ABCD123",        # Replace with your actual roll number
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }

        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 500

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({
        "operation_code": 1
    }), 200

if __name__ == '__main__':
    app.run(debug=True)

