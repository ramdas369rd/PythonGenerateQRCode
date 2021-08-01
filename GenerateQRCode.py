#Import QRCode from pyqrcode
import  pyqrcode
import png
from pyqrcode import QRCode

#String which represents the QR code
s = "https://www.github.com/ramdas369rd/"

#Genereate QR code
url = pyqrcode.create(s)

#Create and save the svg("Scalable Vector Graphics” It's a XML based two-dimensional graphic file format) file naming myGitHubProfile.svg
url.svg("myGitHubProfile.svg", scale = 8)

#Create and save the png file naming myGitHubProfile.svg
url.png('myGitHubProfile.png', scale = 6)
