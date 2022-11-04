from formulariodelogin import app
from formulariodelogin import db


with app.app_context():
    if __name__ == '__main__':
        app.run(debug=True)
        db.create_all()