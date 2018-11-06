# I'm sick of writing papers
# Ctrl shift B to run in Atom
# Inputs here below
Title = input("Title: ")
AuthorFN = input("Author First Name: ") #Author Firstname
AuthorLN = input("Author Last Name: ") #Lastname of Author
Gender = input("M/F?")
AuthorThesis = input("The Authors Thesis: ")
RestateThesis = input("Restate the thesis: ")
RestateSupport = input("Support for thesis:")
SubjectOE = input("Subject of essay: ") #Person or people impacted by essay
Impact = input("Impact to subject of essay: ")
Primary = input("primary argument: ")
Secondary = input("secondary argument: ")
Support1 = input("Support for primary arguement: ")
Support2 = input("Support for secondary argument: ")
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
print ("In the essay",Title,"by", AuthorFN, AuthorLN,",",AuthorLN, "explains")
if Gender == "M":
    print ("his belief that",)
else:
    print ("her belief that")



print (AuthorThesis,".")

if Gender == "M":
    print("He argues that",)
else:
    print ("She argues that")
#THesis
print (SubjectOE, "has", Impact,".",
    AuthorLN,"'s primary argument states that", Primary,".",AuthorLN,"s secondary argument is that",
    Secondary, Support2,".")
print (AuthorLN, "s main point is that", RestateThesis,RestateSupport,". Although this essay")
