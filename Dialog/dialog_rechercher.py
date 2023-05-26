####################################################################################
###  420-2G4 - Programmation orientée objet
###  Travail: Exercice  gestion de la pharmacie
###  Nom: William Dubuc
###  No étudiant: 2243756
###  No Groupe: 2
###  Description du fichier: Dialogue recherche
####################################################################################

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_recherche
from PyQt5 import QtWidgets

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetrerechercher(QtWidgets.QDialog, UI_PY.dialog_recherche.Ui_Dialog_Recherche):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetrerechercher, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Rechercher")

