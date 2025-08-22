from flask import Flask, render_template, request, jsonify
import json
import os
import uuid # BIBLIOTECA DE ID

app = Flask(__name__)

def load_user():
    try:
        if os.path.exists("usuarios.json"):
            with open("usuarios.json", "r", encoding="utf-8") as archive:
                return json.load(archive) # CARREGA O ARQUIVO USUARIOS E RETORNA NA VARIAVEL USUARIOS
        else:
            return [] # CASO CONTRÁRIO RETORNA ARRAY VAZIO
    except:
        return []

def save_user(usuario):
    usuarios = load_user()

    try:
        usuarios.append(usuario)

        with open("usuarios.json", "w", encoding="utf-8") as archive:
            json.dump(usuarios, archive, indent=4)
        return True
    except:
        return False
    
def remove_user(id):
    usuarios = load_user()
    usuarios_filtrados = [usuario for usuario in usuarios if usuario.get("id") != id] # PERCORRE O ARRAY DA LISTA E ADICIONA QUEM NÃO TIVER O ID PASSADO, O PRIMEIRO USUARIO DO PARAMETRO É O QUE IRÁ ARMAZENAR NA LISTA

    if len(usuarios) == len(usuarios_filtrados):
        return False
    
    try:
        with open("usuarios.json", "w", encoding="utf-8") as archive:
            json.dump(usuarios_filtrados, archive, indent=4)
        return True
    except:
        return False
    
def edit_user(usuarios, dados):

    for usuario in usuarios:
        if usuario["id"] == dados["id"]:
            usuario["nome"] = dados["nome"]
            usuario["email"] = dados["email"]
            break
            
    try:
        with open("usuarios.json", "w", encoding="utf-8") as archive:
            json.dump(usuarios, archive, indent=4)
        return True
    except:
        return False

    

@app.route("/") # DEFINE O LINK DA ROTA DA PÁGINA QUE SERÁ RENDERIZADA
def home():

    usuarios = load_user()

    return render_template("formulario.html", usuarios=usuarios)

@app.route("/formulario", methods=["POST"])
def get_info():
    dados = request.get_json() # RECEBE O JSON DO JAVASCRIPT

    nome = dados.get("nome")
    email = dados.get("email")
    idade = dados.get("idade")
    cpf = dados.get("cpf")


    usuario = {
        "id": str(uuid.uuid4()), # ID DOS USUÁRIOS COMO STRING
        "nome": nome,
        "email": email,
        "idade": idade,
        "cpf": cpf
    }

    status = save_user(usuario)

    if status:
        return jsonify({"mensagem": f"Usuário {usuario['nome']} cadastrado com sucesso!",
                        "id": usuario["id"]}), 200
    else:
        return jsonify({"erro": "Algo deu errado, tente novamente!"}), 404

@app.route("/json")
def json_user():
    usuarios = load_user()

    return jsonify(usuarios)

@app.route("/usuarios/<id>", methods=["DELETE"])
def delete_user(id):
    sucesso = remove_user(id)

    if sucesso:
        return jsonify({"mensagem": "Usuário deletado com sucesso!"}), 200 # STATUS 200 É ENVIADO QUANDO ALGO TEM SUCESSO
    else:
        return jsonify({"erro": "Usuário não encontrado."}), 404 # QUANDO AOLGO NÃO É ENCONTRADO
    
@app.route("/editar", methods=["POST"])
def get_user():
    dados = request.get_json()

    usuarios_edit = {
        "id": dados.get("id_user"),
        "nome": dados.get("nome_user"),
        "email": dados.get("email_user")
    }


    usuarios = load_user()

    status = edit_user(usuarios, usuarios_edit)

    if status:
        return jsonify({"mensagem": f"Usuário atualizado com sucesso!"})
    else:
        return jsonify({"erro": "Erro ao atualizar as informações"})


# @app.route("/tabela")
# def table_user():
#     usuarios = load_user()

#     if usuarios == []:
#         return "<h1 style='text-align: center;'>Não há usuários cadastrados</h1>"
#     else:
#         return render_template("tabela.html", usuarios=usuarios)




if __name__ == "__main__":
    app.run(debug=True) # RODA O PROGRAMA