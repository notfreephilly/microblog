import os

# storing configuration variables

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' # used to generate signatures or tokens

