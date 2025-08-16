import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    """Provide a shell context for Flask's shell command."""
    return {
        'sa': sa,
        'so': so,
        'db': db,
        'User': User,
        'Post': Post
    }