from PyQt5.QtWidgets import QLineEdit, QApplication, QWidget, QRadioButton, QMessageBox, QLabel, QHBoxLayout, QVBoxLayout, QGroupBox, QSpinBox, QPushButton, QButtonGroup

menu_win = QWidget() #основне вікно

lb_quest = QLabel('Введіть запитання:') #створюємо напис
lb_right_ans = QLabel('Введіть вірну відповідь:') #створюємо напис
lb_wrong_ans1 = QLabel('Введіть першу хибну відповідь:') #створюємо напис
lb_wrong_ans2 = QLabel('Введіть другу хибну відповідь:') #створюємо напис
lb_wrong_ans3 = QLabel('Введіть третю хибну відповідь:') #створюємо напис

le_question = QLineEdit() #створюємо поле для вводу
le_right_ans = QLineEdit() #створюємо поле для вводу
le_wrong_ans1 = QLineEdit() #створюємо поле для вводу
le_wrong_ans2 = QLineEdit() #створюємо поле для вводу
le_wrong_ans3 = QLineEdit() #створюємо поле для вводу

lb_header_stat = QLabel('Статистика:') #створюємо напис
lb_header_stat.setStyleSheet('font-size: 19px; font-weight: bold') #налаштовуємо шрифт

lb_statistic = QLabel()

vl_labels = QHBoxLayout()
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)

vl_LineEdits = QHBoxLayout()
vl_LineEdits.addWidget(le_question)
vl_LineEdits.addWidget(le_right_ans)
vl_LineEdits.addWidget(le_wrong_ans1)
vl_LineEdits.addWidget(le_wrong_ans2)
vl_LineEdits.addWidget(le_wrong_ans3)

h1_question = QHBoxLayout()
h1_question.addLayout(vl_labels)
h1_question.addLayout(vl_LineEdits)

btn_back = QPushButton('Назад')
btn_add_question = QPushButton('Додати запитання')
btn_clear = QPushButton('Очистити')
h1_buttons = QHBoxLayout()
h1_buttons.addWidget(btn_add_question)
h1_buttons.addWidget(btn_clear)

vl_res = QHBoxLayout()
vl_res.addLayout(h1_question)
vl_res.addLayout(h1_buttons)
vl_res.addWidget(lb_header_stat)
vl_res.addWidget(lb_statistic)
vl_res.addWidget(btn_back)

menu_win.setLayout(vl_res)
menu_win.resize(550,450)

