import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from flask import Blueprint, request, jsonify
from Services.UserService import UserService
from Services.TicketService import TicketService


user_blueprint = Blueprint('user', __name__)
user_service = UserService()

ticket_blueprint = Blueprint('ticket', __name__)
ticket_service = TicketService()

@user_blueprint.route('/submitUser', methods=['POST'])
def submitUser():
    data = request.json
    cedula = data.get('cedula')
    nombres = data.get('nombres')
    apellidos = data.get('apellidos')
    email = data.get('email')
    contrasena = data.get('contrasena')
    telefono = data.get('telefono')
    residencia = data.get('residencia')

    if not cedula or not nombres or not apellidos or not email or not contrasena or not telefono or not residencia:
        return jsonify({'error': 'Faltan campos'}), 400

    user = user_service.insertUser(cedula, nombres, apellidos, email, contrasena, telefono, residencia)
    return jsonify(user.ToJSON()), 201

@user_blueprint.route('/<int:cedula>', methods=['GET'])
def get_user(cedula):
    user = user_service.selectUser(cedula)
    if user:
        return jsonify(user.ToJSON())
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    
@ticket_blueprint.route('/<int:serie>,<int:numero>', methods=['GET'])
def get_ticket(serie,numero):
    ticket = ticket_service.selectTicket(serie,numero)
    if ticket:
        return jsonify(ticket.toJSON())
    else:
        return jsonify({'error': 'Tiquete no encontrado'}), 404
