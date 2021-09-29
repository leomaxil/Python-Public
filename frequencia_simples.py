#FUNCOES
def freq(serie,ordena_nome=False,digitos=2):
    
    import pandas as pd
    
    """Função para retornar frequencia relativa com missing"""
    """serie - dados a serem estudados - Ex: freq(df['Sex'])"""
    """ordena_nome - Se a ordem da tabela é dada pelo nome True, pela Frequencia False"""
    """digitos - Numero de casas decimais, padrão 2 """
    
    temp = pd.DataFrame(serie.value_counts())

    if(ordena_nome):
        temp = temp.sort_index() 

    missing = pd.Series(
        data={temp.columns[0]:serie.isnull().sum()},
        name = '<NA>')

    temp = temp.append(missing, ignore_index=False)

    nr = pd.Series(
        data = {temp.columns[0]:sum(temp[temp.columns[0]])},
        name = 'TOTAL')

    temp = temp.append(nr, ignore_index=False)

    temp['%']=(temp[temp.columns[0]]/temp.loc['TOTAL'][0]*100).round(digitos)

    return temp