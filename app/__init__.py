from flask import Flask

app = Flask(__name__)
#app.config.from_object('config')
app.config.from_object(app.config)


#The import statment comes after the flask object is initialized to avoid circular reference
from app import views
