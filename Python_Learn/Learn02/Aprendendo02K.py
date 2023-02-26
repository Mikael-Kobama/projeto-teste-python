celc=float(input('Digite A temperatura em Celcius: '))
fah=(9/5*celc)+32
kelvin=celc-273.15
while kelvin<-273.15:
    kelvin=float(input('Digite A temperatura novamente: '))
print('A Temperatura {} Celsius se converte em: \n'
      'Fahrenheit: {} \n'
      'Kelvin: {:.2f}'.format(celc,fah,kelvin))