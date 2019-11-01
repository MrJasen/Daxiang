import matplotlib.pyplot as plt
ax=[]
ay=[]
plt.ion()
for i in range(100):
    ax.append(i)
    ay.append(i**2)
    plt.clf()
    plt.plot(ax,ay)
    plt.pause(0.1)
    plt.ioff()
