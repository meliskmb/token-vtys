from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import jwt
import datetime
from config import Config
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt = Bcrypt(app)
CORS(app)

with app.app_context():
    db.create_all()

# Kullanıcı Kaydı – /register
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email ve şifre gereklidir.'}), 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'Bu email zaten kayıtlı.'}), 400

    # Şifreyi hash'le
    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

    # Yeni kullanıcıyı oluştur
    new_user = User(email=email, password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Kayıt başarılı!'}), 201

#JWT TOKEN VE LOGIN
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email ve şifre gereklidir.'}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': 'Geçersiz giriş bilgileri.'}), 401

    # Token oluştur
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60)  # 1 dakika
    }

    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token}), 200

from functools import wraps
# token kontrol fonksiyonu
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]

        if not token:
            return jsonify({'message': 'Token eksik.'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(data['user_id'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token süresi dolmuş.'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Geçersiz token.'}), 401

        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/protected', methods=['GET'])
@token_required
def protected(current_user):
    return jsonify({
        'message': f"Hoş geldin, {current_user.email}! Burası korumalı alan."
    })

if __name__ == '__main__':
    app.run(debug=True)