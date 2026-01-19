# Quantitative Derivatives Pricing Library

This repository contains production-style implementations of
quantitative models for pricing derivatives, with a focus on
Monte Carlo methods and market-consistent calibration.

## Projects
### Equity Derivatives
- Dupire local volatility model
- Heston stochastic volatility model
- Calibration to implied volatility surface
- Monte Carlo pricing of exotic options

### Interest Rate Derivatives
- Curve construction and bootstrapping
- LMM dynamics
- Cap/Floor pricing
- Monte Carlo vs analytical benchmarks

### Inflation-Linked Derivatives
- LMM-based nominal rates
- Deterministic real rates
- Inflation forward construction
- Monte Carlo pricing of caps and floors
- Antithetic variates and moment matching
- Validation against EIOPA curves and market quotes

## Technologies
- Python (NumPy, SciPy, pandas)
- Object-oriented design
- Pytest for validation
- Market data alignment and model validation

## Disclaimer
For educational and research purposes only.
