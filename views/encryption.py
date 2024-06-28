from Crypto.Cipher import DES
import base64


class Encrypt:
    DES_KEY = b'JJWSEDAF'
    DES_IV = b'OTFEGCBZ'

    @staticmethod
    def my_decrypt(string_to_decrypt):
        string_to_decrypt = base64.b64decode(string_to_decrypt)  # Decodifica el string base64
        # Crea una instancia DES, especificando la KEY, modo de operacion(cifrado por bloques con relleno de cadena
        # de bits) y el vector de inicialización (DES_IV).
        cipher = DES.new(Encrypt.DES_KEY, DES.MODE_CBC, Encrypt.DES_IV)
        # Descifra la cadea usando el cifrador anterior, lo decodifica de bytes a cadena de texto y elimina los espacios en blanco
        decrypted = cipher.decrypt(string_to_decrypt).decode('utf-8').strip()
        return decrypted

    @staticmethod
    def my_encrypt(string_to_encrypt):
        # Creamos una instancia del cifrdor DES pasandole la clave, el modo y el vector de inicializacion
        cipher = DES.new(Encrypt.DES_KEY, DES.MODE_CBC, Encrypt.DES_IV)
        # Calcula la longitud del relleno necesario para que la cadena sea un múltiplo de 8 bytes.
        padding_length = 8 - len(string_to_encrypt) % 8
        # Codifica la cadena de texto en bytes utilizando UTF-8.
        string_to_encrypt = string_to_encrypt.encode('utf-8')
        # Agregamos el relleno necesario al final de la cadena.
        string_to_encrypt += bytes([padding_length]) * padding_length
        # Encriptamos la cadena utilizando el cifrador DES
        encrypted = cipher.encrypt(string_to_encrypt)
        return base64.b64encode(encrypted).decode('utf-8')
