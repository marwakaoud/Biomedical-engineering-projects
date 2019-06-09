import matplotlib.pyplot as plt
import  numpy as np


# derivative
def ECG_analysis (data):

  samples = []
  for line in range(0, 2001):  # 2000 samples only from 0 t0 1999
    line = data.readline()
    samples.append(line)

  T = 1 / 512
  factors =[-1,-2,0,2,1]
  n=0
  Sample_d = 0
  sqaured_samples=[]
  for n in range(1,len(samples)-3):
    #line =data.readline()
    sample_d = 0
    for i in range(-2,3):
        sample_d=float(sample_d+(i*float(samples[(n+1)+factors[i+2]]))) #summation for each sample
    sample_d=sample_d*1/(8*T)

    #squaring

    sqaured_samples.append(sample_d*sample_d)
    #output.write(str(sample_d))

###############################
#print((sqaured_samples))

##smoothing
  sample_s=0
  smoothed_samples=[]
  for w in range (30,len(sqaured_samples)):
    sample_s = 0
    for i in range (1,32):
        sample_s = float(sample_s + sqaured_samples[(w  - 31 + i)])

    sample_s=sample_s*(1/31)
    smoothed_samples.append(sample_s)
 #############
  x=np.arange(0,len(smoothed_samples))
  plt.plot(x,smoothed_samples)
  plt.title("smoothed signal")
  plt.xlabel("samples")
  plt.show()
  return smoothed_samples

##auto correlation
def corelation (smoothed_samples):

 A=0
 autocorrelated_signals=[]
 for m in range (0,len(smoothed_samples)):
    A=0
    for i in range(m,len(smoothed_samples)):
      A=A+smoothed_samples[i]*smoothed_samples[i-m]
    autocorrelated_signals.append(A)
##############
 return autocorrelated_signals

def main():
    data1 = open("Data1.txt", "r")
    #samples = []
    #for line in range(0, 2001):  # 2000 samples only from 0 t0 1999
       # line = data.readline()
        #samples.append(line)
    T = 1 / 512
    smoothed_samples=ECG_analysis(data1)
    autocorrelated_signals=corelation(smoothed_samples)
    y = np.arange(0, len(autocorrelated_signals))
    plt.plot(y, autocorrelated_signals)
    plt.xlabel("lag")
    plt.title("Auto Correlation")
    plt.show()

    data2 =open("Data2.txt", "r")
    smoothed_samples2 = ECG_analysis(data2)
    autocorrelated_signals = corelation(smoothed_samples2)
    y = np.arange(0, len(autocorrelated_signals))
    plt.plot(y, autocorrelated_signals)
    plt.xlabel("lag")
    plt.title("Auto Correlation")
    plt.show()
if __name__ == '__main__':
    main()


def atrial_fabrillation (autocorrelated_signal,y):
    x=np.arange(400,500) #for normal person the peak of auto correlation occurs around 450 lag
    threshould = 1
    for i in range(50,500):

      if autocorrelated_signal[i]>threshould :
          pos=y[i]
          max=autocorrelated_signal[i]
          diff=autocorrelated_signal[i]-threshould
    threshould2=100
    if pos <x[0]:
        diff2=float(x[0]-pos)
        if(diff>threshoud2):
            print('patient has atrial fabrillation')
    elif pos >x[100]:
         diff2=float(pos-x[100])
         if(diff>threshould2):
            print('patient has atrial fabrillation')
    else:
     print('patient has no atrial fabrillation')

















