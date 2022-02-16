# Mini Pinteret with Flask for Azure Trial Hackathon

* View demo on https://lmh-flask.azurewebsites.net/

### How to setup on local
```
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
export FLASK_ENV=development
export AZURE_STORAGE_CONNECTION_STRING="your-key"
flask run
```

### Azure Services
- Azure App Service for deployment
- Azure Blog Service for upload file 
- Azure Database for PostgreSQL ( database in production ) - *in processing*
- Computer Vision for Image Analysis, tagging, recommend similar image - *in processing*

### General functionality
- Authenticate users (login/signup pages + logout)
- CRUD Pins
- Upload images
- Like/dislike pins
