from tkinter import *
import tkinter.font as font

# Read questions and answers from files

questions_txt = open('Milktest/!questions.txt', 'r', encoding='utf-8')
questions = questions_txt.read().splitlines()
questions_txt.close()
questionCount = len(questions)

answers_txt = open('Milktest/!answers.txt', 'r', encoding='utf-8')
answers = answers_txt.read().splitlines()
answers_txt.close()
assert(questionCount == len(answers)), 'Number of questions and answers should match!'

questionNum = 0
correctCount = 0

# Create UI

window = Tk()

window.geometry('300x500')
window.title('Milk quiz')
window.resizable(width=False, height=False)
window['background']='#28bf94'

questionlabel = Label(
    window, 
    text = questions[0],
    bg = "#28bf94",
    font = ('Arial',30)
)
questionlabel.place(y=100, x= 50)

answerA = Button(
    window,
    text='A',
    font=20,
    width=10,
    height=2,
    command=(lambda: checkAnswer('A'))
)
answerA.place(x=20, y=300)

answerB = Button(
    window,
    text='B',
    font=15,
    width=10,
    height=2,
    command=(lambda: checkAnswer('B'))
)
answerB.place(x=160, y=300)

answerC = Button(
    window,
    text='C',
    font=20,
    width=10,
    height=2,
    command=(lambda: checkAnswer('C'))
)
answerC.place(x=20, y=400)

answerD = Button(
    window,
    text='D',
    font=20,
    width=10,
    height=2,
    command=(lambda: checkAnswer('D'))
)
answerD.place(x=160, y=400)



def checkAnswer(answer):
    global questionNum
    global correctCount

    answeredCorrect = answers[questionNum] == answer

    print(questionNum, answer, 'Correct' if answeredCorrect else 'Wrong')

    if answeredCorrect:
        correctCount += 1

    questionNum = questionNum + 1

    if questionNum < questionCount:
        questionlabel.config(text = questions[questionNum])
    else:
        questionlabel.config(text = "Score: %s/%s" % (correctCount, questionCount))
        answerA.destroy()
        answerB.destroy()
        answerC.destroy()
        answerD.destroy()
        print('Yes sirr')


window.mainloop()