from flask import render_template, request, redirect, url_for, flash, jsonify
from models.users import db, User

def add_user_function():
    if request.method == "POST":
        portname = request.form.get('portname')
        state = request.form.get('state')
        address = request.form.get('address')
        portcity = request.form.get('portcity')
        contact = request.form.get('contact')
        
        if portname and state and address and portcity and contact:
            new_user = User(
                portname=portname, 
                state=state, 
                address=address, 
                portcity=portcity, 
                contact=contact,
                port_status='active'  # This should now work
            )
            try:
                db.session.add(new_user)
                db.session.commit()
                # Return HTML with JavaScript for the alert and redirect
                return """
                <html>
                    <body>
                        <script>
                            alert('Added Successfully');
                            window.location.href = '/';
                        </script>
                    </body>
                </html>
                """
            except Exception as e:
                db.session.rollback()
                flash('Error: ' + str(e))
    
    return render_template('adduser.html')



def edit_user_function(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if request.method == "POST":
        user.portname = request.form.get('portname')
        user.state = request.form.get('state')
        user.address = request.form.get('address')
        user.portcity = request.form.get('portcity')
        user.contact = request.form.get('contact')
        
        try:
            db.session.commit()
            flash('PORT UPDATED SUCCESSFULLY')
            return redirect(url_for('main.home'))
        except Exception as e:
            db.session.rollback()
            flash('Error: ' + str(e))
    return render_template('edituser.html', user=user)

def delete_user_function(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if request.method == "POST":
        try:
            db.session.delete(user)
            db.session.commit()
            flash('PORT DELETED SUCCESSFULLY')
            return """
            <script>
                alert("PORT DELETED SUCCESSFULLY");
                window.location.href = "/";
            </script>
            """
        except Exception as e:
            db.session.rollback()
            return jsonify({
                "error": "Internal server error",
                "message": str(e)
            }), 500

    return render_template('deleteuser.html', user=user)
