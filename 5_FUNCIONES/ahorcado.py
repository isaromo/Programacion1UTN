import random

lives = 6
defined_words = ["ARGENTINA", "ITALIA", "FRANCIA", "BOLIVIA", "BRASIL"]
random_word = random.choice(defined_words)
print(" ------- JUEGO DEL AHORCADO ------- ")

word_guess = ["_"]*len(random_word)
print('Letras: ', " ".join(word_guess))

while lives!=0:
    letter = input("Ingrese letra: ").upper()
   
    if letter in random_word:
        if letter == random_word:
            for i in range(0, len(random_word)):
                word_guess[i] = random_word[i]
            print(" ".join(word_guess))
            break
        for i in range(0, len(random_word)):
           if letter == random_word[i]:
               word_guess[i] = letter
    else:
       lives-=1
    print('Palabra: ', " ".join(word_guess))

    if "".join(word_guess) == random_word or letter == random_word:
        break

if lives == 0:
    print(f"Perdiste! La palabra era: {random_word}")
else:
    print("Ganaste!!!!!!")