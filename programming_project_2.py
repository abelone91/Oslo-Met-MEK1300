
login_info = {
   'username': 'MEK1300',
   'password': 'Python'
}


def login_validation():

   print("*****QUIZ LOGIN ******")

   logged_in = False

   while logged_in == False:

      username = input('Username: ')
      password = input('Password: ')

      input_info = {
         'username': username,
         'password': password}

      print(input_info)
      print(login_info)

      if input_info['username'] != login_info['username']:
         print('Username is incorrect, please try again')


      elif input_info['password'] != login_info['password']:
         print("Password is incorrect, please try again ")

      else:
         print('***********Login successful, welcome to the quiz***********')
         logged_in = True

login_validation()

questions= [
   'Q1. What is the capital of Norway? \na.Bergen \nb.Oslo \nc.Stavanger \nd.Trondheim',
   'Q2.What is the currency of Norway? \na.Euro \nb.Pound \nc.Krone \nd.Deutsche Mark',
   'Q3.What is the largest city in Norway? \na.Oslo \nb.Stavanger \nc.Bergen \nd.Trondheim',
   'Q4.When is constitution day (the national day) of Norway? \na.27thMay \nb.17thMay \nc.17thApril \nd.27thApril',
   'Q5.What color is the background of the Norwegian flag? \na.Red \nb.White \nc.Blue \nd.Yellow',
   'Q6.How many countries does Norway border? \na.1 \nb.2 \nc.3 \nd.4',
   'Q7.What is the name of the university in Trondheim? \na.UiS \nb.UiO \nc.NMBU \nd.NTNU',
   'Q8.How long is the border between Norway and Russia? \na.96 km \nb.196 km \nc.296 km \nd.396 km',
   'Q9.Where in Norway is Stavanger? \na.North \nb.South \nc.South-west \nd.South-east',
   'Q10.From which Norwegian city did the world’s famous composer Edvard Grieg come? \na.Oslo \nb.Bergen \nc.Stavanger \nd.Tromsø'
]

answers =[
   'b',
   'c',
   'a',
   'b',
   'a',
   'c',
   'd',
   'b',
   'c',
   'b'
]


def quiz():

   points = 0
   i = 0
   wrong_answers = []

   for question in questions:
      print(question)
      print(i)
      answer = input('Enter your answer a,b,c or d: ')

      if answer == answers[i]:
         points += 1
         i +=1
      else:
         i += 1
         wrong_answers.append(i)

   print('your total points is', points, 'out of 10')
   print('you answered wrong on questions', wrong_answers)


   for k in wrong_answers:

      print(questions[(k-1)],'\n Correct answer is', answers[(k-1)])













quiz()
