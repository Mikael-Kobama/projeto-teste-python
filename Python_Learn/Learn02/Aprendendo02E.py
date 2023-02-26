m=float(input('Digite A quantiedade de metros: '))
km=m/1000
hm=m/100
dam=m/10
dm=m*10
cm=m*100
mm=m*1000

print('Usando o número {} em metros, temos: \n'
      'Quilômetro: {:.2f} km \n'
      'Hectômetro: {:.2f} hm \n'
      'Decâmetro: {:.2f} dam \n'
      'Decímetro: {} dm \n'
      'Centímetros: {} cm \n'
      'Milimetros: {} mm'.format(m,km,hm,dam,dm,cm, mm))