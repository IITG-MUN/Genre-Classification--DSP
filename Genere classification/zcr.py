'''This fucntion returns zcr of an audio frame'''
import numpy as np
import scipy.io.wavfile as sp
import matplotlib.pyplot as plt

'''this returns zcr of the audio frame'''
def zero_crossing(frame,size,duration):
    change=0                         #counts the zero crossings
    for i in range(size-1):
        if(frame[i]*frame[i+1]<0):
            change+=1
    return float(change)/float(duration)   # returns the number of zero crossing


