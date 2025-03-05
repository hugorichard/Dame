import numpy as np
from dame.algos import Duchi, DAME, binary_search
from tqdm import tqdm


def phi(a):
    return 579/(n*alpha**2) * 3/2 * np.log( 8 * max(a * n * alpha**2, 1) / np.log( 8 * max(a * n * alpha**2, 1)))

def run_expe(n, alpha, rho, m1, m2, seed):
    rng = np.random.RandomState(seed)
    ms = []
    for i in range(n):
        B = rng.binomial(1, rho)
        if B ==1:
            m = m2
        else:
            m = m1
        ms.append(m)
    ms = np.array(ms)
    m_max = binary_search(phi,m1, m2, 100, ms)
    X = []
    for i in range(n):
        m = ms[i]
        X.append((np.random.binomial(m, 0.5) / m  - 0.5) * 2)
    return (Duchi(X, alpha), DAME(X, ms, alpha, np.min(ms), ms), DAME(X, ms, alpha, m_max, ms))


n = 100000
alpha = 22/35
m1 = 100000
m2 = 100000000
rhos = np.linspace(0, 1, 10)
seeds  = np.arange(50)

duchi_res, kent_res, dame_res = [], [], []
for rho in tqdm(rhos):
    duchis, kents, dames = [], [], []
    for seed in seeds:
        duchi, kent, dame = run_expe(n, alpha, rho, m1, m2, seed)
        duchis.append(duchi)
        kents.append(kent)
        dames.append(dame)
    duchi_res.append(duchis)
    kent_res.append(kents)
    dame_res.append(dames)

np.save("duchi_bernoulli", duchi_res)
np.save("kent_bernoulli", kent_res)
np.save("dame_bernoulli", dame_res)