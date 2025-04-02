from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QMessageBox, QLabel, QHBoxLayout, QVBoxLayout, QGroupBox, QSpinBox, QPushButton, QButtonGroup
from random import shuffle

window = QWidget()

btn_Next = QPushButton("Continue")
btn_Menu = QPushButton("Menu")
btn_Rest = QPushButton("Rest")

rb_ans1 = QRadioButton("1")
rb_ans2 = QRadioButton("2")
rb_ans3 = QRadioButton("3")
rb_ans4 = QRadioButton("4")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rb_ans1)
RadioGroup.addButton(rb_ans2)
RadioGroup.addButton(rb_ans3)
RadioGroup.addButton(rb_ans4)

lb_question = QLabel('Запитання')
lb_rest = QLabel('хвилин')
lb_result = QLabel('Правильно')
lb_right_answer = QLabel('відповідь')

sp_rest = QSpinBox()
gb_question = QGroupBox('Варіанти відповідей')


RadioGroupBox = QGroupBox("Answers:")
RadioGroup = QButtonGroup()

v_rbox_line_1 = QVBoxLayout()
v_rbox_line_2 = QVBoxLayout()
h_rbox_line_1 = QHBoxLayout()

v_rbox_line_1.addWidget(rb_ans1)
v_rbox_line_1.addWidget(rb_ans2)

v_rbox_line_2.addWidget(rb_ans3)
v_rbox_line_2.addWidget(rb_ans4)

h_rbox_line_1.addLayout(v_rbox_line_1)
h_rbox_line_1.addLayout(v_rbox_line_2)

gb_question.setLayout(h_rbox_line_1)
gb_answer = QGroupBox()

v1 = QVBoxLayout()
v1.addWidget(lb_result)
v1.addWidget(lb_right_answer)
gb_answer.setLayout(v1)


h_main_line_1 = QHBoxLayout()
h_main_line_2 = QHBoxLayout()
h_main_line_3 = QHBoxLayout()
h_main_line_4 = QHBoxLayout()
v_main_line_1 = QVBoxLayout()


h_main_line_1.addWidget(btn_Menu)
h_main_line_1.addStretch(1)
h_main_line_1.addWidget(btn_Rest)
h_main_line_1.addWidget(sp_rest)
h_main_line_1.addWidget(lb_rest)


h_main_line_2.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
h_main_line_3.addWidget(gb_answer)
h_main_line_3.addWidget(gb_question)
gb_answer.hide()

h_main_line_4.addStretch(1)
h_main_line_4.addWidget(btn_Next, stretch=2)
h_main_line_4.addStretch(1)


v_main_line_1.addLayout(h_main_line_1, stretch=1)
v_main_line_1.addLayout(h_main_line_2, stretch=2)
v_main_line_1.addLayout(h_main_line_3, stretch=8)
v_main_line_1.addLayout(h_main_line_4)
v_main_line_1.setSpacing(5)
window.setLayout(v_main_line_1)
window.resize(550, 450)