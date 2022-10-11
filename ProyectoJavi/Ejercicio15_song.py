song = "You look so beautiful in this light Your silhouette over me The way it brings out the blue in your eyes Is the " \
       "Tenerife sea And all of the voices surrounding us here hey just fade out when you take a breath Just say the " \
       "word and I will disappear Into the wilderness"

# con este metodo es posible encontrar la palabra en un indice
# el primer indice de la ocurrencia de la palabra, donde inicia la palabra a encontrar
palabraBuscada = song.find("voices")

#Cambiamos la palabra de la letra
palabraCambiada = song.replace("voices","sounds")

print(song)
print(palabraCambiada)