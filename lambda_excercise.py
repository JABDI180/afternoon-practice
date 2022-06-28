#Lambda Excercise 1

#Consider the List

from functools import reduce

prog_lang = [('Python', 3.8),
    ('Java', 13),
    ('JavaScript', 2019),
    ('Scala', 2.13)]


#1. Sort the list by each language's version in ascending order.
#[('Scala', 2.13), ('Python', 3.8), ('Java', 13), ('JavaScript', 2019)]

a = sorted(prog_lang, key = lambda x: x[1])

#2. Sort the list by the length of the name of each language in descending order.
#[('JavaScript', 2019), ('Python', 3.8), ('Scala', 2.13), ('Java', 13)]

b = sorted(prog_lang, key = lambda x: len(x[0]), reverse=True)

#3. Filter the list so that it only contains languages with 'a' in it.
#[('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]

c = list(filter(lambda x: 'a' in x[0], prog_lang))

#4. Filter the list so that it only contains languages whose version is in integer form.
#[('Java', 13), ('JavaScript', 2019)]

d = list(filter(lambda x: x if x[0][1] == int else "d", prog_lang))

#5. Transform the list so that it contains the tuples in the form,
#("language in all lower case", length of the language string)
#[('python', 6), ('java', 4), ('javascript', 10), ('scala', 5)]

e = list(map(lambda x: (x[0].lower(), len(x[0])), prog_lang))

#6. Generate a tuple in the form,
#("All languages separated by commas","All versions separated by commas")
#('Python,Java,JavaScript,Scala', '3.8,13,2019,2.13')

f = reduce(lambda x, y: (x, y), prog_lang)
