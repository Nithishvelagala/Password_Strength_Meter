import json
import re

#Load dictionary words from a JSON file

def load_dictionary(json_file):
	
	with open(json_file,"r") as file:
		
		return set(json.load(file).keys())

def password_strength_check(password, dictionary_words):
	
	strength = 0

	feedback = []

#Checking length of the given password

	if len(password) >= 12:
		strength +=20
	elif len(password) >=8:
		strength +=10
	else:
		feedback.append("Your password must be at least 8 characters long")

#Checking the given password characters 

	if any(char.islower() for char in password):
		strength +=10
	else:
		feedback.append("Please include lowercase letter")
	
	if any(char.isupper() for char in password):
		strength +=10
	else:
		feedback.append("Please include uppercase letter")

	if any(char.isdigit() for char in password):
		strength +=10
	else:
		feedback.append("Add numbers")
	
	if any(char in "!@#$%^&*()_+|}{:?><~/.,';\][=-" for char in password):
		strength +=10
	else:
		feedback.append("Add special characters")


#Checking for the dictionary words in given password

	lower_password = password.lower()
	for word in dictionary_words:
		if word in lower_password:
			feedback.append(f"Aviod using dictionary wordslike '{word}'")
			break

#Checking for repeated characters in given password

	if re.search(r'(.)\1\1',password):
		feedback.append("Avoid repeated characters")


#Evaluating the strength of given password

	if strength >=40:
		level = "Strong Password"

	elif 20<= strength < 40 
		level = "Moderate Password"
	else:
		level = "Weak Password"

	return level, feedback

#Loading dictionary file

dictionary_file = "dictionary_words.json"
dictionary_words = load_dictionary(dictionary_file)


 