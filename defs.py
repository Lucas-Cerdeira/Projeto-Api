def valida_id(dados:set):
    C = 0
    while True:
        if C not in dados:
            dados.add(C)
            break
        C += 1
    return C


