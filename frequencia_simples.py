import pandas as pd

def freq(serie: pd.Series, ordena_nome: bool = False, digitos: int = 2) -> pd.DataFrame:
    """
    Function to return relative frequency with missing values included.

    Parameters:
    ----------
    serie : pd.Series
        Data series to be analyzed. Example: freq(df['Sex']).
    ordena_nome : bool, optional
        Whether to sort the table by name (`True`) or by frequency (`False`). Default is `False`.
    digitos : int, optional
        Number of decimal places for relative frequencies. Default is 2.

    Returns:
    -------
    pd.DataFrame
        A DataFrame containing the frequency table with counts and percentages, including missing values and totals.

    Notes:
    ------
    - The table includes absolute frequencies, relative percentages, missing values (`<NA>`), and a grand total.
    - The `%` column represents the percentage of each category relative to the total count.
    """
    
    # Creating the frequency table with absolute counts
    temp: pd.DataFrame = pd.DataFrame(serie.value_counts())

    # Sorting by name if requested
    if ordena_nome:
        temp = temp.sort_index() 

    # Adding missing value counts
    missing: pd.Series = pd.Series(
        data={temp.columns[0]: serie.isnull().sum()},
        name='<NA>'
    )
    temp = temp.append(missing, ignore_index=False)

    # Adding total row
    nr: pd.Series = pd.Series(
        data={temp.columns[0]: sum(temp[temp.columns[0]])},
        name='TOTAL'
    )
    temp = temp.append(nr, ignore_index=False)

    # Calculating percentages and adding the '%' column
    temp['%'] = (temp[temp.columns[0]] / temp.loc['TOTAL'][0] * 100).round(digitos)

    return temp
