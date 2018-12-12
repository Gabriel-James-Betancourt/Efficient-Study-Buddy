import json
import random

class FlashCard:
	"""
	Stores terms and definitions that the user has inputed
	(user can input as many as they want, my file contains 
	three for simplicity's sake) in a one to one ratio. The 
	class has methods that carry out the program's purpose.
	"""

	def __init__(self, file_name):		
		"""
		Taking the file name converting into a dictionary using json.loads()
		
		Parameters
		----------
		file_name : string
			name of file that has the terms/definitions, gets called
		"""

		terms_file = open(file_name, "r")
		self.terms_dictionary = json.loads(terms_file.read())		
		self.number_of_wrong_answers = {}
		self.user_guess = ""


	def check_term(self, definition, term):
		"""
		Check term provides the term's definition to the user,
		simultaneously prompting the user to type in the term,
		THEN checks if the term matches the value  of the provided
		definition 

		Parameters
		----------
		definition : string
			the key in the dictionary, to be displayed to user
		term : string
			the value in the dictionary, to be typed in by user

		Returns
		-------
		True : boolean
			user typed in the term that correctly matched its definition
		False : boolean
			User typed in the incorrect term that did not correspond to its definition
		"""

		self.user_guess = input(definition + '\nType Term: ') 
		if term in self.user_guess.lower():
			return True 
		else:
			return False

	
	def random_term_selector(self):
		"""
		This function randomly loops through all the terms 
		Calling the check_term function
		"""

		random_terms = list(self.terms_dictionary.items())
		random.shuffle(random_terms)
		for definition,term in random_terms:
			if self.check_term(definition, term):
				print("Correct")
			else:
				print("The Answer is Actually: " + term)
	
	
	def answer_dependent_selector(self):
		"""
		Based on the number of times a user names a definition
		wrong, this function assigns that number to the definition
		within a dictionary. Based on this assignment, the probability 
		of that term being called increases. The probability does not 
		continue to increase after 3 wrong answers. When a user inputs 
		the correct term, it resets the term's number of wrong answers 
		back to zero."
		"""

		while (self.user_guess != "exit"):
			definition = random.choice(list(self.terms_dictionary.keys()))
			term = self.terms_dictionary[definition]


			if definition not in self.number_of_wrong_answers or self.number_of_wrong_answers[definition] == 0: 
				definition = random.choice(list(self.terms_dictionary.keys()))
				term = self.terms_dictionary[definition]
				if self.check_term(definition, term):
					print("Correct")
				else:
					if (self.user_guess == "exit"):
						print("bye!")
					else:
						print("Wrong")
						self.number_of_wrong_answers[definition] = 1	


			elif self.number_of_wrong_answers[definition] == 1:
				if random.random() < .4:
					if self.check_term(definition, term):
						print("Correct")
						self.number_of_wrong_answers[definition] = 0
					else:
						if (self.user_guess == "exit"):
							print("bye!")
						else:
							print("Wrong")
							self.number_of_wrong_answers[definition] += 1


			elif self.number_of_wrong_answers[definition] == 2:
				if random.random() < .5:
					if self.check_term(definition, term):
						print("Correct")
						self.number_of_wrong_answers[definition] = 0
					else:
						if (self.user_guess == "exit"):
							print("bye!")
						else:
							print("Wrong")
							self.number_of_wrong_answers[definition] += 1


			elif self.number_of_wrong_answers[definition] >= 3:
				if random.random() < .6:
					if self.check_term(definition, term):
						print("Correct")
						self.number_of_wrong_answers[definition] = 0
					else:
						if (self.user_guess == "exit"):
							print("bye!")
						else:
							print("Wrong")
							self.number_of_wrong_answers[definition] += 1
