from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QMessageBox, QLabel, QHBoxLayout, QVBoxLayout, QGroupBox, QSpinBox, QPushButton, QButtonGroup
from random import shuffle, choice
from time import sleep

app = QApplication([])

from menu_window import*
from main_window import*

window = QWidget()
window.resize(1000,700)
window.move(1000,299)
window.setWindowTitle("Memory Card:")
window.show()

class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.correct = 0
        self.attempts = 0

    def got_right(self):
        self.correct += 1
        self.attempts += 1

    def got_wrong(self):
        self.attempts += 1

q1 = Question('Яблуко', 'Apple', 'Application', 'Aplause', 'Apply')
q2 = Question('Дім', 'House', 'Horse', 'Hobby', 'Hear')
q3 = Question('Миша', 'Mouse', 'Mouth', 'Muse', 'Museum')
q4 = Question('Число', 'Number', 'Digit', 'Summary', 'Amount')

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4]

def new_question():
   global cur_q
   cur_q = choice(questions)
   lb_question.setText(cur_q.question)
   lb_right_answer.setText(cur_q.answer)
   shuffle(radio_buttons)


   radio_buttons[0].setText(cur_q.wrong_answer1)
   radio_buttons[1].setText(cur_q.wrong_answer2)
   radio_buttons[2].setText(cur_q.wrong_answer3)
   radio_buttons[3].setText(cur_q.answer)


new_question()


def check():
   RadioGroup.setExclusive(False)
   for answer in radio_buttons:
       if answer.isChecked():
           if answer.text() == lb_right_answer.text():
               cur_q.got_right()
               lb_result.setText('Вірно!')
               answer.setChecked(False)
               break
   else:
       lb_result.setText('Не вірно!')
       cur_q.got_wrong()
   RadioGroup.setExclusive(True)


def click_ok():
   if btn_Next.text() == 'Відповісти':
       check()
       gb_question.hide()
       gb_answer.show()
       btn_Next.setText('Наступне запитання')
   else:
       new_question()
       gb_question.show()
       gb_answer.hide()
       btn_Next.setText('Відповісти')

btn_Next.clicked.connect(click_ok)


def back_menu():
    menu_win.hide()
    window.show()

btn_back.clicked.connect(back_menu)


def right():
    message = QMessageBox()
    message.resize(700,400)
    message.setWindowTitle("Congrats!        ")
    message.setText("Right!")
    message.exec_()

def wrong():
    message = QMessageBox()
    message.resize(700,400)
    message.setWindowTitle(":(")
    message.setText("Wrong!")
    message.exec_()

def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show

btn_Rest.clicked.connect(rest)

def menu_generations():
    if cur_q.attempts == 0:
        c = 0 
    else:
        c = (cur_q.correct/cur_q.attempts)*100

    text = f'Разів відповіли: {cur_q.attemps}\n'\
           f'Вірних відповіли: {cur_q.correct}\n'\
           f'Успішність: {round(c,2)}%'
    lb_statistic.setText(text)
    menu_win.show()
    window.hide()

btn_Menu.clicked.connect(menu_generations)

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(),
                     le_wrong_ans1.text(), le_wrong_ans2.text(),
                     le_wrong_ans3.text())
    questions.append(new_q)
    clear()

btn_add_question.clicked.connect(add_question)

window.show()
app.exec_()