# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code
site = "https://www.google.com"

# Generate QR code
url_qr = pyqrcode.create(site)

# Create and save the svg file naming "url_qr.svg"
url_qr.svg("great.svg", scale = 8)

# Create and save the png file naming "url_qr.png"
url_qr.png('great.png', scale = 6)
