use viagens;

db.createCollection("usuarios")
db.createCollection("destinos")


// Ou vc pode inserir diretamente um documento e ele já ira criar a collection
db.usuarios_novo.insertOne({});