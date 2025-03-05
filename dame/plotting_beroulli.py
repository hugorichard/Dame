import numpy as np
import matplotlib.pyplot as plt




rc = {
    "pdf.fonttype": 42,
    "text.usetex": True,
    "font.size": 16,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16,
    "text.usetex": True,
    "font.family": "serif",
}
plt.rcParams.update(rc)

rhos = np.linspace(0, 1, 10)
duchi = np.load("duchi_bernoulli.npy")
kent = np.load("kent_bernoulli.npy")
dame = np.load("dame_bernoulli.npy")
print(duchi.shape)
plt.figure(figsize=(6, 2), frameon=False)
plt.xlabel(r"$\rho$")
plt.ylabel("Risk")
plt.plot(rhos, np.median(duchi**2, axis=1), label="(Duchi, 2018)", color="blue")
plt.fill_between(rhos, np.quantile(duchi**2, 0.1, axis=1), np.quantile(duchi**2, 0.9, axis=1), color="blue", alpha=0.2)
plt.plot(rhos, np.median(kent**2, axis=1), label="(Kent, 2024)", color="orange")
plt.fill_between(rhos, np.quantile(kent**2, 0.1, axis=1), np.quantile(kent**2, 0.9, axis=1), color="orange", alpha=0.2)
plt.plot(rhos, np.median(dame**2, axis=1), label="DAME (this paper)", color="green")
plt.fill_between(rhos, np.quantile(dame**2, 0.1, axis=1), np.quantile(dame**2, 0.9, axis=1), color="green", alpha=0.2)
plt.legend(loc="upper center", ncol=2, bbox_to_anchor=(0.45, 1.6))
plt.yscale("log")
plt.savefig("fig_bernoulli.pdf", bbox_inches="tight")

