#rachel thomas
#9/9/19
#madlibs
name = input("Enter your Name")


word_1 = input("pick an adj")
word_2 = input("pick a noun")
word_3 = input("pick a verb") #example: nap
word_4 = input("pick an adverb") #example: ran
word_5 = input("pick an adj")
word_6 = input("pick a noun") #animal
word_7 = input("pick an adj") #flavor of ice cream
word_8 = input("pick a verb") #example: run
word_9 = input("pick an adj") #example: long
word_10 = input("pick a noun")

#now we are putting the text in where the words are at
text = str.format("""
Today I went to the zoo. I saw a {}
{ } jumping up and down in its tree.
He { } + { }
through the large tunnel that led to its 
{}. I got some peanuts and passed
them through the cage to a gigantic gray { }
towering above my head. Feeding that animal made
me hungry. I went to get a { } scoop
of ice cream. Afterwards I had to
{ } to catch our bus.
When I got home I took a { }.""",word_1,word_2,word_3,word_4,word_5,word_6,word_7,word_8,word_9,word_10)

print(text)


