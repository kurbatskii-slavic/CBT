import numpy as np

def solve(a, b, c, f):
    n = len(b)
    x = np.zeros(n)
    alpha = np.zeros(n)
    beta = np.zeros(n)

    alpha[0] = -c[0] / b[0]
    beta[0] = f[0] / b[0]

    for i in range(1, n - 1):
        denominator = b[i] + a[i - 1] * alpha[i - 1]
        alpha[i] = -c[i] / denominator
        beta[i] = (f[i] - a[i - 1] * beta[i - 1]) / denominator

    x[-1] = (f[-1] - a[-1] * beta[-2]) / (b[-1] + a[-1] * alpha[-2])

    for i in range(n - 2, -1, -1):
        x[i] = alpha[i] * x[i + 1] + beta[i]
    return np.array(x)

def u_(x):
    return np.sin(5 * x) + np.cos(3 * x)

def f_(x):
    return 25 * np.sin(5 * x) + 9 * np.cos(3 * x)
