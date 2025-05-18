from flask import Flask, request, jsonify
from flask_cors import CORS
from schema import schema

app = Flask(__name__)
CORS(app)  

@app.route("/shopAPI", methods=["POST"])
def procesar_consulta_graphql():
    contenido = request.get_json()

    if contenido is None or "query" not in contenido:
        return jsonify({"error": "No se proporcionó una consulta válida"}), 400

    resultado = schema.execute(
        contenido["query"],
        variables=contenido.get("variables"),
        operation_name=contenido.get("operationName")
    )

    respuesta = {}
    if resultado.errors:
        respuesta["errors"] = [str(err) for err in resultado.errors]
    if resultado.data:
        respuesta["data"] = resultado.data

    return jsonify(respuesta)

@app.route("/", methods=["GET"])
def pagina_inicio():
    return """
    <html>
        <head><title>API GraphQL</title></head>
        <body>
            <h2>Accede a la API de la tienda en GraphQL desde <code>/shopAPI</code></h2>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
