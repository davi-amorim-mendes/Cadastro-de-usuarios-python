function excluir_usuario(id, cpf) // FUNÇÃO DE EXCLUIR O USUÁRIO
{
    if(!confirm(`Tem certeza que deseja excluir o usuário com o CPF ${cpf}?`))
    {
        return
    }

    fetch(`/usuarios/${id}`, { // CONECTA E REALIZA A BUSCA NA ROTA DO PYTHON
        method : 'DELETE'
    })
    
    .then(response => { // RECEBE A RESPOSTA E TRATA OS ERROS
        return response.json().then(data => {
            if(!response.ok){
                throw new Error(data.erro || "Erro desconhecido")
            }
            return data;
        })
    })

    .then(data => {
        alert(data.mensagem);
        const linha = document.getElementById(`linha-${id}`); // REMOVE A LINHA DO USUÁRIO DESEJADO
        if(linha) linha.remove();
    })
    .catch(error => {
        console.error("Erro na requisição", error);
        alert("Erro ao excluir usuário: "+error.message)
    })
}