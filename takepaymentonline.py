import qrcode

#Taking UPI ID As a input
upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment URL based on the UPI ID and the payment app
#You can modify these URLs based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
gpay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
gpay_qr = qrcode.make(gpay_url)

#Save the QR code to image file(optional) STEP 4
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
gpay_qr.save('gpay_qr.png')

#STEP 5
#Display the QR Codes(you may need to installPIL/Pillow Library)
phonepe_qr.show()
paytm_qr.show()
gpay_qr.show()

