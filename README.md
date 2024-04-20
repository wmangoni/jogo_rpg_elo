# Simulador de Jogo de RPG de Cartas

Este é um simulador de jogo de cartas. O simulador é escrito em Python e permite simular várias situações com base em classificações, características e cartas selecionadas.

## Requisitos

- Python 3.x

## Como usar

1. Clone o repositório para o seu ambiente local:

    ```bash
    git clone https://github.com/wmangoni/jogo_rpg_elo.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd jogo_rpg_elo
    ```

3. Execute o script Python para iniciar o simulador:

    ```bash
    python main.py
    ```

4. Siga as instruções apresentadas no console para fornecer a classificação, características e simular o saque de cartas.

## Funcionalidades

- Simula o saque de cartas com base na classificação e características fornecidas.
- Modifica a classificação com base em características específicas.
- Remove as cartas selecionadas do conjunto disponível para evitar seleções repetidas.

## Exemplos de Uso

### Exemplo 1

```python
classificacao = "ilogica"
caracteristicas = ["Atento"]
cartas_disponiveis = ['espadas A', 'espadas 2', 'ouro 3', 'copas 4', 'ouro 5', 'paus 6', 'espadas 7', 'paus 8', 'ouro 9', 'paus 10', 'espadas J', 'copas Q', 'copas K']

cartas_sacadas = sacar_cartas(classificacao, caracteristicas, cartas_disponiveis)
print("Cartas sacadas:", cartas_sacadas)
print("Cartas restantes:", cartas_disponiveis)
```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar uma solicitação pull com melhorias ou novas funcionalidades.

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.
