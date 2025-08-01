def categorizar_faixa_etaria(idade):
    '''
    Função para categorizar faixa etária de acordo com a coluna 'Idade'.
    '''
    if idade < 25:
        return '< 25'
    elif idade < 35:
        return '25-35' 
    elif idade < 50:
        return '35-50'
    else:
        return '50 >'
