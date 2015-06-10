__author__ = 'haseeb'
import os
from titmit import TimitFileReader
from subprocess import check_call
import sys

#train_file_list = "/home/haseeb/tmp/parse_timit/scripts/train_file_list.txt"
#converted_train_file_dir = "/home/haseeb/tmp/parse_timit/converted/train"
#conv_train_list = "/home/haseeb/tmp/parse_timit/converted/train_list.txt"
train_file_list = sys.argv[1]
converted_train_file_dir = sys.argv[2]
conv_train_list = converted_train_file_dir + "/" + "data.txt"

phones_list = ["aa","ae","ah","ao","aw","ax","ax-h","axr","ay","b","bcl","ch","d","dcl","dh","dx","eh","el","em","en","eng","epi","er","ey","f","g","gcl","h#","hh","hv","ih","ix","iy","jh","k","kcl","l","m","n","ng","nx","ow","oy","p","pau","pcl","q","r","s","sh","t","tcl","th","uh","uw","ux","v","w","y","z","zh"]

Fs=16000
NFFT=1024
noverlap=64

print ">>>>> " + train_file_list

train_file_list_file = open(train_file_list, 'r')
conv_train_list_file = open(conv_train_list, 'w')
for file_path in train_file_list_file:
    file_path = file_path[:-1]
    reader = TimitFileReader(file_path)
    phones = reader.get_phones()
    phone_id = 0
    for phone in phones:
        output_file_dir = converted_train_file_dir + "/" + phone.get_label()
        if not os.path.exists(output_file_dir):
            os.makedirs(output_file_dir)
        wav_output_file_path = output_file_dir + "/" +reader.get_utterance_id() + str(phone_id) + ".wav"
        reader.save_wav(wav_output_file_path, phone.get_frames(), Fs)

        # ruby audio-fft.rb /home/haseeb/tmp/parse_timit/scripts/phones_wav/w27.wav
        check_call(["ruby", "audio-fft.rb", wav_output_file_path])

        conv_train_list_file.write(wav_output_file_path + " " + str(phones_list.index(phone.get_label())))
        conv_train_list_file.write("\n")
        phone_id += 1

conv_train_list_file.close()
