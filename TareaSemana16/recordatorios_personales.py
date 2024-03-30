# Abrimos el archivo de texto en modo lectura ('r')📝
recordatorios_personales = open('my_notes.txt','r')

# Leemos las primeras tres líneas del archivolinea1 = recordatorios_personales.readline()📖
linea1 = recordatorios_personales.readline()
linea2 = recordatorios_personales.readline()
linea3 = recordatorios_personales.readline()

# Mostramos las tres líneas leídas en la consola 👀
print(linea1)
print(linea2)
print(linea3)
recordatorios_personales.close() # Cerramos el archivo 🔒
