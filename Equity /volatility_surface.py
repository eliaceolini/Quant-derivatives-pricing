import numpy as np
from scipy.interpolate import RectBivariateSpline


class VolatilitySurface:
    """
    Smooth implied volatility surface in log-moneyness and maturity.
    """

    def __init__(self, market_data):
        self.market_data = market_data
        self.spot = market_data.spot

        # Extract grid
        maturities = market_data.implied_vol_surface.maturities
        strikes = market_data.implied_vol_surface.strikes
        vols = market_data.implied_vol_surface.vols

        # Forward approximation
        forwards = self.spot * np.exp(
            -market_data.dividend_curve(maturities)
            * maturities
            + market_data.discount_curve(maturities)
            * maturities
        )

        log_moneyness = np.log(strikes[None, :] / forwards[:, None])
        total_variance = (vols ** 2) * maturities[:, None]

        self._spline = RectBivariateSpline(
            maturities,
            log_moneyness[0],
            total_variance,
            kx=3,
            ky=3,
        )

    def total_variance(self, K, T):
        F = self.spot * np.exp(
            -self.market_data.dividend_curve(T) * T
            + self.market_data.discount_curve(T) * T
        )
        k = np.log(K / F)
        return self._spline(T, k, grid=False)

    def implied_vol(self, K, T):
        w = self.total_variance(K, T)
        return np.sqrt(w / T)

    def dwdk(self, K, T):
        F = self.spot * np.exp(
            -self.market_data.dividend_curve(T) * T
            + self.market_data.discount_curve(T) * T
        )
        k = np.log(K / F)
        return self._spline(T, k, dx=0, dy=1, grid=False)

    def dwdT(self, K, T):
        F = self.spot * np.exp(
            -self.market_data.dividend_curve(T) * T
            + self.market_data.discount_curve(T) * T
        )
        k = np.log(K / F)
        return self._spline(T, k, dx=1, dy=0, grid=False)

