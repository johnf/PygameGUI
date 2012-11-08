#Import Pygame Library
import pygame

#Skin Class for image reference
class Skin():
    texture_normal = None
    texture_over = None
    texture_down = None
    border = False
    font = None
    def __init__(self, tn, to, td, fnt, brdr=0):
        self.texture_normal = pygame.image.load(tn)
        self.texture_over = pygame.image.load(to)
        self.texture_down = pygame.image.load(td)
        self.texture_normal.convert(self.texture_normal)
        self.texture_over.convert(self.texture_over)
        self.texture_down.convert(self.texture_down)
        self.font = fnt
        self.border = brdr

global default_skin
default_skin = None


#Initialise Pygame, the display
def init(area, def_skin=None, fullscreen=False):
    global default_skin
    pygame.init()
    default_skin = def_skin
    return pygame.display.set_mode(area, fullscreen)

#Clear Screen Function
def Clear(surface, color):
    surface.fill(color)
    surface.blit(surface, pygame.display.get_surface().get_rect())

#Check if mouse is in rectangle Function
def MouseInRect(area):
        if (pygame.mouse.get_pos()[0] > area.x and pygame.mouse.get_pos()[0] < area.x + area.width):
                if (pygame.mouse.get_pos()[1] > area.y and pygame.mouse.get_pos()[1] < area.y + area.height):
                        return True
                else:
                        return False
        else:
                return False

def RectInRect(area, area2):
    if (area.x > area2.x and area.x < area2.x + area2.width):
        if (area.y > area2.y and area.y < area2.y + area2.height):
            return True
        else:
            return False
    else:
        if (area.x > area2.x and area.x < area2.x + area2.width):
            if (area.y + area.height > area2.y and area.y + area.height < area2.y + area2.height):
                return True
            else:
                return False
        else:
            if (area.x + area.width > area2.x and area.x + area.width < area2.x + area2.width):
                if (area.y + area.height > area2.y and area.y + area.height < area2.y + area2.height):
                    return True
                else:
                    return False
            else:
                if (area.x + area.width > area2.x and area.x + area.width < area2.x + area2.width):
                    if (area.y > area2.y and area.y < area2.y + area2.height):
                        return True
                    else:
                        return False

#Texture Drawing for both user and inbuilt uses
def DrawTexture(textureinput, area, isGUI=False):
    texture = textureinput
    #Cache Screen
    screen = pygame.display.get_surface()
    if (isGUI):
        w = texture.get_width()
        h = texture.get_height()
        #Print Centre
        tex = pygame.transform.scale(texture, ((area.width-w)*2, (area.height-h)*2))
        screen.blit(tex, (area.x + w/2, area.y + h/2), pygame.Rect(area.width-w, area.height-h, area.width-w, area.height-h))
        #Print Left Edge
        tex = pygame.transform.scale(texture, (w, (area.height-h)*2))
        screen.blit(tex, (area.x, area.y + h/2), pygame.Rect(0, area.height-h, w/2, area.height-h))
        #Print Right Edge
        tex = pygame.transform.flip(texture, True, False)
        tex = pygame.transform.scale(tex, (w, (area.height-h)*2))
        screen.blit(tex, (area.x + area.width - w/2, area.y + h/2), pygame.Rect(w/2, area.height-h, w/2, area.height-h))
        #Print Top Edge
        tex = pygame.transform.scale(texture, ((area.width-w)*2, h))
        screen.blit(tex, (area.x + w/2, area.y), pygame.Rect(area.width-w, 0, area.width-w, h/2))
        #Print Bottom Edge
        tex = pygame.transform.flip(texture, False, True)
        tex = pygame.transform.scale(tex, ((area.width-w)*2, h))
        screen.blit(tex, (area.x + w/2, area.y + area.height - h/2), pygame.Rect(area.width-w, h/2, area.width-w, h/2))
        #Print Top Left Corner
        screen.blit(texture, (area.x, area.y), pygame.Rect(0, 0, w/2, h/2))
        #Print Bottom Left Corner
        tex = pygame.transform.rotate(texture, 90)
        screen.blit(tex, (area.x, area.y + area.height - h/2), pygame.Rect(0, h/2, w/2, h/2))
        #Print Bottom Right Corner
        tex = pygame.transform.rotate(texture, 180)
        screen.blit(tex, (area.x + area.width - w/2, area.y + area.height - h/2), pygame.Rect(w/2, h/2, w/2, h/2))
        #Print Top Right Corner
        tex = pygame.transform.rotate(texture, 270)
        screen.blit(tex, (area.x + area.width - w/2, area.y), pygame.Rect(w/2, 0, w/2, h/2))
    else:
        texture = pygame.transform.scale(texture, (area.width, area.height))
        screen.blit(texture, area)

#Draw a Butoon Function
def Button(area, content, skin=None, type=0, state=-1):
    global default_skin
    if (skin == None):
        skin = default_skin
    area.x += skin.border
    area.y += skin.border
    area.width -= skin.border*2
    area.height -= skin.border*2
    output = False
    if (MouseInRect(area) or state > 0):
        if (state == -1):
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONUP):
                    output = True
        if (pygame.mouse.get_pressed()[type] or state == 1):
            DrawTexture(skin.texture_down, area, True)
        else:
            DrawTexture(skin.texture_over, area, True)
    else:
        DrawTexture(skin.texture_normal, area, True)
    if (content != ""):
        area.x += area.width/2 - skin.font.size(str(content))[0]/2
        area.y += area.height/2 - skin.font.size(str(content))[1]/2
        pygame.display.get_surface().blit(skin.font.render(str(content), True, pygame.Color("white")), area)
    return output

def RepeatButton(area, content, skin=None, type=0):
    global default_skin
    if (skin == None):
        skin = default_skin
    area.x += skin.border
    area.y += skin.border
    area.width -= skin.border*2
    area.height -= skin.border*2
    output = False
    if (MouseInRect(area)):
        if (pygame.mouse.get_pressed()[type]):
            DrawTexture(skin.texture_down, area, True)
            output = True
        else:
            DrawTexture(skin.texture_over, area, True)
    else:
        DrawTexture(skin.texture_normal, area, True)
    if (content != ""):
        area.x += area.width/2 - skin.font.size(str(content))[0]/2
        area.y += area.height/2 - skin.font.size(str(content))[1]/2
        pygame.display.get_surface().blit(skin.font.render(str(content), True, pygame.Color("white")), area)
    return output

def Box(area, content, skin=None):
    global default_skin
    if (skin == None):
        skin = default_skin
    area.x += skin.border
    area.y += skin.border
    area.width -= skin.border*2
    area.height -= skin.border*2
    DrawTexture(skin.texture_normal, area, True)
    if (content != ""):
        area.x += area.width/2 - skin.font.size(str(content))[0]/2
        area.y += area.height/2 - skin.font.size(str(content))[1]/2
        pygame.display.get_surface().blit(skin.font.render(str(content), True, pygame.Color("white")), area)

def TextField(area, istring, ifocus, skin=None, type=0):
    global default_skin
    if (skin == None):
        skin = default_skin
    area.x += skin.border
    area.y += skin.border
    area.width -= skin.border*2
    area.height -= skin.border*2
    if (ifocus):
        DrawTexture(skin.texture_down, area, True)
        if (not(MouseInRect(area)) and pygame.mouse.get_pressed()[type]):
            ifocus = False
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.unicode):
                    if (event.unicode == unichr(8)):
                        istring = istring[:-1]
                    elif (event.unicode == unichr(3) or event.unicode == unichr(13)):
                        ifocus = False
                    else:
                        istring += event.unicode
    else:
        DrawTexture(skin.texture_normal, area, True)
        if (MouseInRect(area) and pygame.mouse.get_pressed()[type]):
            ifocus = True
    
    if (istring != ""):
        area.x += area.width/2 - skin.font.size(str(istring))[0]/2
        area.y += area.height/2 - skin.font.size(str(istring))[1]/2
        pygame.display.get_surface().blit(skin.font.render(str(istring), True, pygame.Color("white")), area)
    return istring, ifocus

def Label(area, content, skin=None):
    global default_skin
    if (skin == None):
        skin = default_skin
    area.x += skin.border
    area.y += skin.border
    area.width -= skin.border*2
    area.height -= skin.border*2
    if (content != ""):
        area.x += area.width/2 - skin.font.size(str(content))[0]/2
        area.y += area.height/2 - skin.font.size(str(content))[1]/2
        pygame.display.get_surface().blit(skin.font.render(str(content), True, pygame.Color("white")), area)

def SelectionGrid(area, xsplit, selected, content, skin=None, type=0):
    global default_skin
    if (skin == None):
        skin = default_skin
    x = area.x
    y = area.y
    ysplit = round(len(content)/xsplit)
    i = 0
    for c in content:
        if (content[i]):
            if (i == selected):
                Button(pygame.Rect(x, y, area.width/xsplit, area.height/ysplit), content[i], skin, state=1)
            else:
                if (RepeatButton(pygame.Rect(x, y, area.width/xsplit, area.height/ysplit), content[i], skin)):
                    selected = i
        else:
            Box(pygame.Rect(x, y, area.width/xsplit, area.height/ysplit), "", skin)
        x += area.width/xsplit
        i += 1
        if x > area.x + area.width/xsplit*(xsplit-1):
            x = area.x
            y += area.height/ysplit
    return selected
