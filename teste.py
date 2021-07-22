# nome = str(input('Seu nome: '))
# cont = 1
# aux = ""
# for i in nome:
#     aux += i
#     if len(aux) == cont:
#         print(aux)
#         cont += 1
#         aux=""
# print(aux)
# # if __name__ == '__main__':
## é pra escrever: j
##                 un
##                 ior
nome = str(input("qual o seu nome? "))

for i in range (len(nome)):
    print(f"menssagem [{i}] = {nome[i]}")
else:
    print(nome)