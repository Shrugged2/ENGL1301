# I'm sick of writing papers.
# Rough framework for a simple "critical thinking" 600 word essay.
# Ctrl shift B to run/save in Atom
# Inputs here below
Title = input("Title: ")
AuthorFN = input("Author First Name: ") #Author Firstname
AuthorLN = input("Author Last Name: ") #Lastname of Author
Gender = input("M/F author? ") #gender of author. what a headache. I say we use gender neutral pronouns for everyone!
Topic = input("General topic (Education, health, pokemon): ")
AuthorThesis = input("The Authors Thesis statement: ")
RestateThesis = input("Restate the thesis: ")
RestateSupport = input("Support for thesis:")
SubjectOE = input("Subject of essay. Who is impacted by thesis: ") #Person or people impacted by essay
Impact = input("Impact to subject of essay: ")
Primary = input("primary argument: ")
Secondary = input("secondary argument: ")
Support1 = input("Support for primary arguement: ")
Support2 = input("Support for secondary argument: ")
Weakness = input("Weaknesses of essay: ")
Strength = input("Strength of essay: ")
# placeholder input because I'm sure I'll think of more
#  = input("")

# pulling current date for formatting
# "now.year, now.month, now.day, now.hour, now.minute, now.second" is format.
import datetime #Print out formatting using Datetime
now = datetime.datetime.now()

# output for header
print ("Rick Wilson")
print ("ENGL 1301 MW 7:30-10:30PM")
print (now.month, now.day, now.year)
print ("Essay #")

#Intro PPH.
print ("In the essay",Title,"by", AuthorFN, AuthorLN,",",AuthorLN, "explains", end = ' ')
#There is a better way to handle gender pronouns. I know there must be, but I do not know what it is. Input appreciated.
if Gender == "M":
    print ("his belief that", end = ' ')
else:
    print ("her belief that", end = ' ')

print (AuthorThesis, end = '. ')

if Gender == "M":
    print("He argues that",end = ' ')
else:
    print ("She argues that", end = ' ')
#THesis
print (SubjectOE, "has", Impact,". ", AuthorLN,"'s primary argument states that", Primary,".",AuthorLN,"'s secondary argument is that",
    Secondary, Support2, end = '. ')
print (AuthorLN, "'s main point is that", RestateThesis,RestateSupport,".","Although this essay",Weakness,", the author", Strength)

#Paragraph 2-Logic based appeal.
print (" ") # Line Spacer
print (AuthorLN, "effectively uses logic to convince and persuade", end = ' ')
if Gender == "M":
    print(" his readers to conect with his thought process",end = '. ')
else:
    print (" her readers to connect with her thought process", end = '. ')
print ("While", AuthorLN, "at times lacks",) #did a negative thing. Then contrast with all the positive.
print ("The majority of this essay demonstrates") #thought process, strong framework, compare and contrast. strong personal experience


#Paragraph 3-Credibility of author
print (" ") # line spacer
print (AuthorLN, "speaks from a position of authority on matters regarding", Topic, end ='. ')
if Gender == "M":
    print("His experience",end = ' ')
else:
    print ("Her experience", end = ' ')


#Conclusion
print (" ") #line spacer
print (AuthorLN, "was successful in presenting and persuading",end = ' ')

if Gender == "M":
    print(" his audience of",end = ' ')
else:
    print (" her audience of", end = ' ')

print (SubjectOE, end = '. ') #Tie back to original subject

if Gender == "M":
    print(" His arguments", end = ' ')
else:
    print (" Her arguments", end = ' ')

print ("served to effectively convey the message intended.", )
