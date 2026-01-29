from Equity.volatility_surface import VolatilitySurface
from Equity.dupire.local_vol_surface import DupireLocalVolSurface


class DupireCalibrator:
    """
    Calibration pipeline for Dupire local volatility model.
    """

    def __init__(self, market_data):
        self.market_data = market_data

    def calibrate(self):
        """
        Market implied vols -> smooth vol surface -> local vol surface
        """
        vol_surface = VolatilitySurface(self.market_data)
        local_vol_surface = DupireLocalVolSurface(vol_surface)

        return vol_surface, local_vol_surface

