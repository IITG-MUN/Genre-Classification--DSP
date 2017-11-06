'''this is code to test various funtions for extracting features'''

import numpy as np
import scipy.io.wavfile as sp
import matplotlib.pyplot as plt
import zcr

'''the below code give a smalll testing of zcr library'''
'''frame=[-1,1,1,-1,-1,1]
print zcr.zero_crossing(frame,len(frame),6)'''

file_name="C:\\Users\\deekshisth raya\\Desktop\\Genere classification\\classical.00000.wav"
rate,data=sp.read(file_name)



