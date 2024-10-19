from models.userAuth import db, UserAuth, LoginForm, RegisterForm
from flask import render_template, redirect, url_for, flash, session
from flask_wtf import FlaskForm

def register_user():
	form = RegisterForm()
	if form.validate_on_submit():
		name = form.name.data
		email = form.email.data
		password = form.password.data  


		user = UserAuth(name=name, email=email)
		user.set_password(password)

		db.session.add(user)
		db.session.commit()

		flash('Registration Successful! Please Login.', 'success')
		return redirect(url_for('authroutes.login'))

	return render_template('register.html', form=form)  



def login_user():
	form = LoginForm()
	if form.validate_on_submit():
		email = form.email.data
		password = form.password.data

		user = UserAuth.query.filter_by(email=email).first()

		if user and user.check_password(password):
			session['user_id'] = user.id
			flash('Login Successful!', 'success')
			return redirect(url_for('authroutes.dashboard'))  

		else:
			flash('Login failed. Please check your email and password', 'danger')
	return render_template('login.html', form=form)


def show_dashboard():
	if 'user_id' in session:
		user_id = session['user_id']
		user = UserAuth.query.get(user_id)
		if user:
			return render_template('dashboard.html',user=user.name,email=user.email)

	return redirect(url_for('authroutes.login'))


def logout_user():
	session.pop('user_id', None)
	flash("You have been logged out successfully.", 'success')
	return redirect(url_for('authroutes.login'))
