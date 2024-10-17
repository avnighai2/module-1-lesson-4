#take 5 user input. print what percantage score they haev 

percent1 = int(input(" Add the score for subject 1 : "))
percent2 = int(input(" Add the score for subject 2 : "))
percent3 = int(input(" Add the score for subject 3 : "))
percent4 = int(input(" Add the score for subject 4 : "))
percent5 = int(input(" Add the score for subject 5 : "))

calculate = ((percent1 + percent2 + percent3 + percent4 + percent5)/500)*100

print(f" The total score is {calculate}%")