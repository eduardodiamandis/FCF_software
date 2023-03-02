import math

while True:
    #solicitar o ponto de menor metragem
    metragem_min = float(input("Digite a metragem em metros do menor ponto: "))

    #solicitar o ponto de maior metragem
    metragem_max = float(input("Digite a metragem em metros do maior ponto: "))


    #solicitar a quantidade de pontos wi-fi
    ponto_wifi = int(input("Quantidade de wi-fi: "))

    #solicitar a quantidade de pontos cameras(cftv)
    ponto_cftv = int(input("Quantidade de cameras: "))

    #solicitar a quantidade de pontos controle de acesso
    ponto_ca = int(input("Quantidade de C.A: "))

    #solicitar a quantidade de pontos alvenaria ou mobiliário 
    ponto_po = int(input("Quantidade pontos: "))

    total_pontos = ponto_wifi + ponto_cftv + ponto_ca + ponto_po

    barra = print('-'*35)

    media_metragem = (metragem_min + metragem_max) / 2

    caixa_cabos = (media_metragem * total_pontos) / 305
    if caixa_cabos <= 0:
        caixa_cabos = 1
    else:
        caixa_cabos = math.ceil(caixa_cabos)

    print(f'Total de pontos: {total_pontos}'.center(40))
    print(f'Média de metragem: {media_metragem:.2f} m'.center(40))
    print(f'Quantidade de caixas: {caixa_cabos}'.center(40))
    print('-'*35)

    resposta = input("Deseja continuar? (S/N) ")
    if resposta.upper() == 'N':
        break
