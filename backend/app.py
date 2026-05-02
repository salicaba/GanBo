from flask import Flask, jsonify, request
from flask_cors import CORS
from modelos import ContabilidadModel
from modelos import registrar_arqueo_bd

app = Flask(__name__)
CORS(app)

@app.route('/api/balance/<tipo>', methods=['POST'])
def get_balance(tipo):
    # Recibimos la lista de asientos desde el Frontend
    asientos = request.json.get('asientos', [])
    data = ContabilidadModel.obtener_datos(tipo, asientos)
    return jsonify(data)

@app.route('/api/tesoreria/arqueo', methods=['POST'])
def procesar_arqueo():
    try:
        datos = request.get_json()
        exito = registrar_arqueo_bd(datos)

        if exito:
            return jsonify({"status": "success", "message": "Arqueo registrado exitosamente."}), 201
        else:
            return jsonify({"status": "error", "message": "Error interno del servidor."}), 500

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)