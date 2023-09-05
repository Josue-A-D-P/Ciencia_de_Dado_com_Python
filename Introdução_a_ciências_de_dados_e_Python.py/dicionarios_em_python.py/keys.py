contatos = {
    "josueporto59@gmail.com": {"nome": "Josué", "telefone": "3333-2221", "regiao":{"estado": "RS"}}
}

resultado = contatos.keys()
print(resultado)

result = contatos["josueporto59@gmail.com"]["regiao"]
print(result.keys())