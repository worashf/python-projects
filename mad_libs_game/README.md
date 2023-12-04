
# Mad  Libs Game

##### Mad Libs is a word game where players fill in blanks in a story with different parts of speech (nouns, verbs, adjectives, etc.) to create a funny or absurd story. 



Learn and create a simple Mad Libs game using string concatenation.

## Altenative way to do  mad libs game 
   ###  Using  python  f-strings 

 ```python: 
 
 programer_name = input("Enter Programer Name: ")

adjective  = input("Enter adjective: ")

verb  =  input("Enter verb: ")

noun  =  input("Enter noun: ")

story = f'Once upon a time, there was a young programmer named {programer_name}. 
{programer_name} was always {adjective} about programming and loved to {verb} new code. 
One day, {programer_name} decided to {verb} a new {noun} for a coding competition.'

print(stroy)


``` 
 ## Using format method

 ```python: 
 programer_name = input("Enter Programer Name: ")

adjective  = input("Enter adjective: ")

verb  =  input("Enter verb: ")

noun  =  input("Enter noun: ")
 
 story = 'Once upon a time, there was a young programmer named {}. 
{} was always {} about programming and loved to {} new code. 
One day, {} decided to {} a new {} for a coding competition.'.format(programer_name, adjective, verb, verb, programer_name, verb, noun)

print(story)

 ```







