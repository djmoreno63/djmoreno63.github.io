from flask import Flask , render_template

#render_template crea un plantilla donde podemos llamarla en el return para que todo se ejecute global

#rutas del servidor variable app
app=Flask(__name__)

#utilizar un decorador y metodo route, pasa el nombre para crear una url

@app.route('/')

#Retorna un texto

def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/h')   
def h():
    return render_template('h.html')

@app.route('/c')   
def c():
    return render_template('c.html')

@app.route('/p')   
def p():
    return render_template('p.html')

#Se debe mantener en escucha la aplicacion siempre
if __name__ == '__main__':

#debug=true -> especifica que refresca la pagina sin usar 'python pagina.py'
    app.run(debug = True)
