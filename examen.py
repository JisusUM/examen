
import re

result= str(input("ingrese la cadena de caracteres a valitar ejemplo unoDosTres"))
print(re.sub(r"([A-Z][a-z])", r" \1", result).split())
