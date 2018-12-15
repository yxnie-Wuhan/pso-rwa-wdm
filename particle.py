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
		self.__components = None
		self.__fit        = None
		self.__p_best     = None
		self.__g_best     = None

	def make(self):
		count = 0
		# 1. start from source node
		current_router = start_router
		chromosome = [allels.pop(allels.index(current_router))]
		while len(allels):
			# 2. randomly choose, with equal probability, one of the nodes that
			# is SURELY connected to the current node to be the next in path
			next_router = random.choice(allels)

			# SURELY: check whether there is an edge/link/connection or not
			if nsfnet[current_router][next_router] > 0.0: 
				# 3. if the chosen node hasn't been visited before, mark it as the
				# next in the path (gene). Otherwise find another node
				current_router = next_router
				chromosome.append(allels.pop(allels.index(current_router)))

				# 6. do this until the destination node is found
				if current_router == end_router:
					break

				count = 0
			else:
				# max trials to find a valid path: average of 100 chances per gene
				count += 1
				if count > 100:
					chromosome = False
					break

		if chromosome and len(chromosome) > info.NSF_NUM_NODES:
			chromosome = False

		return chromosome

	def get_fit(self):
		return self.fit

	def get_components(self):
		return self.components
