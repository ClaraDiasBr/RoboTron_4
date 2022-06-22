* Settings *
Documentation       Keywords e Variaveis para ações do endpoint /usuarios

#Sessão para setagem de variáveis para utilização
* Variables *
${nome_do_usuario}          tony stark
${senha_do_usuario}         test123
${email_do_usuario}         tony.stark@gmail.com


* Keywords *
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