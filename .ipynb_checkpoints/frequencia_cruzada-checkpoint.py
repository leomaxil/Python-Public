#Frequencia cruzada e relativa
def cfreq(a,b,digit=2,ref='columns'):

    """Função para retornar frequencia cruzada relativa com missing e totais"""
    """[a] e [b]  - dados a serem estudados - Ex: ctable(df['Sex'],df['age'])"""
    """ref - se a referência para proporção é nas linhas['index'] ou""
    ""nas colunas ['columns']"""
    """digit - Numero de casas decimais, padrão 2 """
   
    import pandas as pd
    import numpy as np
    
    #guardando os nomes das variáveis
    r_name = a.name
    c_name = b.name

    #Inserindo os indicadores de dados perdidos
    b = np.where(b.isnull(),'<NA>',b)
    a = np.where(a.isnull(),'<NA>',a)
    
    #criando as tabelas de frequencia absoluta e relativa
    temp0 = pd.DataFrame(pd.crosstab(a,b,dropna=False))
    temp1 = pd.DataFrame(pd.crosstab(a,b,normalize=ref,dropna=False))
    temp1 = (temp1*100).round(digit)
    temp3 = temp0.copy()
    
    #unificando as tabelas
    for i in range(len(temp0)):
        for j in range(len(temp0.columns)):

            temp3.iloc[i,j]=str(
                temp0.iloc[i,j])+ ' [' + str(temp1.iloc[i,j]) + ']'    

    #adicionando totais 
    temp3.loc['TOTAL'] = temp0.sum()
    tot = temp0.transpose().sum()
    temp3.insert(loc=len(temp3.columns),column='TOTAL',value=tot)
    temp3.iloc[len(temp3)-1,len(temp3.columns)-1] = temp3['TOTAL'].sum()
    temp3['TOTAL'] = temp3['TOTAL'].astype(int) 
    
    #adicionando nomes das variáveis
    temp3.index.name = r_name
    temp3.columns.name = c_name

    return temp3