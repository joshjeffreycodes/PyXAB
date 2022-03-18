import math
import numpy as np
import pdb


def mysin2(x):
    return (np.sin(x*2*np.pi)+1)/2.

class DoubleSine:
    def __init__(self, rho1, rho2, tmax):
        self.ep1 = -math.log(rho1, 2)
        self.ep2 = -math.log(rho2, 2)
        self.tmax = tmax
        self.fmax = 0.

    def f(self, x):
        x = x[0]
        u = 2*np.fabs(x-self.tmax)
        if u == 0:
            return 0.
        else:
            envelope_width = math.pow(u, self.ep2)-math.pow(u, self.ep1)
            return mysin2(math.log(u, 2)/2.)*envelope_width - math.pow(u, self.ep2)

    def fmax(self):
        return self.fmax


# DoubleSine function perturbed by Gaussian noise

class Perturbed_DoubleSine:

    def __init__(self, rho1, rho2, tmax):
        self.ep1 = -math.log(rho1, 2)
        self.ep2 = -math.log(rho2, 2)
        self.tmax = tmax
        self.perturb = np.random.normal(0, 1)

        self.fmax = 0. + self.perturb

    def f(self, x):
        x = x[0]
        u = 2*np.fabs(x-self.tmax)
        if u == 0:
            return 0.
        else:
            envelope_width = math.pow(u, self.ep2)-math.pow(u, self.ep1)
            return mysin2(math.log(u, 2)/2.)*envelope_width - math.pow(u, self.ep2) + self.perturb

