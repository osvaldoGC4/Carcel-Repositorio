from Crypto.Cipher import AES
import base64
import os

class EncriptadorAES:
    def __init__(self, clave):
        self.clave = clave.encode('utf-8')  # Clave de encriptación (debe ser de 16, 24 o 32 bytes)
        self.bs = AES.block_size  # Tamaño del bloque AES (por defecto 16)

    def encriptar(self, texto):
        # Rellenar el texto para que sea múltiplo del tamaño del bloque
        padding = self.bs - len(texto) % self.bs
        texto = texto + chr(padding) * padding
        cipher = AES.new(self.clave, AES.MODE_CBC, iv=self.clave)  # Usamos la clave como IV por simplicidad
        encrypted = cipher.encrypt(texto.encode('utf-8'))
        # Retornar como base64 para almacenar como texto
        return base64.b64encode(encrypted).decode('utf-8')

    def desencriptar(self, texto_encriptado):
        encrypted_data = base64.b64decode(texto_encriptado)
        cipher = AES.new(self.clave, AES.MODE_CBC, iv=self.clave)  # Usamos la clave como IV por simplicidad
        decrypted = cipher.decrypt(encrypted_data).decode('utf-8')
        # Eliminar el padding
        padding = ord(decrypted[-1])
        return decrypted[:-padding]

# Instancia de la clase de encriptación con una clave de 16 caracteres
encriptador = EncriptadorAES("admin1234")
