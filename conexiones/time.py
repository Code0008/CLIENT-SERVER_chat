from datetime import *
import re
def validar_correo(correo):
        dominios=['gmail.com', 'hotmail.com', 'upc.edu']
        return f"correo correcto enviao al domino {correo}" if correo in dominios else f"correo no enviao A {correo} no tiene dominio correcto aña"               
text = "CONTACTO ELTINGLING@UPC.EDU.PE Y ELPEPE@UPC.EDU.PE Y ESTANISPENDEJO@HOTMAIL.COM Y PENEDOL@GMAIL.COM Y SEXOLOGOENZO@SENATINO.COM"
for x in re.findall("@(\w+\.\w+)", text): print(validar_correo(x.lower()))
