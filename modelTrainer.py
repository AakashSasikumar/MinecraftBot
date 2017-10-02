import numpy as np
from Alexnet import alexnet

WIDTH = 160
HEIGHT = 90
LR = 0.001
EPOCH = 30
MODEL_NAME = 'MinecraftBot-{}-{}-{}-epochs.model'.format(LR, 'alexnet', EPOCH)

model = alexnet(WIDTH, HEIGHT, LR)

trainingData = np.load('Data/balancedTrainingDataWONone.npy')

train = trainingData[:-500]
test = trainingData[-500:]

X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
y = np.array([i[1] for i in train])

testX = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 1)
testy = np.array([i[1] for i in test])

model.fit({'input': X}, {'targets': y}, n_epoch=EPOCH,
          validation_set=({'input': testX}, {'targets': testy}),
          snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

# tensorboard --logdir=foo:D:/Code/Python/MinecraftBot/log/Alexnet
model.save(MODEL_NAME)
