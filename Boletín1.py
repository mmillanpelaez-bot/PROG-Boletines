print('Boletín 1.')
# 1.
def ejercicio1():
    print('1. Resultado das expresións:')
    a = ((3 + 2) % 2 - 15) / 2 * 5
    b = (6 + 6 / 7) + 35 / 2 -8 * 5 / 4 * 2
    c = 3 + 6 * 14 % 3
    d = 8 + 7 * 3 + 4 * 6 /2 % 4
    e = 27 % 4 +15 / 4
    f = 37 / 42 - 2
    g = 9 * 2 / 3 * 25 * 3
    h = (7 * 3 - 4 * 4) * 2 / 4 * 2

    print('a = ',a)
    print('b = ',b)
    print('c = ',c)
    print('d = ',d)
    print('e = ',e)
    print('f = ',f)
    print('g = ',g)
    print('h = ',h)
ejercicio1()
# 2.
print('2. Variables non válidos:')
print('Invalidos en (a): Salto- mortal, salto + mortal, 2salto, "salto"')
print("Invalidos en (b): cantidade total")
#3
print('3. Expresar, utilizando operadores aritméticos:')
print('a) (m + n) / n')
print('b) ((m + n) / p) / ((p - r) / s)')
print('c) (m + 4) / (p - q)')
print('d) (c * r * t / 100)')
print('e) (m + n) / (p + (q / r))')
print('f) (m / n) * (p + q)')
print('g) (n(1 + i) ** t) / ((1 + i) ** t - 1)')
#4
print('4. Avalia as seguintes expresións:')
print('a) True and True == False'' ->', False)
print('b) not False == True'' ->', True)
print('c) (True and True) or False == True'' ->', True)
print('d) (False or False) and False != True'' ->', False)
print('e) (not(True and False)) == False'' ->', False)
print('f) “12” + “12” == “24”'' ->', False,'-> "1212"')
print('g) “34” + “43” == “3443”'' ->', True)
print('h) 12 + 12 == 24'' ->', True)
print('i) 34 + 43 == “3443”'' ->', False, '-> 77')
#5
def ejercicio5():
    print('5.  Avaliar espresións, tendo en conta as variables')
    def ejercicio5a():
        i = 1
        j = 0
        k = 1
        print('a = ', i + k <= j - k * 3 and k >= 2)
    ejercicio5a()
    def ejercicio5b():
        i = 3
        j = 2
        k = -1
        print('b = ', i == 3 or j <= 2 and k > 0)
    ejercicio5b()
    def ejercicio5c():
        tipo = 10
        rede = 7.5
        print('c = ', tipo < rede + 1.5)
    ejercicio5c()
    def ejercicio5d():
        ano = 1993
        print('d = ', ano % 400 == 0)
    ejercicio5d()
    def ejercicio5e():
        print('e = ', 3 == 2 or 5 > 1 + 1)
    ejercicio5e()
    def ejercicio5f():
        print('f = ', 5 - 2 > 4 and not(0,5 == 1 / 5))
    ejercicio5f()
    def ejercicio5g():
        a = 2
        b = 5
        c = 6
        d = 10
        print('g = ', a >= b or a >= c and a <d)
    ejercicio5g()
    def ejercicio5h():
        a = 2
        b = 5
        c = 6
        d = 10
        print('h = ', a + b < c and a + c < d or 2 * a < a + b)
    ejercicio5h()
    def ejercicio5i():
        a = 2
        b = 5
        c = 6
        d = 10
        print('i = ', not(a * b < d) and not(a * b < c) or b + c <= d)
    ejercicio5i()
ejercicio5()