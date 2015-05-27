__author__ = 'haseeb'
from scikits.audiolab import Sndfile
import numpy as np
from matplotlib import pyplot

def test_read_wave():
    f = Sndfile("../fcjf0/sa1.wav", 'r')
    data = f.read_frames(46797)
    data_arr = np.array(data)
    #print data_arr
    pyplot.figure()
    pyplot.specgram(data_arr)
    pyplot.show()

if __name__ == '__main__':
    test_read_wave()
