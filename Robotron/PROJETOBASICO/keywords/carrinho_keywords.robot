* Settings *
Documentation       Keywords e Variaveis para ações do endpoint /carrinhos
Resource            ./common.robot

#Sessão para setagem de variáveis para utilização
* Variables *
${id_carrinho}     qbMqntef4iTOwWfg

* Keywords *

GET Endpoint /carrinhos
    ${response}             GET On Session       serverest       /carrinhos
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}

GET Endpoint /carrinhos ID
    ${response}             GET On Session       serverest       /carrinhos/${id_carrinho}
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}

Criar Carrinho Valido
    ${produtos}             Importar JSON Estatico  json_carrinho.json
    ${payload}              Set Variable     ${produtos}
    Set Global Variable     ${payload}

# Criar Carrinho Valido
#     ${produtos}                 Importar JSON Estatico  json_carrinho.json
#     ${produtos}=   Evaluate      json.dumps(${produtos})     json
#     #Set Test Variable       ${lista_produtos}    ${produtos["produtos"]}
#     ${payload}              Set Variable     ${produtos}
#     Set Global Variable     ${payload} 

POST Endpoint /carrinhos
    Criar Carrinho Valido
    &{header}               Create Dictionary     Authorization=${token_auth}  Content-Type=application/json
    ${response}             POST On Session       serverest       /carrinhos      json=${payload}    headers=${header}   
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}
 
    