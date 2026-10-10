"""
Part 1 - Gestor de còpies de seguretat

Esquelet inicial de l'aplicació: es carrega una interfície bàsica des
d'un fitxer .ui i es connecta un botó a una funció que simula l'inici
d'una còpia de seguretat, confirmant-ho per pantalla i per terminal.
"""

# ==============================
# Imports
# ==============================
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys


# ==============================
# Variables globals
# ==============================
total_copies = 0


# ==============================
# Funcions (Slots)
# ==============================
def iniciar_copia():
    """
    Funció de resposta (slot) que s'executa quan l'usuari clica el
    botó 'btn_iniciar'.
    """
    global total_copies

    # ------------ -----------
    total_copies += 1

    # ------------ -----------
    # TODO: Escriu per consola un missatge indicant que s'ha iniciat
    # una còpia de seguretat i el total acumulat fins ara.
    print(f"S'ha iniciat una còpia de seguretat. Total acumulat: {total_copies}")

    # ------------ -----------
    # TODO: Mostra un QMessageBox.information a l'usuari confirmant
    # l'inici de la còpia i indicant el mateix total acumulat.
    QMessageBox.information(
    window,
    "Còpia de seguretat",
    f"S'ha iniciat una còpia de seguretat. Total: {total_copies}"
)


# ==============================
# Programa principal
# ==============================
app = QApplication(sys.argv)

loader = QUiLoader()
file = QFile("gestor_backups/backup_p1.ui")

if not file.open(QFile.ReadOnly):
    print(f"Error: No s'ha pogut obrir el fitxer {file.fileName()}")
    sys.exit(-1)

window = loader.load(file)
file.close()

window.btn_iniciar.clicked.connect(iniciar_copia)

window.show()
sys.exit(app.exec())
