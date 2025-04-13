# Para obtener los indices del alfabeto de 26 letras y saber cuáles son mayúsculas
def getIndexes(m:str):
  alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  msg = list(m)

  isUpper = list(map(lambda c: c.isupper(), msg))
  indexes = list(map(lambda c: alphabet.index(c.lower()), msg))

  return (indexes, isUpper)

# Para transformar los indices del alfabeto en letras y devolver el mensaje como un string
def getMessage(indexes:list, isUpper:list):
  alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  msg = list(map(lambda i, u: alphabet[i].upper() if u else alphabet[i], indexes, isUpper))

  return ''.join(msg)


# Para desencriptar el mensaje hacer -n
def cifradoCesar(m:str, n:int):
  (msg, isUpper) = getIndexes(m)
  cesar = list(map(lambda c: (c + n) % 26, msg))

  return getMessage(cesar, isUpper)

