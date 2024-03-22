import random

words = ['python', 'java', 'swift', 'django', 'flask']

secret_word = random.choice(words)
word_display = ['_' for _ in secret_word]
attempts = 8

print('HANGMAN GAME!')
print('Try to guess the correct letters to discover the secret word!')

while attempts > 0 and '_' in word_display:
	print('\n' + ' '.join(word_display))
	guess = input('Guess a correct letter: ').lower()
	if guess in secret_word:
		for index, letter in enumerate(secret_word):
			if letter == guess:
				word_display[index] = guess

	else:
		print('That letter is not in the secret word.')
		attempts -= 1
		print(attempts)

if '_' not in word_display:
	print('Congratulations!')
	print(' '.join(word_display))
	print('You survived and discovered the secret word!')

else:
	print("You lose. It's a shame you didn't survive")