senhacorreta = input("configure a senha")
nome = input("digite o nome")
salario = float(input("digite seu salario"))
senha =input("digite a senha")

while senha != senhacorreta:
    print("senha incorreta") 
    senha = input("digite a senha")
print("bem vindo",nome)

salarioanual = salario * 12
if(salarioanual > 100,000):
    print("Rico")
else:
    print("Faça o L")


#pedir nome e senha ao usuario,  mostrar "Bem vindo" quando acertar a senha, e o nome.
 #-Após, pedir o salario do usuario  -Mostrar salario anual  -se o salario anual for maior que 100 mil mostrar mensagem "Rico"
        