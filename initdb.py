from Belly_Button_Biodiversity.app import db
import os

db.create_all()



# source activate pet_pals_env

# pip install gunicorn
# pip install psycopg2
# pip install flask
# pip install flask-sqlalchemy
# pip install pandas

# # Test by initializing DB
# python initdb.py

# # Run app
# FLASK_APP=pet_pals/app.py flask run

# # save package name and version to file
# pip freeze > requirements.txt

# # pet_pals is the name of our Python package (due to __init__.py file)
# echo “web: gunicorn pet_pals.app:app” > Procfile

# # To initialize in Heroku
# heroku run python initdb.py