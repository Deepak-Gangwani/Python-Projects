import qrcode
import image
qr = qrcode.QRCode(
    version=15,  # 15 means the version of the qr code high the number bigger the code image and complicated picture
    box_size=10, # size of the box where qr code will be dispalyed
    border=5   # it is the white part of image --border
)

data = "7414804515"
# here we will give the path of the channel like the same way you can give any link,number,name
# if you don't want to redirect  and create  for normal text that write text in the quotes

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
img.save("test1.png")
