import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = 'development key' # keep this key secret during production
if os.getenv('FLASK_ENV') == 'development':
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
else:   # production
    db_user =  os.getenv('db_user')
    db_pass =  os.getenv('db_pass')
    db_host =  os.getenv('db_host')
    db_port = '5432'
    db_name = 'pinterest_dev'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{}:{}@{}:{}/{}?sslmode=require".format(db_user, db_pass, db_host, db_port, db_name)

SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
AZURE_STORAGE_REMOTE=  os.getenv("AZURE_STORAGE_REMOTE")
SUBSCRIPTION_KEY = os.getenv('SUBSCRIPTION_KEY')
ENDPOINT = os.getenv('ENDPOINT')
