from word_generator import*

choice = 2001

while (choice > 2000):
    choice = int(input("How many words do you want to generate? [ Less than 2000 :< ]\n>>> "))

print((generate_str(choice)))
