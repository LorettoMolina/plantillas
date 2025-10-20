from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'una_clave_muy_secreta_123'

correos_registrados = []
@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/animales')
def animales():
    return render_template('animales.html')

@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html')

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        gender = request.form['gender']

        if email in correos_registrados:
            flash("El correo electrónico ya está registrado. Intenta con otro.", "error")
            return render_template('registro.html')
        if password != confirm_password:
            flash("Las contraseñas no coinciden.", "error")
            return render_template('registro.html')
        
        
        correos_registrados.append(email)
        flash("Registro exitoso. ¡Bienvenido/a!", "success")
        print(f"Usuario registrado: {username} - {email}")
        return redirect(url_for('inicio'))
    
    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Inicio de sesión de {username}")
        flash("Inicio de sesión exitoso.", "success")
        return redirect(url_for('inicio'))
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
