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

### A simple Box

The most simple part of a GUI is a box with some text.
PygameGUI makes it easy.
The first parameter is a `pygame.Rect` for positiong and scaling of the Box.
The second parameter is the text displayed in the box.
The last parameter is an optional skin parameter, overwriting the use of default skin on this box only.

```python
GUI.Box(pygame.Rect(0, 0, 100, 50), "Hello World", skin=other_skin)
```

### The usefull Button

The most usefull feature in a GUI engine is a simple Button.
Just like a Box, it iis very easy to use with as much customisation as you want.
The first three parameters are exactly the same as a box.
The fourth one is the mouse button which should be pressed to activate the box as an integer, defaulted to 0.
The fith is an optional state the button should be locked at, default is -1. 0 is for normal look, 1 is for over look, 2 is for down look.
This function returns a boolean weather the button was pressed.

```python
if (GUI.Button(pygame.Rect(0, 0, 100, 50), "Hi!", skin=other_skin, type=0)):
  GUI.Button(pygame.Rect(0, 50, 100, 50), "Down", state=2)
```

### Repeatable Button

Exactly the same as a button, only it returns true even if it is held down.

```python
if (GUI.Button(pygame.Rect(posx, posy, 100, 50), "Movable")):
  posx = pygame.mouse.get_pos()[0]
  posy = pygame.mouse.get_pos()[1]
```

### An Input Box (Text Field)

What is a GUI Library without an input box?
The first parameter is the same as a box.
The second parameter is the current text in the box.
The third parameter is a boolean for the text field being active or not.
the fourth parameter is the same as a button, the type of mouse button to activate the text field.
This function returns 2 parameters, the new text and the new focus variables.

```python
field_text, field_active = GUI.TextField(pygame.Rect(0, 0, 100, 50), field_text, field_active, type=0)
```

### Just some text (Label)

This is exactly the same as a Box, just without the box.
Parameters are also the same.

```python
GUI.Label(pygame.Rect(0, 0, 100, 50), "Hello World")
```

### The power of a Selection Gid

What if you wanted to only select one item in a gird and have it stay selected?
`GUI.SelectionGid` allows you to do exactly that!
The first parameter is again a `pygame.Rect` every part of the grid is perfectly scaled.
The second parameter is the amount of boxes that should be horizontally.
The third parameter is the currently selected box as an index (integer).
The fourth parameter is a list of every string for every box. It also determines how many boxes there should be.
The last 2 parameters are from previous elements as well: override skin and mouse press type.
This function returns the currently selected grid index.

```python
selected = GUI.SelectionGid(pygame.Rect(0, 0, 300, 300), 2, selected, ["1", "2", "3", "4", "5"], skin=None, type=0)
```