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

class ParticleSwarmOptimization:
	def __init__(self, size_sw, c1, c2, c3, alpha_vec, cvg_iter):
		super(ParticleSwarmOptimization, self).__init__()
		self.size_swarm = size_sw
		self.c          = (c1, c2, c3)
		self.a          = alpha_vec
		self.convg_iters = cvg_iter

		# init object to class swarm
		self.swarm = Swarm()

	def evaluate(self, p):
		c = self.a[0] * ( 1 / (p.get_num_wavs_free()+self.a[1]) ) + \
			self.a[2] * p.get_num_hops() + \
			self.a[3] * p.get_min_free_wav_index()
		return c

	def run(self, net, htime, unext):
		# init swarm
		self.swarm.create()

		# evaluate particles & update pbest
		for particle in self.swarm.get_swarm():
			fit = self.evaluate(particle)
			particle.update_fitvalue(fit)
			particle.update_lbest(particle) # at first each part is its own lbest

		# sort swarm according to fitness 
		self.swarm.sort()

		# update swarm's gbest
		self.swarm.update_gbest(self.swarm.get_swarm[0])

		# update local information
		# TODO

		# update global information
		# TODO

		iters = 0
		while iters < self.convg_iters:
			pass
### EOF ###
