import numpy as np

def Duchi(X, alpha):
    """
    X: data
    List of len n
    """
    Z = []
    for x in X:
        z = x + np.random.laplace(0, 2/alpha)
        Z.append(z)
    return np.mean(Z)


def DAME(X, ms, alpha, m_max, M):
    """Implements DAME algorithm

    Args:
        X (np array of size n_users): X[i] is the empirical mean of the dataset of user i
        ms (np array of size n_users): ms[i] is the dataset size of user i
        alpha (float): Privacy leakage level
        m_max (int): Effective maximum dataset size
        M (np array): Samples from the distribution of dataset sizes. It is used to approximate expectations. The higher the number of samples is, the more precise the approximation.

    Returns:
        theta (float): The mean estimate
    """
    n = len(X)
    tau  = np.sqrt(2 * np.log(8 * max(np.sqrt(m_max * n * alpha**2), 1)) / m_max)
    X1 = X[:int(n/2)]
    X2 = X[int(n/2):]

    votes = np.zeros(int(np.ceil(1/tau)))
    bins = []
    for j in range(int(np.ceil(1/tau))):
        bins.append(( -1 + j*2 * tau, min(-1 + (j+1) * 2 * tau, 1) ))
    real_votes = np.zeros(int(np.ceil(1/tau)))
    for index in range(len(X1)):
        x = X1[index]
        Vu = np.zeros(int(np.ceil(1/tau)))
        if ms[index] >= m_max:
            for j in range(int(np.ceil(1/tau))):
                if (bins[j][0] <= x <= bins[j][1]):
                    Vu[j] = 1
                    Vu[max(j-1, 0)] = 1
                    Vu[min(j+1, int(np.ceil(1/tau)) - 1)] = 1
        real_votes += Vu

        B = np.random.binomial(1, np.exp(alpha/6) / (1 + np.exp(alpha/6)), size=int(np.ceil(1/tau)))
        tVu = np.zeros(int(np.ceil(1/tau)))
        for j in range(int(np.ceil(1/tau))):
            if B[j] == 1:
                tVu[j] = Vu[j]
            else:
                tVu[j] = 1- Vu[j]
        votes += tVu
    jhat = np.argmax(votes)
    sj = (bins[jhat][0] + bins[jhat][1]) / 2
    Lj, Uj = bins[jhat][0], bins[jhat][1]
    Lj = max(-1, Lj - 6 * tau)
    Uj = min(1, Uj + 6 * tau)

    theta_m = []
    for index in range(len(X2)):
        x = X2[index]
        mu = ms[index]
        xhat = np.sqrt(min(mu, m_max))/np.sqrt(m_max) * (x + (np.sqrt(m_max) / np.sqrt(min(mu, m_max)) - 1) * sj)
        if xhat < Lj:
            xhat = Lj
        if xhat > Uj:
            xhat = Uj
        thetau = xhat + np.random.laplace(0, min(14 * tau, 2) / alpha)
        theta_m.append(thetau)

    ss = np.mean((np.sqrt(m_max) - np.sqrt(M)) * (M <= m_max))
    # ss = (np.sqrt(m_max) - np.sqrt(m_1)) * (1 - rho) + rho * (np.sqrt(m_max) - np.sqrt(min(m_max, m_2)))
    # mm  = np.sqrt(min(m_1, m_max)) * (1 - rho) + np.sqrt(min(m_2, m_max)) * rho
    mm = np.mean(np.minimum(M, np.sqrt(m_max)))
    theta = (np.mean(theta_m) * np.sqrt(m_max) - ss * sj) / mm
    return theta

def binary_search(phi, m1, m2, n_iter, M):
    """Binary search to solve argmax_a {P(m >= a)^2 >= min(phi(a), 1)}

    Args:
        phi (int -> float): an increasing function
        n_iter (int): Maximum number of binary search iterations to perform
        m1 (int): m1 is such that P(m >= m1)^2 - min(phi(m1), 1) >= 0
        m2 (int): m2 is such that P(m >= m2)^2 - min(phi(m2), 1) < 0
        M (np array): Samples from the distribution of dataset sizes. It is used to approximate expectations. The higher the number of samples is, the more precise the approximation.

    Returns:
        a: A solution to argmax_a {P(m >= a)^2 >= min(phi(a), 1)}
    """
    s1 = m1
    s2 = m2
    s = (s1 + s2)/2
    for i in range(n_iter):
        Pm = np.mean(M >= s)
        if Pm**2 >= phi(s):
            s1 = s
            s = (s + s2)/2
        else:
            s2 = s
            s = (s + s1)/2
        if np.floor(s1) == np.floor(s2):
            return np.floor(s)
    print("Binary SEARCH convergence not reached - s1: %f, s2: %f , f(s1): %f, f(s2): %f " % (s1, s2, np.mean(M >= s1)**2 - phi(s1), np.mean(M >= s2)**2 - phi(s2)))
    return np.floor(s)




