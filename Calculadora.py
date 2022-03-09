import math
angulo = float(input('Digite o angulo que voce deseja: '))
sen = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {}'.format(angulo, sen))

cos = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSSENO de {}'.format(angulo, cos))

tan = math.tan(math.radians(angulo))
print('O angulo de {} tem a TANGENTE de {}'.format(angulo, tan))