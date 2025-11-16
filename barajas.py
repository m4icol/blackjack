import random
palos = ['♥️','♦️','♠️','♣️']
valores = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10,
    'A' : 11
}

def crear_baraja():
  baraja = []
  for palo in palos:
      for carta in valores:
        baraja.append((carta, palo))
  return baraja

def mezclar_baraja(baraja):
  random.shuffle(baraja)
  return baraja

def repartir_carta(baraja):
  if len(baraja) == 0:
      return None
  return baraja.pop()

def calcular_valor(mano):
  valor_total = 0
  ases = 0

  for carta in mano:
      valor_carta = valores[carta[0]]
      valor_total += valor_carta
      if carta[0] == 'A':
          ases += 1

  while valor_total > 21 and ases > 0:
      valor_total -= 10
      ases -= 1

  return valor_total

def mostrar_mano(mano, ocultar_primera=False):
    if ocultar_primera:
        print("[¿?], ", end=" ")
        for i in range(1, len(mano)):
            print(f"{mano[i][0]}{mano[i][1]}", end=" ")
    else:
        for carta in mano:
            print(f"{carta[0]}{carta[1]}", end=" ")
    print()