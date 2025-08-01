def perfil_investidor(renda):
    '''
    Função para categorizar perfil do investidor de acordo com a renda mensal.
    '''
    if renda < 100000:
        return 'Conservador'
    elif renda < 200000:
        return 'Moderado'
    else:
        return 'Arrojado'