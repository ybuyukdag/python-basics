#QUESTİON

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self,answer):
        return self.answer == answer

#QUİZ
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]
         
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("-" + q)

        answer = input("cevap: ")
        self.guess(answer)
        self.loadQuestions()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestions(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()
            self.displayProgress()
    
    def showScore(self):
        print("Score", self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionsNumber = self.questionIndex + 1

        if questionsNumber > totalQuestion:
            print("Quiz bitti.")
        else:
            print(f'Question {questionsNumber} of {totalQuestion}'.center(100,'*'))

q1 = Question("Türkiye'nin başkenti neresidir?", ["Ankara","İzmir","İstanbul","Edirne"], "Ankara")
q2 = Question("Türkiye'nin en az nüfuslu ili hangisidir?", ["Burdur","Bartın","Kilis","Tunceli"], "Tunceli")
q3 = Question("Türkiye'nin en büyük dağı hangisidir?", ["Süphan","Erciyes","Ağrı","Uludağ"], "Ağrı")

questions = [q1, q2 , q3]

quiz = Quiz(questions)

quiz.loadQuestions()
