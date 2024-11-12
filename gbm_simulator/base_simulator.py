import numpy as np

class GBMSimulator:
    """
    Description of GBMSimulator

    Attributes:
        y0=y0 (type):
        mu=mu (type):
        sigma=sigma (type):

    Args:
        y0 (undefined):
        mu (undefined):
        sigma (undefined):

    """
    def __init__(self, y0, mu, sigma):
       
        self.y0=y0
        self.mu=mu
        self.sigma=sigma

    def simulate_path(self, T, N):
        """
        Simulates a path of the Geometric Brownian Motion.

        Args:
            T (float): The time horizon.
            N (int): The number of steps up to T.
        """
        #T is time horizon
        #N is number of steps up to T
        dt = T / N  # time increment

        # Time increments
        t = np.linspace(0, T, N)

        # Brownian motion
        B = np.random.standard_normal(size=N)
        B = np.cumsum(B) * np.sqrt(dt)

        #note t, B are vectors
        Y=(self.y0)*np.exp( ( self.mu - (self.sigma**2)/2 )  * t + self.sigma * B )

        return t, Y