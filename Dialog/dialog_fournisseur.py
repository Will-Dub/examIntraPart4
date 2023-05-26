####################################################################################
###  420-2G4 - Programmation orientée objet
###  Travail: Exercice  gestion de la pharmacie
###  Nom: William Dubuc
###  No étudiant: 2243756
###  No Groupe: 2
###  Description du fichier: Dialogue fournisseur
####################################################################################

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_fournisseur
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Classes.Patient import Patient
from Classes.Fournisseur import Fournisseur


def cacher_labels_erreur(obj):
    """
    Cache tous les label erreur
    :param obj: objet Fenetre
    """
    obj.label_erreur_code_fournisseur.setVisible(False)
    obj.label_erreur_nom_compagnie.setVisible(False)


def refresh_comboBox_patient(obj):
    obj.comboBox_numero_patient.clear()
    for i in Patient.ls_patients:
        obj.comboBox_numero_patient.addItem(i.Numero_patient)

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################


class Fenetrefournisseur(QtWidgets.QDialog, UI_PY.dialog_fournisseur.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetrefournisseur, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Fournisseur")
        cacher_labels_erreur(self)
        refresh_comboBox_patient(self)

        self.ls_patient_listView = []
        self.model = QStandardItemModel()
        self.model.clear()


    @pyqtSlot()
    def on_pushButton_ajouter_patient_listview_clicked(self):
        cacher_labels_erreur(self)
        current_patient = None
        for i in Patient.ls_patients:
            if i.Numero_patient == self.comboBox_numero_patient.currentText():
                current_patient = i

        if current_patient is None:
            return

        if current_patient in self.ls_patient_listView:
            return

        item = QStandardItem(current_patient.Numero_patient + " : " + current_patient.Nom + " " + current_patient.Prenom)
        self.model.appendRow(item)
        self.listView_list_patients.setModel(self.model)
        self.ls_patient_listView.append(current_patient)
        refresh_comboBox_patient(self)


    @pyqtSlot()
    def on_pushButton_serialiser_clicked(self):
        cacher_labels_erreur(self)

        fournisseur_temp = Fournisseur()

        fournisseur_temp.Code_fournisseur = self.lineEdit_code_fournisseur.text()
        fournisseur_temp.Nom_compagnie = self.lineEdit_nom_compagnie.text()

        if fournisseur_temp.Code_fournisseur == "":
            self.label_erreur_code_fournisseur.setVisible(True)

        if fournisseur_temp.Nom_compagnie == "":
            self.label_erreur_nom_compagnie.setVisible(True)

        if fournisseur_temp.Code_fournisseur != "" and fournisseur_temp.Nom_compagnie != "":
            Fournisseur.ls_fournisseur.append(fournisseur_temp)
            for i in self.ls_patient_listView:
                fournisseur_temp.Ls_patient.append(i)

            fournisseur_temp.serialiserFournisseur(fournisseur_temp.Code_fournisseur + ".json")


