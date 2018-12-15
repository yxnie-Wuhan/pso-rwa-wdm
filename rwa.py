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
np.set_printoptions(precision=2)

from termcolor import colored

import config
from net import NationalScienceFoundation
from pso import ParticleSwarmOptimization

class RoutingAndWavelengthAssignment:
	def __init__(self):
		super(RoutingAndWavelengthAssignment, self).__init__()

	def run():
		# init networks
		self.nsf = NationalScienceFoundation(config.NSF_NUM_CHANNELS)
		self.nsf.reset_net()

		blocked = []

		if config.DEGUB:
			for w in range(self.nsf.get_num_channels()):
				for i in range(self.nsf.get_num_nodes()):
					for j in range(self.nsf.get_num_nodes()):
						if self.nsf.wave_mtx[i][j][w]:
							print(colored('N%0.2f' % N[i][j][w], 
										'green', attrs=['reverse']), end=' ')
						else:
							print('N%0.2f' % self.nsf.wave_mtx[i][j][w], end=' ')
					print(end='\t')
					for j in range(self.nsf.get_num_nodes()):
						if self.nsf.time_mtx[i][j][w]:
							print(colored('T%0.2f' % self.nsf.time_mtx[i][j][w], 
										'green', attrs=['reverse']), end=' ')
						else:
							print('T%0.2f' % self.nsf.time_mtx[i][j][w], end=' ')
					print()
				print()

		# init PSO
		self.pso = ParticleSwarmOptimization()

		# increment load 
		for load in range(config.SIM_MIN_LOAD, config.SIM_MIN_LOAD):
			# reset networks
			self.nsf.reset_net()

			# Poisson call arrival
			for call in range(config.SIM_NUM_CALLS):
				until_next   = -np.log(1-np.random.rand())/load
				holding_time = -np.log(1-np.random.rand())

				# TODO apply PSO 
				block_count = pso.run(until_next, holding_time)

				# update networks' traffic matrix
				for link in self.nsf.get_edges():
					i, j = link
					for w in xrange(self.nsf.get_num_channels()):
						if  self.nsf.time_mtx[i][j][w]  > until_next:
							self.nsf.time_mtx[i][j][w] -= until_next
							self.nsf.time_mtx[j][i][w] -= until_next
						else:
							self.time_mtx[i][j][w] = 0
							self.time_mtx[j][i][w] = 0
							if not self.nsf.wave_mtx[i][j][w]:
								self.nsf.wave_mtx[i][j][w] = 1 # free channel
								self.nsf.wave_mtx[j][i][w] = 1

			# save BP per load
			block_count *= 100.0
			blocked.append(float('%.3f' % (block_count/config.SIM_NUM_CALLS)))

		# save BP to file
		with open('block.txt', 'a') as f:
			f.write(blocked)

		# plot

if __name__=='__main__':
	rwa = RoutingAndWavelengthAssignment()
	rwa.run()
### EOF ###
