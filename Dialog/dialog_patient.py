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
    def on_pushButton_quitter_clicked(self):
        # fermer la fenêtre
        self.close()
