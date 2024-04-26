from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config) #telling flask to read and apply config.py file

from app import routes