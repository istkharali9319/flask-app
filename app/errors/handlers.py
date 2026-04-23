from flask import jsonify
import app.utils.response as response
from werkzeug.exceptions import HTTPException

def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception(e):
        return response.error_response(str(e), 500)

    @app.errorhandler(404)
    def not_found(_error):
        return response.error_response("Resource not found",404)
        # return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(500)
    def internal_error(_error):
        return response.error_response("Internal server error",500)
        return jsonify({"error": "Internal server error"}), 500

    @app.errorhandler(405)
    def method_not_allowed(_error):
        return response.error_response("The method is not allowed for the requested URL.",405)

   