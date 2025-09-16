from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'CAMBIA_POR_UNA_CLAVE_SECRETA'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET','POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            nota1 = float(request.form.get('nota1', 0))
            nota2 = float(request.form.get('nota2', 0))
            nota3 = float(request.form.get('nota3', 0))
            asistencia = float(request.form.get('asistencia', 0))
        except ValueError:
            flash('Ingrese valores numéricos válidos.')
            return redirect(url_for('ejercicio1'))

        for n in (nota1, nota2, nota3):
            if not (10 <= n <= 70):
                flash('Cada nota debe estar entre 10 y 70.')
                return redirect(url_for('ejercicio1'))
        if not (0 <= asistencia <= 100):
            flash('La asistencia debe ser entre 0 y 100.')
            return redirect(url_for('ejercicio1'))

        promedio = round((nota1 + nota2 + nota3) / 3, 2)
        estado = 'Aprobado' if (promedio >= 40 and asistencia >= 75) else 'Reprobado'
        return render_template('resultado1.html', notas=[nota1, nota2, nota3],
                               promedio=promedio, asistencia=asistencia, estado=estado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET','POST'])
def ejercicio2():
    if request.method == 'POST':
        n1 = request.form.get('nombre1', '').strip()
        n2 = request.form.get('nombre2', '').strip()
        n3 = request.form.get('nombre3', '').strip()

        if not (n1 and n2 and n3):
            flash('Ingrese los tres nombres.')
            return redirect(url_for('ejercicio2'))

        lowered = {n1.lower(), n2.lower(), n3.lower()}
        if len(lowered) < 3:
            flash('Los nombres deben ser diferentes.')
            return redirect(url_for('ejercicio2'))

        nombres = [n1, n2, n3]
        longitudes = {n: len(n) for n in nombres}
        max_len = max(longitudes.values())
        nombres_max = [n for n, l in longitudes.items() if l == max_len]

        return render_template('resultado2.html', nombres_max=nombres_max, max_len=max_len, nombres=nombres)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
