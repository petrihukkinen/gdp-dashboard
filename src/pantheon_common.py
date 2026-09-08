"""Shared Pantheon+ loader and profiled-chi2 likelihood (identical to the one used in src/pantheon_fit.py)."""
import math, numpy as np, pandas as pd
from scipy import integrate

def load(zmin=0.01):
    dat = pd.read_csv("sources/Pantheon+SH0ES.dat", sep=r"\s+")
    N = len(dat); assert N == 1701
    cov_raw = np.loadtxt("sources/Pantheon+SH0ES_STAT+SYS.cov"); assert int(cov_raw[0]) == N
    C = cov_raw[1:].reshape(N, N); C = 0.5*(C + C.T)
    sel = dat["zHD"].values > zmin
    return dict(z=dat["zHD"].values[sel], zhel=dat["zHEL"].values[sel], m=dat["m_b_corr"].values[sel],
                C=C[np.ix_(sel, sel)], Cinv=np.linalg.inv(C[np.ix_(sel, sel)]), N=int(sel.sum()))

def chi2_profiled(D, mu_shape, idx=None):
    """chi2 minimised analytically over the additive constant (M + 5log10(c/H0/10pc)). Optional index subset."""
    if idx is None:
        m, Cinv = D["m"], D["Cinv"]
    else:
        m = D["m"][idx]; Cinv = np.linalg.inv(D["C"][np.ix_(idx, idx)]); mu_shape = mu_shape[idx]
    one = np.ones_like(m); r = m - mu_shape
    oCr = one @ Cinv @ r; oCo = one @ Cinv @ one
    return r @ Cinv @ r - oCr**2/oCo, oCr/oCo

def dc_flat(zz, Om):
    E = lambda x: 1/math.sqrt(Om*(1+x)**3 + (1-Om))
    return np.array([integrate.quad(E, 0, zi, epsabs=1e-10)[0] for zi in zz])

def mu_lcdm(D, Om):  return 5*np.log10((1+D["zhel"])*dc_flat(D["z"], Om))
def mu_du_p(D, p):    # D_L = R4 * z * (1+z)^p   (p = exponent of (1+z) in the DISTANCE; p = q_mine/2)
    return 5*np.log10(D["z"]) + 5*p*np.log10(1+D["zhel"])
