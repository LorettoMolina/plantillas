from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)

app.secret_key = 'una_clave_muy_secreta_123'


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
        
        if password != confirm_password:
            flash("La contraseña no coincide", "error")
            return render_template('registro.html')
        else:
            print(f"Registrado: {username}, Correo: {email}, Contraseña: {password}, Género: {gender}")
            flash("Usuario registrado exitosamente", "success")
            return redirect(url_for('inicio'))
    
    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        print(f"Iniciado sesión: {username}")
        return redirect(url_for('inicio')) 
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
