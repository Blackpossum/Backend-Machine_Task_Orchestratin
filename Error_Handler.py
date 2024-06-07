from flask import Blueprint, jsonify

error_bp = Blueprint('error_handlers', __name__)

@error_bp.app_errorhandler(400)
def bad_request(error):
    response = jsonify({'error': 'Bad Request', 'message': str(error)})
    response.status_code = 400
    return response

@error_bp.app_errorhandler(404)
def not_found(error):
    response = jsonify({'error': 'Not Found', 'message': str(error)})
    response.status_code = 404
    return response

@error_bp.app_errorhandler(500)
def internal_error(error):
    response = jsonify({'error': 'Internal Server Error', 'message': str(error)})
    response.status_code = 500
    return response

@error_bp.app_errorhandler(Exception)
def unhandled_exception(error):
    response = jsonify({'error': 'Unhandled Exception', 'message': str(error)})
    response.status_code = 500
    return response
