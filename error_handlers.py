from flask import Blueprint, render_template, abort, json
from werkzeug.exceptions import HTTPException

error_handlers = Blueprint("error_handlers", __name__, 
static_folder="static", template_folder="templates/errors/")


# Error handler for attribute errors 
@error_handlers.app_errorhandler(Exception)
def handle_bad_request(e):
    if type(AttributeError):
        return render_template("error.html")
    return render_template("error.html")


# Error handler for 403 unauthorized
@error_handlers.app_errorhandler(401)
def unauthorized(e):
    return render_template("401.html")


# Error handler for 403 forbidden
@error_handlers.app_errorhandler(403)
def forbidden(e):
    return render_template("403.html")


# Error handler for 404 not found
@error_handlers.app_errorhandler(404)
def not_found(e):
    return render_template("404.html")


# Error handler for 405 method not allowed
@error_handlers.app_errorhandler(405)
def not_allowed(e):
    return render_template("405.html")


# Error handler for 500 server error
@error_handlers.app_errorhandler(500)
def server_error(e):
    return render_template("500.html")


# Error handler for 501 not implemented
@error_handlers.app_errorhandler(501)
def not_implemented(e):
    return render_template("501.html")


# Error handler for 502 bad gateway
@error_handlers.app_errorhandler(502)
def bad_gateway(e):
    return render_template("502.html")


# Error handler for 503 service unavailable
@error_handlers.app_errorhandler(503)
def service_unavailable(e):
    return render_template("503.html")


# Error handler for 504 gateway timeout
@error_handlers.app_errorhandler(504)
def gateway_timeout(e):
    return render_template("504.html")