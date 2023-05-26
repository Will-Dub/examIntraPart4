####################################################################################
###  420-2G4 - Programmation orientée objet
###  Travail: Exercice  gestion de la pharmacie
###  Nom: William Dubuc
###  No étudiant: 2243756
###  No Groupe: 2
###  Description du fichier: Dialogue medicament
####################################################################################

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_medicament
from PyQt5 import QtWidgets


def cacher_labels_erreur(obj):
    """
    Cache tous les label erreur
    :param obj: objet Fenetre
    """
    obj.label_erreur_code_medicament_existe_pas.setVisible(False)
    obj.label_erreur_code_medicamen_existe.setVisible(False)
    obj.label_erreur_code_medicament_invalide.setVisible(False)
    obj.label_erreur_nom_commercial.setVisible(False)
    obj.label_erreur_dose_quot_max.setVisible(False)
    obj.label_erreur_nom_chimique.setVisible(False)
    obj.label_erreur_prix.setVisible(False)
    obj.label_erreur_duree_prise_max.setVisible(False)

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################


class Fenetremedicament(QtWidgets.QDialog, UI_PY.dialog_medicament.Ui_Dialog_Medicament):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetremedicament, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Médicament")
        cacher_labels_erreur(self)

