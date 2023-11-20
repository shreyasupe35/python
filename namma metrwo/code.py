import pyqrcode
import png
myUPI="myupiid988@okhdfc"
qrcode=pyqrcode.create(myUPI)
qrcode.png("myUPIid.png",scale=8)