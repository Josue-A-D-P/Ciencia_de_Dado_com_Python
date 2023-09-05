contatos = {
    "josueporto59@gmail.com": {"nome": "Josué", "telefone": "3333-2221", "regiao":{"estado": "RS"}}
    }

resultado = contatos.get("chave")
print(resultado)

resultado = contatos.get("chave", {})
print(resultado)

resultado = contatos.get(
    "josueporto59@gmail.com", {}
)
print(resultado)