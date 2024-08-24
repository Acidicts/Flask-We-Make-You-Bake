# Website/extensions.py
from flask_sqlalchemy import SQLAlchemy

try :
    del db
except:
    pass

db = SQLAlchemy()
