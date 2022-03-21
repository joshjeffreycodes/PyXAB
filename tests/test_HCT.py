from synthetic_obj import *

from algos.HCT import HCT
from partition.BinaryPartition import BinaryPartition
import numpy as np

T = 5000
Target = HimmelBlau.Himmelblau()
domain = [[-5, 5], [-5, 5]]
partition = BinaryPartition(domain)
algo = HCT(partition=partition)

cumulative_regret = 0
cumulative_regret_list = [0]



for t in range(1, T+1):

    # HCT
    point = algo.pull(t)
    reward = Target.f(point) + np.random.uniform(-0.1, 0.1)
    algo.receive_reward(t, reward)
    inst_regret = Target.fmax - Target.f(point)
    cumulative_regret += inst_regret
    cumulative_regret_list.append(cumulative_regret)
    #pdb.set_trace()
    print(t, point)