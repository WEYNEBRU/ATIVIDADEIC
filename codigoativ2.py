def comparar_dnas(dna1, dna2):
    """
    Compara duas sequências de DNA e retorna o número de diferenças entre elas.
    Também conta e classifica bases inválidas (letras inválidas ou outros caracteres).

    :param dna1: Primeira sequência de DNA (string)
    :param dna2: Segunda sequência de DNA (string)
    :return: Um dicionário com:
        - 'desigualdades': Número total de diferenças entre as sequências
        - 'bases_invalidas': Contagem de bases inválidas, separadas por tipo
    :raises ValueError: Se as sequências de DNA não tiverem o mesmo comprimento
    """
    # Bases válidas do DNA
    bases_validas = {"A", "T", "C", "G"}
    
    # Verifica se as duas sequências têm o mesmo comprimento
    if len(dna1) != len(dna2):
        raise ValueError("As sequências de DNA devem ter o mesmo comprimento.")
    
    # Contadores e classificação de bases inválidas
    desigualdades = 0
    bases_invalidas = {
        "letras_invalidas": 0,
        "outros_caracteres": 0
    }
    
    # Compara as bases de ambas as sequências
    for base1, base2 in zip(dna1, dna2):
        # Verifica base1
        if base1 not in bases_validas:
            if base1.isalpha():
                bases_invalidas["letras_invalidas"] += 1
            else:
                bases_invalidas["outros_caracteres"] += 1
            desigualdades += 1
        
        # Verifica base2
        if base2 not in bases_validas:
            if base2.isalpha():
                bases_invalidas["letras_invalidas"] += 1
            else:
                bases_invalidas["outros_caracteres"] += 1
            desigualdades += 1
        
        # Conta desigualdade se as bases forem diferentes e válidas
        if base1 in bases_validas and base2 in bases_validas and base1 != base2:
            desigualdades += 1
    
    # Retorna os resultados
    return {
        "desigualdades": desigualdades,
        "bases_invalidas": bases_invalidas,
    }

# Exemplo de uso
dna1 = "ATC1XT@G"
dna2 = "ATCG#TYC"
resultado = comparar_dnas(dna1, dna2)

# Exibe os resultados
print(f"Número de desigualdades: {resultado['desigualdades']}")
print("Contagem de bases inválidas:")
print(f"Letras inválidas: {resultado['bases_invalidas']['letras_invalidas']}")
print(f"Outros caracteres: {resultado['bases_invalidas']['outros_caracteres']}")