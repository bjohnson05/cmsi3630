import random

words = {"noun": ["dog", "carrot", "chair", "toy", "rice cake"],
         "verb": ["ran", "barked", "squeaked", "flew", "fell", "whistled"],
         "adjective": ["small", "great", "fuzzy", "funny", "light"],
         "preposition": ["through", "over", "under", "beyond", "across"],
         "adverb": ["barely", "mostly", "easily", "already", "just"],
         "color": ["pink", "blue", "mauve", "red", "transparent"] };
tokens = ["Yesterday", "the", "color", "noun",
          "verb", "preposition", "the", "coach's",
          "adjective", "color", "noun", "that", "was",
          "adverb", "adjective", "before"];

firstWord = True
for token in tokens:
   if( not firstWord ):
      print( " ", end = "" )
   if( token in words ):
      choices = words.get( token )
      print( choices[random.randint( 0, (len(choices) - 1) )], end = "" )
   else:
      print( token, end = "" )
   firstWord = False

print( "." )
