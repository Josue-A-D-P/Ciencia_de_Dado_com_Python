contatos = {
    "josueporto59@gmail.com": {"nome": "Josué", "telefone": "3333-2221", "regiao":{"estado": "RS"}}
}

resultado = contatos.pop("josueporto59@gmail.com")
print(resultado)

resultado = contatos.pop("josueporto59@gmail.com", "Não encontrado")
print(resultado)