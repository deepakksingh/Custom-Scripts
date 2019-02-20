#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 23:05:16 2019

@author: deepak
"""
import subprocess
import ipResponderConfiguration as cfg


def getHostIP():
    retVal = subprocess.check_output(['hostname','-I'])
    return retVal

#IPVal = getHostIP().decode('utf-8')
#print(IPVal)
    
def getStoredIP():
    f = open(cfg.dataFile,'r')
    line = f.readline()
    print(line)
    f.close()
    
    return line
    
#getStoredIP()
    
def runnerFunc():
    storedIPVal = getStoredIP()
    currIPVal = getHostIP()
    
    if currIPVal != storedIPVal:
        pass
        