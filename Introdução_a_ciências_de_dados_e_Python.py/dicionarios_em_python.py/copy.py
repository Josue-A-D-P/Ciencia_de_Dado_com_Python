contatos = {"josueporto59@gmail.com" : {"nome": "Josué", "telefone": "3333-2221", "regiao":{"estado": "RS"}}}

copia = contatos.copy()
copia["josueporto59@gmail.com"] = {"nome": "JA"}

print(contatos["josueporto59@gmail.com"])

print(copia["josueporto59@gmail.com"])