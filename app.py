from dbm import error

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    errores = []
    if request.method == "POST":
        try:
            n1 = float(request.form.get("nota1", ""))
            n2 = float(request.form.get("nota2", ""))
            n3 = float(request.form.get("nota3", ""))
            asistencia = float(request.form.get("asistencia", ""))

            #validaciones de rango
            if not (10 <= n1 <= 70 and 10 <= n2 <= 70 and 10 <= n3 <= 70):
                errores.append("Las notas deben estar entre 10 y 70.")
            if not (0 <= asistencia <= 100):
                errores.append("La asistencia debe estar entre 0 y 100.")

            if not errores:
                promedio = round((n1 + n2 + n3) / 3, 1)
                estado = "Aprobado" if (promedio >= 40 and asistencia >= 75) else "Reprobado"
                resultado = {"promedio": promedio, "asistencia": asistencia, "estado": estado}
        except ValueError:
            errores.append("Completa todos los campos con valores numéricos válidos.")

    return render_template("ejercicio1.html", resultado=resultado, errores=errores)

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    salida = None
    error = None
    if request.method == "POST":
        a = (request.form.get("nombre1") or "").strip()
        b = (request.form.get("nombre2") or "").strip()
        c = (request.form.get("nombre3") or "").strip()

        if not a or not b or not c:
            error = "Ingresa los tres nombres."
        elif len({a.lower(), b.lower(), c.lower()}) < 3:
            error = "Los tres nombres deben ser diferentes."
        else:
            # nombre con mayor cantidad de caracteres
            mayor = max([a, b, c], key=lambda x: len(x))
            salida = {"nombre": mayor, "largo": len(mayor)}

    return render_template("ejercicio2.html", salida=salida, error=error)

if __name__ == "__main__":
   app.run(debug=True)  # modo debug para desarrollo

