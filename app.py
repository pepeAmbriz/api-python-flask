from flask import Flask, jsonify, request

app = Flask(__name__)
from producto import productos

@app.route('/productos', methods=['GET'])
def obtenerProductos():
    return jsonify(productos)     

@app.route("/producto/<string:prodNombre>",methods=['GET'])
def obtenerProducto(prodNombre):
    productoEncontrado  = [producto for producto in productos if producto["Nombre"] == prodNombre ]
    if len(productoEncontrado) > 0:
         return jsonify({"producto":productoEncontrado})
    return jsonify({"mensage": 404})

@app.route("/producto",methods=['POST'])
def GuardarProducto ():
    new_Product = {
        "Nombre": request.json["Nombre"],
        "Precio": request.json["Precio"],
        "Cantidad": request.json["Cantidad"]
    }
    productos.append(new_Product)
    return jsonify({"productos":productos})

@app.route('/producto/<string:ProdNombre>', methods=['PUT'])
def editarProducto(ProdNombre):
    productoEncontrado = [producto for producto in productos if producto["Nombre"] == ProdNombre]
    if len(productoEncontrado) > 0:
        productoEncontrado[0]["Nombre"] = request.json["Nombre"]
        productoEncontrado[0]["Precio"] = request.json["Precio"]
        productoEncontrado[0]["Cantidad"] = request.json["Cantidad"]
        return jsonify({"producto":productoEncontrado[0]})
    return jsonify({"mensage": 404})

@app.route('/producto/<string:ProdNombre>', methods=['DELETE'])
def eliminarProducto(ProdNombre):
    productoEncontrado = [producto for producto in productos if producto["Nombre"] == ProdNombre]
    if len(productoEncontrado) > 0:
        productos.remove(productoEncontrado[0])
        return jsonify({"mensage":"eliminado","productos":productos})
    return jsonify({"mensage": "no encontrado"})


if __name__ == "__main__":
    app.run(debug=True, port=4000)