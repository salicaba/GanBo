from flask import Flask, jsonify, request
from flask_cors import CORS
from modelos import ContabilidadModel

app = Flask(__name__)
CORS(app)

@app.route('/api/balance/<tipo>', methods=['POST'])
def get_balance(tipo):
    # Recibimos la lista de asientos desde el Frontend
    asientos = request.json.get('asientos', [])
    data = ContabilidadModel.obtener_datos(tipo, asientos)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)