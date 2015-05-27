# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

## Play with the trained speech recognition model from words_net.prototxt: numbers_iter_5000.caffemodel
## Notebook might need minor adjustments on your machine

# <codecell>

# Make sure that caffe is on the python path:
# this file is expected to be in {caffe_root}/examples/speech

caffe_root = '/home/omar/Documents/KTH/1.4/Speech/digits-1.0/caffe/' 
import sys
sys.path.insert(0, caffe_root + 'python')
sys.path.insert(0, caffe_root + 'python/caffe')
import caffe
import classifier

model="numbers_deploy.prototxt"
weights="numbers_iter_101.caffemodel"
# net = caffe.Net(model,weights)
net = classifier.Classifier(model, weights, raw_scale=255.0)
#net.set_phase_test()
#net.set_raw_scale('data', 255.0)
#net.set_mode_gpu()

# Prime a second net with some numbers weights
# model2=caffe_root+"/examples/speech/numbers_net.prototxt30"
# copy_net = caffe.Net(model2)
# net.share_with(copy_net)
# copy_net.save(caffe_root+"test.net") YAY! OK!!

# some reflections:
# help(net)
# print net.params
# print net.layers LayerVec
# print net.layers[0] #PyLayer __reduce__() .blobs
# c++: layer_param,loss(int top_index),type_name(),
# print net.layers[0].blobs[0] #Blob 
# Blob   channels, count,data,diff,height,num,width
# print net.layers[0].type_name #added in branch

# <codecell>

#import Image
import numpy as np
from PIL import Image as Image
import matplotlib.pyplot as pyplot
import skimage.io

# load input and configure preprocessing
image_file="/home/omar/Documents/KTH/1.4/Speech/caffe-speech-recognition_old/spoken_numbers/7_Karen_260.wav.png"
# input_image = skimage.io.imread(image_file).astype(np.float32)
pyplot.figure()
input_image = caffe.io.load_image(image_file)
pyplot.imshow(input_image)

im = skimage.color.rgb2gray(input_image)
print im.shape
# <codecell>

    

# <codecell>

import numpy as np
import matplotlib.pyplot as plt


preds = net.predict(im)

### make classification map by forward and print prediction indices at each location
##data=np.asarray([net.transformer.preprocess('data', im)])
##out = net.forward_all(data=data)
##print out.keys()
##print out['prob'][0]
###print out['prob'][0].argmax(axis=0)
#
## show net input and confidence map (probability of the top prediction at each location)
#plt.subplot(1, 2, 1)
#plt.imshow(out['prob'][0].max(axis=0))
#plt.subplot(1, 2, 2)
#data2=data #net.blobs['data'].data[0] #huh?
#plt.imshow(net.deprocess('data', data2))
##print out => 7 YAY !!
## {'prob': array([[[[ 0.]],[[ 0.]],[[ 0.]],[[ 0.]],[[ 0.]],[[ 0.]],[[ 0.]],[[ 1.]],[[ 0.]],[[ 0.]]]], dtype=float32)}

