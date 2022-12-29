import discord
import numpy as np
import pandas as pd
import string
import numexpr as ne
from sympy import Derivative, Symbol, symbols
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext import commands, tasks
import datetime
import itertools
from datetime import datetime, timezone, date
import matplotlib.pyplot as plt
from matplotlib import colors
from plotly.offline import plot
from matplotlib.ticker import PercentFormatter
import os
import requests
import schedule
import asyncio
import time
import random
import queue
from urllib.request import Request, urlopen
import sched
from bs4 import BeautifulSoup
import numexpr as ne

from urllib.request import Request, urlopen
from urllib.error import HTTPError ####
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from PIL import Image
import seaborn as sns
import math
import matplotlib as faggot

from threading import Thread

# alarm_time = '22:24'#24hrs
# channel_id = '400673288768192524' #modchat
Test = 50


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '☆', Intents = intents)
Bot = discord.Client(intents=intents)
dick = 0

async def create_thread(self,name,minutes,message):
    token = 'Bot ' + self._state.http.token
    url = f"https://discord.com/api/v9/channels/{self.id}/messages/{message.id}/threads"
    headers = {
        "authorization" : token,
        "content-type" : "application/json"
    }
    data = {
        "name" : name,
        "type" : 11,
        "auto_archive_duration" : minutes
    }

    return requests.post(url,headers=headers,json=data).json()

discord.TextChannel.create_thread = create_thread

def Titles(S):
    list1 = [x.a['title'] for x in S.find_all('div', {'class':"mw-search-result-heading"})] #names
    list2 = [x.a['href'] for x in S.find_all('div', {'class':"mw-search-result-heading"})] #links
    stringo = ""
    for i in range(len(list1)):
        stringo += f"[{i}]."+ list1[i] + '\n '
    # print(list1)
    return [stringo, list2]

shock = ["will is so hard", "will is so sexy"]
NUG = ['nugget', 'Nugget', 'NUGGET', 'nuget', 'Nuget']
nono = ['221533934314455041', '704334452398096534']
n = []
UHM = ['umm', 'uhm', 'umwhat']
dick = -0.1
# @client.event
# async def on_member_update(before, after):
#
#     print("print before get_channel()")
#     channel = client.get_channel(83566743976411136)
#     print("hewwo")
#
#     #print("hewwo")
#     channel.send("hi!")
#     if before.game != after.game:
#         print("O:::::::")
#         await channel.send("o:")
def unique(list):
    newlist=[]
    for i in list:
        if i in newlist:
            pass
        else:
            newlist.append(i)
    return newlist







def aroll(massDist):
    randRoll = random.random() # in [0,1]
    summ = 0
    result = True
    for mass in massDist:
        summ += mass
        if randRoll < summ:
            return result
        else:
            return False













def pitychaintilldeath(lastroll, faith, *args): #with pity system - 2 fails in a row leads to one auto success | NEW:lastroll is option to retain information from previous roll to start from where you ended off from previous attempt!!!!
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        summ = 0
        result = True
        for mass in massDist:
            summ += mass
            if randRoll < summ:
                return result
            else:
                return False
    level=1
    string = ' '
    RETARDED = []
    for i in args:
        if '*' in str(i):
            RETARDED.append(float(i[:-1]))
        else:
            RETARDED.append(float(i))
    print(len(RETARDED))
    #print(RETARDED)
    #print(RETARDED[level])
    #print(1-RETARDED[level])
    count = 1
    bottom = 0
    #Lets try to establish which arguments are critical points at which falling below is not possible - for now I think it is reasonable to expect that the critical points
    #behave exactly like the first level that we provide
    #First - let's try to extract and 'look for' critical points denoted by * after the probability values
    criticalno = []
    for i in range(len(args)):
        if '*' in str(args[i]):
            criticalno.append(i+1)   
    failedatcheckpoint = False  #To record if failure at checkpoint occurred in last roll - because if you fail once alr at a checkpoint, you CANNOT be given pity rank up if you fail at it again            
    while count < int(faith)+1 and level+lastroll<len(args)+1:
        print(level-1+lastroll)
        sampleMassDist = (RETARDED[level-1+lastroll],1-RETARDED[level-1+lastroll])
        t = roll(sampleMassDist)
        count+=1
        string+=str(t)+' '
        if t:
            level+=1
            failedatcheckpoint = False
        elif string.split(' ')[-1] == 'False' and failedatcheckpoint == False:
            level-=0 #just to indicate that you failed AND succeeded because of pity rank up right after at 100%
            string+='True '
            count+=1
            failedatcheckpoint = False
        elif len(criticalno) > 0:
            for i in criticalno:
                if level + lastroll == i:  #If you are at one of the critical points, you will not fail.
                    failedatcheckpoint = True
                    bottom += 1
        elif level+lastroll>1:  #Catch all term for dropping a level if no check point was triggered in previous if statement
            level-=1
            failedatcheckpoint = False
        else:
            bottom+=1
            failedatcheckpoint = True
    return [string, bottom]







def pitychaintilldeath0(lastroll, faith, *args): #with pity system - 2 fails in a row leads to one auto success | NEW:lastroll is option to retain information from previous roll to start from where you ended off from previous attempt!!!! 100% false dependent.
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        summ = 0
        result = True
        for mass in massDist:
            summ += mass
            if randRoll < summ:
                return result
            else:
                return False
    def countFalses(stringie):
        cunt = 0
        for i in stringie.split(' '):
            if i == 'False':cunt+=1
            else:pass
        return cunt
    level=1
    string = ' '
    #RETARDED = [float(x) for x in args]
    RETARDED = []
    for i in args:
        if '*' in str(i):
            RETARDED.append(float(i[:-1]))
        else:
            RETARDED.append(float(i))
    print(len(RETARDED))
    #print(RETARDED)
    #print(RETARDED[level])
    #print(1-RETARDED[level])
    count = 1
    bottom =0 #Number of times failed at bottom
    #Lets try to establish which arguments are critical points at which falling below is not possible - for now I think it is reasonable to expect that the critical points
    #behave exactly like the first level that we provide
    #First - let's try to extract and 'look for' critical points denoted by * after the probability values
    criticalno = []
    for i in range(len(args)):
        if '*' in str(args[i]):
            criticalno.append(i+1)     
    failedatcheckpoint = False  #To record if failure at checkpoint occurred in last roll - because if you fail once alr at a checkpoint, you CANNOT be given pity rank up if you fail at it again            
    while countFalses(string) < int(faith) and level+lastroll<len(args)+1:
        sampleMassDist = (RETARDED[level-1+lastroll],1-RETARDED[level-1+lastroll])
        t = roll(sampleMassDist)
        count+=1
        string+=str(t)+' '           
        if t:
            level+=1
            failedatcheckpoint = False
        elif string.split(' ')[-1] == 'False' and failedatcheckpoint == False:
            level-=0
            string+='True '
            count+=1
            failedatcheckpoint = False
        elif len(criticalno) > 0:
            for i in criticalno:
                if level + lastroll == i:  #If you are at one of the critical points, you will not fail.
                    failedatcheckpoint = True
                    bottom += 1            
        elif level+lastroll>1:
            level-=1
            failedatcheckpoint = False
        else:
            bottom+=1
            failedatcheckpoint = True
    return [string, bottom]





#Simple "AI". If softcap of successes is not reached and total count is alr reached, carry on for a small fail target. - A more conservative tapping higher failure aversive rolling session. You are aiming for a 
#More complex "AI". If last 3 taps were not FFT (pity) + last tap was T, then try a few more taps 

def hybridchain1(lastroll, softcap, faith, push,*args):  #So this is the simple version
#Hence, faith here is going to be the total number of taps cap BUT, it will decide to override it based off of softcap
#How much we push past despite reaching count cap is determined by input variable 'push'. 'push is the new number of failures we are willing to accept.
    push = int(push)
    softcap = int(softcap) #Low end number of failures you are willing to accept
    faith = int(faith) #This is going to be total number of taps you are 'generally' willing to accept
    softcap = min(softcap,len(args))
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        summ = 0
        result = True
        for mass in massDist:
            summ += mass
            if randRoll < summ:
                return result
            else:
                return False
    def countFalses(stringie):
        cunt = 0
        for i in stringie.split(' '):
            if i == 'False':cunt+=1
            else:pass
        return cunt
    level=1
    string = ' '
    # RETARDED = [float(x.translate) for x in args]
    RETARDED = []
    for i in args:
        if '*' in str(i):
            RETARDED.append(float(i[:-1]))
        else:
            RETARDED.append(float(i))
    print(len(RETARDED))
    #print(RETARDED)
    #print(RETARDED[level])
    #print(1-RETARDED[level])
    count = 1
    pushcount = 0
    bottom =0 #Number of times failed at bottom
    pityT = 0
    criticalno = []
    for i in range(len(args)):
        if '*' in str(args[i]):
            criticalno.append(i+1)     
    failedatcheckpoint = False  #To record if failure at checkpoint occurred in last roll - because if you fail once alr at a checkpoint, you CANNOT be given pity rank up if you fail at it again       
    while level+lastroll<len(args)+1: #The only condition when we break... when we reach our goal. This endpoint is always absolute. We are going to add break functions to stop this from "infiniting"
        sampleMassDist = (RETARDED[level-1+lastroll],1-RETARDED[level-1+lastroll])
        t = roll(sampleMassDist)
        count+=1
        string+=str(t)+' '
        if t:
            level+=1
            failedatcheckpoint = False
        elif string.split(' ')[-1] == 'False' and failedatcheckpoint == False:
            level-=0
            string+='True '
            count+=1
            pityT+=1
            failedatcheckpoint = False
        elif len(criticalno) > 0:
            for i in criticalno:
                if level + lastroll == i:  #If you are at one of the critical points, you will not fail.
                    failedatcheckpoint = True
                    bottom += 1               
        elif level+lastroll>1:
            level-=1
            failedatcheckpoint = False
        else:  #This is supposedly at the bottom where we fail and do not drop a level
            bottom += 1
            failedatcheckpoint = True 
        if count >= int(faith) and len(string.split(' '))-countFalses(string) - bottom - pityT<softcap:
            break
        elif count>= int(faith) and len(string.split(' '))-countFalses(string) - bottom  - pityT>=softcap and pushcount <= push:
            if t==False:
                pushcount += 1
                if pushcount >= push:
                    break
        else:pass
            

    return [string, bottom]


def hybridchain2(lastroll, softcap, faith, push,*args):  #So this is the simple version
#More aggressive mechanism.
#This reaches softcap and faith cap but then decides to push despite both being reached until push fail limit is reached.
    push = int(push)
    softcap = int(softcap) #Low end number of failures you are willing to accept
    faith = int(faith) #This is going to be total number of taps you are 'generally' willing to accept
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        summ = 0
        result = True
        for mass in massDist:
            summ += mass
            if randRoll < summ:
                return result
            else:
                return False
    def countFalses(stringie):
        cunt = 0
        for i in stringie.split(' '):
            if i == 'False':cunt+=1
            else:pass
        return cunt
    level=1
    string = ' '
    # RETARDED = [float(x) for x in args]
    RETARDED = []
    for i in args:
        if '*' in str(i):
            RETARDED.append(float(i[:-1]))
        else:
            RETARDED.append(float(i))
    print(len(RETARDED))
    #print(RETARDED)
    #print(RETARDED[level])
    #print(1-RETARDED[level])
    count = 1
    pushcount = 0
    bottom = 0
    criticalno = []
    for i in range(len(args)):
        if '*' in str(args[i]):
            criticalno.append(i+1)    
    failedatcheckpoint = False    
    while level+lastroll<len(args)+1: #The only condition when we break... when we reach our goal. This endpoint is always absolute. We are going to add break functions to stop this from "infiniting"
        sampleMassDist = (RETARDED[level-1+lastroll],1-RETARDED[level-1+lastroll])
        t = roll(sampleMassDist)
        count+=1
        string+=str(t)+' '
        if t:
            level+=1
            failedatcheckpoint = False    
        elif string.split(' ')[-1] == 'False' and failedatcheckpoint == False    :
            level-=0
            string+='True '
            count+=1
            failedatcheckpoint = False    
        elif len(criticalno) > 0:
            for i in criticalno:
                if level + lastroll == i:  #If you are at one of the critical points, you will not fail.
                    failedatcheckpoint = True
                    bottom += 1                   
        elif level+lastroll>1:
            level-=1
            failedatcheckpoint = False    
        else:
            bottom+=1
            failedatcheckpoint = True 
        if count>= int(faith) and countFalses(string)>=softcap:
            if t==True and string.split(' ')[-1] == 'False' and string.split(' ')[-2] == 'False' and pushcount == 0: #Break if pity at the softcap mark
                break
            elif t== False and pushcount == 0: #break if 
                break
            elif t== False and pushcount == push:
                break
            elif t== False:
                pushcount+=1
            else:
                pass


        else:pass
            

    return [string, bottom]


#This means that the total number of successes is actually len(trues) - len(falses) +bottom. This is only important when you are repeating these above











def pitychaintilldeathm(lastroll, faith, *args): #with pity system - 2 fails in a row leads to one auto success | NEW:lastroll is option to retain information from previous roll to start from where you ended off from previous attempt!!!!
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        summ = 0
        result = True
        for mass in massDist:
            summ += mass
            if randRoll < summ:
                return result
            else:
                return False
    level=1
    string = ' '
    RETARDED = []
    Prices = []
    for i in args:
        i, iprice = i.split("|")
        if '*' in str(i):
            RETARDED.append(float(i[:-1]))
        else:
            RETARDED.append(float(i))
        Prices.append(float(iprice))
    print(len(RETARDED))
    #print(RETARDED)
    #print(RETARDED[level])
    #print(1-RETARDED[level])
    count = 1
    bottom = 0
    #Lets try to establish which arguments are critical points at which falling below is not possible - for now I think it is reasonable to expect that the critical points
    #behave exactly like the first level that we provide
    #First - let's try to extract and 'look for' critical points denoted by * after the probability values
    criticalno = []
    for i in range(len(args)):
        if '*' in str(args[i]):
            criticalno.append(i+1)   
    failedatcheckpoint = False  #To record if failure at checkpoint occurred in last roll - because if you fail once alr at a checkpoint, you CANNOT be given pity rank up if you fail at it again   
    mesos = 0         
    while count < int(faith)+1 and level+lastroll<len(args)+1:
        print(level-1+lastroll)
        sampleMassDist = (RETARDED[level-1+lastroll],1-RETARDED[level-1+lastroll])
        t = roll(sampleMassDist) #do the roll
        mesos += Prices[level-1+lastroll]
        count+=1
        string+=str(t)+' '
        if t:
            level+=1
            failedatcheckpoint = False
        elif string.split(' ')[-1] == 'False' and failedatcheckpoint == False:
            level-=0 #just to indicate that you failed AND succeeded because of pity rank up right after at 100%
            string+='True '
            count+=1
            failedatcheckpoint = False
        elif len(criticalno) > 0:
            for i in criticalno:
                if level + lastroll == i:  #If you are at one of the critical points, you will not fail.
                    failedatcheckpoint = True
                    bottom += 1
        elif level+lastroll>1:  #Catch all term for dropping a level if no check point was triggered in previous if statement
            level-=1
            failedatcheckpoint = False
        else:
            bottom+=1
            failedatcheckpoint = True
    return [string, bottom, mesos]







def pitychaintilldeath0m(lastroll, faith, *args): #with pity system - 2 fails in a row leads to one auto success | NEW:lastroll is option to retain information from previous roll to start from where you ended off from previous attempt!!!! 100% false dependent.
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        summ = 0
        result = True
        for mass in massDist:
            summ += mass
            if randRoll < summ:
                return result
            else:
                return False
    def countFalses(stringie):
        cunt = 0
        for i in stringie.split(' '):
            if i == 'False':cunt+=1
            else:pass
        return cunt
    level=1
    string = ' '
    #RETARDED = [float(x) for x in args]
    RETARDED = []
    Prices = []
    for i in args:
        i, iprice = i.split("|")
        if '*' in str(i):
            RETARDED.append(float(i[:-1]))
        else:
            RETARDED.append(float(i))
        Prices.append(float(iprice))
    print(len(RETARDED))
    #print(RETARDED)
    #print(RETARDED[level])
    #print(1-RETARDED[level])
    count = 1
    bottom =0 #Number of times failed at bottom
    #Lets try to establish which arguments are critical points at which falling below is not possible - for now I think it is reasonable to expect that the critical points
    #behave exactly like the first level that we provide
    #First - let's try to extract and 'look for' critical points denoted by * after the probability values
    criticalno = []
    for i in range(len(args)):
        if '*' in str(args[i]):
            criticalno.append(i+1)     
    failedatcheckpoint = False  #To record if failure at checkpoint occurred in last roll - because if you fail once alr at a checkpoint, you CANNOT be given pity rank up if you fail at it again     
    mesos = 0       
    while countFalses(string) < int(faith) and level+lastroll<len(args)+1:
        sampleMassDist = (RETARDED[level-1+lastroll],1-RETARDED[level-1+lastroll])
        t = roll(sampleMassDist)
        mesos += Prices[level-1+lastroll]
        count+=1
        string+=str(t)+' '           
        if t:
            level+=1
            failedatcheckpoint = False
        elif string.split(' ')[-1] == 'False' and failedatcheckpoint == False:
            level-=0
            string+='True '
            count+=1
            failedatcheckpoint = False
        elif len(criticalno) > 0:
            for i in criticalno:
                if level + lastroll == i:  #If you are at one of the critical points, you will not fail.
                    failedatcheckpoint = True
                    bottom += 1            
        elif level+lastroll>1:
            level-=1
            failedatcheckpoint = False
        else:
            bottom+=1
            failedatcheckpoint = True
    return [string, bottom, mesos]





#Simple "AI". If softcap of successes is not reached and total count is alr reached, carry on for a small fail target. - A more conservative tapping higher failure aversive rolling session. You are aiming for a 
#More complex "AI". If last 3 taps were not FFT (pity) + last tap was T, then try a few more taps 

def hybridchain1m(lastroll, softcap, faith, push,*args):  #So this is the simple version
#Hence, faith here is going to be the total number of taps cap BUT, it will decide to override it based off of softcap
#How much we push past despite reaching count cap is determined by input variable 'push'. 'push is the new number of failures we are willing to accept.
    push = int(push)
    softcap = int(softcap) #Low end number of failures you are willing to accept
    faith = int(faith) #This is going to be total number of taps you are 'generally' willing to accept
    softcap = min(softcap,len(args))
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        summ = 0
        result = True
        for mass in massDist:
            summ += mass
            if randRoll < summ:
                return result
            else:
                return False
    def countFalses(stringie):
        cunt = 0
        for i in stringie.split(' '):
            if i == 'False':cunt+=1
            else:pass
        return cunt
    level=1
    string = ' '
    # RETARDED = [float(x.translate) for x in args]
    RETARDED = []
    Prices = []
    for i in args:
        i, iprice = i.split("|")
        if '*' in str(i):
            RETARDED.append(float(i[:-1]))
        else:
            RETARDED.append(float(i))
        Prices.append(float(iprice))
    print(len(RETARDED))
    #print(RETARDED)
    #print(RETARDED[level])
    #print(1-RETARDED[level])
    count = 1
    pushcount = 0
    bottom =0 #Number of times failed at bottom
    pityT = 0
    criticalno = []
    for i in range(len(args)):
        if '*' in str(args[i]):
            criticalno.append(i+1)     
    failedatcheckpoint = False  #To record if failure at checkpoint occurred in last roll - because if you fail once alr at a checkpoint, you CANNOT be given pity rank up if you fail at it again  
    mesos = 0       
    while level+lastroll<len(args)+1: #The only condition when we break... when we reach our goal. This endpoint is always absolute. We are going to add break functions to stop this from "infiniting"
        sampleMassDist = (RETARDED[level-1+lastroll],1-RETARDED[level-1+lastroll])
        t = roll(sampleMassDist)
        mesos += Prices[level-1+lastroll]
        count+=1
        string+=str(t)+' '
        if t:
            level+=1
            failedatcheckpoint = False
        elif string.split(' ')[-1] == 'False' and failedatcheckpoint == False:
            level-=0
            string+='True '
            count+=1
            pityT+=1
            failedatcheckpoint = False
        elif len(criticalno) > 0:
            for i in criticalno:
                if level + lastroll == i:  #If you are at one of the critical points, you will not fail.
                    failedatcheckpoint = True
                    bottom += 1               
        elif level+lastroll>1:
            level-=1
            failedatcheckpoint = False
        else:  #This is supposedly at the bottom where we fail and do not drop a level
            bottom += 1
            failedatcheckpoint = True 
        if count >= int(faith) and len(string.split(' '))-countFalses(string) - bottom - pityT<softcap:
            break
        elif count>= int(faith) and len(string.split(' '))-countFalses(string) - bottom  - pityT>=softcap and pushcount <= push:
            if t==False:
                pushcount += 1
                if pushcount >= push:
                    break
        else:pass
            

    return [string, bottom, mesos]


def hybridchain2m(lastroll, softcap, faith, push,*args):  #So this is the simple version
#More aggressive mechanism.
#This reaches softcap and faith cap but then decides to push despite both being reached until push fail limit is reached.
    push = int(push)
    softcap = int(softcap) #Low end number of failures you are willing to accept
    faith = int(faith) #This is going to be total number of taps you are 'generally' willing to accept
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        summ = 0
        result = True
        for mass in massDist:
            summ += mass
            if randRoll < summ:
                return result
            else:
                return False
    def countFalses(stringie):
        cunt = 0
        for i in stringie.split(' '):
            if i == 'False':cunt+=1
            else:pass
        return cunt
    level=1
    string = ' '
    # RETARDED = [float(x) for x in args]
    RETARDED = []
    Prices = []
    for i in args:
        i, iprice = i.split("|")
        if '*' in str(i):
            RETARDED.append(float(i[:-1]))
        else:
            RETARDED.append(float(i))
        Prices.append(float(iprice))
    print(len(RETARDED))
    #print(RETARDED)
    #print(RETARDED[level])
    #print(1-RETARDED[level])
    count = 1
    pushcount = 0
    bottom = 0
    criticalno = []
    for i in range(len(args)):
        if '*' in str(args[i]):
            criticalno.append(i+1)    
    failedatcheckpoint = False  
    mesos = 0     
    while level+lastroll<len(args)+1: #The only condition when we break... when we reach our goal. This endpoint is always absolute. We are going to add break functions to stop this from "infiniting"
        sampleMassDist = (RETARDED[level-1+lastroll],1-RETARDED[level-1+lastroll])
        t = roll(sampleMassDist)
        mesos += Prices[level-1+lastroll]
        count+=1
        string+=str(t)+' '
        if t:
            level+=1
            failedatcheckpoint = False    
        elif string.split(' ')[-1] == 'False' and failedatcheckpoint == False    :
            level-=0
            string+='True '
            count+=1
            failedatcheckpoint = False    
        elif len(criticalno) > 0:
            for i in criticalno:
                if level + lastroll == i:  #If you are at one of the critical points, you will not fail.
                    failedatcheckpoint = True
                    bottom += 1                   
        elif level+lastroll>1:
            level-=1
            failedatcheckpoint = False    
        else:
            bottom+=1
            failedatcheckpoint = True 
        if count>= int(faith) or countFalses(string)>=softcap:
            if t==True and string.split(' ')[-1] == 'False' and string.split(' ')[-2] == 'False' and pushcount == 0: #Break if pity at the softcap mark
                break
            elif t== False and pushcount == 0: #break if 
                break
            elif t== False and pushcount == push:
                break
            elif t== False:
                pushcount+=1
            else:
                pass


        else:pass
            

    return [string, bottom, mesos]


#This means that the total number of successes is actually len(trues) - len(falses) +bottom. This is only important when you are repeating these above




















def chainular(*args):
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        sum = 0
        result = True
        for mass in massDist:
            sum += mass
            if randRoll < sum:
                return result
            else:
                return False

    string = ''
    for i in args:
        print(i)
        sampleMassDist = (float(i),1-float(i))
        string += str(roll(sampleMassDist))+' '
    return string

def chaintilldeath(faith, *args):  #without pity system
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        sum = 0
        result = True
        for mass in massDist:
            sum += mass
            if randRoll < sum:
                return result
            else:
                return False
    level=1
    string = ' '
    # RETARDED = [float(x) for x in args]
    RETARDED = []
    for i in args:
        if '*' in str(i):
            RETARDED.append(float(i[:-1]))
        else:
            RETARDED.append(float(i))
    #print(RETARDED)
    #print(RETARDED[level])
    #print(1-RETARDED[level])
    count = 1
    while count < int(faith)+1 and level<len(args)+1:
        sampleMassDist = (RETARDED[level-1],1-RETARDED[level-1])
        t = roll(sampleMassDist)
        count+=1
        string+=str(t)+' '
        if t:
            level+=1
        elif level>1:
            level-=1
    return string





@client.event
async def on_ready():
    print("Beep!")

@client.command()
@commands.has_role("Duke")
async def stop(ctx):
    await client.logout()

@client.command()
async def React(ctx):
    choices = ["/╲⎛⎝(•∵•‴)⎠⎞╱\ ", "ᄽὁȍωőὀᄿ", "/╲/\╭ºooooº╮/\╱\ "]
    await ctx.send(random.choice(choices))
    if aroll([0.5])>0.8:
        await ctx.send(random.random(["skfhjsdk"]))





@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()






@client.command()
@commands.has_role("Team Lucid")
async def SF(ctx,trials, faith, *args):  #helps to loop through the tries. This is for batches UNTIL success
    SUCCESSWEWANT = len(args)
    faith = abs(int(faith))
    faith = max(len(args),faith)
    def TrueCount(stringie, lastround):
        final = False
        n = len([x for x in stringie.split(' ') if x == 'False'])
        if len([x for x in stringie.split(' ') if x == 'True']) - len([x for x in stringie.split(' ') if x == 'False']) +int(lastround) == SUCCESSWEWANT:
            final = True
        return [final,n]
    data = []  #Number of tries it took until we got a success and stopped the trial
    N=[]  #Number of falses for the last successful set of attempts per trial
    NAve=[]  #Average number of falses and max for the entire set of attempts per trial: [Average,Maximum]
    NSum = []
    NStat = []
    tapdata = []
    for i in range(int(trials)):
        tapdata_count = 0
        nall = []
        count = 1
        lasttime = 0
        checkthis, BOTTOM = pitychaintilldeath(lasttime, faith, *args) #first run - BOTTOM is the number of times one failed at a critical point which is not to be counted in the overall number of levels progressed
        #per session!
        print(checkthis) #print the string of results for the first batch of runs
        nall.append(TrueCount(checkthis, lasttime)[1])
        tapdata_count += len(checkthis.split(" "))
        while TrueCount(checkthis, lasttime)[0] == False:
            #print(count)
            count += 1
            lasttime += len([x for x in checkthis.split(' ') if x == 'True']) - len([x for x in checkthis.split(' ') if x == 'False'])+BOTTOM  #Update the trial number you previously were at!!!
            lasttime = max(lasttime,0)
            print(lasttime)
            checkthis, BOTTOM = pitychaintilldeath(lasttime, faith, *args)
            nall.append(TrueCount(checkthis, lasttime)[1])
            tapdata_count += len(checkthis.split(" "))
            #print(checkthis)
        tapdata.append(tapdata_count)
        data.append(count)
        N.append(TrueCount(checkthis, lasttime)[1])
        NStat.append([np.mean(nall), max(nall), sum(nall)])
        NSum.append(sum(nall))
        NAve.append(np.mean(nall))
    #Making copies for the histogram 
    histdata = np.array(np.copy(data))
    histdata2 = np.array(np.copy(data))
    histN = np.array(np.copy(N))
    histNSum= np.array(np.copy(NSum))
    histNAve= np.array(np.copy(NAve))
    __,SortedNAve = (np.array(t) for t in zip(*sorted(zip(histdata, histNAve))))
    __,SortedNSum = (np.array(t) for t in zip(*sorted(zip(histdata, histNSum))))
    histdata = sorted(histdata)
    rate = 0.6
    d = max(histdata)/(int(int(trials)**rate)) #bin ranges of attempts
    print(f"Rate is {d}")
    P = []
    for i in range(int(int(trials)**rate)):
        try:
            #y = max([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            #print(i)
            #print(d*(i))
            y = np.max(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            #y1 = min([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            y1 = np.min(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            print(y1,y)
            perbin = [[SortedNAve[x], SortedNSum[x]] for x in range(int(y1),int(y))]
            avg_min = min([x[0] for x in perbin])
            avg_max = max([x[0] for x in perbin])
            total_min = min([x[1] for x in perbin])
            total_max = max([x[1] for x in perbin])
            P.append([avg_min, avg_max,total_min,total_max])
        except:
            pass
        #print(perbin)
        
    x = np.linspace(1,int(trials),int(trials))
    plt.clf()
    fig = plt.figure()
    plt.style.use('fivethirtyeight') 
    plt.figure(figsize=(20,10))
    plt.xlim(0,max(data))
    plt.xlabel("No. of attempts")
    plt.ylabel("Density")
    plt.title("Attempts distribution prior to success - Failures annotated")
    splot = sns.distplot(data, hist=True, kde=True, 
             bins=int(int(trials)**rate), 
             kde_kws={'linewidth': 4})
    labelno = 0
    for p in splot.patches:
        try:
            splot.annotate(f"Average \n {P[labelno][0]:.2f} - {P[labelno][1]:.2f} \n Total  \n {P[labelno][2]} - {P[labelno][3]}",
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center',
                       xytext=(0, 9),
                       textcoords='offset points', set_fontsize = 80)
        except:
            pass
        labelno += 1
    plt.savefig(fname='plot2')
    plt.style.use("seaborn-dark")
    plt.clf()
    plt.figure(figsize=(20,10))
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    plt.grid(color='#2A3459')
    # colors = random.choice(['#99fcff', '#fb53fe', "#FFE74C", "#FFFFFF", "#6BF178", "#BF0603", "#35A7FF", "#8447FF", "#D972FF", "#F6F930", "#D2F898", "#FCFCFC", "#ED4D6E", "#E9D6EC", "#59A96A", "#9BDEAC", "#B4E7CE", "#4392F1", "#61E786", "#E3EBFF", "#38369A", "#020887"])
    colors = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(200)])
    MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    plt.plot(x, data, color = colors, marker = MARK, linestyle = random.choice(linestyle_tuple))
    if int(trials)<300:
        COMB = [str(N[i]) +"\n"+ "["+str(int(NStat[i][0]))+"/" + str(NStat[i][1]) +"/" + str(NStat[i][2]) + "]" for i in range(len(N))]
        for i,txt in enumerate(COMB):
            text = plt.annotate(txt, (x[i],data[i]))
            text.set_fontsize(8)
    plt.xlabel("Trials (separate) from start point")
    plt.ylabel("No of attempts until success")
    plt.title(f"{ctx.message.author}\'s starforce simulation - with pity sys.: {faith} attempts,{trials} times")
    plt.savefig(fname='plot')
    await ctx.send(file=discord.File('plot.png'))
    os.remove('plot.png')
    await ctx.send(file=discord.File('plot2.png'))
    os.remove('plot2.png')








@client.command()
@commands.has_role("Team Lucid")
async def SFI(ctx,trials, faith, *args):  #helps to loop through the tries. This is for batches UNTIL success. HOWEVER, THIS TIME THIS IS FAILURE SAFED INSTEAD. WE SHALL TRY TO CAP BASED OFF OF TOTAL NUMBER OF FAILURES PER SESSION - FAITH.Impulsive tapping. dependent on number of falses
    SUCCESSWEWANT = len(args)
    faith = abs(int(faith))
    # faith = max(len(args),faith)  You do not do this for the impulsive run!!!
    def TrueCount(stringie, lastround):
        final = False
        n = len([x for x in stringie.split(' ') if x == 'False'])
        if len([x for x in stringie.split(' ') if x == 'True']) - len([x for x in stringie.split(' ') if x == 'False']) +int(lastround) == SUCCESSWEWANT:
            final = True
        return [final,n]
    data = []  #Number of tries it took until we got a success and stopped the trial
    N=[]  #Number of falses for the last successful set of attempts per trial
    NAve=[]  #Average number of falses and max for the entire set of attempts per trial: [Average,Maximum]
    NSum = []
    NStat = []
    for i in range(int(trials)):
        nall = []
        count = 1
        lasttime = 0
        checkthis, BOTTOM = pitychaintilldeath0(lasttime, faith, *args) #first run
        print(checkthis) #print the string of results for the first batch of runs
        nall.append(TrueCount(checkthis, lasttime)[1])
        while TrueCount(checkthis, lasttime)[0] == False:
            #print(count)
            count += 1
            lasttime += len([x for x in checkthis.split(' ') if x == 'True']) - len([x for x in checkthis.split(' ') if x == 'False'])+BOTTOM  #Update the trial number you previously were at!!!
            lasttime = max(lasttime,0)
            print(lasttime)
            checkthis, BOTTOM = pitychaintilldeath0(lasttime, faith, *args)
            nall.append(TrueCount(checkthis, lasttime)[1])
            #print(checkthis)
        data.append(count)
        N.append(TrueCount(checkthis, lasttime)[1])
        NStat.append([np.mean(nall), max(nall), sum(nall)])
        NSum.append(sum(nall))
        NAve.append(np.mean(nall))
    #Making copies for the histogram 
    histdata = np.array(np.copy(data))
    histdata2 = np.array(np.copy(data))
    histN = np.array(np.copy(N))
    histNSum= np.array(np.copy(NSum))
    histNAve= np.array(np.copy(NAve))
    __,SortedNAve = (np.array(t) for t in zip(*sorted(zip(histdata, histNAve))))
    __,SortedNSum = (np.array(t) for t in zip(*sorted(zip(histdata, histNSum))))
    histdata = sorted(histdata)
    rate = 0.6
    d = max(histdata)/(int(int(trials)**rate)) #bin ranges of attempts
    print(f"Rate is {d}")
    P = []
    for i in range(int(int(trials)**rate)):
        try:
            #y = max([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            #print(i)
            #print(d*(i))
            y = np.max(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            #y1 = min([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            y1 = np.min(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            print(y1,y)
            perbin = [[SortedNAve[x], SortedNSum[x]] for x in range(int(y1),int(y))]
            avg_min = min([x[0] for x in perbin])
            avg_max = max([x[0] for x in perbin])
            total_min = min([x[1] for x in perbin])
            total_max = max([x[1] for x in perbin])
            P.append([avg_min, avg_max,total_min,total_max])
        except:
            pass
        #print(perbin)
        
    x = np.linspace(1,int(trials),int(trials))
    plt.clf()
    fig = plt.figure()
    plt.style.use('fivethirtyeight') 
    plt.figure(figsize=(20,10))
    plt.xlim(0,max(data))
    plt.xlabel("No. of attempts")
    plt.ylabel("Density")
    plt.title("Attempts distribution prior to success - Failures annotated")
    splot = sns.distplot(data, hist=True, kde=True, 
             bins=int(int(trials)**rate), 
             kde_kws={'linewidth': 4})
    labelno = 0
    for p in splot.patches:
        try:
            splot.annotate(f"Average \n {P[labelno][0]:.2f} - {P[labelno][1]:.2f} \n Total  \n {P[labelno][2]} - {P[labelno][3]}",
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center',
                       xytext=(0, 9),
                       textcoords='offset points')
        except:
            pass
        labelno += 1
    plt.savefig(fname='plot2')
    plt.style.use("seaborn-dark")
    plt.clf()
    plt.figure(figsize=(20,10))
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    plt.grid(color='#2A3459')
    # colors = random.choice(['#99fcff', '#fb53fe', "#FFE74C", "#FFFFFF", "#6BF178", "#BF0603", "#35A7FF", "#8447FF", "#D972FF", "#F6F930", "#D2F898", "#FCFCFC", "#ED4D6E", "#E9D6EC", "#59A96A", "#9BDEAC", "#B4E7CE", "#4392F1", "#61E786", "#E3EBFF", "#38369A", "#020887"])
    colors = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(200)])
    MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    plt.plot(x, data, color = colors, marker = MARK, linestyle = random.choice(linestyle_tuple))
    if int(trials)<300:
        COMB = [str(N[i]) +"\n"+ "["+str(int(NStat[i][0]))+"/" + str(NStat[i][1]) +"/" + str(NStat[i][2]) + "]" for i in range(len(N))]
        for i,txt in enumerate(COMB):
            text = plt.annotate(txt, (x[i],data[i]))
            text.set_fontsize(8)
    plt.xlabel("Trials (separate) from start point")
    plt.ylabel("No of attempts until success")
    plt.title(f"{ctx.message.author}\'s starforce simulation - with pity sys.: {faith} attempts,{trials} times")
    plt.savefig(fname='plot')
    await ctx.send(file=discord.File('plot.png'))
    os.remove('plot.png')
    await ctx.send(file=discord.File('plot2.png'))
    os.remove('plot2.png')            

  



@client.command()
@commands.has_role("Team Lucid")
async def SFH1(ctx,trials, faith, softcap, push, *args):  #helps to loop through the tries. This is for batches UNTIL success. HOWEVER, THIS TIME THIS IS FAILURE SAFED INSTEAD. WE SHALL TRY TO CAP BASED OFF OF TOTAL NUMBER OF FAILURES PER SESSION - FAITH.Impulsive tapping. dependent on number of falses
    SUCCESSWEWANT = len(args)
    faith = abs(int(faith))
    softcap = int(softcap)
    push = int(push)
    # faith = max(len(args),faith)  You do not do this for the impulsive run!!!
    def TrueCount(stringie, lastround):
        final = False
        n = len([x for x in stringie.split(' ') if x == 'False'])
        if len([x for x in stringie.split(' ') if x == 'True']) - len([x for x in stringie.split(' ') if x == 'False']) +int(lastround) == SUCCESSWEWANT:
            final = True
        return [final,n]
    data = []  #Number of tries it took until we got a success and stopped the trial
    N=[]  #Number of falses for the last successful set of attempts per trial
    NAve=[]  #Average number of falses and max for the entire set of attempts per trial: [Average,Maximum]
    NSum = []
    NStat = []
    for i in range(int(trials)):
        nall = []
        count = 1
        lasttime = 0
        checkthis, BOTTOM = hybridchain1(lasttime, softcap, faith,push, *args) #first run
        print(checkthis) #print the string of results for the first batch of runs
        nall.append(TrueCount(checkthis, lasttime)[1])
        while TrueCount(checkthis, lasttime)[0] == False:
            #print(count)
            count += 1
            lasttime += len([x for x in checkthis.split(' ') if x == 'True']) - len([x for x in checkthis.split(' ') if x == 'False'])+BOTTOM  #Update the trial number you previously were at!!!
            lasttime = max(lasttime,0)
            print(lasttime)
            checkthis, BOTTOM = hybridchain1(lasttime, softcap, faith,push, *args)
            nall.append(TrueCount(checkthis, lasttime)[1])
            #print(checkthis)
        data.append(count)
        N.append(TrueCount(checkthis, lasttime)[1])
        NStat.append([np.mean(nall), max(nall), sum(nall)])
        NSum.append(sum(nall))
        NAve.append(np.mean(nall))
    #Making copies for the histogram 
    histdata = np.array(np.copy(data))
    histdata2 = np.array(np.copy(data))
    histN = np.array(np.copy(N))
    histNSum= np.array(np.copy(NSum))
    histNAve= np.array(np.copy(NAve))
    __,SortedNAve = (np.array(t) for t in zip(*sorted(zip(histdata, histNAve))))
    __,SortedNSum = (np.array(t) for t in zip(*sorted(zip(histdata, histNSum))))
    histdata = sorted(histdata)
    rate = 0.6
    d = max(histdata)/(int(int(trials)**rate)) #bin ranges of attempts
    print(f"Rate is {d}")
    P = []
    for i in range(int(int(trials)**rate)):
        try:
            #y = max([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            #print(i)
            #print(d*(i))
            y = np.max(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            #y1 = min([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            y1 = np.min(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            print(y1,y)
            perbin = [[SortedNAve[x], SortedNSum[x]] for x in range(int(y1),int(y))]
            avg_min = min([x[0] for x in perbin])
            avg_max = max([x[0] for x in perbin])
            total_min = min([x[1] for x in perbin])
            total_max = max([x[1] for x in perbin])
            P.append([avg_min, avg_max,total_min,total_max])
        except:
            pass
        #print(perbin)
        
    x = np.linspace(1,int(trials),int(trials))
    plt.clf()
    fig = plt.figure()
    plt.style.use('fivethirtyeight') 
    plt.figure(figsize=(20,10))
    plt.xlim(0,max(data))
    plt.xlabel("No. of attempts")
    plt.ylabel("Density")
    plt.title("Attempts distribution prior to success - Failures annotated")
    splot = sns.distplot(data, hist=True, kde=True, 
             bins=int(int(trials)**rate), 
             kde_kws={'linewidth': 4})
    labelno = 0
    for p in splot.patches:
        try:
            splot.annotate(f"Average \n {P[labelno][0]:.2f} - {P[labelno][1]:.2f} \n Total  \n {P[labelno][2]} - {P[labelno][3]}",
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center',
                       xytext=(0, 9),
                       textcoords='offset points')
        except:
            pass
        labelno += 1
    plt.savefig(fname='plot2')
    plt.style.use("seaborn-dark")
    plt.clf()
    plt.figure(figsize=(20,10))
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    plt.grid(color='#2A3459')
    # colors = random.choice(['#99fcff', '#fb53fe', "#FFE74C", "#FFFFFF", "#6BF178", "#BF0603", "#35A7FF", "#8447FF", "#D972FF", "#F6F930", "#D2F898", "#FCFCFC", "#ED4D6E", "#E9D6EC", "#59A96A", "#9BDEAC", "#B4E7CE", "#4392F1", "#61E786", "#E3EBFF", "#38369A", "#020887"])
    colors = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(200)])
    MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    plt.plot(x, data, color = colors, marker = MARK, linestyle = random.choice(linestyle_tuple))
    if int(trials)<300:
        COMB = [str(N[i]) +"\n"+ "["+str(int(NStat[i][0]))+"/" + str(NStat[i][1]) +"/" + str(NStat[i][2]) + "]" for i in range(len(N))]
        for i,txt in enumerate(COMB):
            text = plt.annotate(txt, (x[i],data[i]))
            text.set_fontsize(8)
    plt.xlabel("Trials (separate) from start point")
    plt.ylabel("No of attempts until success")
    plt.title(f"{ctx.message.author}\'s starforce simulation - with pity sys.: {faith} attempts,{trials} times")
    plt.savefig(fname='plot')
    await ctx.send(file=discord.File('plot.png'))
    os.remove('plot.png')
    await ctx.send(file=discord.File('plot2.png'))
    os.remove('plot2.png')            

    



@client.command()
@commands.has_role("Team Lucid")
async def SFH2(ctx,trials, faith, softcap, push, *args):  #helps to loop through the tries. This is for batches UNTIL success. HOWEVER, THIS TIME THIS IS FAILURE SAFED INSTEAD. WE SHALL TRY TO CAP BASED OFF OF TOTAL NUMBER OF FAILURES PER SESSION - FAITH.Impulsive tapping. dependent on number of falses
    SUCCESSWEWANT = len(args)
    faith = abs(int(faith))
    softcap = int(softcap)
    push = int(push)
    # faith = max(len(args),faith)  You do not do this for the impulsive run!!!
    def TrueCount(stringie, lastround):
        final = False
        n = len([x for x in stringie.split(' ') if x == 'False'])
        if len([x for x in stringie.split(' ') if x == 'True']) - len([x for x in stringie.split(' ') if x == 'False']) +int(lastround) == SUCCESSWEWANT:
            final = True
        return [final,n]
    data = []  #Number of tries it took until we got a success and stopped the trial
    N=[]  #Number of falses for the last successful set of attempts per trial
    NAve=[]  #Average number of falses and max for the entire set of attempts per trial: [Average,Maximum]
    NSum = []
    NStat = []
    for i in range(int(trials)):
        nall = []
        count = 1
        lasttime = 0
        checkthis, BOTTOM = hybridchain2(lasttime, softcap, faith,push, *args) #first run
        print(checkthis) #print the string of results for the first batch of runs
        nall.append(TrueCount(checkthis, lasttime)[1])
        while TrueCount(checkthis, lasttime)[0] == False:
            #print(count)
            count += 1
            lasttime += len([x for x in checkthis.split(' ') if x == 'True']) - len([x for x in checkthis.split(' ') if x == 'False'])+BOTTOM  #Update the trial number you previously were at!!!
            lasttime = max(lasttime,0)
            print(lasttime)
            checkthis, BOTTOM = hybridchain2(lasttime, softcap, faith,push, *args)
            nall.append(TrueCount(checkthis, lasttime)[1])
            #print(checkthis)
        data.append(count)
        N.append(TrueCount(checkthis, lasttime)[1])
        NStat.append([np.mean(nall), max(nall), sum(nall)])
        NSum.append(sum(nall))
        NAve.append(np.mean(nall))
    #Making copies for the histogram 
    histdata = np.array(np.copy(data))
    histdata2 = np.array(np.copy(data))
    histN = np.array(np.copy(N))
    histNSum= np.array(np.copy(NSum))
    histNAve= np.array(np.copy(NAve))
    __,SortedNAve = (np.array(t) for t in zip(*sorted(zip(histdata, histNAve))))
    __,SortedNSum = (np.array(t) for t in zip(*sorted(zip(histdata, histNSum))))
    histdata = sorted(histdata)
    rate = 0.6
    d = max(histdata)/(int(int(trials)**rate)) #bin ranges of attempts
    print(f"Rate is {d}")
    P = []
    for i in range(int(int(trials)**rate)):
        try:
            #y = max([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            #print(i)
            #print(d*(i))
            y = np.max(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            #y1 = min([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            y1 = np.min(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            print(y1,y)
            perbin = [[SortedNAve[x], SortedNSum[x]] for x in range(int(y1),int(y))]
            avg_min = min([x[0] for x in perbin])
            avg_max = max([x[0] for x in perbin])
            total_min = min([x[1] for x in perbin])
            total_max = max([x[1] for x in perbin])
            P.append([avg_min, avg_max,total_min,total_max])
        except:
            pass
        #print(perbin)
        
    x = np.linspace(1,int(trials),int(trials))
    plt.clf()
    fig = plt.figure()
    plt.style.use('fivethirtyeight') 
    plt.figure(figsize=(20,10))
    plt.xlim(0,max(data))
    plt.xlabel("No. of attempts")
    plt.ylabel("Density")
    plt.title("Attempts distribution prior to success - Failures annotated")
    splot = sns.distplot(data, hist=True, kde=True, 
             bins=int(int(trials)**rate), 
             kde_kws={'linewidth': 4})
    labelno = 0
    for p in splot.patches:
        try:
            splot.annotate(f"Average \n {P[labelno][0]:.2f} - {P[labelno][1]:.2f} \n Total  \n {P[labelno][2]} - {P[labelno][3]}",
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center',
                       xytext=(0, 9),
                       textcoords='offset points')
        except:
            pass
        labelno += 1
    plt.savefig(fname='plot2')
    plt.style.use("seaborn-dark")
    plt.clf()
    plt.figure(figsize=(20,10))
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    plt.grid(color='#2A3459')
    # colors = random.choice(['#99fcff', '#fb53fe', "#FFE74C", "#FFFFFF", "#6BF178", "#BF0603", "#35A7FF", "#8447FF", "#D972FF", "#F6F930", "#D2F898", "#FCFCFC", "#ED4D6E", "#E9D6EC", "#59A96A", "#9BDEAC", "#B4E7CE", "#4392F1", "#61E786", "#E3EBFF", "#38369A", "#020887"])
    colors = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(200)])
    MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    plt.plot(x, data, color = colors, marker = MARK, linestyle = random.choice(linestyle_tuple))
    if int(trials)<300:
        COMB = [str(N[i]) +"\n"+ "["+str(int(NStat[i][0]))+"/" + str(NStat[i][1]) +"/" + str(NStat[i][2]) + "]" for i in range(len(N))]
        for i,txt in enumerate(COMB):
            text = plt.annotate(txt, (x[i],data[i]))
            text.set_fontsize(8)
    plt.xlabel("Trials (separate) from start point")
    plt.ylabel("No of attempts until success")
    plt.title(f"{ctx.message.author}\'s starforce simulation - with pity sys.: {faith} attempts,{trials} times")
    plt.savefig(fname='plot')
    await ctx.send(file=discord.File('plot.png'))
    os.remove('plot.png')
    await ctx.send(file=discord.File('plot2.png'))
    os.remove('plot2.png')            

    




@client.command()
@commands.has_role("Team Lucid")
async def SFm(ctx,trials, faith, *args):  #helps to loop through the tries. This is for batches UNTIL success
    SUCCESSWEWANT = len(args)
    faith = abs(int(faith))
    faith = max(len(args),faith)
    def TrueCount(stringie, lastround):
        final = False
        n = len([x for x in stringie.split(' ') if x == 'False'])
        if len([x for x in stringie.split(' ') if x == 'True']) - len([x for x in stringie.split(' ') if x == 'False']) +int(lastround) == SUCCESSWEWANT:
            final = True
        return [final,n]
    data = []  #Number of tries it took until we got a success and stopped the trial
    N=[]  #Number of falses for the last successful set of attempts per trial
    NAve=[]  #Average number of falses and max for the entire set of attempts per trial: [Average,Maximum]
    NSum = []
    NStat = []
    tapdata = []
    Meso = []
    for i in range(int(trials)):
        mesospertrial = 0
        tapdata_count = 0
        nall = []
        count = 1
        lasttime = 0
        checkthis, BOTTOM, meso = pitychaintilldeathm(lasttime, faith, *args) #first run - BOTTOM is the number of times one failed at a critical point which is not to be counted in the overall number of levels progressed
        #per session!
        mesospertrial += meso
        print(checkthis) #print the string of results for the first batch of runs
        nall.append(TrueCount(checkthis, lasttime)[1])
        tapdata_count += len(checkthis.split(" "))
        finalcheck = ""
        while TrueCount(checkthis, lasttime)[0] == False:
            #print(count)
            count += 1
            lasttime += len([x for x in checkthis.split(' ') if x == 'True']) - len([x for x in checkthis.split(' ') if x == 'False'])+BOTTOM  #Update the trial number you previously were at!!!
            lasttime = max(lasttime,0)
            print(lasttime)
            finalcheck = checkthis
            checkthis, BOTTOM, mesos = pitychaintilldeathm(lasttime, faith, *args)          
            mesospertrial += mesos
            nall.append(TrueCount(checkthis, lasttime)[1])
            tapdata_count += len(checkthis.split(" "))
            #print(checkthis)
        tapdata.append(tapdata_count)
        data.append(count)
        Meso.append(round(mesospertrial, 1))
        # print(f"{checkthis} is the final set of true and falses obtained for the last attempt for trial {i}")
        # print(f"Number of fails for trial {i}'s final attempt is {TrueCount(checkthis, lasttime)[1]}")
        N.append(TrueCount(finalcheck, lasttime)[1])
        NStat.append([np.mean(nall), max(nall), sum(nall)])
        NSum.append(sum(nall))
        NAve.append(np.mean(nall))
    #Making copies for the histogram 
    histdata = np.array(np.copy(data))
    histdata2 = np.array(np.copy(data))
    histN = np.array(np.copy(N))
    histNSum= np.array(np.copy(NSum))
    histNAve= np.array(np.copy(NAve))
    __,SortedNAve = (np.array(t) for t in zip(*sorted(zip(histdata, histNAve))))
    __,SortedNSum = (np.array(t) for t in zip(*sorted(zip(histdata, histNSum))))
    histdata = sorted(histdata)
    rate = 0.6
    d = max(histdata)/(int(int(trials)**rate)) #bin ranges of attempts
    print(f"Rate is {d}")
    P = []
    for i in range(int(int(trials)**rate)):
        try:
            #y = max([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            #print(i)
            #print(d*(i))
            y = np.max(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            #y1 = min([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            y1 = np.min(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            print(y1,y)
            perbin = [[SortedNAve[x], SortedNSum[x]] for x in range(int(y1),int(y))]
            avg_min = min([x[0] for x in perbin])
            avg_max = max([x[0] for x in perbin])
            total_min = min([x[1] for x in perbin])
            total_max = max([x[1] for x in perbin])
            P.append([avg_min, avg_max,total_min,total_max])
        except:
            pass
        #print(perbin)
        
    x = np.linspace(1,int(trials),int(trials))
    plt.clf()
    fig = plt.figure()
    plt.style.use('fivethirtyeight') 
    plt.figure(figsize=(20,10))
    plt.xlim(0,max(data))
    plt.xlabel("No. of attempts")
    plt.ylabel("Density")
    plt.title("Attempts distribution prior to success - Failures annotated")
    splot = sns.distplot(data, hist=True, kde=True, 
             bins=int(int(trials)**rate), 
             kde_kws={'linewidth': 4})
    labelno = 0
    for p in splot.patches:
        try:
            splot.annotate(f"Average \n {P[labelno][0]:.2f} - {P[labelno][1]:.2f} \n Total  \n {P[labelno][2]} - {P[labelno][3]}",
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center',
                       xytext=(0, 9),
                       textcoords='offset points', set_fontsize = 80)
        except:
            pass
        labelno += 1
    plt.savefig(fname='plot2')
    plt.style.use("seaborn-dark")
    plt.clf()
    plt.figure(figsize=(20,10))
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    plt.grid(color='#2A3459')
    # colors = random.choice(['#99fcff', '#fb53fe', "#FFE74C", "#FFFFFF", "#6BF178", "#BF0603", "#35A7FF", "#8447FF", "#D972FF", "#F6F930", "#D2F898", "#FCFCFC", "#ED4D6E", "#E9D6EC", "#59A96A", "#9BDEAC", "#B4E7CE", "#4392F1", "#61E786", "#E3EBFF", "#38369A", "#020887"])
    colors = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(200)])
    MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    plt.plot(x, data, color = colors, marker = MARK, linestyle = random.choice(linestyle_tuple))
    if int(trials)<300:
        print(N)
        COMB = [str(Meso[i]) +" u"+ "\n" + str(N[i]) +"\n"+ "["+str(int(NStat[i][0]))+"/" + str(NStat[i][1]) +"/" + str(NStat[i][2]) + "]" for i in range(len(N))] #something wrong with N[i] currently
        for i,txt in enumerate(COMB):
            text = plt.annotate(txt, (x[i],data[i]))
            text.set_fontsize(8)
    plt.xlabel("Trials (separate) from start point")
    plt.ylabel("No of attempts until success")
    plt.title(f"{ctx.message.author}\'s starforce simulation - with pity sys.: {faith} attempts,{trials} times")
    plt.savefig(fname='plot')
    await ctx.send(file=discord.File('plot.png'))
    os.remove('plot.png')
    await ctx.send(file=discord.File('plot2.png'))
    os.remove('plot2.png')






@client.command()
@commands.has_role("Team Lucid")
async def SFIm(ctx,trials, faith, *args):  #helps to loop through the tries. This is for batches UNTIL success. HOWEVER, THIS TIME THIS IS FAILURE SAFED INSTEAD. WE SHALL TRY TO CAP BASED OFF OF TOTAL NUMBER OF FAILURES PER SESSION - FAITH.Impulsive tapping. dependent on number of falses
    SUCCESSWEWANT = len(args)
    faith = abs(int(faith))
    # faith = max(len(args),faith)  You do not do this for the impulsive run!!!
    def TrueCount(stringie, lastround):
        final = False
        n = len([x for x in stringie.split(' ') if x == 'False'])
        if len([x for x in stringie.split(' ') if x == 'True']) - len([x for x in stringie.split(' ') if x == 'False']) +int(lastround) == SUCCESSWEWANT:
            final = True
        return [final,n]
    data = []  #Number of tries it took until we got a success and stopped the trial
    N=[]  #Number of falses for the last successful set of attempts per trial
    NAve=[]  #Average number of falses and max for the entire set of attempts per trial: [Average,Maximum]
    NSum = []
    NStat = []
    Meso = []
    for i in range(int(trials)):
        mesospertrial = 0
        nall = []
        count = 1
        lasttime = 0
        checkthis, BOTTOM, meso = pitychaintilldeath0m(lasttime, faith, *args) #first run
        mesospertrial+=meso
        print(checkthis) #print the string of results for the first batch of runs
        nall.append(TrueCount(checkthis, lasttime)[1])
        finalcheck = ""
        while TrueCount(checkthis, lasttime)[0] == False:
            #print(count)
            count += 1
            lasttime += len([x for x in checkthis.split(' ') if x == 'True']) - len([x for x in checkthis.split(' ') if x == 'False'])+BOTTOM  #Update the trial number you previously were at!!!
            lasttime = max(lasttime,0)
            print(lasttime)
            finalcheck=checkthis
            checkthis, BOTTOM, mesos = pitychaintilldeath0m(lasttime, faith, *args)
            mesospertrial+=mesos
            nall.append(TrueCount(checkthis, lasttime)[1])
            #print(checkthis)
        data.append(count)
        Meso.append(round(mesospertrial, 1))
        N.append(TrueCount(finalcheck, lasttime)[1])
        NStat.append([np.mean(nall), max(nall), sum(nall)])
        NSum.append(sum(nall))
        NAve.append(np.mean(nall))
    #Making copies for the histogram 
    histdata = np.array(np.copy(data))
    histdata2 = np.array(np.copy(data))
    histN = np.array(np.copy(N))
    histNSum= np.array(np.copy(NSum))
    histNAve= np.array(np.copy(NAve))
    __,SortedNAve = (np.array(t) for t in zip(*sorted(zip(histdata, histNAve))))
    __,SortedNSum = (np.array(t) for t in zip(*sorted(zip(histdata, histNSum))))
    histdata = sorted(histdata)
    rate = 0.6
    d = max(histdata)/(int(int(trials)**rate)) #bin ranges of attempts
    print(f"Rate is {d}")
    P = []
    for i in range(int(int(trials)**rate)):
        try:
            #y = max([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            #print(i)
            #print(d*(i))
            y = np.max(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            #y1 = min([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            y1 = np.min(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            print(y1,y)
            perbin = [[SortedNAve[x], SortedNSum[x]] for x in range(int(y1),int(y))]
            avg_min = min([x[0] for x in perbin])
            avg_max = max([x[0] for x in perbin])
            total_min = min([x[1] for x in perbin])
            total_max = max([x[1] for x in perbin])
            P.append([avg_min, avg_max,total_min,total_max])
        except:
            pass
        #print(perbin)
        
    x = np.linspace(1,int(trials),int(trials))
    plt.clf()
    fig = plt.figure()
    plt.style.use('fivethirtyeight') 
    plt.figure(figsize=(20,10))
    plt.xlim(0,max(data))
    plt.xlabel("No. of attempts")
    plt.ylabel("Density")
    plt.title("Attempts distribution prior to success - Failures annotated")
    splot = sns.distplot(data, hist=True, kde=True, 
             bins=int(int(trials)**rate), 
             kde_kws={'linewidth': 4})
    labelno = 0
    for p in splot.patches:
        try:
            splot.annotate(f"Average \n {P[labelno][0]:.2f} - {P[labelno][1]:.2f} \n Total  \n {P[labelno][2]} - {P[labelno][3]}",
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center',
                       xytext=(0, 9),
                       textcoords='offset points')
        except:
            pass
        labelno += 1
    plt.savefig(fname='plot2.png')
    plt.style.use("seaborn-dark")
    plt.clf()
    plt.figure(figsize=(20,10))
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    plt.grid(color='#2A3459')
    # colors = random.choice(['#99fcff', '#fb53fe', "#FFE74C", "#FFFFFF", "#6BF178", "#BF0603", "#35A7FF", "#8447FF", "#D972FF", "#F6F930", "#D2F898", "#FCFCFC", "#ED4D6E", "#E9D6EC", "#59A96A", "#9BDEAC", "#B4E7CE", "#4392F1", "#61E786", "#E3EBFF", "#38369A", "#020887"])
    colors = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(200)])
    MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    plt.plot(x, data, color = colors, marker = MARK, linestyle = random.choice(linestyle_tuple))
    if int(trials)<300:
        COMB = [str(Meso[i]) +" u"+"\n"+str(N[i]) +"\n"+ "["+str(int(NStat[i][0]))+"/" + str(NStat[i][1]) +"/" + str(NStat[i][2]) + "]" for i in range(len(N))]
        for i,txt in enumerate(COMB):
            text = plt.annotate(txt, (x[i],data[i]))
            text.set_fontsize(8)
    plt.xlabel("Trials (separate) from start point")
    plt.ylabel("No of attempts until success")
    plt.title(f"{ctx.message.author}\'s starforce simulation - with pity sys.: {faith} attempts,{trials} times")
    plt.savefig(fname='plot')
    await ctx.send(file=discord.File('plot.png'))
    os.remove('plot.png')
    await ctx.send(file=discord.File('plot2.png'))
    os.remove('plot2.png')            

  

@client.command()
@commands.has_role("Team Lucid")
async def SFH1m(ctx,trials, faith, softcap, push, *args):  #helps to loop through the tries. This is for batches UNTIL success. HOWEVER, THIS TIME THIS IS FAILURE SAFED INSTEAD. WE SHALL TRY TO CAP BASED OFF OF TOTAL NUMBER OF FAILURES PER SESSION - FAITH.Impulsive tapping. dependent on number of falses
    SUCCESSWEWANT = len(args)
    faith = abs(int(faith))
    softcap = int(softcap)
    push = int(push)
    # faith = max(len(args),faith)  You do not do this for the impulsive run!!!
    def TrueCount(stringie, lastround):
        final = False
        n = len([x for x in stringie.split(' ') if x == 'False'])
        if len([x for x in stringie.split(' ') if x == 'True']) - len([x for x in stringie.split(' ') if x == 'False']) +int(lastround) == SUCCESSWEWANT:
            final = True
        return [final,n]
    data = []  #Number of tries it took until we got a success and stopped the trial
    N=[]  #Number of falses for the last successful set of attempts per trial
    NAve=[]  #Average number of falses and max for the entire set of attempts per trial: [Average,Maximum]
    NSum = []
    NStat = []
    Meso = []
    for i in range(int(trials)):
        mesospertrial = 0
        nall = []
        count = 1
        lasttime = 0
        checkthis, BOTTOM, meso = hybridchain1m(lasttime, softcap, faith,push, *args) #first runs
        mesospertrial+=meso
        print(checkthis) #print the string of results for the first batch of runs
        nall.append(TrueCount(checkthis, lasttime)[1])
        finalcheck=""
        while TrueCount(checkthis, lasttime)[0] == False:
            #print(count)
            count += 1
            lasttime += len([x for x in checkthis.split(' ') if x == 'True']) - len([x for x in checkthis.split(' ') if x == 'False'])+BOTTOM  #Update the trial number you previously were at!!!
            lasttime = max(lasttime,0)
            print(lasttime)
            finalcheck = checkthis
            checkthis, BOTTOM, mesos = hybridchain1m(lasttime, softcap, faith,push, *args)
            mesospertrial+=mesos
            nall.append(TrueCount(checkthis, lasttime)[1])
            #print(checkthis)
        data.append(count)
        Meso.append(round(mesospertrial, 1))
        N.append(TrueCount(finalcheck, lasttime)[1])
        NStat.append([np.mean(nall), max(nall), sum(nall)])
        NSum.append(sum(nall))
        NAve.append(np.mean(nall))
    #Making copies for the histogram 
    histdata = np.array(np.copy(data))
    histdata2 = np.array(np.copy(data))
    histN = np.array(np.copy(N))
    histNSum= np.array(np.copy(NSum))
    histNAve= np.array(np.copy(NAve))
    __,SortedNAve = (np.array(t) for t in zip(*sorted(zip(histdata, histNAve))))
    __,SortedNSum = (np.array(t) for t in zip(*sorted(zip(histdata, histNSum))))
    histdata = sorted(histdata)
    rate = 0.6
    d = max(histdata)/(int(int(trials)**rate)) #bin ranges of attempts
    print(f"Rate is {d}")
    P = []
    for i in range(int(int(trials)**rate)):
        try:
            #y = max([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            #print(i)
            #print(d*(i))
            y = np.max(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            #y1 = min([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            y1 = np.min(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            print(y1,y)
            perbin = [[SortedNAve[x], SortedNSum[x]] for x in range(int(y1),int(y))]
            avg_min = min([x[0] for x in perbin])
            avg_max = max([x[0] for x in perbin])
            total_min = min([x[1] for x in perbin])
            total_max = max([x[1] for x in perbin])
            P.append([avg_min, avg_max,total_min,total_max])
        except:
            pass
        #print(perbin)
        
    x = np.linspace(1,int(trials),int(trials))
    plt.clf()
    fig = plt.figure()
    plt.style.use('fivethirtyeight') 
    plt.figure(figsize=(20,10))
    plt.xlim(0,max(data))
    plt.xlabel("No. of attempts")
    plt.ylabel("Density")
    plt.title("Attempts distribution prior to success - Failures annotated")
    splot = sns.distplot(data, hist=True, kde=True, 
             bins=int(int(trials)**rate), 
             kde_kws={'linewidth': 4})
    labelno = 0
    for p in splot.patches:
        try:
            splot.annotate(f"Average \n {P[labelno][0]:.2f} - {P[labelno][1]:.2f} \n Total  \n {P[labelno][2]} - {P[labelno][3]}",
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center',
                       xytext=(0, 9),
                       textcoords='offset points')
        except:
            pass
        labelno += 1
    plt.savefig(fname='plot2')
    plt.style.use("seaborn-dark")
    plt.clf()
    plt.figure(figsize=(20,10))
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    plt.grid(color='#2A3459')
    # colors = random.choice(['#99fcff', '#fb53fe', "#FFE74C", "#FFFFFF", "#6BF178", "#BF0603", "#35A7FF", "#8447FF", "#D972FF", "#F6F930", "#D2F898", "#FCFCFC", "#ED4D6E", "#E9D6EC", "#59A96A", "#9BDEAC", "#B4E7CE", "#4392F1", "#61E786", "#E3EBFF", "#38369A", "#020887"])
    colors = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(200)])
    MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    plt.plot(x, data, color = colors, marker = MARK, linestyle = random.choice(linestyle_tuple))
    if int(trials)<300:
        COMB = [str(Meso[i]) +" u"+"\n"+str(N[i]) +"\n"+ "["+str(int(NStat[i][0]))+"/" + str(NStat[i][1]) +"/" + str(NStat[i][2]) + "]" for i in range(len(N))]
        for i,txt in enumerate(COMB):
            text = plt.annotate(txt, (x[i],data[i]))
            text.set_fontsize(8)
    plt.xlabel("Trials (separate) from start point")
    plt.ylabel("No of attempts until success")
    plt.title(f"{ctx.message.author}\'s starforce simulation - with pity sys.: {faith} attempts,{trials} times")
    plt.savefig(fname='plot')
    await ctx.send(file=discord.File('plot.png'))
    os.remove('plot.png')
    await ctx.send(file=discord.File('plot2.png'))
    os.remove('plot2.png')            

    



@client.command()
@commands.has_role("Team Lucid")
async def SFH2m(ctx,trials, faith, softcap, push, *args):  #helps to loop through the tries. This is for batches UNTIL success. HOWEVER, THIS TIME THIS IS FAILURE SAFED INSTEAD. WE SHALL TRY TO CAP BASED OFF OF TOTAL NUMBER OF FAILURES PER SESSION - FAITH.Impulsive tapping. dependent on number of falses
    SUCCESSWEWANT = len(args)
    faith = abs(int(faith))
    softcap = int(softcap)
    push = int(push)
    # faith = max(len(args),faith)  You do not do this for the impulsive run!!!
    def TrueCount(stringie, lastround):
        final = False
        n = len([x for x in stringie.split(' ') if x == 'False'])
        if len([x for x in stringie.split(' ') if x == 'True']) - len([x for x in stringie.split(' ') if x == 'False']) +int(lastround) == SUCCESSWEWANT:
            final = True
        return [final,n]
    data = []  #Number of tries it took until we got a success and stopped the trial
    N=[]  #Number of falses for the last successful set of attempts per trial
    NAve=[]  #Average number of falses and max for the entire set of attempts per trial: [Average,Maximum]
    NSum = []
    NStat = []
    Meso = []
    for i in range(int(trials)):
        mesospertrial = 0
        nall = []
        count = 1
        lasttime = 0
        checkthis, BOTTOM, meso = hybridchain2m(lasttime, softcap, faith,push, *args) #first run
        mesospertrial+=meso
        print(checkthis) #print the string of results for the first batch of runs
        nall.append(TrueCount(checkthis, lasttime)[1])
        finalcheck=""
        while TrueCount(checkthis, lasttime)[0] == False:
            #print(count)
            count += 1
            lasttime += len([x for x in checkthis.split(' ') if x == 'True']) - len([x for x in checkthis.split(' ') if x == 'False'])+BOTTOM  #Update the trial number you previously were at!!!
            lasttime = max(lasttime,0)
            print(lasttime)
            finalcheck=checkthis
            checkthis, BOTTOM, mesos = hybridchain2m(lasttime, softcap, faith,push, *args)
            mesospertrial+=mesos
            nall.append(TrueCount(checkthis, lasttime)[1])
            #print(checkthis)
        data.append(count)
        Meso.append(round(mesospertrial, 1))
        N.append(TrueCount(finalcheck, lasttime)[1])
        NStat.append([np.mean(nall), max(nall), sum(nall)])
        NSum.append(sum(nall))
        NAve.append(np.mean(nall))
    #Making copies for the histogram 
    histdata = np.array(np.copy(data))
    histdata2 = np.array(np.copy(data))
    histN = np.array(np.copy(N))
    histNSum= np.array(np.copy(NSum))
    histNAve= np.array(np.copy(NAve))
    __,SortedNAve = (np.array(t) for t in zip(*sorted(zip(histdata, histNAve))))
    __,SortedNSum = (np.array(t) for t in zip(*sorted(zip(histdata, histNSum))))
    histdata = sorted(histdata)
    rate = 0.6
    d = max(histdata)/(int(int(trials)**rate)) #bin ranges of attempts
    print(f"Rate is {d}")
    P = []
    for i in range(int(int(trials)**rate)):
        try:
            #y = max([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            #print(i)
            #print(d*(i))
            y = np.max(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            #y1 = min([histdata.index(x) for x in histdata if x<=d*(i+1) if x>d*(i)])
            y1 = np.min(np.where(np.logical_and(histdata>d*(i), histdata<=d*(i+1))))
            print(y1,y)
            perbin = [[SortedNAve[x], SortedNSum[x]] for x in range(int(y1),int(y))]
            avg_min = min([x[0] for x in perbin])
            avg_max = max([x[0] for x in perbin])
            total_min = min([x[1] for x in perbin])
            total_max = max([x[1] for x in perbin])
            P.append([avg_min, avg_max,total_min,total_max])
        except:
            pass
        #print(perbin)
        
    x = np.linspace(1,int(trials),int(trials))
    plt.clf()
    fig = plt.figure()
    plt.style.use('fivethirtyeight') 
    plt.figure(figsize=(20,10))
    plt.xlim(0,max(data))
    plt.xlabel("No. of attempts")
    plt.ylabel("Density")
    plt.title("Attempts distribution prior to success - Failures annotated")
    splot = sns.distplot(data, hist=True, kde=True, 
             bins=int(int(trials)**rate), 
             kde_kws={'linewidth': 4})
    labelno = 0
    for p in splot.patches:
        try:
            splot.annotate(f"Average \n {P[labelno][0]:.2f} - {P[labelno][1]:.2f} \n Total  \n {P[labelno][2]} - {P[labelno][3]}",
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center',
                       xytext=(0, 9),
                       textcoords='offset points')
        except:
            pass
        labelno += 1
    plt.savefig(fname='plot2')
    plt.style.use("seaborn-dark")
    plt.clf()
    plt.figure(figsize=(20,10))
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    plt.grid(color='#2A3459')
    # colors = random.choice(['#99fcff', '#fb53fe', "#FFE74C", "#FFFFFF", "#6BF178", "#BF0603", "#35A7FF", "#8447FF", "#D972FF", "#F6F930", "#D2F898", "#FCFCFC", "#ED4D6E", "#E9D6EC", "#59A96A", "#9BDEAC", "#B4E7CE", "#4392F1", "#61E786", "#E3EBFF", "#38369A", "#020887"])
    colors = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(200)])
    MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    plt.plot(x, data, color = colors, marker = MARK, linestyle = random.choice(linestyle_tuple))
    if int(trials)<300:
        COMB = [str(Meso[i]) +" u"+"\n"+str(N[i]) +"\n"+ "["+str(int(NStat[i][0]))+"/" + str(NStat[i][1]) +"/" + str(NStat[i][2]) + "]" for i in range(len(N))]
        for i,txt in enumerate(COMB):
            text = plt.annotate(txt, (x[i],data[i]))
            text.set_fontsize(8)
    plt.xlabel("Trials (separate) from start point")
    plt.ylabel("No of attempts until success")
    plt.title(f"{ctx.message.author}\'s starforce simulation - with pity sys.: {faith} attempts,{trials} times")
    plt.savefig(fname='plot')
    await ctx.send(file=discord.File('plot.png'))
    os.remove('plot.png')
    await ctx.send(file=discord.File('plot2.png'))
    os.remove('plot2.png')            

    




@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        return


    if client.user.mentioned_in(message):
        if message.content.lower().__contains__('hi'):
            await message.channel.send(f"{message.author.mention}``, boop boop?``")
            time.sleep(1)
            await message.channel.send("``:>``")
        else:
            await message.channel.send("I am available at, ☆ ;)")


    if 'sfcost' in message.content.lower():
        def cost(WORLD, level1, eq):
            level1 = int(level1)
            eq = int(eq)
            if WORLD.lower() == "kms" or WORLD.lower() == "maplesea" or WORLD.lower() == "jms" or WORLD.lower() == "tmsreboot":
                if level1<=9:
                    return (100*round(eq**3*((level1+1)/2500)+10))
                elif level1<=14:
                    return (100*round(eq**3*((level1+1)**2.7/40000)+10))
                elif level1<=24:
                    return (100*round(eq**3*((level1+1)**2.7/20000)+10))
                else:
                    return 0
            elif WORLD.lower() == "gms":
                if level1<=9:
                    return (100*round(eq**3*((level1+1)/2500)+10))
                elif level1<=14:
                    return (100*round(eq**3*((level1+1)**2.7/40000)+10))
                elif level1<=17:
                    return (100*round(0.78*round(eq**3*((level1+1)**2.7/12000))+7.8))
                elif level1<=19:
                    return (100*round(0.78*round(eq**3*((level1+1)**2.7/11000))+7.8))   
                elif level1<=24:
                    return (100*round(0.78*round(eq**3*((level1+1)**2.7/10000))+7.8))                                     
                else:
                    return 0  
            elif WORLD.lower() == "tms":        
                if level1<=9:
                    return (100*round(eq**3*((level1+1)/2500)+10))
                elif level1<=10:
                    return (100*round(eq**3*((level1+1)**2.7/20000)+10))
                elif level1<=14:
                    return (100*round(3*eq**3*((level1+1)**2.7/20000)+10))  
                elif level1<=19:
                    return (100*round(eq**3*((level1+1)**2.7/5000)+10))                                        
                elif level1<=24:
                    return (100*round(eq**3*((level1+1)**2.7/4000)+10))
                else:
                    return 0      
            else:
                return "You fucked up"          
        def check(m):
            return m.content == m.content and m.channel == message.channel
        await channel.send("``What world? <kms/gms/tms/msea/jms/tmsreboot>``")       
        world = await client.wait_for('message',check = check, timeout = 40.0)  
        world = str(world.content)   
        setofworlds = ["kms", "gms", "tms", "msea", "jms", "tmsreboot"]
        if world.lower() in setofworlds:
            pass
        else:
            world = "gms"
        await channel.send("``Between what starforce levels and what equipment level? Separate the numbers with a space <starforce level 1> <'' 2> <equipment level>:``")        
        morecontent = await client.wait_for('message',check = check, timeout = 40.0)
        ans1, ans2, EQ = morecontent.content.split(" ")
        ans1 = int(ans1)
        ans2 = int(ans2)
        EQ = int(EQ)
        finalstring = ""
        costcal = 0
        for i in range(ans2-ans1):
            C = round(cost(world, ans1+i, EQ)*10**(-6), 2)
            costcal+=C
            finalstring += f"{C} "
        await channel.send(f"``` Individual costs are : {finalstring} ```")
        await channel.send(f"``` Total cost is : {costcal} ```")


    if message.content.startswith('wf.wikia'):
        ctx = message.content[9:]
        ctx = ctx.replace(" ", "+")

        animalswikia = f'https://warframe.fandom.com/wiki/Special:Search?query={ctx}'

        print(animalswikia)

        Req = Request(animalswikia)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')
        soup.find_all('a',{ "class", "result-link"})[3]['href']
        if len(soup.find_all('a',{ "class", "result-link"})) >= 10:
            length = 10
        else:
            length = len(soup.find_all('a',{ "class", "result-link"}))

        list = []
        for i in range(length):
            list.append(soup.find_all('a',{ "class", "result-link"})[i]['href'])
            alpha = soup.find_all('li', {'class', 'result'})[i].a.text
            print(i,alpha)
            await channel.send(f'```{alpha}```')

        await channel.send("``Please choose one of the provided links: 0, 1, 2 etc ...``")
        def check(m):
            return m.content == m.content and m.channel == message.channel
        morecontent = await client.wait_for('message',check = check, timeout = 40.0)
        ans = int(morecontent.content)
        eligible = []
        for i in range(len(soup.find_all('a',{ "class", "result-link"}))):
            eligible.append(i)


#Going into the link perhaps
        if ans in eligible:
            await channel.send((soup.find_all('li', {'class', 'result'})[ans].a['href']))   #Post link for now
            animalswikia = soup.find_all('li', {'class', 'result'})[ans].a['href']
            Req = Request(animalswikia)
            uClient = urlopen(Req)
            soup = BeautifulSoup(uClient.read(), 'html5lib')

            isthereatable = len(soup.find_all('aside'))
            if isthereatable == 1:
                img = soup.aside.a['href']
                try:
                    for i in range(len(soup.aside.find_all('div', {'class','pi-item pi-data pi-item-spacing pi-border-color'}))):
                        thing = soup.aside.find_all('div', {'class','pi-item pi-data pi-item-spacing pi-border-color'})[i].div.text
                        Stat = soup.aside.find_all('div', {'class','pi-item pi-data pi-item-spacing pi-border-color'})[i].find_all('a')[-1].text
                        await channel.send(f'```{Stat} \n {thing} ```')
                except:
                    pass



    if len([x for x in [message.content.lower().__contains__(i) for i in shock] if x==True])>.1:
        choices = ['へ( ʘ͡ ₒ ʘ͡ )╮/\╱\ ', 'ಠnಠ', '( ಠ ಠ )', '/╲/\〳 ᴼᴼ ౪ ᴼᴼ 〵/\╱\ ', 'へ(❍∠❍)へ', '/╲/\╭ºooooº╮/\╱\ ', '/╲/\╭( . ರರ ل ರರ . )╮/\╱\ ' ]
        await channel.send(random.choice(choices))








    await client.process_commands(message)

client.run('###YOUR TOKEN HERE###')