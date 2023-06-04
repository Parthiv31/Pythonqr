import pyqrcode
import requests
from pyqrcode import QRCode
print("Enter link (with http://): ")
s=input()
try:
        response = requests.get(s)
        if response.status_code == 200:
            url = pyqrcode.create(s)
            url.svg("myqr.svg", scale=6)
            url.png("myqr.png", scale=6)
            print("QR code generated successfully!")
        else:
            print("Invalid or non-existent link. Please check the URL and try again.")
except requests.exceptions.RequestException as e:
    print("An error occurred while accessing the link:", str(e))

