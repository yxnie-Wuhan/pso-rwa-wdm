import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

import numpy as np

DEGUB = False

FUNC = '$c = \left(\\alpha_0 * \\frac{1}{\lambda+\\alpha_1}\\right) + ' +\
			'\left(\\alpha_2 * hops\\right) + ' +\
			'\left(\\alpha_3 * \min{\lambda} index\\right)$'


hop = [1, 2, 3, 4, 5, 6]
ava = [0, 1, 2, 3, 4, 5]
fir = [0, 1, 2, 3, 4, 5]

alpha = [4.0, 0.5, 1.0, 0.0375]

colors  = ['r', 'g', 'b', 'k', 'm', 'y']
markers = ['o', 's', '^', '<', 'v', '>']
lnstyle = ['-', '--', '-', '--', '--', '--']
mksize  = [ 8,  12,   8,   12,   6,  2 ]
mkfccol = ['r', 'none', 'b', 'none', 'c', 'none', 'y']
offset  = 0.125

custom_lines = [ \
	Line2D([0], [0], color='r', lw=2),
	Line2D([0], [0], color='g', lw=2),
	Line2D([0], [0], color='b', lw=2),
	Line2D([0], [0], color='k', lw=2),
	Line2D([0], [0], color='m', lw=2),
	Line2D([0], [0], color='y', lw=2),
]
custom_markers = [ \
	Line2D([0], [0], color='k', lw=1, marker='s', markersize=6),
	Line2D([0], [0], color='k', lw=1, marker='^', markersize=6),
	Line2D([0], [0], color='k', lw=1, marker='<', markersize=6),
	Line2D([0], [0], color='k', lw=1, marker='v', markersize=6),
	Line2D([0], [0], color='k', lw=1, marker='>', markersize=6),
]

print('(h a f) = c')
myarr = np.empty(shape=(len(hop),len(ava)), dtype=object)
for h in hop:
	for a in ava:
		myarr[hop.index(h)][ava.index(a)] = []
		for f in fir:
			c = alpha[0]*( 1 / (a+alpha[1]) ) + alpha[2]*h + alpha[3]*f
			myarr[hop.index(h)][ava.index(a)].append(c)
			if DEGUB:
				if not a and f:
					print('--------------', end='\t')
				else:
					print('(%d %d %d) = %.2f' % (h, a, f, c), end='\t')
		if DEGUB:
			print()
	if DEGUB:
		print()

# -------------------------------------------------------------------
# define first plot parameters
x = np.arange(6, dtype=np.float16)
p = plt.subplot(121)
#p.tick_params(
#	axis='x',          # changes apply to the x-axis
#	which='both',      # both major and minor ticks are affected
#	bottom=False,      # ticks along the bottom edge are off
#	top=False,         # ticks along the top edge are off
#	right=True,         # ticks along the top edge are off
#	left=True,         # ticks along the top edge are off
#	labelbottom=False) # labels along the bottom edge are off

# plot first plot
eita = []
for i in range(len(hop)):
	for j in range(1,len(ava)):
		p.stem(x, myarr[i][j], colors[i], linefmt=colors[i]+'-', markerfmt=markers[j]+colors[i])
		eita.append(Line2D([0], [0], color=colors[i], lw=1, marker=markers[j], markersize=6))
	x += offset
p.grid()
p.xaxis.grid(False)
p.set_yticks(np.arange(1.6, 9.2, 0.2))
p.set_ylim([1.6, 9.0])
p.set_ylabel(FUNC, fontsize=14)
p.set_xlabel('Minimum free-wavelength ($\lambda$) index', fontsize=14)
p.set_xticks(np.arange(0,6,1)+2*offset+offset/2)
p.set_xticklabels(['$\lambda=%d$' % w for w in range(6)])

p.legend(eita,
			['%d hops, %d $\lambda$ free' % (h,w) for h in range(1,7) for w in range(1,6)],
			loc=3, bbox_to_anchor=(0.975,0.10))

#l1 = p.legend(custom_lines, 
#			['%s hops' % h for h in ['one','two','three','four','five','six']],
#			loc=3, bbox_to_anchor=(1.015,0.75))
#p.legend(custom_markers, 
#			['%s $\lambda$ free' % w for w in ['one','two','three','four','five']],
#			loc=3, bbox_to_anchor=(1.009,0.54))
#plt.gca().add_artist(l1)

# ---------------------------------------------------------------------------
plt.subplots_adjust(left = 0.06, right = 0.975, bottom = 0.05, top = 0.95)

x = np.arange(6, dtype=np.float16)
q = plt.subplot(122)
for i in range(len(hop)):
	for j in range(1,len(ava)):
		q.plot(myarr[i][j], color=colors[i], linestyle='-', linewidth=0.8, 
					marker=markers[j], markersize=5, markerfacecolor=colors[i])
	x += offset
q.grid()
#q.xaxis.grid(False)
q.set_yticks(np.arange(1.6, 9.2, 0.2))
q.set_yticklabels('')
q.set_ylim([1.6, 9.0])
q.set_xlabel('Minimum free-wavelength ($\lambda$) index', fontsize=14)
#q.set_xticks(np.arange(0,6,1)+2*offset+offset/2)
q.set_xticks(np.arange(6))
q.set_xticklabels(['$\lambda=%d$' % w for w in range(6)])

#l2 = q.legend(custom_lines, ['%d hops' % h for h in range(1,7)],
#			loc=2, bbox_to_anchor=(0.01,0.96))
#q.legend(custom_markers, ['%d $\lambda$ free' % w for w in range(1,6)],
#			loc=1, bbox_to_anchor=(0.25,0.96))
plt.subplots_adjust(left = 0.06, right = 0.975, bottom = 0.08, top = 0.95)
#plt.gca().add_artist(l2)

plt.show()
