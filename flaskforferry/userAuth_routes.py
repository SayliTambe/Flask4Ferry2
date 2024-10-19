from flask import Blueprint
from controllers.userAuth import register_user, login_user, show_dashboard, logout_user
#from models import UserAuth  

authroutes = Blueprint('authroutes', __name__)

@authroutes.route('/register', methods=['GET', 'POST'])
def register():
  return register_user()

@authroutes.route('/login', methods=['GET', 'POST'])
def login():
  return login_user()

@authroutes.route('/dashboard')
def dashboard():
  return show_dashboard()

@authroutes.route('/logout')
def logout():
  return logout_user()
