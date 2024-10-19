from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from controllers.user import add_user_function, edit_user_function, delete_user_function
from models.users import User

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    data = User.query.all()
    return render_template('insertport.html', data=data)

@main.route('/adduser', methods=['GET', 'POST'])
def add_user():
    return add_user_function()

@main.route('/edituser/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    return edit_user_function(user_id)

@main.route('/deleteuser/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    return delete_user_function(user_id)

@main.route('/updatestatus/<int:user_id>', methods=['POST'])
def update_status(user_id):
    data = request.get_json()
    status = data.get('status')
    user = User.query.get(user_id)
    if user:
        user.status = status
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False})
