Python GUI Module
===

A Pygame built GUI Library based on the GUI interface of Unity 3d
It allows for very fast, easy but also customisable usage.

## Installation

Install Pygame

## Documentation

### Making a Skin

Skins are objects that hold all relavent information for rendering the GUI
The first 3 parameters are the names of the images relevant for rendering:
Normal texture, Over Texture and the Down texture
The 4th parameter represents the font used in rendering
The last parameter is for an optional border defaulted to 0.
Each GUI element will have a border with this value on every side.

```python
import pygame, GUI

skin = GUI.Skin("Normal.png", "Over.png", "Down.png", pygame.font.Font(None, 16), 5)
```

### Initializing the GUI

PygameGUIAIP's init method can be used as a quick way of starting off Pygame and a window,
As well as setting the default look of the GUI.
The first parameter is a touple containing the width and height of the screen.
The second is a optional setting for the default skin, as a `GUI.Skin`.
The last is an optional parameter for fullscreen, defaulted to `False`.
This function returns a `pygame.Surface` for the screen.

```python
import pygame, GUI

skin = GUI.Skin("Normal.png", "Over.png", "Down.png", pygame.font.Font(None, 16), 5)
screen = GUI.init((800, 487), skin, True)
```

### Every Update

Every frame all relevant GUI functions have to be called.
For the next part of the documentation I assume all the code is called every frame.

### Clear the screen

PygameGUI allwos you to quickly clear the screen with a single call.
The first parameter is the `pygame.Surface` of the screen or other area to clear.
The second parameter is the color to clear to.

```python
GUI.Clear(screen, pygame.Color("Black"))
```