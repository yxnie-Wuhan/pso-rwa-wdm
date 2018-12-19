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

# Debug Parameters
DEGUB = True

##########
# Simulation Parameters
##########
SIM_NUM_CALLS = 150

SIM_MIN_LOAD = 1
SIM_MAX_LOAD = 31

##########
# Network Parameters
##########
NSF_SOURCE_NODE   = 0      # source
NSF_DEST_NODE     = 12     # destination node
NSF_NUM_CHANNELS  = 4      # total number of wavelengths available

##########
# Particle Sawrm Optimization Parameters
##########
PSO_SIZE_SWARM     = 30    # size of the swarm

PSO_INIT_C1        = 2.0   # individual (pbest, self)
PSO_INIT_C2        = 2.0   # local      (lbest, social neighbourhood)
PSO_INIT_C3        = 2.0   # social     (gbest, global)
PSO_INIT_W         = 1.0   # inertia factor

PSO_ALPHA          = [4.0, 0.5, 1.0, 0.0375] # fitness function parameters

PSO_ITERS_TO_CONV   = 500   # min number of generations

### EOF ###
