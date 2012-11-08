import pygame, GUI

pygame.init()
skin = GUI.Skin("Normal.png", "Over.png", "Down.png", pygame.font.Font(None, 14), 3)
skin_large = GUI.Skin("Over.png", "Normal.png", "Down.png", pygame.font.Font(None, 11), 1)
screen = GUI.init((400, 400), skin)

selection = 0
txt_on = False
txt_field = "Hi!"
running = True

while running:
    GUI.Clear(screen, pygame.Color("Black"))
    i = 0
    while i <= 13:
        GUI.Box(pygame.Rect(25*i, 0, 25, 25), "")
        i += 1
    if (GUI.Button(pygame.Rect(325, 0, 50, 25), "QUIT")):
        running = False
    if (GUI.RepeatButton(pygame.Rect(0, 25, 400, 25), "Long Button")):
        GUI.Box(pygame.Rect(0, 50, 50, 350), "")
    selection = GUI.SelectionGrid(pygame.Rect(25, 50, 375, 300), 3, selection, ["1", "2", "3", "4", "5", "6"])
    txt_field, txt_on = GUI.TextField(pygame.Rect(25, 375, 375, 25), txt_field, txt_on, skin_large)
    pygame.display.flip()
    for event in pygame.event.get():
        if (event == pygame.QUIT):
            running = False
    pygame.time.wait(60)
pygame.quit()
