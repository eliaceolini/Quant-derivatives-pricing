## Validation
# The Dupire local volatility framework is validated against the
# Black–Scholes model in the case of a flat implied volatility surface,
# recovering constant local volatility and consistent option prices.

import numpy as np

from Equity.market_data import Curve, ImpliedVolSurface, EquityMarketData
from Equity.dupire.calibration import DupireCalibrator
from Equity.dupire.pricer import DupirePricer

## Step 1 — Market data flat
# Market parameters
spot = 100.0
r = 0.01
q = 0.0
sigma = 0.2

# Grid
maturities = np.array([0.5, 1.0, 2.0])
strikes = np.linspace(60, 140, 9)

vols = sigma * np.ones((len(maturities), len(strikes)))

# Curves
discount_curve = Curve(maturities, r * np.ones_like(maturities))
dividend_curve = Curve(maturities, q * np.ones_like(maturities))

iv_surface = ImpliedVolSurface(maturities, strikes, vols)

market_data = EquityMarketData(
    spot,
    discount_curve,
    dividend_curve,
    iv_surface,
)


## Step 2 — Dupire calibration
calibrator = DupireCalibrator(market_data)
vol_surface, local_vol_surface = calibrator.calibrate()

## Step 3 — Check local vol ≈ constant
Ks = np.array([80, 100, 120])
Ts = np.array([0.5, 1.0, 1.5])

for K in Ks:
    for T in Ts:
        lv = local_vol_surface.local_vol(K, T)
        print(f"K={K}, T={T}, local vol={lv:.4f}")


## Step 4: Pricing test: Dupire vs Black–Scholes
# Dupire MC Price
pricer = DupirePricer(market_data, local_vol_surface)

price_dupire = pricer.price_european_call(
    K=100,
    T=1.0,
    n_paths=200_000,
    n_steps=200,
)

# Black–Scholes analytical price
from scipy.stats import norm

def bs_call(S, K, T, r, q, sigma):
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return (
        S * np.exp(-q * T) * norm.cdf(d1)
        - K * np.exp(-r * T) * norm.cdf(d2)
    )

price_bs = bs_call(spot, 100, 1.0, r, q, sigma)

print("Dupire MC:", price_dupire)
print("BS price:", price_bs)
