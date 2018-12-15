#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8
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

import numpy as np

class NationalScienceFoundation:
	def __init__(self, num_ch):
		super(NationalScienceFoundation, self).__init__()
		self.num_channels = num_ch
		self.num_nodes    = 14
		self.adj_mtx      = None
		self.wave_mtx     = None
		self.time_mtx     = None

		links = self.get_edges()

		# init adjacency matrix
		dimension = (self.num_nodes, self.num_nodes)
		self.__nsf_adj = np.zeros(shape=dimension, dtype=np.uint8)
		node_adjacency = 1
		for link in links:
			self.__nsf_adj[link[0]][link[1]] = node_adjacency
			self.__nsf_adj[link[1]][link[0]] = node_adjacency

		# init wavelength availability matrix
		dimension = (self.num_nodes, self.num_nodes, self.num_channels)
		self.__nsf_wave = np.zeros(shape=dimension, dtype=np.uint8)
		for link in links:
			for w in range(self.num_channels):
				wave_availability = np.random.choice((0,1))
				self.__nsf_wave[link[0]][link[1]][w] = wave_availability
				self.__nsf_wave[link[1]][link[0]][w] = wave_availability

		# init traffic matrix
		dimension = (self.num_nodes, self.num_nodes, self.num_channels)
		self.__nsf_time = np.zeros(shape=dimension, dtype=np.float64)
		for link in links:
			for w in range(self.num_channels):
				random_htime = np.random.rand()
				self.__nsf_time[link[0]][link[1]][w] = random_htime
				self.__nsf_time[link[1]][link[0]][w] = random_htime

	def reset_net(self):
		self.adj_mtx  = self.__nsf_adj.copy()
		self.wave_mtx = self.__nsf_wave.copy()
		self.time_mtx = self.__nsf_time.copy()

	def get_num_nodes(self):
		return self.num_nodes

	def get_num_channels(self):
		return self.num_channels

	# define links or edges as node index pairs 
	def get_edges(self):
		return [\
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
