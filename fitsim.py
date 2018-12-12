import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

FACTOR = 14 / 8

hop = [1, 2, 3, 4, 5, 6]
ava = [0, 1, 2, 3, 4, 5]
fir = [0, 1, 2, 3, 4, 5]

alpha = [4.0, 0.5, 1.0, 0.0375]

print('(h a f) = c')
myarr = np.empty(shape=(len(hop),len(ava)), dtype=object)
x = []
for h in hop:
	for a in ava:
		myarr[hop.index(h)][ava.index(a)] = []
		for f in fir:
			c = alpha[0]*( 1 / (a+alpha[1]) ) + alpha[2]*h + alpha[3]*f
			myarr[hop.index(h)][ava.index(a)].append(c)
			x.append(c)
			if not a and f:
				print('--------------', end='\t')
			else:
				print('(%d %d %d) = %.2f' % (h, a, f, c), end='\t')
		print()
	print()

plotes  = []
colors  = ['r', 'g', 'b', 'k', 'c', 'y']
markers = ['o', 's', '^', 'o', 'v', 'h']
lnstyle = ['-', '--', '-', '--', '--', '--']
mksize  = [ 8,  12,   8,   12,   6,  2 ]
mkfccol = ['r', 'none', 'b', 'none', 'c', 'none', 'y']
p = plt.subplot(111)
for i in range(len(hop)-1):
	for j in range(1,len(ava)):
		p.plot(myarr[i][j], color=colors[i], linestyle=lnstyle[i],
					marker=markers[i], markersize=mksize[i], markerfacecolor=mkfccol[i])
p.grid()
#p.set_yticks(np.arange(0,6,0.3))
#p.set_ylim([0,1.5])
plt.show()
