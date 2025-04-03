import pandas as pd
import numpy as np

# Relative and cross-frequency analysis
def cfreq(a: pd.Series, b: pd.Series, digit: int = 2, ref: str = 'columns') -> pd.DataFrame:
    """
    Function to return a relative cross-tabulation frequency table with missing values and totals.

    Parameters:
    ----------
    a : pd.Series
        First data series to be studied. Example: ctable(df['Sex'], df['age']).
    b : pd.Series
        Second data series to be studied.
    digit : int, optional
        Number of decimal places for relative frequencies, default is 2.
    ref : str, optional
        Reference for proportion calculation, either 'index' (rows) or 'columns', default is 'columns'.

    Returns:
    -------
    pd.DataFrame
        A DataFrame containing the unified table of absolute frequencies and relative frequencies, including missing values and totals.

    Notes:
    ------
    - The output table contains both absolute counts and relative proportions (in percentage) enclosed in square brackets.
    - Missing values are represented as '<NA>'.
    - Totals are added to rows and columns, including a grand total.
    """
    
    # Saving variable names
    r_name: str = a.name  # Row variable name
    c_name: str = b.name  # Column variable name

    # Adding indicators for missing data
    b = np.where(b.isnull(), '<NA>', b)
    a = np.where(a.isnull(), '<NA>', a)
    
    # Creating absolute and relative frequency tables
    temp0: pd.DataFrame = pd.DataFrame(pd.crosstab(a, b, dropna=False))
    temp1: pd.DataFrame = pd.DataFrame(pd.crosstab(a, b, normalize=ref, dropna=False))
    temp1 = (temp1 * 100).round(digit)
    temp3: pd.DataFrame = temp0.copy()
    
    # Merging the tables
    for i in range(len(temp0)):
        for j in range(len(temp0.columns)):
            temp3.iloc[i, j] = str(
                temp0.iloc[i, j]) + ' [' + str(temp1.iloc[i, j]) + ']'
    
    # Adding totals
    temp3.loc['TOTAL'] = temp0.sum()
    tot: pd.Series = temp0.transpose().sum()
    temp3.insert(loc=len(temp3.columns), column='TOTAL', value=tot)
    temp3.iloc[len(temp3) - 1, len(temp3.columns) - 1] = temp3['TOTAL'].sum()
    temp3['TOTAL'] = temp3['TOTAL'].astype(int)
    
    # Adding variable names
    temp3.index.name = r_name
    temp3.columns.name = c_name

    return temp3