// Projeção
db.usuarios.find({}, { nome: 1, idade: 1 })

// Ordenação
db.usuarios.find().sort({ idade: 1 })
// Limitação
db.usuarios.find().limit(10)
// Paginação
db.usuarios.find().skip(10).limit(5)