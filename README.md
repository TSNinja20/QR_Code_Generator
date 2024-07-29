**UPI Payment QR Code Generator**
Description
This Python script generates UPI payment QR codes for PhonePe, Paytm, and Google Pay. Simply input your UPI ID, and the script creates, saves, and displays QR codes for easy payment acceptance.

**Features**
Input your UPI ID
Generate QR codes for:
PhonePe
Paytm
Google Pay
Save QR codes as image files
Display QR codes for scanning

**Requirements**
Python 3.x
qrcode library
PIL/Pillow library

**Installation**
Install the required libraries using pip:
pip install qrcode[pil]
pip install pillow

**Usage**
Run the script.
Input your UPI ID when prompted.
The script will generate QR codes for PhonePe, Paytm, and Google Pay.
The QR codes will be saved as image files (phonepe_qr.png, paytm_qr.png, gpay_qr.png).
The QR codes will also be displayed for immediate scanning.


**Example Code**
import qrcode

# Taking UPI ID as input
upi_id = input("Enter your UPI ID = ")

# Define the payment URLs
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
gpay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Create QR codes
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
gpay_qr = qrcode.make(gpay_url)

# Save QR codes as images (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
gpay_qr.save('gpay_qr.png')

# Display QR codes
phonepe_qr.show()
paytm_qr.show()
gpay_qr.show()
Customization
Modify the URLs for different UPI payment apps by changing the phonepe_url, paytm_url, and gpay_url variables.
Customize the recipient name, merchant code, amount, and other parameters as needed.
Contributing
Contributions are welcome! Please feel free to submit issues or pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for details.
