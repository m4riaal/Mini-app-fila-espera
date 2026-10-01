from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

fila = []
proximo_id = 1


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/fila", methods=["GET"])
def listar_fila():
    return jsonify(fila)


@app.route("/api/clientes", methods=["POST"])
def cadastrar_cliente():
    global proximo_id

    dados = request.get_json()
    nome = dados.get("nome", "").strip()

    if not nome:
        return jsonify({"erro": "Informe o nome do cliente."}), 400

    cliente = {
        "id": proximo_id,
        "senha": f"{proximo_id:03d}",
        "nome": nome,
        "status": "Aguardando",
        "entrada": datetime.now().strftime("%H:%M:%S")
    }

    fila.append(cliente)
    proximo_id += 1

    return jsonify(cliente), 201


@app.route("/api/clientes/proximo", methods=["POST"])
def chamar_proximo():
    for cliente in fila:
        if cliente["status"] == "Aguardando":
            cliente["status"] = "Em atendimento"
            return jsonify(cliente)

    return jsonify({"erro": "Não há clientes aguardando."}), 404


@app.route("/api/clientes/<int:cliente_id>/status", methods=["PUT"])
def alterar_status(cliente_id):
    dados = request.get_json()
    novo_status = dados.get("status")

    status_validos = [
        "Aguardando",
        "Em atendimento",
        "Concluído",
        "Cancelado"
    ]

    if novo_status not in status_validos:
        return jsonify({"erro": "Status inválido."}), 400

    for cliente in fila:
        if cliente["id"] == cliente_id:
            cliente["status"] = novo_status
            return jsonify(cliente)

    return jsonify({"erro": "Cliente não encontrado."}), 404


@app.route("/api/clientes/<int:cliente_id>/cancelar", methods=["PUT"])
def cancelar_cliente(cliente_id):
    for cliente in fila:
        if cliente["id"] == cliente_id:
            cliente["status"] = "Cancelado"
            return jsonify(cliente)

    return jsonify({"erro": "Cliente não encontrado."}), 404


if __name__ == "__main__":
    app.run(debug=True)
