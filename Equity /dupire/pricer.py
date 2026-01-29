import numpy as np


class DupirePricer:
    """
    Monte Carlo pricer under Dupire local volatility model.
    """

    def __init__(self, market_data, local_vol_surface):
        self.market_data = market_data
        self.local_vol_surface = local_vol_surface

    def price_european_call(
        self,
        K,
        T,
        n_paths=100_000,
        n_steps=200,
        seed=42,
    ):
        np.random.seed(seed)

        dt = T / n_steps
        S = np.full(n_paths, self.market_data.spot)

        for i in range(n_steps):
            t = (i + 1) * dt
            Z = np.random.normal(size=n_paths)

            sigma_loc = self.local_vol_surface.local_vol(S, t)
            r = self.market_data.discount_curve(t)
            q = self.market_data.dividend_curve(t)

            S *= np.exp(
                (r - q - 0.5 * sigma_loc ** 2) * dt
                + sigma_loc * np.sqrt(dt) * Z
            )

        payoff = np.maximum(S - K, 0.0)
        discount = np.exp(-self.market_data.discount_curve(T) * T)

        return discount * payoff.mean()

