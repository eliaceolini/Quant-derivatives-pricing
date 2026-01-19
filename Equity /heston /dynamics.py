from dataclasses import dataclass

@dataclass
class HestonParams:
    kappa: float
    theta: float
    xi: float
    rho: float
    v0: float

class HestonModel:
    def __init__(self, params: HestonParams, r: float):
        self.params = params
        self.r = r
