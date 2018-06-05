#Python Script to Automate Google's Dinosaur Game
'''----------------------------------------------------------------------------------
| To Make the Dinosaur Jump, in this script, a box is considered so that whenever    |
| an obstacle is encountered, the value of pixels calculated before is changed,      |
| and this change makes the Dinosaur Jump.                                           |
| No Machine Learning is embedded! The Coordinates of the Dinosaur and the Box       |
| matters! Even a slight change might affect the game!                               |                     
| Calculate the exact coordinates by Trial and Error! Iniatial approx coordinates    |
| can be obtained by screenshotting the dinasaur and knowing the pixels from tools   |
| like Paint.net. Also this script does'nt support Night Mode! For Day only version  |
| visit http://www.trex-game.skipser.com/                                            |
| Have Fun!                                                                          |
| ~Siddharth.S                                                                       |
|-----------------------------------------------------------------------------------'''


from PIL import ImageGrab, ImageOps
import time
from numpy import *
import pyautogui

class coordinates():
    replaybtn = (300, 420)  #Change the coordinates of replay button
    dino = (135, 464)       #X coordinate of Dinaraur will be the coordinate when the Dinosaur is standing and Y coordinate would be when it's ducking
    
def replay():
    pyautogui.click(coordinates.replaybtn)
    pyautogui.keyDown('down')
def spaceclick():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print("Jump")
    time.sleep(0.16)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')
def imageGrab():
    box = (coordinates.dino[0]+37, coordinates.dino[1], coordinates.dino[0]+128, coordinates.dino[1]+5 )  #Upper Left Corner and Lower Right corner coordinates
    image = ImageGrab.grab(box)                                                                           #are used here. Upper corner will be Dinosaur coordinate+offset.   
    grayImage = ImageOps.grayscale(image)                                                                 #Offset will be the dist of box from the Dino. Similiarly lower Y coordinate  
    a = array(grayImage.getcolors())                                                                      #will be the width of the Box.
    print(a.sum())                                                                                        # The Pixels in the box are converted to Grayscale	
    return a.sum()                                                                                        #for eff. and sum is calculated.
def main():
     replay()
     while True:
         if( imageGrab() != 702):                                                                         #The Value returned by the imageGrab fn decides whether the Dino should jump
             spaceclick()                                                                                 #or not, change the sum accordingly!
             time.sleep(0.1)

main()
