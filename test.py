import qrcode

def payment(upi_vpa,amount,rideid):
    # UPI details
    
    transaction_note = "Test transaction"

    # Encode UPI details in the correct format
    # upi_string = f"upi://pay?pa={upi_vpa}&am={amount}&tn={transaction_note}"
    upi_string =f'upi://pay?pn={upi_vpa}&pa={upi_vpa}&am={amount}'
    link = 'pay?pn={upi_vpa}&pa={upi_vpa}&am={amount}'
    # Create the QR code image
    img = qrcode.make(upi_string)

    # Save the image to a file
    img.save(f"media/upi/{rideid}_upi_qr.png")

    return link