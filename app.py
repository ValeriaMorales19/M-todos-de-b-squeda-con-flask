from flask import Flask, render_template, request, redirect, url_for
from algoritmos_busqueda import busqueda_secuencial, busqueda_binaria
import random

app = Flask(__name__)

def generar_lista(ordenada=False, n=10):
    lista = [random.randint(1, 99) for _ in range(n)]
    if ordenada:
        lista.sort()
    return lista

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/secuencial', methods=['GET', 'POST'])
def secuencial():
    resultado = None
    lista = []
    valor = ''
    comparaciones = 0
    if request.method == 'POST':
        if 'generar' in request.form:
            lista = generar_lista()
        else:
            lista = [int(x) for x in request.form['lista'].split(',') if x.strip().isdigit()]
            valor = int(request.form['valor']) if request.form['valor'].isdigit() else ''
            if valor != '':
                resultado, comparaciones = busqueda_secuencial(lista, valor)
    else:
        lista = generar_lista()
    return render_template('busqueda_secuencial.html', lista=lista, resultado=resultado, valor=valor, comparaciones=comparaciones, enumerate=enumerate)

@app.route('/binaria', methods=['GET', 'POST'])
def binaria():
    resultado = None
    lista = []
    valor = ''
    comparaciones = 0
    if request.method == 'POST':
        if 'generar' in request.form:
            lista = generar_lista(ordenada=True)
        else:
            lista = [int(x) for x in request.form['lista'].split(',') if x.strip().isdigit()]
            lista.sort()
            valor = int(request.form['valor']) if request.form['valor'].isdigit() else ''
            if valor != '':
                resultado, comparaciones = busqueda_binaria(lista, valor)
    else:
        lista = generar_lista(ordenada=True)
    return render_template('busqueda_binaria.html', lista=lista, resultado=resultado, valor=valor, comparaciones=comparaciones, enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)