#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 23:05:16 2019

@author: deepak
"""
import subprocess
import os
import ipResponderConfiguration as cfg


def getHostIP():
    retVal = subprocess.check_output(['hostname','-I'])
    if(retVal == ' '):
        retVal = cfg.HOSTNOTCONNECTED
        
    return retVal.decode('utf-8')

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

def getDestinationAddress():
    return cfg.DESTINATION_EMAIL
        
def sender():
    currIPVal = getHostIP()
    hostnameVal = subprocess.check_output(['hostname'])
    hostnameVal = hostnameVal.decode("utf-8")
    #prepare and send the mail
    destEmail = getDestinationAddress()
    
    emailContent = 'The current IP of '+hostnameVal+' is '+currIPVal
    
    emailObj = {}
    emailObj['destEmail']=destEmail
    emailObj['emailContent']=emailContent
    
    sendEmail(emailObj)
    
def createFile(emailObj):
    f = open('./mailData.txt','w')
    f.write(emailObj['emailContent'])    
    f.close()
 
def sendEmail(emailObj):
    
    createFile(emailObj)
    #subprocess.call(['ssmtp',emailObj['destEmail'],'<','mailData.txt'])
    os.system('ssmtp '+emailObj['destEmail']+' < ./mailData.txt')
    
#sender()

    