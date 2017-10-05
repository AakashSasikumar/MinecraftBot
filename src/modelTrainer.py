import numpy as np
from Alexnet import alexnet

WIDTH = 480
HEIGHT = 270
LR = 0.0001
EPOCH = 50
MODEL_NAME = 'MinecraftBot-{}-{}-{}-epochs.model'.format(LR, 'alexnetColor', EPOCH)

model = alexnet(WIDTH, HEIGHT, LR)

trainingData = np.load('./Data/test/balancedTrainingDataColor.npy')
print(len(trainingData))

train = trainingData[:-100]
test = trainingData[-100:]


X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 3) 
# last parameter is 1 for grayscale and 3 for color
y = np.array([i[1] for i in train])

testX = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 3)
# last parameter is 1 for grayscale and 3 for color
testy = np.array([i[1] for i in test])

print(len(testX))
print(len(testy))
trainingData = []
test = []
train = []

model.fit({'input': X}, {'targets': y}, n_epoch=EPOCH,
          validation_set=({'input': testX}, {'targets': testy}),
          snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

# tensorboard --logdir=foo:D:/Code/Python/mAInstein/log/Alexnet
model.save('./TrainedModels/Color/' + MODEL_NAME)
