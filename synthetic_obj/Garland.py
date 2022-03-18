import math
import numpy as np
import pdb

class Garland:
    def __init__(self):

        self.fmax = 1

    def f(self, x):

        x = x[0]

        return x * (1-x) * (4 - np.sqrt(np.abs(np.sin(60 * x))))



# Garland function perturbed by Gaussian noise

class Perturbed_Garland:

    def __init__(self):



        self.perturb = np.random.normal(0, 1)

        self.fmax = 1 + self.perturb

    def f(self, x):

        x = x[0]

        return x * (1-x) * (4 - np.sqrt(np.abs(np.sin(60 * x)))) + self.perturb
