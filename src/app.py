"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Manejador global para cualquier error 500
@app.errorhandler(500)
def handle_server_error(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Obtener a todos los miembros de la familia
@app.route('/members', methods=['GET'])
def obtener_miembros():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Obtener a un miembro de la familia
@app.route('/member/<int:member_id>', methods=['GET'])
def obtener_un_miembro(member_id):
    member = jackson_family.get_member(member_id)
    if member is None:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member), 200

# Añadir un nuevo miembro a la familia
@app.route('/member', methods=['POST'])
def añadir_miembro():
    request_body = request.get_json()
    if not request_body.get("first_name") or not request_body.get("age") or not request_body.get("lucky_numbers"):
        return jsonify({"error": "Invalid member data"}), 400
    
    jackson_family.add_member(request_body)
    return jsonify({"message": "Miembro añadido correctamente"}), 200

# Eliminar un miembro de la familia 
@app.route('/member/<int:id>', methods=['DELETE'])
def eliminar_miembro(id):
    result = jackson_family.delete_member(id)
    if result:
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404
    
    
    



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)