# Equity Derivatives Pricing

This module contains implementations of local and stochastic
volatility models for equity derivatives pricing, with a focus on
market-consistent calibration and Monte Carlo simulation.

## Models

### Local Volatility (Dupire)
- Construction of implied volatility surface
- Dupire local volatility formula
- Numerical stabilization techniques
- Monte Carlo pricing of European and exotic options

### Stochastic Volatility (Heston)
- Risk-neutral Heston dynamics
- Calibration to implied volatility surface
- Monte Carlo pricing of European and exotic options

## Methodology
- Calibration performed via least squares minimization
- Monte Carlo simulation with correlated Brownian motions
- Validation against analytical benchmarks where available

## Structure
- `market_data.py`: synthetic or market-like implied vol data
- `volatility_surface.py`: interpolation and surface handling
- `dupire/`: local volatility model implementation
- `heston/`: stochastic volatility model implementation
- `monte_carlo/`: shared Monte Carlo engine

## Disclaimer
This code is for educational and research purposes only.

## Module Structure
Equity/
├── README.md
├── market_data.py
├── volatility_surface.py
├── heston/
│   ├── dynamics.py
│   ├── calibration.py
│   └── pricer.py
├── dupire/
│   ├── local_vol_surface.py
│   ├── calibration.py
│   └── pricer.py
├── monte_carlo/
│   └── engine.py
└── examples/
    ├── heston_calibration.ipynb
    ├── dupire_calibration.ipynb
    └── exotic_pricing.ipynb

