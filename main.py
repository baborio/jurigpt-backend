from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    consulta = data.get("consulta", "")
    respuesta = f"Has preguntado: {consulta}. Esta función debería procesar eso."
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)