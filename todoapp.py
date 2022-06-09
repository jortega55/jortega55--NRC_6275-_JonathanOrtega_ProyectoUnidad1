#Importar la biblioteca de flask
from flask import Flask, redirect, render_template, request, url_for, flash


#Objeto para inicilizar la aplicacion
#1. nombre por defecto
#2. ruta donde esta los templates o nombre de la carpeta
app = Flask(__name__, template_folder='plantillas')

#Clave secreta de la aplicacion
app.secret_key = '123456789'


#Arreglo para almacenar las tareas
lista_tareas = []

#Controlador de la ruta por defecto
# Ingreso de datos por formulario
# Mostras las tareas pendientes
@app.route('/')
def principal():
    return render_template('principal.html', lista_tareas=lista_tareas)

@app.route('/agro')
def agro():
    return render_template('agro.html')

@app.route('/bio')
def bio():
    return render_template('bio.html')

@app.route('/docentes')
def docentes():
    return render_template('docentes.html')

@app.route('/dosk')
def dosk():
    return render_template('dosk.html')

@app.route('/entrenamiento')
def entrenamiento():
    return render_template('entrenamiento.html')

@app.route('/estiramiento')
def estiramiento():
    return render_template('estiramiento.html')

@app.route('/itin')
def itin():
    return render_template('itin.html')

@app.route('/Rfisica')
def Rfisica():
    return render_template('Rfisica.html')

@app.route('/salud')
def salud():
    return render_template('salud.html')

@app.route('/tresk')
def tresk():
    return render_template('tresk.html')

@app.route('/unok')
def unok():
    return render_template('unok.html')

#Controlador para enviar los datos
@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':

        tarea_descripcion = request.form['tarea_descripcion']
        tarea_correo = request.form['tarea_correo']
        tarea_prioridad = request.form['tarea_prioridad']


        if tarea_descripcion == '' or tarea_correo == '':
            flash('Por favor ingresar todos los campos de texto  y verificar que no esten vacios')
            return redirect(url_for('principal'))
        else:

            flash('Te encunetras Inscrito, te esperamos en el punto de partida!!!!')

            lista_tareas.append({'tarea_descripcion': tarea_descripcion, 'tarea_correo': tarea_correo, 'tarea_prioridad': tarea_prioridad })

            return redirect(url_for('principal'))

#Controlador de la ruta para borrar
@app.route('/borrar', methods=['POST'])
def borrar():
    if request.method == 'POST':
        
        if lista_tareas == []:

            flash('No existen tareas en la lista')
            return redirect(url_for('principal'))

        else:
            lista_tareas.clear()
            flash('')
            return redirect(url_for('principal'))


#Metodo para correr la aplicacion
if __name__ == '__main__':
    app.run(debug=True)