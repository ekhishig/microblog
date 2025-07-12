from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config) # Load configuration from the Config class

from app import routes  # Import routes to register them with the Flask app