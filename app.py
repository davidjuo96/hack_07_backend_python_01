from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# H - 1: Ruta para obtener una lista de usuarios.
@app.route("/users", methods=["GET"])
def get_users():
    if request.method == "GET":
        # Response simulada indicando "success":
        response = {"payload": "success"}
        return jsonify(response), 200
    
# H - 2: Ruta para agregar un usuario.
@app.route("/user", methods=["POST"])
def post_user():
    if request.method == "POST":
        # Response simulada indicando "success":
        response = {"payload": "success"}
        return jsonify(response), 200

# H - 3: Ruta para eliminar un usuario.
@app.route("/user", methods=["DELETE"])
def delete_user():
    if request.method == "DELETE":
        # Response simulada indicando "success":
        response = {"payload": "success"}    
        return jsonify(response), 200

# H - 4: Ruta para actualizar la información de un usuario.
@app.route("/user", methods=["PUT"])
def put_user():
    if request.method == "PUT":
        # Response simulada indicando "success" y sin errores:
        response = {
            "payload": "success",
            "error": False,
            }                     
        return jsonify(response), 200
    
# H - 5: Ruta para obtener una lista.
@app.route("/api/v1/users", methods=["GET"])
def get_list():
    if request.method == "GET":
        # Response simulada con una lista vacía []:
        response = {"payload": []}    
        return jsonify(response), 200

# H - 6: Ruta para obtener información de un usuario a partir de parámetros de consulta en una URL.
@app.route("/api/v1/user", methods=["POST"])
def get_user():
    if request.method == "POST":
        # Obtener parámetros de consulta en la URL (query params):
        email = request.args.get("email")
        name = request.args.get("name")
        # Validar campos requeridos:
        if not email or not name:
            return jsonify({"error": "Missing fields from request"}), 400
        # Response con los datos proporcionados:
        response = {
            "payload": {
                "email": email,
                "name": name,
            }
        }
        return jsonify(response), 200
    
# H - 7: Ruta para agregar un usuario usando datos enviados en el formulario.
@app.route("/api/v1/user/add", methods=["POST"])
def add_user():
    if request.method == "POST":
        # Obtener datos del formulario:
        email = request.form.get("email")
        name = request.form.get("name")
        user_id = request.form.get("id")
        # Validar campos requeridos:
        if not email or not name or not user_id:
            return jsonify({"error": "Missing fields from request"}), 400
        # Response con los datos proporcionados:
        response = {
            "payload": {
                "email": email,
                "name": name,
                "id": user_id,
            }
        }
        return jsonify(response), 200

# H - 8: Ruta para crear un usuario usando datos en formato JSON.
@app.route("/api/v1/user/create", methods=["POST"])
def create_user():
    if request.method == "POST":
        # Obtener datos JSON:
        data = request.get_json()
        # Validar si se proporcionaron datos:
        if not data:
            return jsonify({"error": "No data provided"}), 400
        # Extraer campos necesarios del JSON:
        email = data.get("email")
        name = data.get("name")
        user_id = data.get("id")
        # Validar campos requeridos:
        if not email or not name or not user_id:
            return jsonify({"error": "Missing fields from request"}), 400
        # Response con los datos proporcionados:
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
