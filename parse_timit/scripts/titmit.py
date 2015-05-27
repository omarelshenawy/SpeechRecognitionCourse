__author__ = 'haseeb'
from scikits.audiolab import Sndfile
from scikits.audiolab import wavread
import numpy as np
import sys

class Phone():
    def __init__(self, label, frames):
        self.label = label
        self.frames = frames

    def get_label(self):
        return self.label

    def get_frames(self):
        return self.frames


class TimitFileReader():
    def __init__(self, file_path):
        self.wav_file_path = file_path
        self.file = self.open_wav_file()
        self.wav_file_ext = ".wav"
        self.txt_file_ext = ".txt"
        self.word_file_ext = ".wrd"
        self.phone_file_ext = ".phn"

    def open_wav_file(self):
        return Sndfile(self.wav_file_path, 'r')

    def get_utterance_id(self):
        return self.wav_file_path.split("/")[-1].replace(self.wav_file_ext, "")

    def get_number_of_frames(self):
        """
        it reads the total number of frames from the .txt file
        :return: total number of frames
        """
        txt_file_path = self.wav_file_path.replace(self.wav_file_ext, self.txt_file_ext)
        txt_file = open(txt_file_path, 'r')
        return int(txt_file.readline().split()[1])

    def get_all_frames(self):
        try:
            frames = np.array(self.file.read_frames(self.get_number_of_frames()))
        except RuntimeError:
            print self.wav_file_path
            print sys.exc_info()[1]
            correct_frames_number = int(str(sys.exc_info()[1]).split(",")[1].replace("read", ""))
            print correct_frames_number
            self.file.close()
            self.file = self.open_wav_file()
            frames = np.array(self.file.read_frames(correct_frames_number))
        return frames

    def get_phones(self):
        phone_file_path = self.wav_file_path.replace(self.wav_file_ext, self.phone_file_ext)
        phone_file = open(phone_file_path, 'r')
        all_frames = self.get_all_frames()
        phones = []
        for line in phone_file:
            line_split = line.split()
            begin_sample = int(line_split[0])
            end_sample = int(line_split[1])
            phone_label = line_split[2]
            phones.append(Phone(phone_label, all_frames[begin_sample:end_sample+1]))
        return phones


if __name__ == '__main__':
    reader = TimitFileReader("../fcjf0/sa1.wav")
    phones = reader.get_phones()
    print len(phones)
    for phone in phones:
        print phone.get_label() + " " + str(phone.get_frames())