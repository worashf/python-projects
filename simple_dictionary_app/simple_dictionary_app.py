
#  load dictionary

def load_dictionary(file_path):

    definitions =  {}
    with open(file_path,'r') as dictionary_file:
       
        dictionary_lines  =  dictionary_file.readlines()
       

        for line in dictionary_lines:
         

            if line.strip():
              
                if  len(line) > 2:
                    word, definition =  line.split(' ', 1) 
                    definitions[word.strip()] = definition.strip()
        return  definitions


def search_definition(word, dictionary):
     word = word.capitalize()
     if word in dictionary:
         return dictionary.get(word)
     else:
         return "Word not found in the dictionary."
     
dictionary_path  = "simple_dictionary_app/oxford_dictionary.txt"

dictionary  = load_dictionary(dictionary_path)


while True:
    user_input = input("Enter a word to search (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    translation = search_definition(user_input, dictionary)
    print(translation)


