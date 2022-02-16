import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'db.sqlite')
AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING')