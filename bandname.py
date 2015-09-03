import random


titles = ["Huge","sour","steamy","sweaty","stupid",
			"Greasy","tangy","smelly","small",
				"cool","pickeled","prickly"
					"blue",]
					
adjs = ["tiny","fat","shiny","ecclectic","fluffy","bright",
			"corrupt","aggresive","alarming","amazing","magical"
					,"red","faboules","fergalicous","dangerous",
					]
					
plural_nouns = ["apples", "oragens", "kwiwis","clemeanteisn",
				"wildebeast", "mammonts", "rabbits", "slotsl", "crashes","chicken","lordGaben"
				"cowboys","csgo","love","chicken","chanlder","dog","lol","ayy lmao",
				]

def title():
	return random.choice(titles)
def adj():
	return random.choice(adjs)
def plural_noun():
	return random.choice(plural_nouns)

def main():
	while True:
		name = raw_input("Enter Your name\n")
		if name == "q":
			break
		random.seed(name)
		print title(), name, "and the", adj(), plural_noun()




main()	