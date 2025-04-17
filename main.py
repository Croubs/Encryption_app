# ===== Autor =====
# Sustituir con los datos del autor
# Autor: croubs
# Matrícula: XXXXX
# =================

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

# Para mostrar el menú
def menu():
  print("¡Bienvenid@!")
  print("¿Qué desea hacer?")
  print("1. Cifrado César")
  print("2. Descifrado César")
  print("3. Cifrado RSA")
  print("4. Descifrado RSA")
  print("5. Autor")
  print("6. Código fuente")
  print("7. Salir")
  
  option = int(input("Opción: "))
  print("=======================================================")
  return option

# Esta es la "ejecución" del programa
def main():
  option = menu()

  while option != 7:
    if option == 1:
      print("=== Cifrado Cesar ===")
      msg = input("Mensaje: ")
      n = int(input("Cantidad de carácteres que quiere recorrer el alfabeto: "))
      print("Mensaje encriptado:", cifradoCesar(msg, n))

    elif option == 2:
      print("=== Descifrado Cesar ===")
      msg = input("Mensaje encriptado: ")
      n = int(input("Cantidad de carácteres que el alfabeto se movió: "))
      print("Mensaje desencriptado:", cifradoCesar(msg, -n))
    
    elif option == 3:
      print("=== Cifrado RSA ===")
      msg = input("Mensaje: ")
      
      print("A continuación deberá ingresar dos números primos distintos, por lo cual ponemos a disposición la siguiente lista de números primos")
      primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609]
      print(primes[:30])

      morePrimes = input("¿Desea ver más números primos? (s/n): ")
      if morePrimes == 's':
        print(primes[30:60])
        morePrimes = input("¿Desea ver más números primos? (s/n): ")
        if morePrimes == 's':
          print(primes[60:90])
          morePrimes = input("¿Desea ver más números primos? (s/n): ")
          if morePrimes == 's':
            print(primes[90:])

      p = int(input("Ingrese un número primo: "))
      while not isPrime(p):
        print("El número no es primo")
        p = int(input("Ingrese un número primo: "))

      q = int(input("Ingrese un segundo número primo: "))
      while not isPrime(q) or p == q:
        if not isPrime(q):
          print("El número no es primo")
        elif p == q:
          print("Los números no pueden ser iguales")
        q = int(input("Ingrese un segundo número primo: "))

      (n, e, d) = getKeysRSA(p, q)
      (rsa, isUpper) = cifradoRSA(msg, e, n)
      print("Mensaje encriptado:", rsa)
      print("Llave pública:", e)
      print("Llave privada:", d)
      print("n:", n)

    elif option == 4:
      print("=== Descifrado RSA ===")
      rsa = eval(input("Mensaje encriptado: "))
      d = int(input("Llave privada: "))
      n = int(input("n: "))

      print("Mensaje desencriptado:", descifradoRSA(rsa, d, n))

    elif option == 5:
      print("=== Autor ===")
      # Sustituir con los datos del autor
      print("Autor: croubs")
      print("Matrícula: XXXXX")
      
    elif option == 6:
      print("=== Código fuente ===")
      print("\n\n\n")

      file = open("main.py", "r", encoding="utf-8")
      print(file.read())
      
      print("\n\n\n")

    else:
      print("Opción inválida")

    print("=======================================================")
    option = menu()

  print("¡Gracias por usar el programa!")

# Se llama a main para que "inicie el programa"
main()