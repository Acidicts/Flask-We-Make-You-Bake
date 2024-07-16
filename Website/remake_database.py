from Website import create_app
from Website.extensions import db
from flask_migrate import upgrade

app = create_app()

def remake_database():
    with app.app_context():
        # Reflect and drop all tables
        db.reflect()
        db.drop_all()

        # Create all tables
        db.create_all()

        # Apply migrations
        upgrade()

if __name__ == "__main__":
    remake_database()
