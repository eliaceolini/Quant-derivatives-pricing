import numpy as np
import pandas as pd
from scipy.interpolate import interp1d, RegularGridInterpolator


class Curve:
    """
    Generic term structure (e.g. discount or dividend curve).
    """

    def __init__(self, times, values, kind="linear"):
        self.times = np.asarray(times)
        self.values = np.asarray(values)
        self._interp = interp1d(
            self.times,
            self.values,
            kind=kind,
            fill_value="extrapolate",
        )

    def __call__(self, T):
        return self._interp(T)


class ImpliedVolSurface:
    """
    Implied volatility surface defined on a (T, K) grid.
    """

    def __init__(self, maturities, strikes, vols):
        self.maturities = np.asarray(maturities)
        self.strikes = np.asarray(strikes)
        self.vols = np.asarray(vols)

        self._interp = RegularGridInterpolator(
            (self.maturities, self.strikes),
            self.vols,
            bounds_error=False,
            fill_value=None,
        )

    def __call__(self, K, T):
        point = np.array([T, K]).T
        return self._interp(point)


class EquityMarketData:
    """
    Container for equity market data.
    """

    def __init__(
        self,
        spot: float,
        discount_curve: Curve,
        dividend_curve: Curve,
        implied_vol_surface: ImpliedVolSurface,
    ):
        self.spot = spot
        self.discount_curve = discount_curve
        self.dividend_curve = dividend_curve
        self.implied_vol_surface = implied_vol_surface

    def discount_factor(self, T):
        return self.discount_curve(T)

    def dividend_yield(self, T):
        return self.dividend_curve(T)

    def implied_vol(self, K, T):
        return self.implied_vol_surface(K, T)
