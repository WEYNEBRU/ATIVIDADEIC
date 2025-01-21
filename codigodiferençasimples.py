    def comparar_dnas(dna1, dna2):
    """
    Compara duas sequências de DNA e retorna o número de diferenças entre elas.

    :param dna1: Primeira sequência de DNA (string)
    :param dna2: Segunda sequência de DNA (string)
    :return: Número total de desigualdades (diferenças entre as sequências)
    :raises ValueError: Se as sequências de DNA não tiverem o mesmo comprimento
    """
    #Atenção com o uso do ":" para as funções funcionarem corretamente
    # Verificar se as sequências têm o mesmo comprimento
    if len(dna1) != len(dna2):  # O ":" é necessário aqui
        raise ValueError("As sequências de DNA devem ter o mesmo comprimento.")
    
    # Inicializar contador de desigualdades
    desigualdades = 0
    
    # Comparar as bases de ambas as sequências
    for base1, base2 in zip(dna1, dna2):  # O ":" é necessário aqui
        # Contar desigualdade se as bases forem diferentes
        if base1 != base2:  # O ":" é necessário aqui
            desigualdades += 1
    
    # Retornar o número de desigualdades
    return desigualdades  # Não precisa de ":" aqui

resultado = comparar_dnas(dna1, dna2)
print(f"Número de desigualdades: {resultado}")
