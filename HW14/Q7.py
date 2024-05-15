import matplotlib.pyplot as plt
import numpy as np
import csv

h = [
    0.005347333847943900,
    0.004546014530102697,
    0.003592883372736597,
    0.002503789906745420,
    0.001298414615133528,
    -0.000000000000000002,
    -0.001364999980012160,
    -0.002767346739034416,
    -0.004175513108856049,
    -0.005556239981236629,
    -0.006875143518785017,
    -0.008097361682795132,
    -0.009188227819777815,
    -0.010113958281703432,
    -0.010842340547161138,
    -0.011343408075448463,
    -0.011590088171103284,
    -0.011558809464803921,
    -0.011230056224172886,
    -0.010588857585193640,
    -0.009625200926299022,
    -0.008334359971854942,
    -0.006717129783811907,
    -0.004779962549241264,
    -0.002534999962879733,
    0.000000000000000002,
    0.002801842064235499,
    0.005842176449072653,
    0.009087881472216095,
    0.012501539957782411,
    0.016042001543831706,
    0.019665021229645332,
    0.023323962927128305,
    0.026970555417875814,
    0.030555686996545022,
    0.034030224226345392,
    0.037345839662443925,
    0.040455833126813730,
    0.043315931150381126,
    0.045885049535839106,
    0.048126004631495106,
    0.050006159831129639,
    0.051497995009224577,
    0.052579588041653857,
    0.053234999220474449,
    0.053454551214750033,
    0.053234999220474449,
    0.052579588041653857,
    0.051497995009224577,
    0.050006159831129639,
    0.048126004631495106,
    0.045885049535839106,
    0.043315931150381126,
    0.040455833126813730,
    0.037345839662443925,
    0.034030224226345392,
    0.030555686996545022,
    0.026970555417875814,
    0.023323962927128305,
    0.019665021229645332,
    0.016042001543831706,
    0.012501539957782411,
    0.009087881472216095,
    0.005842176449072653,
    0.002801842064235499,
    0.000000000000000002,
    -0.002534999962879733,
    -0.004779962549241264,
    -0.006717129783811907,
    -0.008334359971854942,
    -0.009625200926299022,
    -0.010588857585193640,
    -0.011230056224172886,
    -0.011558809464803921,
    -0.011590088171103284,
    -0.011343408075448463,
    -0.010842340547161138,
    -0.010113958281703432,
    -0.009188227819777815,
    -0.008097361682795132,
    -0.006875143518785017,
    -0.005556239981236629,
    -0.004175513108856049,
    -0.002767346739034416,
    -0.001364999980012160,
    -0.000000000000000002,
    0.001298414615133528,
    0.002503789906745420,
    0.003592883372736597,
    0.004546014530102697,
    0.005347333847943900,
]




def myfft(data,time):
    
    y = data # the data to make the fft from
    n = len(y) # length of the signal
    Fs = n/time[-1] # sample rate
    k = np.arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(int(n/2))] # one side frequency range
    Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[range(int(n/2))]

    return abs(Y),frq

def myFIR(data,coef):
    mafdata = []
    window_size = len(coef)

    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]

        average = np.sum(np.multiply(window,coef))
        mafdata = np.append([mafdata],[average])
        print(i)
    mafdata = np.append(np.zeros(window_size-1),[mafdata])
    return mafdata


t = [] # column 0
data1 = [] # column 1


with open('C:/Users/59201/Desktop/NU/2024 Spring/ME433/ME433_2024SP_Homeworks/HW14/sigD.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
            # read the rows 1 one by one
            t.append(float(row[0])) # leftmost column
            data1.append(float(row[1])) # second column

data2 =  myFIR(data1,h)

fig, ax1 = plt.subplots(1, 1)
ax1.plot(t,data1,'black')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax1.plot(t,data2,'red')
ax1.set_title('sigD,Cutoff = 10Hz,Transition = 10Hz, method = Rectangular')


plt.show()