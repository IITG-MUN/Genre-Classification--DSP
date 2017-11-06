'''this libraray has verious modules to compute various freawquncy domain features : spectral centroid , spectral roll off '''
import math
import cmath
import numpy as np

#fucnction to return centroid
#input : arrya of complex numbers ,array of frequencies, size
#output : the centroid frequency

def centroid(dft,size):
    pi=math.pi
    freq=np.array([(2*pi*n)/2*size for n in range(size)]) # the array of frequencies
    amp=np.array([math.sqrt(x.real**2+x.imag**2) for x in dft])
    out=np.sum(freq*amp)/np.sum(amp)
    return out

#the
def dft(frame, size):
    if(size==2):

        return np.reshape(np.array([frame[0]+frame[1],frame[0]-frame[1]]),(2,1))
    else:
        frame_even=[frame[i*2] for i in range(size/2)]
        frame_odd=[frame[i*2+1] for i in range(size/2)]
        #print frame_even,frame_odd
        w_k_N=np.array([[cmath.exp(-1j*((cmath.pi*2*k)/float(size)))] for k in range(size)])
        G=np.concatenate((dft(frame_even,size/2,),dft(frame_even,size/2)),axis=0)
        H= np.concatenate((dft(frame_odd, size / 2), dft(frame_odd, size / 2)), axis=0)
        #print size
        #print G
        #print H
        return G+w_k_N*H
#dft(np.reshape(dft(np.array([1,0,-1,0]),4),(1,4))[0],4) applying dft twic will give inverse fourier transform
print dft(np.array([1,-1]),2)