__author__ = 'haseeb'
import os
from titmit import TimitFileReader
from matplotlib import pyplot
import matplotlib.cm as cm

train_file_list = "/home/haseeb/tmp/speech/scripts/train_file_list.txt"
test_file_list = "/home/haseeb/tmp/speech/scripts/test_file_list.txt"

converted_train_file_dir = "/home/haseeb/tmp/speech/converted/train"
converted_test_file_dir = "/home/haseeb/tmp/speech/converted/test"

train_file_list_file = open(train_file_list, 'r')
for file_path in train_file_list_file:
    file_path = file_path[:-1]
    reader = TimitFileReader(file_path)
    phones = reader.get_phones()
    phone_id = 0
    for phone in phones:
        output_file_dir = converted_train_file_dir + "/" + phone.get_label()
        if not os.path.exists(output_file_dir):
            os.makedirs(output_file_dir)
        output_file_path = output_file_dir + "/" + reader.get_utterance_id() + str(phone_id) + ".png"
        pyplot.figure()
        pyplot.specgram(phone.get_frames())
        pyplot.savefig(output_file_path, bbox_inches='tight', pad_inches=0)
        pyplot.close()
        phone_id += 1