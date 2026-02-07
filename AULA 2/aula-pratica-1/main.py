"""
                    Expressões algébricas
> Escreva as seguintes expressões algébricas em linguagem Python:
"""
# a) O somatório dos 5 primeiro números inteiros e positivos
print(1 + 2 + 3 + 4 + 5)

# b) A média entre 23, 19 e 31
print((23 + 19 + 31) / 3)

# c) O número de vezes que 73 cabe em 403
print(403 // 73)

# d) A sobra quando 403 é dividido por 73
print(403 % 73)

# e) 2 elevado à 10 a potência
print(2 ** 10)

# f) O valor absoluto da diferença entre 54 e 57
print(abs(54 - 57))

# g) O menor valor entre 34, 29 e 31
print(min(34, 29, 31))

"""
                    Atribuição
> Escreva as expressões em Python para:
"""
# a) Atribuir o valor inteiro 3 à variável a
a = 3

# b) Atribuir o valor 4 à variável b
b = 4

# c) Atribuir à variável c o valor da expressão a * a + b * b
c = a * a + b * b
print(c)


"""
                    Strings
> Execute as seguintes atribuições:
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
Agora, utilizando operadores + e *, crie as saídas a seguir:
"""
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'


# a) 'ant bat cod'
res = s1 + ' ' + s2 + ' ' + s3
print(res)
# b) 'ant ant ant ant ant ant ant ant ant ant'
res = 10 * (s1 + ' ')
print(res)
# c) 'ant bat bat cod cod cod'
res = (s1 + ' ') + 2 * (s2 + ' ') + 3 * (s3 + ' ')
print(res)
# d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
res = ((s1 + ' ') + (s2 + ' '))* 7
print(res)
# e) 'batbatcod batbatcod batbatcod batbatcod batbatcod'
res = ((s2 + s2 + s3) + ' ') * 5
print(res)












































