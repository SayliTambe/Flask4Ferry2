import urllib.parse

password = 'Khoji@123'
encoded_password = urllib.parse.quote_plus(password)

class Config:
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://khoji:{encoded_password}@144.24.96.48:3306/FerryOne'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'ganesh'
    SQLALCHEMY_DATABASE_URI_auth = f'mysql+pymysql://khoji:{encoded_password}@144.24.96.48:3306/FerryOne'
