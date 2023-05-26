####################################################################################
###  420-2G4 - Programmation orientée objet
###  Travail: Exercice  gestion de la pharmacie
###  Nom: William Dubuc
###  No étudiant: 2243756
###  No Groupe: 2
###  Description du fichier: Dialogue patient
####################################################################################
#
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_patient
from PyQt5 import QtWidgets
from Classes.Patient import Patient

def cacher_labels_erreur(obj):
    """
    Cache tous les label erreur
    :param obj: objet Fenetre
    """
    obj.label_erreur_num_patient_existe.setVisible(False)
    obj.label_errreur_num_patient_existe_pas.setVisible(False)
    obj.label_erreur_num_patient_valider.setVisible(False)
    obj.label_erreur_nom_patient.setVisible(False)
    obj.label_erreur_prenom_patient.setVisible(False)
    obj.label_erreur_date_naiss.setVisible(False)

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################


class Fenetrepatient(QtWidgets.QDialog, UI_PY.dialog_patient.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetrepatient, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Patient")
        cacher_labels_erreur(self)

    @pyqtSlot()
    def on_pushButton_Ajouter_patient_clicked(self):
        cacher_labels_erreur(self)

        patient_temp = Patient()

        bool_ajouter_etudiant_existe = False

        for i in Patient.ls_patients:
            if i.Numero_patient == self.lineEdit_numero_patient.text():
                bool_ajouter_etudiant_existe = True

        patient_temp.Numero_patient = self.lineEdit_numero_patient.text()
        patient_temp.Nom = self.lineEdit_nom_patient.text().capitalize()
        patient_temp.Prenom = self.lineEdit_prenom_patient.text().capitalize()
        patient_temp.Date_naiss = self.dateEdit_date_naiss_patient.date().toPyDate()

        if bool_ajouter_etudiant_existe is True:
            self.label_erreur_num_patient_existe.setVisible(True)
            self.lineEdit_numero_patient.clear()

        if patient_temp.Numero_patient == "":
            self.label_erreur_num_patient_valider.setVisible(True)
            self.lineEdit_numero_patient.clear()

        if patient_temp.Nom == "":
            self.label_erreur_nom_patient.setVisible(True)
            self.lineEdit_nom_patient.clear()

        if patient_temp.Prenom == "":
            self.label_erreur_prenom_patient.setVisible(True)
            self.lineEdit_prenom_patient.clear()

        if patient_temp.Date_naiss is None:
            self.label_erreur_date_naiss.setVisible(True)
            self.dateEdit_date_naiss_patient.clear()

        if bool_ajouter_etudiant_existe is False and patient_temp.Numero_patient != "" and patient_temp.Nom != "" and patient_temp.Prenom != "" and patient_temp.Date_naiss is not None:
            Patient.ls_patients.append(patient_temp)
            self.dateEdit_date_naiss_patient.clearMinimumDate()
            self.lineEdit_prenom_patient.clear()
            self.lineEdit_nom_patient.clear()
            self.lineEdit_numero_patient.clear()

    @pyqtSlot()
    def on_pushButton_supprimer_patient_clicked(self):
        cacher_labels_erreur(self)

        etudiant_a_supprimer = None

        for i in Patient.ls_patients:
            if i.Numero_patient == self.lineEdit_numero_patient.text():
                etudiant_a_supprimer = i

        if etudiant_a_supprimer is None:
            self.label_errreur_num_patient_existe_pas.setVisible(True)
            self.lineEdit_numero_patient.clear()
        else:
            Patient.ls_patients.remove(etudiant_a_supprimer)
            self.lineEdit_numero_patient.clear()
