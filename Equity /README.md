# Option Pricing Models with Monte Carlo

This project implements and compares three advanced option pricing models:

- Heston Stochastic Volatility Model
- Merton Jump-Diffusion Model
- Local Volatility Model (Dupire)

## 🔍 Objectives

- Calibrate models to a synthetic implied volatility surface
- Compare pricing performance on vanilla options
- Analyze differences in pricing exotic options:
  - Asian options
  - Barrier options (Down-and-Out)
  - Cliquet options

## ⚙️ Methods

- Monte Carlo simulation
- Numerical optimization:
  - Nelder-Mead (Heston)
  - Differential Evolution (Merton)
- Local volatility via Dupire formula

## 📊 Results

- Local Vol achieves best calibration (lowest RMSE)
- Merton captures jump risk but overestimates some prices
- Heston provides a balance between realism and flexibility

## 🧪 Technologies

- Python
- NumPy / SciPy
- Matplotlib

## 📁 Structure

- `src/`: model implementations
- `notebooks/`: analysis and experiments
- `report/`: full project report

## Author

Elia Ceolini
