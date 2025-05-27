def ContarDigito(n):
    if n == 0:
        return 0
    ultimo_digito = n % 10
    restante = n // 10
    return 1 + ContarDigito(restante)
def ValidarNumero(n):
    if n < 0: 
        return False
    else:
        return True
def InvertirNumero(n):
    if n <= -2**31 or n >= 2**31 - 1:
        return 0
    if n == 0:
        return n
    positivo = ValidarNumero(n)
    nuevo_numero = 0
    if positivo == False:
        n = n * -1
    digitos = ContarDigito(n)
    multiplicador = 10 ** (digitos - 1)
    ultimo_digito = n % 10
    restante = n // 10
    x = ultimo_digito*multiplicador + InvertirNumero(restante)
    if not positivo:
        return x* -1
    return x

n = 326
print(InvertirNumero(n))
