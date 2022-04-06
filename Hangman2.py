# -*- coding: cp1252 -*-
import random

HANGMANPICS = ['''

    +------+
    |	   |
    |      |
	   |
	   |
	   |
	   |
	   |
	   |
	   |
	   |
=============''', '''

    +------+
    |      |
    |      |
    O      |
           |
	   |
	   |
	   |
	   |
	   |
	   |
=============''', '''

    +------+
    |      |
    |      |
    O      |
    |      |
    |      |
    |      |
           |
           |
           |
           |
=============''', '''


    +------+
    |      |
    |      |
    O      |
   /|      |
  / |      |
    |      |
           |
	   |
	   |
	   |
=============''', '''


    +------+
    |      |
    |      |
    O      |
   /|\     |
  / | \    |
    |      |
           |
	   |
	   |
	   |
=============''', '''


    +------+
    |      |
    |      |
    O      |
   /|\     |
  / | \    |
    |      |
   /       |
  /        |
	   |
	   |
=============''', '''


    +------+
    |      |
    |      |
    O      |
   /|\     |
  / | \    |
    |      |
   /\      |
  /  \     |
	   |
	   |
=============''']

words = 'absorption acceleration accurate adaptations adolescence aerobic respiration air resistance anomalous results antagonistic muscles antibiotic antibodies antigens artery asteroid atmosphere bacteria balance basalt bicarbonate of soda biomass boiling bronchus carbohydrate carbon dioxide carbonate carnivore catalyst characteristics chlorides chlorophyll chromatography cilia circuit  circulation classification clone combustion community competition compound conductor conservation consumer convection correlation corrosive data logger deficiency density dependent variable diffusion digestion displacement dissolve distillation D.N.A. dynamo eclipse ecosystem electromagnet element elodea emphysema environment enzyme epidemic equation evaluate evaporation fair test fertilisation foetus filtration food chain formula freezing frequency friction fuel fungicide gamete gas pressure gene  genetically modified germination gestation global warming glucose granite gravity habitat haemoglobin hazard hereditary herbicide hibernation hydraulic hydrochloric acid hydrogen hypothesis identify igneous immunisation immunity independent variable indicator infection inherited inoculation insoluble insulation intestine  invertebrate irreversible joule kinetic energy lava lever light beam light gate limestone line graph  line of best fit liquid litmus luminous magma magnetic field mammal mass measurement melt menstruation metamorphic methane microbe micro-organisms mirror image mixture molecule moment multi-cellular muscle natural gas neutralisation Newton nitrates north-seeking pole nucleus nutrient nutrition observation obsidian opaque opinion orbit order of reactivity organisms oscilloscope ovary oviduct ovulation oxide oxygen ozone depletion palisade cell particle pathogen pesticide pH range photosynthesis pitch pivot placenta planet  pneumatic pollen pollination population size porous potential difference potential  energy precipitation precision predator prediction prey producer product propagation protease protein puberty pulse rate pumice pyramid of numbers quadrat  qualitative quantitative radiation reactants reaction reflection refraction reliability repeats reproduction repulsion respiration reversible rotation salt sampling sandstone satellite saturated  sedimentary selective breeding sepal separate shadow side effect slate sodium solidify soluble solute solution solvent sound species spectrum sperm sphere/spherical  stamen starch stationary steam sterilising stigma streamline strength of evidence style suspension sustainable development symbol equation taxonomic group tension testis tissues tobacco toxic trachea transect translucent transmission transparent trial run tuning fork upthrust uterus vaccination vagina validity  variable variation vegetation cover vein ventilation vertebrate vibration/vibrate villi virus vitamins volcano volume water cycle wave weathering weedkiller weight word equation  ylem yield'.split()

def getRandomWord(wordList):
	# This funstion returns a random string from the passed list of strings.
	wordIndex = random.randint(0, len(wordList) - 1)
	return wordList[wordIndex]
	
def displayBoard (HANGMANPICS, missedLetters, correctLetters, secretWord):
	print HANGMANPICS [len(missedLetters)]
	print
	
	print 'Missed letters:',
	for letter in missedLetters:
		print letter,
	print
	
	blanks = '_' * len(secretWord)
	
	for i in range (len(secretWord)): #replace blanks with correctly guessed letters
		if secretWord[i] in correctLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
			
	for letter in blanks: #show the secret word with spaces in between each letter
		print letter
	print
	
def getGuess(alreadyGuessed):
	#returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
	while True:
		print 'Guess a letter.'
		guess = raw_input()
		guess = guess.lower()
		if len(guess) != 1:
			print 'Please enter a single letter.'
		elif guess in alreadyGuessed:
			print 'You have already guessed that letter. Choose again.'
		elif guess not in 'abcdefghijklmnopqrestuvwxyz':
			print 'Please enter a LETTER.'
		else:
			return guess

def playAgain():
	#This function returns True if the player wants to play again, otherwise it returns False.
	print 'Do you want to play again? (yes or no)'
	return raw_input().lower().startswith('y')
	
	
print 'H A N G M A N'
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
	displayBoard (HANGMANPICS, missedLetters, correctLetters, secretWord)
	
	# Let the player type in a letter.
	guess = getGuess(missedLetters + correctLetters)
	
	if guess in secretWord:
		correctLetters = correctLetters + guess
		
		# Check if the player has won
		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print 'Yes! the secret word is "' + secretWord + '"! You have won!'
			gameIsDone = True
	else:
		missedLetters = missedLetters + guess
		
		# Check if player has guessed too many times and lost
		if len(missedLetters) == len(HANGMANPICS) -1:
			displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
			print 'You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '" '
			gameIsDone = True
		
	# Ask the player if they want to play again (but only if the game is done).
	if gameIsDone:
		if playAgain():
			missedLetters = ''
			correctLetters = ''
			gameIsDone = False
			secretWord = getRandomWord(words)
		else:
			break
			
raw_input()
			
