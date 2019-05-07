#importing relevant modules
import sys
import pandas as pd   #creating shortcut to panda module via nametag pd
from qtpy import QtWidgets   #using the qt-creator
from ui.mainwindow import Ui_MainWindow
import csv #module for comma seperated values(excel files)

app = QtWidgets.QApplication(sys.argv)

#loading data for operations and storing it in lists
file = open("data/GeographicalEurope.csv", "r", newline="") #opens the file GeographicalEurope
first = file.readline().strip().split(";") #get the first line from file

index=[] #we need index for DataFrame structure(see below)
for i in range(0, 47):
    index.append(i)

countries =[]
capitol =[]
space =[]
inhabit =[]
inhabits_per_km =[]
bip =[]
bip_per_capita =[]
region =[]

for line in file:
    countries.append(line.strip().split(";")[0])
    capitol.append(line.strip().split(";")[1])
    space.append(line.strip().split(";")[2])
    inhabit.append(line.strip().split(";")[3])
    inhabits_per_km.append(line.strip().split(";")[4])
    bip.append(line.strip().split(";")[5])
    bip_per_capita.append(line.strip().split(";")[6])
    region.append(line.strip().split(";")[7])

dp = pd.DataFrame({first[0]: countries,
                    first[1]: capitol,
                    first[2]: space,
                    first[3]: inhabit,
                    first[4]: inhabits_per_km,
                    first[5]: bip,
                    first[6]: bip_per_capita,
                    first[7]: region},
                    index)
#country codes for easier handeling when operating on DataFrame
country_codes ={"Albania" : 0,
                "Andorra" : 1,
                "Austria" : 2,
                "Belarus" : 3,
                "Belgium" : 4,
                "Bosnia and Herzegowina" : 5,
                "Bulgaria" : 6,
                "Croatia" : 7,
                "Czech Republic" : 8,
                "Denmark" : 9,
                "Estonia" : 10,
                "Finland" : 11,
                "France" : 12,
                "Germany" : 13,
                "Greece" : 14,
                "Hungary" : 15,
                "Iceland" : 16,
                "Ireland" : 17,
                "Italy" : 18,
                "Kazakhstan" : 19,
                "Kosovo" : 20,
                "Latvia" : 21,
                "Liechtenstein" : 22,
                "Lithuania" : 23,
                "Luxembourg" : 24,
                "Malta" : 25,
                "Moldova" : 26,
                "Monaco" : 27,
                "Montenegro" : 28,
                "Netherlands" : 29,
                "Northern Macedonia" : 30,
                "Norway" : 31,
                "Poland" : 32,
                "Portugal " : 33,
                "Romania" : 34,
                "Russia" : 35,
                "San Marino" : 36,
                "Serbia" : 37,
                "Slovakia" : 38,
                "Slovenia" : 39,
                "Spain" : 40,
                "Sweden" : 41,
                "Switzerland" : 42,
                "Turkey" : 43,
                "Ukraine" : 44,
                "United Kingdom" : 45,
                "Vatican" : 46,}
file.close()

#class MainWindow, setting up the ui (userinterface)
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Wikipedia")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.eigenschaft_combo.addItem("All Data")
        #routine for filling combo boxes with choices for data
        with open("data/GeographicalEurope.csv", "r", newline="") as file: #"data/dateneuropa.txt"
            first_line = file.readline().strip().split(";")
            for choice in first_line:
                if choice == "ï»¿Country": #we need to skip the first Item, as its not useful
                    continue
                self.ui.eigenschaft_combo.addItem(choice)

        #routine for filling combo boxes with choices of countries
        with open("data/GeographicalEurope.csv", "r", newline="") as file:
            file.readline()
            for line in file:
                line_splitted = line.strip().split(";")
                self.ui.land_combo.addItem(line_splitted[0])

        #connecting the signals to slots, so their functionality is provided
        self.ui.ok.clicked.connect(self.onOKclicked)
        self.ui.abbr.clicked.connect(self.onAbbrclicked)
        self.ui.close_button.clicked.connect(self.onCloseclicked)

    def onOKclicked(self): #shows data in textBrowser
        country = self.ui.land_combo.currentText()
        self.ui.ausgabe_label.setText(country +":")
        attr = self.ui.eigenschaft_combo.currentText() #attr = attribut
        self.ui.label_2.setText(attr +":")

        if attr == "All Data":
            self.ui.label_2.setText("Capitol, Area in km^2, Inhabitants, Inhabitants per km^2, GDP (bn USD, 2016), GDP per capita (bn USD, 2016), Region:")
            self.ui.textBrowser.setPlainText(dp.at[country_codes[country], "Capitol"])
            self.ui.textBrowser.append(dp.at[country_codes[country], "Area in km2"])
            self.ui.textBrowser.append(dp.at[country_codes[country], "Inhabitants"])
            self.ui.textBrowser.append(dp.at[country_codes[country], "Inhabitants per km2"])
            self.ui.textBrowser.append(dp.at[country_codes[country], "GDP (bn USD, 2016)"])
            self.ui.textBrowser.append(dp.at[country_codes[country], "GDP per capita (bn USD, 2016)"])
            self.ui.textBrowser.append(dp.at[country_codes[country], "Region"])


        elif attr == "Inhabitants":
            self.ui.textBrowser.setPlainText(dp.at[country_codes[country], attr])
        elif attr == "Area in km2":
            self.ui.textBrowser.setPlainText(dp.at[country_codes[country], attr])
        elif attr == "Capitol":
            self.ui.textBrowser.setPlainText(dp.at[country_codes[country], attr])
        elif attr == "Inhabitants per km2":
            self.ui.textBrowser.setPlainText(dp.at[country_codes[country], attr])
        elif attr == "GDP (bn USD, 2016)":
            self.ui.textBrowser.setPlainText(dp.at[country_codes[country], attr])
        elif attr == "GDP per capita (bn USD, 2016)":
            self.ui.textBrowser.setPlainText(dp.at[country_codes[country], attr])
        elif attr == "Region":
            self.ui.textBrowser.setPlainText(dp.at[country_codes[country], attr])

    def onAbbrclicked(self): #clears textBrowser
        self.ui.ausgabe_label.clear()
        self.ui.label_2.clear()
        self.ui.textBrowser.clear()

    def onCloseclicked(self): #closes application
        self.close()

window = MainWindow()
window.show()
sys.exit(app.exec_())