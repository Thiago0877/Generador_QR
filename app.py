import qrcode

def generar_qr(url):
    # Crear el código QR
    qr = qrcode.QRCode(
        version=1,  # Tamaño del QR (1 a 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Tamaño de cada cuadro
        border=4,  # Bordes del QR
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Crear imagen del QR
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Guardar la imagen
    img.save("codigo_qr.png")
    print("✅ Código QR generado y guardado como 'codigo_qr.png'")

# Ejemplo de uso
if __name__ == "__main__":
    enlace = input("🔗 Ingresa la URL que deseas convertir en QR:")
    generar_qr(enlace)
