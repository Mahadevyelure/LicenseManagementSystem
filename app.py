from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory database for licenses
licenses = {
    "example-license-key-82918291": "2025-12-31"
}

# Endpoint to validate a license
@app.route('/validate', methods=['POST'])
def validate_license():
    data = request.get_json()
    license_key = data.get('license_key')

    if not license_key:
        return jsonify({"message": "License key is missing"}), 400

    if license_key in licenses:
        return jsonify({"message": "License is valid"}), 200
    else:
        return jsonify({"message": "Invalid license"}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
