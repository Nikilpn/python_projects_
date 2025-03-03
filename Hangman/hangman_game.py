import hangman_stages
import word_file
import random
word_list=["apple","beautiful","potato"]
lives=6


chosen_word=random.choice(word_file.words) #generate a random word(apple)
print(chosen_word)

display=[]
for i in range(len(chosen_word)):  #generating (_____) as how much letter present in the letter
    display+="_"
print(display)


game_over=False

while not game_over:#while loops iterates for whether a condition becomes true

    guessed_letter = input("guessed letter :").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]

        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)


    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("you lose")
    if '_' not in display:
        game_over=True
        print("You win")
    print(hangman_stages.stages[lives])

