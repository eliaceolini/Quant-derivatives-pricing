import numpy as np


class DupireLocalVolSurface:
    """
    Dupire local volatility surface derived from implied volatility surface.
    """

    def __init__(self, vol_surface, eps=1e-6):
        self.vol_surface = vol_surface
        self.eps = eps

    def local_variance(self, K, T):
        w = self.vol_surface.total_variance(K, T)
        dwdT = self.vol_surface.dwdT(K, T)
        dwdk = self.vol_surface.dwdk(K, T)

        # Second derivative in log-moneyness via finite differences
        dk = 1e-4
        w_plus = self.vol_surface.total_variance(
            K * np.exp(dk), T
        )
        w_minus = self.vol_surface.total_variance(
            K * np.exp(-dk), T
        )
        d2wdk2 = (w_plus - 2 * w + w_minus) / dk ** 2

        # Forward moneyness
        F = self.vol_surface.market_data.spot * np.exp(
            -self.vol_surface.market_data.dividend_curve(T) * T
            + self.vol_surface.market_data.discount_curve(T) * T
        )
        k = np.log(K / F)

        numerator = dwdT

        denominator = (
            1
            - (k / w) * dwdk
            + 0.25 * (-0.25 - 1.0 / w) * dwdk ** 2
            + 0.5 * d2wdk2
        )

        denominator = np.maximum(denominator, self.eps)

        return numerator / denominator

    def local_vol(self, K, T):
        lv2 = self.local_variance(K, T)
        return np.sqrt(np.maximum(lv2, 0.0))

