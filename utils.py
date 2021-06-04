from models import Pessoas

def inserir_pessoas():
    pessoa = Pessoas(nome='Maria',idade=23)
    print(pessoa)
    pessoa.save()

def consultar_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Maria').first()
    print(pessoa.idade)
def alterar_pessoa():
    pessoa= Pessoas.query.filter_by(nome='Gabriel').first()
    pessoa.idade = 22
    pessoa.save()

def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Gabriel').first()
    pessoa.delete()
if __name__ == '__main__':
    #inserir_pessoas()
    #alterar_pessoa()
    excluir_pessoa()
    consultar_pessoas()