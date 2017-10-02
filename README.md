# mAInstein

mAInstein is an AI agent that can play Minecraft on it's own.



### Features to be implemented:
- [x] Navigation (v1.0 has accomplished this to some extent)
- [ ] Controlling Mouse
- [ ] Wood Collection
- [ ] Hunting/Getting Food
- [ ] Combat
- [ ] Tool Making
- [ ] Resource Collection (Coal, Silver ...)
- [ ] House Making
- [ ] Start Minecraft and load the map on it's own



### Implementation:

This bot will be implemented using a convolutional neural network (since we're dealing with images). If you want to use this model, and you're not using Windows, you will need to use PIL's ImageGrab to get the screen image instead of pywin32's win32gui.I chose pywin32 because it's highly optimized for the Windows Platform and has a much higher FPS.



### Dependencies:
1. TFLearn
2. Tensorflow (I'm using the GPU version)
3. pywin32
4. OpenCV (>3.0)



### Versions:

#### v1.0
* Used the alexnet convolutional network
* Learning rate was 0.001 with 30 epochs,
* Training size was somewhere around 22000 (around 10 - 15 minutes of gameplay)
* The agent can only control space, w, a, and d
* Trained only using data from day time and clear weather

Here's a demo (I am moving the mouse)

![alt text](https://github.com/AakashSasikumar/MinecraftBot/blob/master/GIFs/v1.0.gif)


The agent knows how to keep itself floating when in water, and can avoid trees and dirt blocks pretty well

Issues with v1.0 are
* Since I'm using creative mode, the flying mode gets switched on frequently (can fix this by changing key mapping)
* It doesn't know how to jump, most of the time it just ends up moving forward (need better training data)
