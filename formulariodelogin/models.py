from formulariodelogin import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(usuario_id):
    return Usuario.query.get(int(usuario_id))


class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    senha = db.Column(db.String, nullable=False)
    foto_perfil = db.Column(db.String, default='default.jpg')




