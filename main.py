from tkinter import Tk, Frame, Label, Button


class Cuestionario:
    def __init__(self, pregunta, respuesta, letraCorrecta):
        self.question = pregunta
        self.answers = respuesta
        self.correctLetter = letraCorrecta

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Correcto!")
            right += 1
        else:
            label = Label(view, text="Error!")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))

    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question).pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()


def askQuestion():
    global questions, window, index, button, right, number_of_questions
    if(len(questions) == index + 1):
        Label(window, text="Gracias por responder a las preguntas. " + str(right) + " de " + str(number_of_questions) + "\n preguntas respondidas correctamente").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()


questions = []
file = open("preguntas.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range(4):
        answers.append(file.readline())
    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Cuestionario(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

window = Tk()
button = Button(window, text="inicio de Cuestionario", command=askQuestion)
button.pack()
window.mainloop()
