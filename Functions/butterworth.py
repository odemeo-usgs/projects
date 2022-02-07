from scipy import signal

def butterworth(data, samp_rate, order, window):
    # data = u or v component
    # samp_rate = sampling rate in seconds
    # order = filter order
    # window = filter window in hours
    cutOff = 1/(window*3600)
    nyq = (1/samp_rate)/2
    N  = order    
    fc = cutOff / nyq 
    b, a = signal.butter(N, fc)
    filt_data = signal.filtfilt(b, a, data)
    return filt_data