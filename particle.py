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

class Particle:
	def __init__(self):
		super(Particle, self).__init__()
		# init pso parameters
		self.__route          = None         # genes-like
		self.__fitness        = float('nan') # fitness
		self.__p_best         = None         # 
		self.__g_best         = None         # 

		self.__num_waves_free = float('nan')
		self.__num_hops       = float('nan')

	def create(self, s_node, d_node, allels):
		count = 0
		# 1. start from source node
		current_router = s_node
		particle = [allels.pop(allels.index(current_router))]
		while len(allels):
			# 2. randomly choose, with equal probability, one of the nodes that
			# is SURELY connected to the current node to be the next in path
			next_router = random.choice(allels)

			# SURELY: check whether there is an edge/link/connection or not
			if nsfnet[current_router][next_router] > 0.0: 
				# 3. if the chosen node hasn't been visited before, mark it as the
				# next in the path (gene). Otherwise find another node
				current_router = next_router
				particle.append(allels.pop(allels.index(current_router)))

				# 6. do this until the destination node is found
				if current_router == d_node:
					break

				count = 0
			else:
				# max trials to find a valid path: average of 100 chances per gene
				count += 1
				if count > 100:
					particle = False
					break

		if particle and len(particle) > self.__net.get_num_nodes():
			particle = False

		return particle

	def update_fitvalue(self, value):
		self.__fitness = value

	def get_fit(self):
		return self.__fit

	def get_components(self):
		return self.__route

	def get_num_wavs_free(self):
		return self.__num_waves_free

	def get_num_hops(self):
		return self.__num_hops

	def get_min_free_wav_index(self)
		for w in self.__net.get_num_channels():
			for i in range(self.get_num_hops()-1):
				curr_node = self.get_components()[i]
				next_node = self.get_components()[i+1]
				if self.__net.wave_mtx[curr_node][next_node][w]
					min_idx = w
				else:
					min_idx = float('inf') # FIXME
					break
			if min_idx < float('inf'):
				break
		return min_idx
