import numpy as np

# Make sure that caffe is on the python path:
caffe_root = '../'  # this file is expected to be in {caffe_root}/examples
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

# Set the right path to your model definition file, pretrained model weights,
# and the image you would like to classify.
testfile = "/home/ubuntu/test.txt"
MODEL_FILE = '/home/ubuntu/deploy.prototxt'
PRETRAINED = '/home/ubuntu/alexnet_2_1.caffemodel'
IMAGE_FILE = '/mnt/2_regions_timit/test/dr1/aa/si153929.wav.spec.png'

import os
if not os.path.isfile(PRETRAINED):
    print("Downloading pre-trained CaffeNet model...")

caffe.set_mode_gpu()
blob = caffe.proto.caffe_pb2.BlobProto()
data = open('/mnt/.digits/jobs/20150531-151831-4c0f/mean.binaryproto', 'rb').read()
blob.ParseFromString(data)
arr = np.array(caffe.io.blobproto_to_array(blob))
out = arr[0]
net = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       mean=out.mean(1).mean(1),
                       raw_scale=255,
                       image_dims=(128, 128))
testfiles = open(testfile, 'r')
error = 0
for line in testfiles:
    (imagefile, target) = line.split(" ")
    input_image = caffe.io.load_image(imagefile, color=False)
    prediction = net.predict([input_image])  # predict takes any number of images, and formats them for the Caffe net automatically
    if prediction[0].argmax() != target:
        error += 1


print error/len(testfiles)