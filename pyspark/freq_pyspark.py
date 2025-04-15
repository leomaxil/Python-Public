from pyspark.sql import functions as F
from pyspark.sql import Window
from pyspark.sql.types import *
from pyspark.sql import DataFrame

#DEFINING UTILS FUNCTIONS

def freq_simples(x: str, df: DataFrame, decimal_cases: int = 3, relative_perc: str = "Column_name") -> DataFrame:
    """This function will compute the frequency and the percentual
        of a silgle variable. 
        params:
            x: The name or a list of names of the varibles of interess
            df: The datafram whos contains the variable of interess
            decimal_cases: The number of decimal cases to be used in the percentual column.
            relative_perc: The name of the column that will be used to calculate the relative percentual.
        return: A dataframe with the frequency and the percentual of the variable.
    """
    df_result =(df
                .groupBy(x).count()
                .withColumn('Percentual [%]',
                            F.round( F.col('count')*100/F.sum('count')
                                    .over(Window.partitionBy()),decimal_cases)
                            )
                )
    
    if relative_perc != "Column_name":
        df_result = (df_result.withColumn('total_relative', F.sum('count').over(Window.partitionBy(relative_perc)))
                     .withColumn(f'Relative [%] of {relative_perc}',
                            F.round( F.col('count')*100/F.col('total_relative'),decimal_cases)
                            )
                     .drop('total_relative')
                     
                     )    


    return df_result.display()