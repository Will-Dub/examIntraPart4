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
from Classes.Fournisseur import Fournisseur
from PyQt5.QtGui import QStandardItemModel, QStandardItem


def refresh_comboBox_fournisseur(obj):
    obj.comboBox_nom_fournisseur.clear()
    for i in Fournisseur.ls_fournisseur:
        obj.comboBox_nom_fournisseur.addItem(i.Code_fournisseur)

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
        refresh_comboBox_fournisseur(self)

    @pyqtSlot()
    def on_pushButton_afficher_clicked(self):
        model = QStandardItemModel()
        self.listView_list_patients_fournisseur.setModel(model)
        model.clear()

        fournisseur_temp = None

        for i in Fournisseur.ls_fournisseur:
            if i.Code_fournisseur == self.comboBox_nom_fournisseur.currentText():
                fournisseur_temp = i
                break

        if fournisseur_temp is None:
            return

        for i in fournisseur_temp.Ls_patient:
            item = QStandardItem(i.Numero_patient + " - " + i.Nom + " " + i.Prenom)
            model.appendRow(item)

