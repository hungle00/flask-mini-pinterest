# Mini Pinteret with Flask for Azure Trial Hackathon

* View demo on https://lmh-pinterest.azurewebsites.net

### How to setup on local
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
export FLASK_ENV=development
```
Rename .env.example to .env and put your key.
```
flask run
```

### Azure Services
- Azure App Service for deployment
- Azure Blog Service for upload file 
- Azure Database for PostgreSQL ( database in production ) 
- Computer Vision for Image Analysis, tagging, recommend similar image

### General functionality
- Authenticate users (login/signup pages + logout)
- CRUD Pins
- Upload images as a pin
- Search pins by tag
- Recomendation similar image by tagging
