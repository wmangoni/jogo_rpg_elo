import random


# Função para sacar cartas
def sacar_cartas(classificacao, caracteristicas, baralho, cemiterio, jogador):

  if (len(baralho) < 1):
    baralho = cemiterio
    cemiterio = []

  mao = []
  # Reduz a classificação se uma característica se encaixa
  if any(caracteristica in jogador["caracteristicas"] for caracteristica in caracteristicas):
    if classificacao == "logica":
      classificacao = "trivial"
    elif classificacao == "ilogica":
      classificacao = "logica"
    elif classificacao == "impossivel":
      classificacao = "ilogica"

  # Sacar cartas de acordo com a classificação
  for _ in range(classificacoes[classificacao]):
    carta_sacada = random.choice(baralho)
    mao.append(random.choice(baralho))
    cemiterio.append(carta_sacada)
    baralho.remove(carta_sacada)  # Remove a carta selecionada do array original
  return mao, baralho, cemiterio

# Função para interpretar cartas
def interpretar_cartas(cartas):
  # Verificar se todas as cartas são pretas
  if all(carta.startswith("preto") for carta in cartas):
    return "sim"
  else:
    return "não"

# Função para calcular a intensidade da resposta
def calcular_intensidade(carta):
  valor = carta[-1:]
  if valor == 'J':
    valor = 11
  elif valor == 'Q':
    valor = 12
  elif valor == 'K':
    valor = 13
  elif valor == 'A':
    valor = 1

  if carta.startswith("espadas") or carta.startswith("paus"):
    return int(valor)
  else:
    return -int(valor)

# Função para verificar cartas especiais
def verificar_cartas_especiais(cartas):
  for carta in cartas:
    if carta[-1:] in ["J", "Q", "K"]:
      return True
  return False

def jogar(pergunta, classificacao, caracteristicas, baralho, cemiterio, jogador):
  # Sacar cartas
  cartas, baralho, cemiterio = sacar_cartas(classificacao, caracteristicas, baralho, cemiterio, jogador)

  print(f"mao_jogador: {cartas}")

  # Interpretar cartas
  resposta = interpretar_cartas(cartas)

  # Calcular intensidade da resposta
  intensidade = calcular_intensidade(cartas[-1])

  # Verificar cartas especiais
  cartas_especiais = verificar_cartas_especiais(cartas)

  # Mostrar resultados
  print(f"Pergunta: {pergunta}")
  print(f"Resposta: {resposta}")
  print(f"Intensidade: {intensidade}")
  print(f"Cartas especiais: {cartas_especiais}")
  print()
  print("#####################")
  print()

  return baralho, cemiterio


# Função principal
def main():

  jogador = {
      "nome": "Joãozinho",
      "idade": 25,
      "sexo": "Masculino",
      "vida": 40,
      "caracteristicas": ["Atento", "Forte"]
  }

  # Dicionário de classificações e quantidades de cartas
  classificacoes = {
      "trivial": 0,
      "logica": 1,
      "ilogica": 2,
      "impossivel": 3,
  }

  CARTAS = [
      "paus A", "paus 2", "paus 3", "paus 4", "paus 5", "paus 6", "paus 7", "paus 8", "paus 9", "paus 10", "paus J", "paus Q", "paus K",
      "espadas A", "espadas 2", "espadas 3", "espadas 4", "espadas 5", "espadas 6", "espadas 7", "espadas 8", "espadas 9", "espadas 10", "espadas J", "espadas Q", "espadas K",
      "copas A", "copas 2", "copas 3", "copas 4", "copas 5", "copas 6", "copas 7", "copas 8", "copas 9", "copas 10", "copas J", "copas Q", "copas K",
      "ouro A", "ouro 2", "ouro 3", "ouro 4", "ouro 5", "ouro 6", "ouro 7", "ouro 8", "ouro 9", "ouro 10", "ouro J", "ouro Q", "ouro K",
    ]

  CARTAS_SACADAS = []

  CARTAS, CARTAS_SACADAS = jogar("Há algo útil dentro do carro?", "ilogica", ["Atento"], CARTAS, CARTAS_SACADAS, jogador)
  CARTAS, CARTAS_SACADAS = jogar("Tem comida dentro do armário?", "logica", ["Esperto"], CARTAS, CARTAS_SACADAS, jogador)
  CARTAS, CARTAS_SACADAS = jogar("Tem uma arma dentro da caixa?", "impossivel", ["Forte"], CARTAS, CARTAS_SACADAS, jogador)

  print()
  print("#### ESTADO JOGO ####")
  print()
  print("Cartas sacadas:")
  for carta in CARTAS_SACADAS:
    print(carta)
  print()
  print("Cartas restantes:")
  for carta in CARTAS:
    print(carta)

# Executar função principal
main()
