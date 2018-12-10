#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8
#
# GA: RWA with GOF
# Genetic Algorithm  
# Routing and Wavelength Assignment
# General Objective Function
#
# Copyright 2017
# Programa de Pós-Graduação em Ciência da Computação (PPGCC)
# Universidade Federal do Pará (UFPA)
#
# Author: April 2016
# Cassio Trindade Batista - cassio.batista.13@gmail.com

# Debug Parameters
DEGUB = False

##########
# Simulation Parameters
##########
SIM_NUM_GEN = 150

SIM_MIN_LOAD = 1
SIM_MAX_LOAD = 31

##########
# Network Parameters
##########
NSF_SOURCE_NODE   = 0      # source
NSF_DEST_NODE     = 12     # destination node
NSF_NUM_NODES     = 14     # number of nodes on NSF network
NSF_NUM_CHANNELS  = 4      # total number of wavelengths available
NSF_CHANNEL_FREE  = False  # init all link wavelengths available at once?

##########
# Particle Sawrm Optimization Parameters
##########
PSO_SIZE_SWARM     = 30    # size of the swarm

PSO_INIT_C1        = 2.0   # individual
PSO_INIT_C2        = 2.0   # social
PSO_INIT_W         = 1.0   # inertia factor

PSO_MIN_GEN        = 25    # min number of generations
PSO_MAX_GEN        = 80    # max number of generations

### EOF ###
