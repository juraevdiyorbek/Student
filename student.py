from PyQt5.QtWidgets import (QApplication, 
                            QWidget, 
                            QLineEdit, 
                            QRadioButton, 
                            QHBoxLayout,
                            QPushButton, 
                            QFormLayout, 
                            QComboBox, 
                            QSpinBox
                        )
class Student(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet("font-size: 30px;")
        self.init_ui()

    def init_ui(self):
        self.fname_input = QLineEdit(self)
        self.lname_input = QLineEdit(self)

        self.gender_male = QRadioButton("Male" ,self)
        self.gender_female = QRadioButton("Female" ,self)

        self.age = QSpinBox(self)
        self.age.setMinimum(16)
        self.age.setMaximum(50)

        self.regions = QComboBox(self)
        self.regions.addItems(["Toshkent","Andijon","Farg'ona","Xorazm","Samarqand","Navoiy"])
        self.phoneNum_input = QLineEdit(self)
        self.faculty_input = QLineEdit(self)

        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.save)
        hbox = QHBoxLayout()
        hbox.addWidget(self.gender_male)
        hbox.addWidget(self.gender_female)

        layout = QFormLayout()
        layout.addRow('First name:', self.fname_input)
        layout.addRow('Last name:', self.lname_input)
        layout.addRow('Sex:', hbox)
        
        layout.addRow('Age:', self.age)
        layout.addRow('Region:', self.regions)
        layout.addRow('Phone number:', self.phoneNum_input)
        layout.addRow('Faculty:', self.faculty_input)
        layout.addRow('', self.save_btn)
    
        
        self.setLayout(layout)

    def save(self):
        name = self.fname_input.text()
        surname = self.lname_input.text()
        gender  = "Male" if self.gender_male.isChecked() else "Female"
        age = self.age.value()  
        region = self.regions.currentText()
        phone = self.phoneNum_input.text()
        faculty = self.faculty_input.text()
        file_name = f"{surname}.txt"
        with open(file_name,"w") as file:
            file.write(f"Name : {name}\nSurname : {surname}\nGender: {gender}\nAge : {age}\nRegion : {region} \nPhone : {phone} \nFaculty : {faculty} \n")

        self.close()
app = QApplication([])
classs = Student()
classs.show()
app.exec_()
