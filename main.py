


def cifradoCesar(m:str, n:int):
  alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  print(n)
  msg = list(m)

  isLower = list(map(lambda c: c.isupper(), msg))
  cesar = list(map(lambda c: alphabet[(alphabet.index(c.lower()) + n) % 26], msg))
  encrypted = list(map(lambda c, l: c.upper() if l else c, cesar, isLower))

  return ''.join(encrypted)


msg = input('Mensaje: ')
n = int(input('Desplazamiento: '))

encrypted = cifradoCesar(msg, n)
print(encrypted)
print(cifradoCesar(encrypted, -n))
