import pywhatkit as whatsapp

phone_numbers = ["+123456789"]
message = "Hello from Python! This is an instant WhatsApp message."

for phone_number in phone_numbers:
    whatsapp.sendwhats_image(phone_number, image_path, message, 15, True, 5)

