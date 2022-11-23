#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa

#exemplo de uso
lucasTambasco = Pessoa(1, "Lucas Tambasco")
print(lucasTambasco)

#Mostrar só o nome
print(lucasTambasco.nome)
