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

from particle import Particle

class Swarm:
	def __init__(self, size_sw=0):
		super(Swarm, self).__init__()
		self.__swarm      = []
		self.__size_swarm = size_sw

	def create(self):
		if self.get_size_swarm() > 0:
			for i in range(self.get_size_swarm()):
				particle = Particle()
				self.add_particle(particle)

	def add_particle(self, part):
		self.__swarm.append(part)
		self.update_size_swarm(+1)

	def place_particle_at(self, part, pos):
		self.__swarm[pos] = part

	def rm_worst_particle(self):
		self.__swarm.pop(-1)
		self.update_size_swarm(-1)

	def update_size_swarm(self, num_parts):
		self.__size_swarm += num_parts

	def sort(self):
		self.__swarm.sort(key=lambda x:x.get_fit(), reverse=False)

	def get_swarm(self):
		return self.__swarm

	def get_size_swarm(self):
		return self.__size_swarm

	def get_particle(self, position):
		return self.get_swarm()[position]

	def get_fittest_particle(self):
		return self.get_population()[0]

	def get_bestfit(self):
		return self.get_fittest().get_fit()

### EOF ###
