import pandas as pd

def drawdown (rets: pd.Series):
    """take a time series of asset returs.
     returns a dataframe with columns for 
     the wealth index,
     the previous peaks, and 
     the percentage drawdown """

    wealth_in_dex = 1000*(1+rets).cumprod()
    previous_peaks = wealth_index.cummax ()
    drawdowns = (wealth_index - previous_peaks)/previous_peaks
    return pd.DataFrame ({"Wealth": wealth_index,
                          "Previous Peak": previous_peaks,
                          "Drawdown": drawdowns
                         })


def get_ffme_rets():

    me_m = pd.read_csv ("Portfolios_Formed_on_ME_monthly_EW.csv",
                    header=0, index_col=0, parse_dates=True, na_values=-99.99)
    rets = me_m [['Lo 10','Hi 10']]
    rets.columns = ['SmallCap','LargeCap']
    rets = rets/100
    rets.plot.line(figsize=(10,4))


def get_hfi_rets():

    hfi = pd.read_csv ("edhec-hedgefundindices.csv",
                   header=0, index_col=0, parse_dates=True, dayfirst=True)
    
    hfi = hfi/100
    return hfi


def skewness (r):
    """
    Alternative to scipy.stats.skew()
    Computes the skewness of the supplied Series or DataFrame
    Returns a float or a series
    """
    demanded_r = r - r.mean()
    # use the population standard deviation, so set dof=0
    sigma_r = r.std (ddof=0)
    exp = (demanded_r**3).mean()
    return exp/sigma_r**3


def kurtosis (r):
    """
    Alternative to scipy.stats.kurtosis()
    Computes the kurtosis of the supplied Series or DataFrame
    Returns a float or a series
    """
    demanded_r = r - r.mean()
    # use the population standard deviation, so set dof=0
    sigma_r = r.std (ddof=0)
    exp = (demanded_r**4).mean()
    return exp/sigma_r**4



def var_historic (r, level=5):
    """
    Var Historic
    """
    if isinstance (r, pd.DataFrame):
        return r.aggregate(var_historic, level=level)
    elif isinstance (r, pd.Series):
        return np.percentile (r,level)
    else:
        raise TypeError ("Expected r to be a Series or DataFrame")

from scipy.stats import norm
def var_gaussian (r, level=5):
    """
    Return the Parametric Gaussian Var 
    """
    z =norm.ppf (level/100)
    return -(hfi.mean() + z*hfi.std (ddof=0))
       













