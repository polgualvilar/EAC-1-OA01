### OA01 EAC 1 ACTIVITAT 3 ###

### --- Imports --- ###

# No calen imports addicionals per a aquesta activitat.

### --- Constants --- ###
mida_total_mb = 250
mida_paquet_mb = 40

### --- Lògica de sortida --- ###
paquets_complets = mida_total_mb // mida_paquet_mb
mb_restants = mida_total_mb % mida_paquet_mb
percentatge_ultima_paquet = mb_restants / mida_paquet_mb * 100

print(f"Informe de transmissió: {mida_total_mb}MB\nPaquets complets: {paquets_complets}\nMB restants: {mb_restants}MB\nPercentatge de l'últim paquet: {percentatge_ultima_paquet:.2f}%")