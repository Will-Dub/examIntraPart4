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
from Classes.Medicament import Medicament
from Classes.Analgesique import Analgesique
from Classes.Antibiotique import Antibiotique
from Classes.Corticoide import Corticoide


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


def cacher_propriete(obj):
    obj.label_duree_prise_maximale.setDisabled(True)
    obj.label_antibiotique.setDisabled(True)
    obj.lineEdit_duree_prise_max.setDisabled(True)

    obj.label_dose_quot_max.setDisabled(True)
    obj.label_analgesique.setDisabled(True)
    obj.lineEdit_dose_quot_max.setDisabled(True)

    obj.label_corticoide.setDisabled(True)
    obj.label_effet_medicament.setDisabled(True)
    obj.comboBox_effet_medicament.setDisabled(True)

    obj.lineEdit_duree_prise_max.clear()
    obj.lineEdit_dose_quot_max.clear()
    obj.comboBox_effet_medicament.setCurrentIndex(0)

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
        self.comboBox_categorie.currentIndexChanged.connect(self.choisirCategorie)
        self.choisirCategorie()

    def choisirCategorie(self):
        cacher_propriete(self)
        if self.comboBox_categorie.currentText() == "Antibiotique":
            self.label_duree_prise_maximale.setDisabled(False)
            self.label_antibiotique.setDisabled(False)
            self.lineEdit_duree_prise_max.setDisabled(False)
        elif self.comboBox_categorie.currentText() == "Analgésique":
            self.label_dose_quot_max.setDisabled(False)
            self.label_analgesique.setDisabled(False)
            self.lineEdit_dose_quot_max.setDisabled(False)
        elif self.comboBox_categorie.currentText() == "Corticoïde":
            self.label_corticoide.setDisabled(False)
            self.label_effet_medicament.setDisabled(False)
            self.comboBox_effet_medicament.setDisabled(False)

    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        cacher_labels_erreur(self)

        if self.comboBox_categorie.currentText() == "Antibiotique":
            medicament_temp = Antibiotique()
            if self.lineEdit_duree_prise_max.text().isnumeric():
                medicament_temp.Duree_prix_max = int(self.lineEdit_duree_prise_max.text())
            medicament_temp.Categorie = "Antibiotique"
        elif self.comboBox_categorie.currentText() == "Analgésique":
            medicament_temp = Analgesique()
            if self.lineEdit_dose_quot_max.text().isnumeric():
                medicament_temp.Dose_quot_max = int(self.lineEdit_dose_quot_max.text())
            medicament_temp.Categorie = "Analgésique"
        elif self.comboBox_categorie.currentText() == "Corticoïde":
            medicament_temp = Corticoide()
            medicament_temp.Effet_medic = self.comboBox_effet_medicament.currentText()
            medicament_temp.Categorie = "Corticoïde"
        else:
            return

        bool_ajouter_medicament_existe = False
        for i in Medicament.ls_medicaments:
            if i.Code_medicament == self.lineEdit_code_medicament.text():
                bool_ajouter_medicament_existe = True
                break

        medicament_temp.Code_medicament = self.lineEdit_code_medicament.text()
        medicament_temp.Nom_chimique = self.lineEdit_nom_chimique.text()
        medicament_temp.Nom_commercial = self.lineEdit_nom_commercial.text()

        if self.lineEdit_prix.text().isnumeric() is True:
            medicament_temp.Prix = int(self.lineEdit_prix.text())

        if bool_ajouter_medicament_existe is True:
            self.label_erreur_code_medicamen_existe.setVisible(True)
            self.lineEdit_code_medicament.clear()

        if medicament_temp.Code_medicament == "":
            self.label_erreur_code_medicament_invalide.setVisible(True)
            self.lineEdit_code_medicament.clear()

        if medicament_temp.Nom_chimique == "":
            self.label_erreur_nom_chimique.setVisible(True)
            self.lineEdit_nom_chimique.clear()

        if medicament_temp.Nom_commercial == "":
            self.label_erreur_nom_commercial.setVisible(True)
            self.lineEdit_nom_commercial.clear()

        if medicament_temp.Prix == 0:
            self.label_erreur_prix.setVisible(True)
            self.lineEdit_prix.clear()

        # Verification des propriété de catégorie
        bool_propriete_categorie_valide = True

        if self.comboBox_categorie.currentText() == "Antibiotique":
            if medicament_temp.Duree_prix_max == 0:
                self.label_erreur_duree_prise_max.setVisible(True)
                self.lineEdit_duree_prise_max.clear()
                bool_propriete_categorie_valide = False

        if self.comboBox_categorie.currentText() == "Analgésique":
            if medicament_temp.Dose_quot_max == 0:
                self.label_erreur_dose_quot_max.setVisible(True)
                self.lineEdit_dose_quot_max.clear()
                bool_propriete_categorie_valide = False

        if bool_ajouter_medicament_existe is False and medicament_temp.Code_medicament != "" and \
            medicament_temp.Nom_chimique != "" and medicament_temp.Nom_commercial != "" and \
                medicament_temp.Prix != 0 and bool_propriete_categorie_valide is True:
            Medicament.ls_medicaments.append(medicament_temp)
            self.lineEdit_code_medicament.clear()
            self.lineEdit_code_medicament.clear()
            self.lineEdit_nom_chimique.clear()
            self.lineEdit_nom_commercial.clear()
            self.lineEdit_prix.clear()
            self.lineEdit_duree_prise_max.clear()
            self.lineEdit_dose_quot_max.clear()

    @pyqtSlot()
    def on_pushButton_rechercher_clicked(self):
        cacher_labels_erreur(self)
        medicament_recherche_obj = None

        for i in Medicament.ls_medicaments:
            if i.Code_medicament == self.lineEdit_code_medicament.text():
                medicament_recherche_obj = i
                break

        if medicament_recherche_obj is None:
            self.label_erreur_code_medicament_existe_pas.setVisible(True)
            return

        self.lineEdit_prix.setText(str(medicament_recherche_obj.Prix))
        self.lineEdit_nom_chimique.setText(medicament_recherche_obj.Nom_chimique)
        self.lineEdit_nom_commercial.setText(medicament_recherche_obj.Nom_commercial)
        self.comboBox_categorie.setCurrentText(medicament_recherche_obj.Categorie)

        if medicament_recherche_obj.Categorie == "Antibiotique":
            self.lineEdit_duree_prise_max.setText(str(medicament_recherche_obj.Duree_prix_max))
        elif medicament_recherche_obj.Categorie == "Analgésique":
            self.lineEdit_dose_quot_max.setText(str(medicament_recherche_obj.Dose_quot_max))
        elif medicament_recherche_obj.Categorie == "Corticoïde":
            self.comboBox_effet_medicament.setCurrentText(medicament_recherche_obj.Effet_medic)
