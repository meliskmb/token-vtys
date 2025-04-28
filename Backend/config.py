import os

class Config:
    SECRET_KEY = "my-super-secret-key"  # JWT için gizli anahtar
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  # SQLite veritabanı
    SQLALCHEMY_TRACK_MODIFICATIONS = False