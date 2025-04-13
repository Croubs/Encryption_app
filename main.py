import math

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
  msg = list(map(lambda i, u: alphabet[(i%26)].upper() if u else alphabet[(i%26)], indexes, isUpper))

  return ''.join(msg)

# Para desencriptar el mensaje hacer -n
def cifradoCesar(m:str, n:int):
  (msg, isUpper) = getIndexes(m)
  cesar = list(map(lambda c: (c + n) % 26, msg))

  return getMessage(cesar, isUpper)

# Para verificar si un número es primo
def isPrime(n:int):
  if n < 2:
    return False

  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False

  return True

# Para obtener las llaver del RSA
def getKeysRSA(p:int, q:int):
  n = p * q
  phi = (p - 1) * (q - 1)

  # Llave pública
  e = 0
  for i in range(2, phi):
    if math.gcd(i, phi) == 1:
      e = i
      break

  # Llave privada
  d = 0
  for i in range(2, phi):
    if (i * e) % phi == 1:
      d = i
      break

  return (n, e, d)

# Para cifrar con RSA
def cifradoRSA(m:str, e:int, n:int):
  (msg, isUpper) = getIndexes(m)
  rsa = list(map(lambda c: pow(c, e, n), msg))

  # Retornará la lista con los índices encriptados y la lista para saber cuáles eran mayúsculas
  return (rsa, isUpper)

# Para descifrar con RSA
def descifradoRSA(rsa:list, d:int, n:int, isUpper:list=[]):
  decrypted = list(map(lambda c: pow(c, d, n), rsa))

  # Si no se envió una lista para saber cuáles carácteres son mayúsculas, considera todo como minúscula
  if len(isUpper) == 0: isUpper = [False] * len(decrypted)

  return getMessage(decrypted, isUpper)



