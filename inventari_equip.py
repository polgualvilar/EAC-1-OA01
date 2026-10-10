### OA01 EAC 1 ACTIVITAT 2 ###

### --- Imports --- ###

# No calen imports addicionals per a aquesta activitat.

### --- Constants --- ###

codi_inventari = "PC-AULA02-ID045"

### --- Lògica de sortida --- ###
tipus_equip = codi_inventari[:2]
ubicacio = codi_inventari[3:9]
identificador = codi_inventari[10:]

print(f"Informe de l'equip:\t{codi_inventari}\nTipus:\t{tipus_equip}\nUbicació:\t{ubicacio}\nID:\t{identificador}")
