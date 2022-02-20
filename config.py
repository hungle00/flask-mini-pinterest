import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = 'development key' # keep this key secret during production
if os.getenv('FLASK_ENV') == 'development':
    DB_PATH = os.path.join(os.path.dirname(__file__), 'pin.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_PATH) # development
else:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')     # production
    
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
SUBSCRIPTION_KEY = os.getenv('SUBSCRIPTION_KEY')
ENDPOINT = os.getenv('ENDPOINT')
