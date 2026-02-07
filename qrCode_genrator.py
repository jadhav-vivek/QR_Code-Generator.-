import qrcode

upi_id = input("enter the uip id = ")

upi_url = f'upi://pay?pa={upi_id}&pn=Recipt%20Nmae&mc=1234'

phonepay_qr = qrcode.make(upi_url)
paytm_qr = qrcode.make(upi_url)
gpay_qr = qrcode.make(upi_url)

phonepay_qr.save('phonepay_qr.png')
paytm_qr.save('paytm_qr.png')
gpay_qr.save('gpay_qr.png')

phonepay_qr.show()
paytm_qr.show()
gpay_qr.show()


