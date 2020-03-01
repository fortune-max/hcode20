# Hashcode 2020
This year's problem is based on the Google Book's platform  

Essentially you're to try to maximize the total score of books scanned  

Libraries contain books, some of these which occur in more than one library  

Libraries also have a property which states how long it takes to get a library signed up before book scanning  

# Using The Judge
To use the judge simply join your input and output  

`$ cat a.in a.out > a.concat  `

And send that as input to the judge system  

`$ python judge.py < a.concat  `

This outputs:

_Your submission scored 21 points  
The library signup has been completed for 2 out of 2 libraries (100.0%)  
A total of 6 books have been scanned. 6 of which where distinct with an avg score of 3.5. This is 100.0% of the 6 books available across all libraries. The minimum score of a scanned book was 1 and the maximum was 6.  _

# Files
inputs/xxxx.txt => Question inputs  
outputs/xxxx.out => Solution outputs  
concats/xxxx.concat => concat of input and output for use with judge.py  
practice => Practice problem pizza slice  
lib_books.py => Solution program  
judge.py => takes in concatenated input and output to return insights on output solution  
scores => scores obtained  
insights => judge ouputs for previous and current solutions
