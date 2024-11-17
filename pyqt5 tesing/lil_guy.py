import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("lil guy app")
        
        #image of otje
        image = QLabel()
        image.setPixmap(QPixmap('pyqt5 tesing\otje.jpg'))
        #scale with window
        image.setScaledContents(True)

        #checkbox
        checkbox = QCheckBox()
        checkbox.setText("i like this lil guy")
        checkbox.setCheckState(Qt.Checked)
        #connect to show state method
        checkbox.stateChanged.connect(self.show_box_state)

        #combobox
        #using self to make it modifyable bt non-init methods
        self.combobox = QComboBox()
        self.combobox.addItems(["why do you not like him?","big mouth","harbors a hidden evil", "other"])
        self.combobox.setEditable(True)
        self.combobox.setInsertPolicy(QComboBox.InsertAtBottom)

        #slider label
        self.slabel = QLabel("Enter your hatred level:")

        #slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setSingleStep(1)
        self.slider.sliderMoved.connect(self.set_hatred)

        #Layout is used by central widget to define layout
        layout = QVBoxLayout()

        #add horizontal layout to layout
        Hlayout = QHBoxLayout()

        #add widgets to layouts:
        layout.addWidget(image)
        Hlayout.addWidget(checkbox)
        Hlayout.addWidget(self.combobox)

        #adding sub layout
        layout.addLayout(Hlayout)

        #vertical widgets below sub layout
        layout.addWidget(self.slabel)
        layout.addWidget(self.slider)

        #central widget takes up full space in window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        #default visibilities
        self.combobox.setVisible(False)
        self.slabel.setVisible(False)
        self.slider.setVisible(False)

    #prints state of checkbox  
    # also changes widget visibility  
    def show_box_state(self, s,):
        # print state of check
        print(s == Qt.Checked)

        #change checkbox visibility
        if s == Qt.Checked:
            self.combobox.setVisible(False)
            self.slabel.setVisible(False)
            self.slider.setVisible(False)
        else:  
            self.combobox.setVisible(True)
            self.slabel.setVisible(True)
            self.slider.setVisible(True)

    def set_hatred(self ,s,):
        self.slabel.setText("Enter your hatred level: " + str(s)+"%")

        
              
   
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()