def main():
    print("ingrese un numero entero de 3 digitos")
    x= int(input())
    n = x
    
    if x < 0:
        n = n * -1

    n1=(n //100)
    n2=(n%100)
    x2=(n2//10)
    n3=(n2 % 10)


    if n3 == 0:
            print(f'{x2}{n1}')
    elif x > 0 and n3 > 1:
        print(f'{n3}{x2}{n1}')
    elif x < 0 and n3 > 1:
        print(f'-{n3}{x2}{n1}')



main()
