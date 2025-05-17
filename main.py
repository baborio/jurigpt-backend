from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

# Clave de API desde variables de entorno en Render
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    consulta = data.get("consulta", "")

    if not consulta:
        return jsonify({"respuesta": "Por favor, escribe una consulta válida."})

    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un experto en Derecho Penal español. El usuario te describirá una situación y tú debes indicar si es delito, qué artículo del Código Penal se aplica, cómo se interpreta y un ejemplo práctico."
                },
                {
                    "role": "user",
                    "content": consulta
                }
            ]
        ).choices[0].message.content

        return jsonify({"respuesta": respuesta})

    except Exception as e:
        return jsonify({"respuesta": f"Ha ocurrido un error: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
