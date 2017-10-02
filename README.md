# MinecraftBot

MinecraftBot is an AI agent that plays Minecraft on it's own (survival mode).

### Features to be implemented:
1. Navigation
2. Wood Collection
3. Hunting/Getting Food
4. Combat (against enemies)
5. House Making
6. Took Making
7. Resource Collection (Coal, Silver ...)

### Implementation:

This bot will be implemented using a convolutional neural network. If you want to use this model, and you're not using Windows, you will need to use PIL's ImageGrab to get the screen image instead of pywin32's win32gui.I chose pywin32 because it's highly optimized for the Windows Platform and has a much higher FPS.

### Dependencies:
1. TFLearn
2. Tensorflow (I'm using the GPU version)
3. pywin32
4. OpenCV (>3.0)


### Versions:

#### v1.0
* Used the alexnet convolutional network
* Learning rate was 0.001 with 30 epochs,
* Training size was somewhere around 22000
* The agent can only control space, w, a, and d


<a href="https://giphy.com/embed/l378k2uWWPO5nmjLO"><img src="https://media.giphy.com/media/l378k2uWWPO5nmjLO/giphy.gif" title="MinecraftBot"/></a>

The agent, knows how to keep itself floating when in water, and can avoid trees and sand blocks pretty well

The problems with v1.0 are
* Since I'm using creative mode, the flying mode gets switched on frequently (can fix this by chaniging game mapping)
* It doesn't know how to jump, most of the time it just ends up moving forward


