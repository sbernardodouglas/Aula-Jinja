import soma
import subtrair
import multiplicar
import divisao
import potencia
import raizquadrada

def calculadora():
    a=float(input("Digite um número: "))
    b=float(input("Digite outro número: "))
    print("CAUCULADORA")
    print("1 SOMAR")
    print("2 SUBTRAIR")
    print("3 MULTIPLICAR")
    print("4 DIVISÃO")
    print("5 POTENCIA")
    print("6 RAIZ QUADRADA")
    r=int(input("Escolha uma dessas opções: "))
    if r==1:
        print(soma.somar(a,b))
    elif r==2:
        print(subtrair.subtrair(a,b))
    elif r==3:
        print(multiplicar.multiplicar(a,b))
    elif r==4:
        print(divisao.divisao(a,b))
    elif r==5:
        print(potencia.potencia(a,b))
    elif r==6:
        print(raizquadrada.raiz_quadrada(a,b))

