import time

number_boletos = randint(8, 12)
    hours_inicial = 0.00
    cont =0

while hours_inicial <= 24:
    cont=0



    while cont < number_boletos:
        cont += 1
        print(cont)



    time.sleep(10800)
    hours_inicial += 3.01
    print(hours_inicial)
