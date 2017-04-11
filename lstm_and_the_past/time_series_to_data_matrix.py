"""
@author: Nikolay Lysenko
"""
# TODO: Write script-level docstring


def convert_to_lag_matrix(ser, n_lags=3):
    """
    Converts time series represented by `ser`
    to a data matrix with lag features
    and target variable.
    Parameter `n_lags` defines number of
    previous values to be used.
    
    @type ser: pandas.Series
    @type n_lags: int
    @return: pandas.DataFrame
    """
    df = pd.DataFrame(ser, columns=['target'])
    for i in range(1, n_lags + 1):
        df['lag_{}'.format(i)] = df['target'].shift(i)
    df = df.dropna()
    features = ['lag_{}'.format(i) for i in range(1, n_lags + 1)]
    return df[features + ['target']]
