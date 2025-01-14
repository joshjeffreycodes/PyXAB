from PyXAB.synthetic_obj import *
from PyXAB.algos import *

from PyXAB.partition.BinaryPartition import BinaryPartition
from PyXAB.utils.plot import compare_regret, compare_regret_withsd
import numpy as np


def main(algo_list, target, domain, partition, noise=0.1, rounds=1000):
    algo_dictionary = {'T-HOO': HOO.T_HOO(rounds=rounds, domain=domain, partition=partition),
                       'HCT': HCT.HCT(domain=domain, partition=partition),
                       'VHCT': VHCT.VHCT(domain=domain, partition=partition),
                       'POO': POO.POO(domain=domain, partition=partition, algo=HOO.T_HOO),
                       'PCT': PCT.PCT(domain=domain, partition=partition)}

    results_dictionary = {}
    for name in algo_list:
        print(name, ": training")
        algo = algo_dictionary[name]
        regret_list = []
        regret = 0
        for t in range(1, rounds + 1):

            print(t)
            point = algo.pull(t)
            reward = target.f(point) + np.random.uniform(-noise, noise)
            algo.receive_reward(t, reward)
            inst_regret = target.fmax - target.f(point)
            regret += inst_regret
            regret_list.append(regret)

        results_dictionary[name] = np.array(regret_list)

    return results_dictionary


target = Rastrigin.Rastrigin()
domain = [[-1, 1], [-1, 1], [-1, 1], [-1, 1]]
partition = BinaryPartition
rounds = 500
noise = 0.1


trials = 5
regret_array_HOO = np.array([main(['T-HOO'], target, domain, partition, noise, rounds) for _ in range(trials)])
regret_array_HCT = np.array([main(['HCT'], target, domain, partition, noise, rounds) for _ in range(trials)])
regret_array_VHCT = np.array([main(['VHCT'], target, domain, partition, noise, rounds) for _ in range(trials)])
regret_array_POO = np.array([main(['POO'], target, domain, partition, noise, rounds) for _ in range(trials)])
regret_array_PCT = np.array([main(['PCT'], target, domain, partition, noise, rounds) for _ in range(trials)])


regret_dic = {"regret": [regret_array_VHCT, regret_array_HCT, regret_array_HOO, regret_array_POO, regret_array_PCT],
              "labels": ["VHCT", "HCT", 'T-HOO',  'POO', 'PCT'],
              "colors": ['red', 'blue', 'green', 'grey', 'orange']}

compare_regret_withsd(regret_dic)