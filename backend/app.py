from flask import Flask, jsonify
from flask_cors import CORS
from modelos import ContabilidadModel

app = Flask(__name__)
CORS(app)

@app.route('/api/balance/<tipo>', methods=['GET'])
def get_balance(tipo):
    # Ya no busca archivos, pide el dato directo al modelo
    data = ContabilidadModel.obtener_datos(tipo)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)