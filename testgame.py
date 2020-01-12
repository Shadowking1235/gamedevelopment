import wave

import inline as inline
import matplotlib
import numpy as np
from scipy.fftpack import fft
matplotlib, inline
import matplotlib.pyplot as plt

wav = wave.open("sample.wav", mode="r")
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
content = wav.readframes(nframes)

types = { 1: np.int8, 2: np.int16, 4: np.int32 }
samples = np.fromstring(content, dtype=types[sampwidth])
N=512 #Размер БПФ
hissing = 14900
vowels = 16900
win=np.hanning(N) # Сгенерируем временное окно 
k = np.arange(N)
T = float(N)/framerate
frq = k/T # Полный диапазон (период) спектра
frq = frq[0:int(N/2)] #Основная полоса частот (по Котельникову) 
f, ax = plt.subplots(2, 2,figsize=(13, 6))
x=np.arange(hissing,hissing+N)    #Номера отсчетов сигнала в текущем интервале анализа
y=win*samples[hissing:hissing+N] #Взвешанная копия интервала анализа
Y=abs(fft(y)/N)   #Вычисление БПФ и нормализация
Y1=20*np.log10(Y)
ax[0,0].plot(x, samples[hissing:hissing+N])
ax[0,1].plot(frq, Y1[0:int(N/2)],'r') 
x=np.arange(vowels,vowels+N)    #Номера отсчетов сигнала в текущем интервале анализа
y=win*samples[vowels:vowels+N] #Взвешанная копия интервала анализа
Y=abs(fft(y)/N)   #Вычисление БПФ и нормализация
Y1=20*np.log10(Y)
ax[1,0].plot(x, samples[vowels:vowels+N])
ax[1,1].plot(frq, Y1[0:int(N/2)],'r')

