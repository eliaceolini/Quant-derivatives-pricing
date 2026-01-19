import numpy as np
from scipy.optimize import least_squares

class HestonCalibrator:

    def __init__(self, pricer, market_surface):
        self.pricer = pricer
        self.market_surface = market_surface

    def objective(self, x):
        params = self._build_params(x)
        errors = []

        for option in self.market_surface.options:
            model_price = self.pricer.price(
                params=params,
                strike=option.strike,
                maturity=option.maturity
            )
            errors.append(model_price - option.price)

        return np.array(errors)

    def calibrate(self, x0, bounds):
        result = least_squares(
            self.objective,
            x0=x0,
            bounds=bounds,
            method="trf"
        )
        return result
