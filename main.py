from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form.get('nombre', '')
        edad = int(request.form.get('edad', 0))
        tarros = int(request.form.get('tarros', 0))

        precio_por_tarro = 9000
        total_sin_descuento = tarros * precio_por_tarro

        if 18 <= edad <= 30:
            porcentaje_descuento = 0.15
        elif edad > 30:
            porcentaje_descuento = 0.25
        else:
            porcentaje_descuento = 0.0

        descuento = float(total_sin_descuento * porcentaje_descuento)
        total_pagar = float(total_sin_descuento - descuento)

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'descuento': descuento,
            'total_pagar': total_pagar
        }

    return render_template('ejercicio1.html', resultado=resultado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form.get('usuario', '')
        contrasena = request.form.get('contrasena', '')

        if usuario == "juan" and contrasena == "admin":
            mensaje = "Bienvenido administrador juan"
        elif usuario == "pepe" and contrasena == "user":
            mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)