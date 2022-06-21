#Sessão para configuração, documemtação, imports de arquivos e library
* Settings *
Documentation   Arquivo simples para requisições HTTP em APIs REST
Library         RequestsLibrary

#Sessão para setagem de variáveis para utilização
* Variables *
${nome_do_usuario}          tony stark
${senha_do_usuario}         test123
${email_do_usuario}         tony.stark@gmail.com


#Sessão para criação dos cenários de teste
* Test Cases *
Cenario: GET Todos os Usuarios 200
    [tags]      GET
    Criar Sessao
    GET Endpoint /usuarios
    Validar Status Code "200"
    Validar Quantidade "${4}"
    Printar Conteudo Response

Cenario: POST Cadastrar Usuario 201
    [tags]      POST
    Criar Sessao
    POST Endpoint /usuarios
    Validar Status Code "201"
    Validar Se Mensagem Contem "sucesso"

Cenario: PUT Editar Usuario 200
    [tags]      PUT
    Criar Sessao
    PUT Endpoint /usuarios
    Validar Status Code "200"

Cenario: DELETE Usuario 200
    [tags]      DELETE
    Criar Sessao
    DELETE Endpoint /usuarios
    Validar Status Code "200"

#Sessão para criação de Keywords Personalizados
* Keywords *
Criar Sessao
    Create Session       serverest       http://localhost:3000

GET Endpoint /usuarios
    ${response}             GET On Session      serverest       /usuarios
    Set Global Variable     ${response}


POST Endpoint /usuarios
    &{payload}              Create Dictionary     nome=${nome_do_usuario}     email=${email_do_usuario}      password=${senha_do_usuario}    administrador=true
    ${response}             POST On Session      serverest       /usuarios      data=&{payload}
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}

PUT Endpoint /usuarios
    &{payload}              Create Dictionary     nome=5 priest     email=testeiuq5@exemplo.com      password=123    administrador=true
    ${response}             PUT On Session      serverest       /usuarios/YDwgzPU8CnGu5yzN      data=&{payload}
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}

DELETE Endpoint /usuarios
    ${response}             DELETE On Session      serverest       /usuarios/AKN4pWQ4dp0cH7vW
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}

Validar Status Code "${statuscode}"
    Should Be True          ${response.status_code} == ${statuscode}

Validar Quantidade "${quantidade}"
    Should Be Equal     ${response.json()["quantidade"]}        ${quantidade}

Validar Se Mensagem Contem "${palavra}"
    Should Contain      ${response.json()["message"]}           ${palavra}

Printar Conteudo Response
    Log To Console      Response: ${response.json()["usuarios"][0]["nome"]}
