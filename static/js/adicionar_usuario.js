const form = document.getElementById("cadastro");

form.addEventListener("submit", function(event){
    event.preventDefault();

    const dados_form = { // OBJETO QUE COLETA OS DADOS DO FORMULÁRIO
        nome: document.getElementById("nome").value,
        email: document.getElementById("email").value,
        idade: document.getElementById("idade").value,
        cpf: document.getElementById("cpf").value
    };

        fetch("/formulario", {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json' // INFORMA A APLICAÇÃO QUE IRÁ RECEBER UM ARQUIVO JSON
        },
        body: JSON.stringify(dados_form) // CONVERTE OS DADOS DO FORMULÁRIO EM JSON
    })

    .then(response => {
        return response.json().then(data => {
            if(!response.ok)
            {
                throw new Error(data.erro || "Erro desconhecido");
            }
            return data;
        })
    })

    .then(data => {
        alert(data.mensagem);

        const tbody = document.getElementById("corpo-tabela");
        const linha = document.createElement("tr");

        linha.innerHTML = `<td>${dados_form.nome}</td>
                           <td>${dados_form.email}</td>
                           <td>${dados_form.idade}</td>
                           <td>${dados_form.cpf}</td>
                           <td>
                                <button class="butao acao" id="excluir" onclick="excluir_usuario('${data.id}','${dados_form.cpf}')"><i class="bi bi-trash-fill"></i></button>
                                <button class="butao acao" id="editar" onclick="editar_usuario('${data.id}', '${dados_form.nome}', '${dados_form.email}')"><i class="bi bi-pencil-square"></i></button>
                           </td>`

        linha.id = `linha-${data.id}`;
        tbody.appendChild(linha);

        
    })
})