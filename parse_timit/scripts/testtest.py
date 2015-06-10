__author__ = 'haseeb'
import os
from titmit import TimitFileReader
from matplotlib import pyplot
import matplotlib.cm as cm
import numpy as np

test_file_list = "/home/haseeb/tmp/parse_timit/scripts/test_file_list_list.txt"
converted_test_file_dir = "/home/haseeb/tmp/parse_timit/converted/test"

conv_test_list = "/home/haseeb/tmp/parse_timit/converted/test_list.txt"

phones_list = ["aa","ae","ah","ao","aw","ax","ax-h","axr","ay","b","bcl","ch","d","dcl","dh","dx","eh","el","em","en","epi","eng","er","ey","f","g","gcl","h#","hh","hv","ih","ix","iy","jh","k","kcl","l","m","n","ng","nx","ow","oy","p","pau","pcl","q","r","s","sh","t","tcl","th","uh","uw","ux","v","w","y","z","zh"]

Fs=16000
NFFT=128
noverlap=64

train_file_list_file = open(test_file_list, 'r')
conv_test_list_file = open(conv_test_list, 'w')
for file_path in train_file_list_file:
    file_path = file_path[:-1]
    reader = TimitFileReader(file_path)
    phones = reader.get_phones()
    phone_id = 0
    print np.shape(phones)

