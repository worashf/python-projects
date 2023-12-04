
# define the story 

story = '''Once upon a time, there was a young programmer named [Programer's name]. 
[Programer's name] was always [Adjective] about programming and loved to [Verb] new code. 
One day, [Programer's name] decided to [Verb] a new [Noun] for a coding competition.'''

# ask the user (player)  to fill  the blanks

programer_name = input("Enter Programer Name: ")

adjective  = input("Enter adjective: ")

verb  =  input("Enter verb: ")

noun  =  input("Enter noun: ")

# create the mad libs game by concatinating the strings

mad_libs_stroy  = story.replace("[Programer's name]", programer_name)
mad_libs_stroy  = mad_libs_stroy.replace("[Adjective]", adjective)
mad_libs_stroy =  mad_libs_stroy.replace("[Verb]", verb)
mad_libs_stroy = mad_libs_stroy.replace("[Noun]", noun)

#print the complete story

print("Here is the complete stroy.")

print(mad_libs_stroy)


