from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'una_clave_muy_secreta_123'


usuarios_registrados = {}

@app.route('/')
def inicio():
    return render_template('inicio.html', logueado='usuario' in session, usuario=session.get('usuario'))

@app.route('/animales')
def animales():
    return render_template('animales.html', logueado='usuario' in session, usuario=session.get('usuario'))

@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html', logueado='usuario' in session, usuario=session.get('usuario'))

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html', logueado='usuario' in session, usuario=session.get('usuario'))

@app.route('/acerca')
def acerca():
    return render_template('acerca.html', logueado='usuario' in session, usuario=session.get('usuario'))



@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if email in usuarios_registrados:
            flash("El correo ya está registrado.", "error")
            return render_template('registro.html')

        if password != confirm_password:
            flash("Las contraseñas no coinciden.", "error")
            return render_template('registro.html')

        usuarios_registrados[email] = {'username': username, 'password': password}
        flash("Registro exitoso. Ya puedes iniciar sesión.", "success")
        return redirect(url_for('login'))

    return render_template('registro.html')



@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')



@app.route('/validaLogin', methods=['POST'])
def validaLogin():
    email = request.form['email']
    password = request.form['password']

    usuario = usuarios_registrados.get(email)

    if not usuario or usuario['password'] != password:
        flash("Correo o contraseña incorrectos.", "error")
        return redirect(url_for('login'))

    session['usuario'] = usuario['username']
    flash(f"Bienvenido {usuario['username']}!", "success")
    return redirect(url_for('inicio'))



@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash("Has cerrado sesión correctamente.", "info")
    return redirect(url_for('inicio'))


if __name__ == '__main__':
    app.run(debug=True)
