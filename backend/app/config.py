# filepath: c:\Users\Alexs\APP MERCADO\backend\app\config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-secreta'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:22121396jG@@localhost/mercado'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-chave-secreta'