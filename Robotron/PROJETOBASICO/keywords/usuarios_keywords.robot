* Settings *
Documentation       Keywords e Variaveis para ações do endpoint /usuarios
Resource            ./common.robot

#Sessão para setagem de variáveis para utilização
* Variables *
${nome_do_usuario}          tony stark
${senha_do_usuario}         test123
${email_do_usuario}         tony.stark@gmail.com
${id_do_usuario}            9Ma0mdfiQO8Gd3st
${id_nao_usuario}           AKN4pWQ4dp0cH7vW


* Keywords *
GET Endpoint /usuarios
    ${response}             GET On Session      serverest       /usuarios
    Set Global Variable     ${response}


POST Endpoint /usuarios
   # &{payload}              Create Dictionary     nome=${nome_do_usuario}     email=${email_do_usuario}      password=${senha_do_usuario}    administrador=true
    ${response}             POST On Session      serverest       /usuarios      json=&{payload}
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

Validar Quantidade "${quantidade}"
    Should Be Equal     ${response.json()["quantidade"]}        ${quantidade}

Validar Se Mensagem Contem "${palavra}"
    Should Contain      ${response.json()["message"]}           ${palavra}

Printar Conteudo Response
    Log To Console      Response: ${response.json()["usuarios"]}

Criar Usuario Estatico Valido
    ${json}                 Importar JSON Estatico  json_usuario_ex.json
    ${payload}              Set Variable    ${json["user_valido"]}
    Set Global Variable     ${payload}
    POST Endpoint /usuarios

Buscar Usuario por ID
    ${response}             GET On Session      serverest       /usuarios/${id_do_usuario}
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}

Buscar Usuario Nao Cadastrado por ID
    ${response}             GET On Session      serverest       /usuarios/${id_nao_usuario}     expected_status=400
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}

POST Invalido Endpoint /usuarios
   # &{payload}              Create Dictionary     nome=${nome_do_usuario}     email=${email_do_usuario}      password=${senha_do_usuario}    administrador=true
    ${response}             POST On Session      serverest       /usuarios      json=&{payload}     expected_status=400
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}

Criar Usuario Estatico Invalido
    ${json}                 Importar JSON Estatico  json_usuario_ex.json
    ${payload}              Set Variable    ${json["user_invalido"]}
    Set Global Variable     ${payload}
    POST Invalido Endpoint /usuarios

Criar Usuario Estatico Sem Senha
    ${json}                 Importar JSON Estatico  json_usuario_ex.json
    ${payload}              Set Variable    ${json["user_sem_senha"]}
    Set Global Variable     ${payload}
    POST Invalido Endpoint /usuarios

Criar Usuario Estatico Sem Email
    ${json}                 Importar JSON Estatico  json_usuario_ex.json
    ${payload}              Set Variable    ${json["user_sem_email"]}
    Set Global Variable     ${payload}
    POST Invalido Endpoint /usuarios

Criar Usuario Estatico Nao Admin
    ${json}                 Importar JSON Estatico  json_usuario_ex.json
    ${payload}              Set Variable    ${json["user_nao_admin"]}
    Set Global Variable     ${payload}
    POST Endpoint /usuarios