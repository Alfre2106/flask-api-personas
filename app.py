from flask import Flask, jsonify

app = Flask(__name__)

# Lista de nombres de ejemplo
nombres = ["Alfredo", "Miguel", "Carlos", "Daniela", "Alberto", "Luisa"]

@app.route('/personas', methods=['GET'])
def obtener_personas():
    """
    Endpoint para obtener una lista de nombres de personas.
    Retorna un JSON con la lista de nombres.
    """
    return jsonify({"personas": nombres})

if __name__ == '__main__':
    app.run(debug=True)
