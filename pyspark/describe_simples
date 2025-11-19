def describe_simples(x: str, df: DataFrame, group_by: str = [], decimal_cases: int = 3) -> DataFrame:
    """
    Generates descriptive statistics for a numeric column with optional grouping.
    
    Calculates summary statistics including minimum, quartiles, mean, maximum,
    and standard deviation for a specified numeric column, with optional grouping
    by one or more categorical columns.

    Args:
        x (str): Name of the numeric column to analyze
        df (DataFrame): Input Spark DataFrame containing the data
        group_by (str, optional): Column name(s) to group by. Can be a single
            column name as string or list of column names. Defaults to [] (no grouping).
        decimal_cases (int, optional): Number of decimal places to round results to.
            Defaults to 3.

    Returns:
        DataFrame: A DataFrame with summary statistics including:
            - min: Minimum value
            - P25: 25th percentile (first quartile)
            - avg: Mean/average value
            - P50: 50th percentile (median)
            - P75: 75th percentile (third quartile)
            - max: Maximum value
            - std: Standard deviation
            - Nulls: Missing values

    Examples:
        >>> # Basic usage without grouping
        >>> stats = describe_simples("salary", employees_df)
        
        >>> # With grouping by department
        >>> stats_by_dept = describe_simples("salary", employees_df, "department")
        
        >>> # With multiple grouping columns and custom decimal precision
        >>> stats_detail = describe_simples("salary", employees_df, ["department", "level"], 2)
    """
    df_result = (df.groupBy(group_by).agg(
        F.round(F.min(x),decimal_cases).alias('Min'),
        F.round(F.approx_percentile(x, 0.25),decimal_cases).alias('P25'),
        F.round(F.avg(x), decimal_cases).alias('Avg'),
        F.round(F.approx_percentile(x, 0.5),decimal_cases).alias('P50'),
        F.round(F.approx_percentile(x, 0.75),decimal_cases).alias('P75'),
        F.round(F.max(x),decimal_cases).alias('Max'),
        F.round(F.stddev(x),decimal_cases).alias('Std'),
        F.count('*').alias('N'),
        F.round(F.sum(F.col(x).isNull().cast("int")),decimal_cases).alias('Nulls') 
            ).withColumn('perc_nuls', F.round(F.col('Nulls')/F.col('N'),3)*100)
                 
                 )

    
    return df_result.display()
