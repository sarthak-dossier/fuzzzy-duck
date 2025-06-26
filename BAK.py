import qrcode


data = input("Enter the URL to encode in the QR code: ")

qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_H,  
    box_size=10,  
    border=4 
)

# Add data
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="yellow", back_color="black")


img.save("qrcode.png")

print("QR Code generated and saved as qrcode.png")
