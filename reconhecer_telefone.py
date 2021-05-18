import re


# Reconhecer ddd no formato xx ou (xx)
ddd = r"^([1-9]{2}|\([1-9]{2}\))"

# Reconhecer número no formato 9xxxx-xxxx ou 9xxxxxxxx
numero_telefone = r"(\s?9\d{4}-?\d{4})$"

# Concatena ddd e numero_telefone e obtem a expressão
telefone_expressao = ddd + numero_telefone

# Compila a expressão regex
telefone_regex = re.compile(telefone_expressao)

# Números fictcios para teste
numeros_telefone = ["(91)99999-9999", "9899999-9999", "(11)91111-1111", "(51))988888888", "(81)96655842", "(91)977777777", "11 999999999"]

# String para guardar de forma separada DDD e números encontrados
dados_encontrados = ""

# Laço para percorrer os números
for numero in numeros_telefone:
    # Faz a busca dos padrões nos números disponibilizados
    numero_buscar = telefone_regex.findall(numero)
    # Extrai os padrões encontrados, separando em DDD e número
    if numero_buscar:
        for dados in numero_buscar:
            dados_encontrados += f"DDD: {dados[0].strip('()')}" \
                                 f"\nNúmero: {dados[1].strip()}\n" 

# Imprime o resultado
if dados_encontrados:
    print(dados_encontrados)                                
else:
    print("Nenhum número padrão de telefone encontrado.")


# DDD: 91
# Número: 99999-9999
# DDD: 98
# Número: 99999-9999
# DDD: 11
# Número: 91111-1111
# DDD: 91
# Número: 977777777
# DDD: 11
# Número: 999999999       