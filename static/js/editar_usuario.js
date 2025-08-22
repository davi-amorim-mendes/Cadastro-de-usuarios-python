function editar_usuario(id, nome, email){
    
    if(!confirm(`Deseja editar as informações do usuário: ${nome}?`))
    {
        return
    }

    const tabela = document.querySelector(".tabela");
    const cad_form = document.querySelector(".cadastro");
    const edit_form = document.querySelector(".editar");
    
    tabela.style.display = "none";
    cad_form.style.display = "none";
    edit_form.style.display = "flex";
    
    const input_nome = document.getElementById("nome-edit");
    const input_email = document.getElementById("email-edit");

    input_nome.value = nome;
    input_email.value = email;

    const form = document.getElementById("editar_usuario");


    form.addEventListener("submit", function(event){
        event.preventDefault();

        const dados_form = {
            id_user: id,
            nome_user: input_nome.value,
            email_user: input_email.value
        };

        fetch("/editar", {
            method : "POST",
            headers : {
                'Content-Type': 'application/json'
                
            },
            body : JSON.stringify(dados_form)
        })

        .then(response => {
            return response.json().then(data => {
                if(!response.ok)
                {
                    throw new Error(data.erro | "Erro desconhecido");
                }
                return data;
            })
        })

        .then(data => {
            alert(data.mensagem);

            tabela.style.display = 'flex';

            cad_form.style.display = "flex";
            edit_form.style.display = "none";

        })

    })


}