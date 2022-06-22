* Settings *
Documentation       Keywords e Variaveis para ações do endpoint /produtos

#Sessão para setagem de variáveis para utilização
* Variables *
${token_auth}           Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImZ1bGFub0BxYS5jb20iLCJwYXNzd29yZCI6InRlc3RlIiwiaWF0IjoxNjU1ODk5NjI3LCJleHAiOjE2NTU5MDAyMjd9.qSAQjeCK-lXK2p5WtnvdtSYNCaCBhSAY4gMJ6x71ess

* Keywords *
POST Endpoint /produtos
    &{header}               Create Dictionary     Authorization=${token_auth}
    &{payload}              Create Dictionary     nome=MouseTech    preco=100   descricao=Mouse     quantidade=550 
    ${response}             POST On Session       serverest       /produtos      data=&{payload}    headers=${header}
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}