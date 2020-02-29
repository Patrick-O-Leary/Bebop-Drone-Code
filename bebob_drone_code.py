/home/techgarage/Downloads/CustomDrone-masterimport pygame
import cv2
from commands import *
import logging
from bebop import Bebop

wnd = None
def video_frame(frame):
   cv2.imshow("Drone", frame)
   cv2.waitKey(10)

def video_start():
   print("Starting video...")


def video_end():
   print("Ending video...")
   cv2.destroyWindow("Drone")
   # Have to send waitKey several times on Unix to make window disappear
   for i in range(1, 5):
       cv2.waitKey(1)

print("Connecting to drone..")
drone = Bebop()
drone.video_callbacks(video_start, video_end, video_frame)
drone.videoEnable()
print("Connected.")

pygame.init()
size = [100, 100]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Drone Teleop")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

if pygame.joystick.get_count() == 0:
   print("No joysticks found")
   done = True
else:
   joystick = pygame.joystick.Joystick(0)
   joystick.init()
   print("Initialized %s" % (joystick.get_name()))
   print("Number of buttons %d. Number of axis %d, Number of hats %d" %
         (joystick.get_numbuttons(), joystick.get_numaxes(),
          joystick.get_numhats()))


