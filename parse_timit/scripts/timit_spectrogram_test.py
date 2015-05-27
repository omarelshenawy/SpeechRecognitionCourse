__author__ = 'haseeb'
import os
from titmit import TimitFileReader
from matplotlib import pyplot
import matplotlib.cm as cm
import numpy as np

train_file_list = "/home/haseeb/tmp/speech/scripts/train_file_list.txt"
test_file_list = "/home/haseeb/tmp/speech/scripts/test_file_list.txt"

converted_train_file_dir = "/home/haseeb/tmp/speech/converted/train"
converted_test_file_dir = "/home/haseeb/tmp/speech/converted/test"

train_file_list_file = open(test_file_list, 'r')
for file_path in train_file_list_file:
    file_path = file_path[:-1]
    reader = TimitFileReader(file_path)
    phones = reader.get_phones()
    phone_id = 0
    for phone in phones:
        output_file_dir = converted_test_file_dir + "/" + phone.get_label()
        if not os.path.exists(output_file_dir):
            os.makedirs(output_file_dir)
        output_file_path = output_file_dir + "/" + reader.get_utterance_id() + str(phone_id) + ".png"
        fig = pyplot.figure()
        ax = fig.add_subplot(111)
        pyplot.axis('off')
        #ax.specgram(phone.get_frames(), cmap=cm.Greys, aspect='auto', interpolation='nearest', origin='lower')
        (spectrum, freqs, t, im) = ax.specgram(phone.get_frames(), cmap=cm.Greys, aspect='auto')
        print im.get_extent()
        extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        #fig.savefig(output_file_path, bbox_inches=extent)
        fig.savefig(output_file_path, bbox_inches=extent)
        pyplot.close()
        phone_id += 1