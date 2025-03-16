from laplace import *
import matplotlib.pyplot as plt

N = 2
y = [4, 10, 20, 50, 100, 250, 500, 1000, 5000]
L2_error = np.zeros(len(y))
C_error = np.zeros(len(y))
j = 0
for N in y:
    h = 1 / N
    a = np.full(N - 2, -1)
    b = np.full(N - 1, 2)
    c = np.full(N - 2, -1)

    x = np.linspace(0, 1, N + 1)
    f = np.array([f_(x[i]) for i in range(1, N)]) * h**2

    u0, uN = u_(0), u_(1)
    f[0] += u0
    f[-1] += uN

    u = np.array([u_(x[i]) for i in range(1, N)])
    solution = solve(a, b, c, f)
    error = np.abs(solution - u)
    L2_error[j] = np.linalg.norm(error)
    C_error[j] = np.max(error)
    j += 1

plt.figure(figsize=(12, 6))
plt.plot(y, L2_error, marker='o', color='forestgreen', label='L2-norm')
plt.plot(y, C_error, marker='o', color='y', label='Max-norm')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('error')
plt.grid(True)
plt.show()
