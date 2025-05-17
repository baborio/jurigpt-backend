from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    import openai
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    consulta = data.get("consulta", "")

    prompt = f"""Analiza si los hechos siguientes podrían constituir un delito según el Código Penal español. 
    Indica el artículo aplicable, su interpretación y un ejemplo práctico similar. Hechos: {consulta}"""

    try:
        respuesta_openai = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente jurídico experto en derecho penal español."},
                {"role": "user", "content": prompt}
            ]
        )
        respuesta = respuesta_openai["choices"][0]["message"]["content"].strip()
    except Exception as e:
        respuesta = f"Error al procesar la consulta: {str(e)}"

    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
