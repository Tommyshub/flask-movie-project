from flask import Blueprint, render_template, abort, json
from werkzeug.exceptions import HTTPException

error_handlers = Blueprint("error_handlers", __name__, 
static_folder="static", template_folder="templates/errors/")

error_messages = {
    401: ('Unauthorized!', 'You are not unauthorized to view this page.'),
    403: ('Forbidden!', 'You are not authorized to view this page.'),
    404: ('Not Found!', 'The page cannot be found on this server.'),
    405: ('Method Not Allowed!', 'Method is not supported for the requested resource.'),
    500: ('Server Error!', 'There has been an error with the server'),
    502: ('Bad Gateway!', 'Bad or invalid gateway.'),
    503: ('Service Unavailable!', 'This service is temporarily unavailable.'),
    504: ('Gateway Timeout!', 'The connection to the server was lost.')
}

