import ctypes
import time

mouse_event = ctypes.windll.user32.mouse_event
MOUSEEVENTF_MOVE = 0x0001

ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

while True:
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
    mouse_event(MOUSEEVENTF_MOVE, 1, 0, 0, 0)
    time.sleep(1)#sleep for 60 seconds
    mouse_event(MOUSEEVENTF_MOVE, -1, 0, 0, 0)