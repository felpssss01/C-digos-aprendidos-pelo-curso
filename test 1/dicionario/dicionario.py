import os
os.system("cls")

aluno = {
    "nome": "Ana Paula",
    "idade": 17,
    "matricula": "2026001",
    "media": 8.5,
    "ativo": True
}

aluno["nome"] = "Ana Paula Silva"

del aluno["matricula"]
aluno.pop("matricula") 

print(aluno["nome"])
print(aluno["idade"])
print(aluno["media"])
print(aluno["ativo"])
 