#Frequencia cruzada e relativa
def cfreq(a,b,digit=2,ref='index'):

    """Função para retornar frequencia cruzada relativa com missing e totais"""
    """[a] e [b]  - dados a serem estudados - Ex: ctable(df['Sex'],df['age'])"""
    """ref - se a referência para proporção é nas linhas['index'] ou nas colunas ['columns']"""
    """digit - Numero de casas decimais, padrão 2 """
   
    import pandas as pd
    import numpy as np

    b = np.where(b.isnull(),'<NA>',b)
    a = np.where(a.isnull(),'<NA>',a)
    
    temp0 = pd.DataFrame(pd.crosstab(a,b,dropna=False))
    temp1 = pd.DataFrame(pd.crosstab(a,b,normalize=ref,dropna=False))
    temp1 = (temp1*100).round(digit)
    temp3 = temp0.copy()

    for i in range(len(temp0)):
        for j in range(len(temp0.columns)):

            temp3.iloc[i,j]=str(temp0.iloc[i,j]) + ' [' + str(temp1.iloc[i,j]) + ']'    

    temp3.loc['TOTAL'] = temp0.sum()
    tot = temp0.transpose().sum()
    temp3.insert(loc=len(temp3.columns),column='TOTAL',value=tot)
    temp3.iloc[len(temp3)-1,len(temp3.columns)-1] = temp3['TOTAL'].sum()
    temp3['TOTAL'] = temp3['TOTAL'].astype(int) 

    return temp3