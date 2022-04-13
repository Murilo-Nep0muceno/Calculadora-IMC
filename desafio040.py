print('='*18)
print('Calculadora de IMC')
print('='*18)


repete = 'S'



while repete in 'Ss':
    alt = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso : '))
    soma = peso / (alt ** 2)
    if soma < 18.5 :
        print('voce esta abaixo do peso imc de  {:.2f}'.format(soma))
    elif soma == 18.5 :
        print('voce esta no peso ideal imc de  {:.2f}'.format(soma))
    elif soma <= 25 :
        print('voce esta no peso ideal imc de  {:.2f}'.format(soma))
    elif soma <=30:
        print('voce esta com obesidade  imc de  {:.2f}'.format(soma))
    elif soma <= 40:
        print('voce esta com obesidade II  imc de  {:.2f}'.format(soma))
    else:
        print('Voce esta com obesidade morbida {:.2f}'.format(soma))
    repete = str(input('Quer digitar um novo imc ? [N/S]: ')).upper().strip()



