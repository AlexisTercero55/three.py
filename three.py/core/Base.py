import pygame
import sys
import time

from core import Input

class Base(object):

    def __init__(self):

        # initialize the pygame display and OpenGL context
        pygame.display.init()# render images
        pygame.font.init()# render text
        
        # load a custom icon
        pygame.display.set_icon(pygame.image.load("images/icon.png"))
        
        # initialize buffers to perform antialiasing
        # Pygame will use one buffer for multi-sampling
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        # sets the number of samples per pixel to 4, which means that each pixel will be sampled 4 times for anti-aliasing
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
    
        self.setWindowTitle("Three.py")
        self.setWindowSize(640, 640)

        self.clock = pygame.time.Clock()
        self.deltaTime = 0
        self.input = Input()
        self.running = True

    # set window title
    def setWindowTitle(self, text):
        pygame.display.set_caption(text)

    
        # WARNING: calling this method loses the original OpenGL context;
    #   only use before calling OpenGL functions
    def setWindowSize(self, width, height):
        '''
This is a Python method that sets the size of the Pygame window that will be used to render OpenGL graphics.

The first line of the method is a warning that calling this method will lose the original OpenGL context. This means that any OpenGL objects or state that were previously bound or set will need to be reinitialized after this method is called.

The method takes two arguments, 'width' and 'height', which are used to set the size of the Pygame window. These values are stored in a tuple called 'screenSize'.

Next, the method sets some Pygame display flags using bitwise OR (|) operations. These flags include:

    DOUBLEBUF: This flag enables double buffering, which means that Pygame will render the graphics off-screen before displaying them on-screen. This can help prevent flickering and improve performance.
    OPENGL: This flag tells Pygame that we will be using OpenGL to render graphics.
    RESIZABLE: This flag allows the Pygame window to be resized by the user.

These display flags are stored in a variable called 'displayFlags'.

Finally, the method calls 'pygame.display.set_mode()' to create the Pygame window with the specified size and display flags. The resulting Pygame 'Surface' object is stored in a class variable called 'screen'.

In summary, this method sets up a Pygame window for rendering OpenGL graphics with double buffering, OpenGL rendering, and resizable capabilities. However, it should be used with caution as it may cause the loss of the original OpenGL context.
        '''
        self.screenSize = (width, height)
        self.displayFlags = pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE
        self.screen = pygame.display.set_mode( self.screenSize, self.displayFlags )
    # implement by extending class
    def initialize(self):
        pass
    
    # implement by extending class
    def update(self):
        pass

    def run(self):

        self.initialize()
        
        while self.running:
        
            # update input state (down, pressed, up)
            self.input.update()
    
            if self.input.quit():
                self.running = False

            # debug tools
            
            # print FPS (Ctrl+F)
            if (self.input.isKeyPressed(pygame.K_LCTRL) or self.input.isKeyPressed(pygame.K_RCTRL)) and self.input.isKeyDown(pygame.K_f):
                fps = self.clock.get_fps()
                print( "FPS: " + str(int(fps)) )
                
            # save screenshot (Ctrl+S)
            if (self.input.isKeyPressed(pygame.K_LCTRL) or self.input.isKeyPressed(pygame.K_RCTRL)) and self.input.isKeyDown(pygame.K_s):
                timeString = str( int(1000 * time.time()) )
                fileName = "image-" + timeString + ".png"
                pygame.image.save(self.screen, fileName)
                
            self.deltaTime = self.clock.get_time() / 1000.0
            
            self.update()
            
            # display image on screen
            pygame.display.flip()

            # limit to 60 FPS
            self.clock.tick(60)

        # end of program
        pygame.quit()
        sys.exit()
        
    
