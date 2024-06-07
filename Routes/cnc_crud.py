from flask import Blueprint,request,jsonify
from Connection.Db_connect import db
from models.cnc_programs import CNCPrograms

cncCrud_bp= Blueprint('cnc_crud',__name__)
    
@cncCrud_bp.route('/add_programs', methods=['POST'])
def create_programs():
    try:
        data = request.get_json()
        cnc_program = CNCPrograms(data['name'], data['description'], data['content'])
        db.session.add(cnc_program)
        db.session.commit()
        return jsonify(cnc_program.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@cncCrud_bp.route('/cnc_programs',methods=['GET'])
def get_programs():
    try:
        cnc_programs = CNCPrograms.query.all()
        return jsonify([cnc_program.to_dict() for cnc_program in cnc_programs])
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@cncCrud_bp.route('/cnc_programs/<int:id>', methods=['GET'])
def get_program(id):
    try:
        cnc_program = CNCPrograms.query.get(id)
        return jsonify(cnc_program.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cncCrud_bp.route('/cnc_programs/<int:id>', methods=['PUT'])
def update_program(id):
    try:
        data = request.get_json()
        cnc_program = CNCPrograms.query.get(id)
        cnc_program.name = data['name']
        cnc_program.description = data['description']
        cnc_program.content = data['content']
        db.session.commit()
        return jsonify(cnc_program.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cncCrud_bp.route('/cnc_programs/<int:id>', methods=['DELETE'])
def delete_program(id):
    try:
        cnc_program = CNCPrograms.query.get(id)
        db.session.delete(cnc_program)
        db.session.commit()
        return jsonify({'message': 'Program deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500