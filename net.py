#!/usr/bin/env python3
#
# Routing and Wavelength Assignment in All-Optical, Wavelength-Multiplexed 
# Networks with Static Traffic using Particle Swarm Optimization
#
# Coyright (2018) LabVIS - PPGCC - UFPA
# Visualization, Interaction and Intelligent Systems Lab
# Computer Science Graduate Program
# Federal University of Pará
#
# Author: Nov 2018
# Cassio Batista - cassio.batista.13@gmail.com
# Belém, Brazil

import config
import numpy as np

class Network:
	def __init__(self):
		super(Network, self).__init__()
		self.nsf_adj  = np.zeros(dtype=np.uint8,
					shape=(config.NSF_NUM_NODES, config.NSF_NUM_NODES))
		self.nsf_wave = np.zeros(dtype=np.uint8,
					shape=(config.NSF_NUM_NODES, config.NSF_NUM_NODES, config.NSF_NUM_CHANNELS))
		self.nsf_time = np.zeros(dtype=np.float64,
					shape=(config.NSF_NUM_NODES, config.NSF_NUM_NODES, config.NSF_NUM_CHANNELS))
		# define links or edges as node index pairs 
		self.nsf_links = [\
			(0,1), (0,2), (0,5),  # 0
			(1,2), (1,3),         # 1
			(2,8),                # 2
			(3,4), (3,6), (3,13), # 3
			(4,9),                # 4
			(5,6), (5,10),        # 5
			(6,7),                # 6
			(7,8),                # 7
			(8,9),                # 8
			(9,11), (9,12),       # 9
			(10,11), (10,12),     # 10
			(11,13)               # 11
		]

	def generate(self):
		for link in self.nsf_links:
			self.nsf_adj[link[0]][link[1]] = 1
			self.nsf_adj[link[1]][link[0]] = self.nsf_adj[link[0]][link[1]] 

		for i in range(0, config.NSF_NUM_NODES):
			for j in range(i+1, config.NSF_NUM_NODES):
				if self.nsf_adj[i][j]:
					for w in range(config.NSF_NUM_CHANNELS):
						self.nsf_wave[i][j][w] = np.random.choice((0,1))
						self.nsf_wave[j][i][w] = self.nsf_wave[i][j][w]

		for i in range(0, config.NSF_NUM_NODES):
			for j in range(i+1, config.NSF_NUM_NODES):
				if self.nsf_adj[i][j]:
					for w in range(config.NSF_NUM_CHANNELS):
						if self.nsf_wave[i][j][w]:
							self.nsf_time[i][j][w] = np.random.rand()
							self.nsf_time[j][i][w] = self.nsf_time[i][j][w]

		return self.nsf_wave, self.nsf_adj, self.nsf_time, self.nsf_links
