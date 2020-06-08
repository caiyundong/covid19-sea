import scipy.integrate as spi
import numpy as np
import matplotlib
import platform
if platform.system() == 'Darwin':
    matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt

N = 10000                   # N为人群总数
beta = 0.9                  # β为传染率系数
gamma = 0.1                 # gamma为恢复率系数
Te = 14                     # Te为疾病潜伏期
I_0 = 1                     # I_0为感染者的初始人数
E_0 = 0                     # E_0为潜伏者的初始人数
R_0 = 0                     # R_0为治愈者的初始人数
S_0 = N - I_0 - E_0 - R_0   # S_0为易感者的初始人数
T = 150                     # T为传播时间

# INI为初始状态下的数组
INI = (S_0, E_0, I_0, R_0)


def funcSEIR(inivalue, _):
    Y = np.zeros(4)
    X = inivalue
    # 易感个体变化
    Y[0] = - (beta * X[0] * X[2]) / N
    # 潜伏个体变化
    Y[1] = (beta * X[0] * X[2]) / N - X[1] / Te
    # 感染个体变化
    Y[2] = X[1] / Te - gamma * X[2]
    # 治愈个体变化
    Y[3] = gamma * X[2]
    return Y

T_range = np.arange(0, T + 1)

RES = spi.odeint(funcSEIR, INI, T_range)

plt.plot(RES[:, 0], color='darkblue', label='Susceptible', marker='.')
plt.plot(RES[:, 1], color='orange', label='Exposed', marker='.')
plt.plot(RES[:, 2], color='red', label='Infection', marker='.')
plt.plot(RES[:, 3], color='green', label='Recovery', marker='.')

plt.title('SEIR Model')
plt.legend()
plt.xlabel('Day')
plt.ylabel('Number')
plt.show()
