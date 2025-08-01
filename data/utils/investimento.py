def potencial_investimento(renda):
    '''
    Função para categorizar potencial de investimento de acordo com a renda anual.
    '''
    if renda < 200000:
        return 'Baixo'
    elif renda < 500000:
        return 'Médio'
    else:
        return 'Alto'