from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
    error = None  
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        gender = request.form['gender']
        
        
        if password != confirm_password:
            error = "La contraseña no coincide"  
        else:
            print(f"Registrado: {username}, Correo: {email}, Contraseña: {password}, Género: {gender}")
            return redirect(url_for('inicio'))  
        
    return render_template('registro.html', error=error) 

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
