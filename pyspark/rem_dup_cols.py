
from pyspark.sql import DataFrame


def remove_dup_cols(df:DataFrame) -> DataFrame:
    """ This function will remove duplicated columns from a dataframe.
        params: df: The dataframe to be processed.
        return: A dataframe with the duplicated columns removed.
    """
    cols= [] 
    seen = set()
    for c in df.columns:
        cols.append('{}_dup'.format(c) if c in seen else c)
        seen.add(c)
    return df.toDF(*cols).select(*[c for c in cols if not c.endswith('_dup')])