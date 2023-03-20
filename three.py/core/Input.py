import pygame

class Input(object):

    def __init__(self):
        self.keyDownList     = []
        self.keyPressedList  = []
        self.keyUpList       = []
        self.mouseButtonDown    = False
        self.mouseButtonPressed = False
        self.mouseButtonUp      = False
        self.quitStatus         = False
        # did the window resize since the last update?
        self.windowResize       = False
        self.windowWidth        = None
        self.windowHeight       = None
        
    def update(self):
        """
        Processes the Pygame events and updates the game input variables.

        This method should be called once per frame to update the input status of the game. It processes the Pygame events 
        and updates the input variables that can be used to control the game logic. The input variables that can be updated 
        include the following:

            - keyDownList: A list of the keys that were pressed down since the last update.
            - keyUpList: A list of the keys that were released since the last update.
            - mouseButtonDown: A boolean indicating whether the mouse button was pressed down since the last update.
            - mouseButtonUp: A boolean indicating whether the mouse button was released since the last update.
            - windowResize: A boolean indicating whether the game window was resized since the last update.
            - windowWidth: The width of the game window, in pixels.
            - windowHeight: The height of the game window, in pixels.

        Returns:
            None
        """
        self.keyDownList = []
        self.keyUpList   = []
        self.mouseButtonDown = False
        self.mouseButtonUp   = False
        self.windowResize    = False
        for event in pygame.event.get(): # checks input events (discrete)
            if event.type == pygame.KEYDOWN:
                self.keyDownList.append( event.key )
                self.keyPressedList.append( event.key )
            elif event.type == pygame.KEYUP:
                self.keyPressedList.remove( event.key )
                self.keyUpList.append( event.key )
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseButtonDown = True
                self.mouseButtonPressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouseButtonPressed = False
                self.mouseButtonUp = True
            elif event.type == pygame.QUIT:
                self.quitStatus = True
            elif event.type == pygame.VIDEORESIZE:
                self.windowResize = True
                self.windowWidth = event.w
                self.windowHeight = event.h

    def isKeyDown(self, keyCode):
        return keyCode in self.keyDownList
    
    def isKeyPressed(self, keyCode):
        return keyCode in self.keyPressedList

    def isKeyUp(self, keyCode):
        return keyCode in self.keyUpList

    def isMouseDown(self):
        return self.mouseButtonDown

    def isMousePressed(self):
        return self.mouseButtonPressed

    def isMouseUp(self):
        return self.mouseButtonUp

    def getMousePosition(self):
        return pygame.mouse.get_pos()

    def quit(self):
        return self.quitStatus
    
    def resize(self):
        return self.windowResize
        
    def getWindowSize(self):
        return { "width": self.windowWidth, "height": self.windowHeight }
        
