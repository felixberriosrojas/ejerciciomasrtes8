from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='template', static_folder='static')
registros = []

@app.route('/')
def index():
    return redirect(url_for('registro'))

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario_registrado = {
            'nombre': request.form.get('nombre'),
            'apellido': request.form.get('apellido'),
            'edad': request.form.get('edad')
        }
        registros.append(usuario_registrado)
        return redirect(url_for('lista'))
    return render_template('registro.html')

@app.route('/lista')
def lista():
    return render_template('lista.html', registros=registros)

if __name__ == '__main__':
    app.run(debug=True)