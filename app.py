from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# H - 1
@app.route("/users", methods=["GET"])
def get_users():
    if request.method == "GET":
        response = {"payload": "success"}
        return jsonify(response), 200
    
# H - 2
@app.route("/user", methods=["POST"])
def post_user():
    if request.method == "POST":
        response = {"payload": "success"}
        return jsonify(response), 200

# H - 3
@app.route("/user", methods=["DELETE"])
def delete_user():
    if request.method == "DELETE":
        response = {"payload": "success"}
        return jsonify(response), 200

# H - 4
@app.route("/user", methods=["PUT"])
def put_user():
    if request.method == "PUT":
        response = {
            "payload": "success",
            "error": False,
            }
        return jsonify(response), 200
    
# H - 5
@app.route("/api/v1/users", methods=["GET"])
def get_list():
    if request.method == "GET":
        response = {"payload": []}
        return jsonify(response), 200

# H - 6
@app.route("/api/v1/user", methods=["POST"])
def get_user():
    if request.method == "POST":
        email = request.args.get("email")
        name = request.args.get("name")
        
        if not email or not name:
            return jsonify({"error": "Missing fields in request"}), 400
        
        response = {
            "payload": {
                "email": email,
                "name": name,
            }
        }
        return jsonify(response), 200
    
# H - 7
@app.route("/api/v1/user/add", methods=["POST"])
def add_user():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        user_id = request.form.get("id")
        
        if not email or not name or not user_id:
            return jsonify({"error": "Missing fields in request"}), 400
        
        response = {
            "payload": {
                "email": email,
                "name": name,
                "id": user_id,
            }
        }
        return jsonify(response), 200

# H - 8
@app.route("/api/v1/user/create", methods=["POST"])
def create_user():
    if request.method == "POST":
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        email = data.get("email")
        name = data.get("name")
        user_id = data.get("id")

        if not email or not name or not user_id:
            return jsonify({"error": "Missing fields in request"}), 400

        response = {
            "payload": {
                "email": email,
                "name": name,
                "id": user_id,
            }
        }
        return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
