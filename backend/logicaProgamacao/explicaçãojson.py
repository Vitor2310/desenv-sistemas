# padaria.json [{
#    "nome":"pão" 
#     "valor": "22,90"
    
#     },]

#{} -> chaves:definir um objeto -> ficha de cadastro->            - nome
#                                                        pessoa { - cpf
#                                                                 - tel
#[] -> colchete : definir uma lista

#sempre importar json

import json 

inventario = []
#lendo o comentario
try:
    with open("loja.json", "r") as arquivo:
        inventario = json.load (arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado")

try:
    nome= input ("digite o nome do produto: ")
    quantidade= int (input("digite a quantidade do produto: "))
    preco= float (input("digite o preco do produto: "))
 
except ValueError:
    print("Digite o valor corretamente")
novo_produto= {
    "nome" : nome,
    "quantidade" : quantidade,
    "preco": preco,
    "em_estoque": quantidade >0 #expressão verdadeiro falso
    }

            
    #escrever o objeto no arquivo
inventario.append(novo_produto)
with open ("loja.json", "w") as arquivo:
    json.dump(inventario, arquivo, indent = 4)
    
    #indent -> formatar o arquivo json
print(" produto cadastrado com sucesso")
        

        
        










