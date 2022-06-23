* Settings *
Documentation       Keywords e Variaveis para ações do endpoint /produtos



* Keywords *
POST Endpoint /produtos
    &{header}               Create Dictionary     Authorization=${token_auth}
    &{payload}              Create Dictionary     nome=Processador    preco=100   descricao=i9     quantidade=550 
    ${response}             POST On Session       serverest       /produtos      data=&{payload}    headers=${header}
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}

DELETE Endpoint /produtos
    &{header}               Create Dictionary     Authorization=${token_auth} 
    ${response}             DELETE On Session       serverest       /produtos/${id_produto}         headers=${header}
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}

Validar Ter Criado Produto
    Should be Equal         ${response.json()["message"]}               Cadastro realizado com sucesso
    Should Not Be Empty     ${response.json()["_id"]} 

Criar Produto e Armazenar ID
  POST Endpoint /produtos
  Validar Ter Criado Produto
  ${id_produto}             Set Variable        ${response.json()["_id"]}
  Log to Console          Response: ${id_produto}
  Set Global Variable     ${id_produto}

