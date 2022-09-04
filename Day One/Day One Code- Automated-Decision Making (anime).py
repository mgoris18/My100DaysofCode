from random import choice

# create lists of animes
animes = [['Haikyuu', 'Sports', 'Short', 'Series'],
['Naruto', 'adventure', 'forever', 'Series'],
['Jujutsu Kaisen', 'Adventure', 'Short', 'Series'], 
['Bungo Stray Dogs', 'Action', 'Long', 'Series']]

# Input mood
print('What mood are you in?')
mood = input()

for item in animes:
    if item[1] == mood:
       print (mood + 'anime: ' + item[0])