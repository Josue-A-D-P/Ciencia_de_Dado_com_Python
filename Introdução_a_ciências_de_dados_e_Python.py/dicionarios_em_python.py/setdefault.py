contato = {
    "josueporto59@gmail.com": {"nome": "Josué", "telefone": "3333-2221", "regiao":{"estado": "RS"}}
}

contato.setdefault("nome")
print(contato)

contato.setdefault("idade", 28)
print(contato)