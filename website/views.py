from flask import Blueprint

# defines URLs
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"