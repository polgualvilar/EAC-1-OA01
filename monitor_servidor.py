### OA01 EAC 1 ACTIVITAT 1 ###

### --- Imports --- ###

# No calen imports addicionals per a aquesta activitat.

### --- Constants --- ###

nom_servidor = "srv-backup-02"
cpu_us = 67.348
memoria_lliure_gb = 3.5
servei_actiu = True

### --- Lògica de sortida --- ###
print(
    "SERVIDOR | PARÀMETRE | VALOR",
    f"{nom_servidor} | CPU (%) | {cpu_us:.2f}",
    f"{nom_servidor} | MEMÒRIA LLIURE (GB) | {memoria_lliure_gb:.2f}",
    f"{nom_servidor} | ACTIU | {servei_actiu}",
    sep="\n"
)