#!/home/deepak/anaconda3/bin/python3.7

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
        
    return retVal.decode('utf-8')[:-2]

#IPVal = getHostIP().decode('utf-8')
#print(IPVal)
    
def getStoredIP():
    f = open(cfg.dataFile,'r')
    line = f.readline()
    #line = line[:-1]
    #print(line)
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

def updateDataFile(content):
    f = open('./data','w+')
    f.write(content)    
    f.close()

def checkValidity(currIP,storedIP):
    
    send=True
    dontSend=False
    
    if currIP == " ":
        updateDataFile(cfg.IPMISSINGKW)
        return currIP,dontSend
    
    else:
        if storedIP == cfg.IPMISSINGKW:
            updateDataFile(currIP)
            return currIP,send
        
        if storedIP == currIP:
            return currIP,dontSend
        
        if storedIP != currIP:
            updateDataFile(currIP)
            return currIP,send

        
def sender():
    currIPVal = getHostIP()
    storedIPVal= getStoredIP()
    IPVal,isValid = checkValidity(currIPVal,storedIPVal)
    
    if isValid:
        hostnameVal = subprocess.check_output(['hostname'])
        hostnameVal = hostnameVal.decode("utf-8")
        #prepare and send the mail
        destEmail = getDestinationAddress()
        
        emailContent = 'The current IP of '+hostnameVal+' is '+IPVal
        
        emailObj = {}
        emailObj['destEmail']=destEmail
        emailObj['emailContent']=emailContent
        
        sendEmail(emailObj)
    
def createEmailFile(emailObj):
    f = open('./mailData.txt','w')
    f.write(emailObj['emailContent'])    
    f.close()
 
def sendEmail(emailObj):
    createEmailFile(emailObj)
    #subprocess.call(['ssmtp',emailObj['destEmail'],'<','mailData.txt'])
    os.system('ssmtp '+emailObj['destEmail']+' < ./mailData.txt')
    
sender()

    