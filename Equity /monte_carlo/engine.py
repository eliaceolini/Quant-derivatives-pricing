import numpy as np


class MonteCarloEngine:
    """
    Generic Monte Carlo engine.
    """

    def __init__(self, n_paths, n_steps, T, seed=None):
        self.n_paths = n_paths
        self.n_steps = n_steps
        self.T = T
        self.dt = T / n_steps

        if seed is not None:
            np.random.seed(seed)

    def brownian_increments(self, dim=1):
        """
        Generate Brownian increments.
        """
        return np.random.normal(
            scale=np.sqrt(self.dt),
            size=(self.n_steps, self.n_paths, dim),
        )

