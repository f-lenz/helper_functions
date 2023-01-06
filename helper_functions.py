def ftab(df, var, dropna = False):
    ft = df.groupby(var, dropna = dropna).agg(n = ("churned", "size"),
                                    churned = ("churned", "sum"),
                                    churn_rate= ("churned", "mean")).reset_index()
    return ft
