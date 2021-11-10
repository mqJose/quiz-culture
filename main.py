from tkinter import PhotoImage, Tk, Frame, Label, Button

# Clase Cuestionario
class Cuestionario:

    # Constructor
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    # Funcion que verifica si la respuesta es correcta
    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Correcto!")
            right += 1
        else:
            label = Label(view, text="Error!")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))

    # Funcion que pregunta la siguiente pregunta
    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question, fg="#6d57e4", font=("Arial", 14)).pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    # Funcion que deshace la vista
    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

# Funcion de preguntas
def askQuestion():
    global questions, window, index, button, right, number_of_questions
    if(len(questions) == index + 1):
        Label(window, text="Gracias por responder a las preguntas. " + str(right) + " de " + str(number_of_questions) + "\n preguntas respondidas correctamente").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

# Main: Consumo del archivo de preguntas.txt
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

#dimenciones de la ventana
window.geometry("1000x700")

#titulo pricipal
principal = Label(window, text="Cuestionario de Conocimiento General", fg="green", font=("Arial", 20))
principal.pack()

#titulo secundario
secundario = Label(window, text="Bienvenido al cuestionario tienes las siguientes Categorías elige una por favor", fg="black", font=("Arial", 14))
secundario.pack()

#boton para iniciar el cuestionario con imagen
imageArt = PhotoImage(file='./images/image-01.png')
button = Button(window, text="Arte", command=askQuestion, image=imageArt, padx=280, pady=217, bg="white", activebackground="white")
button.pack()

#renderizado de la ventana
window.mainloop()
