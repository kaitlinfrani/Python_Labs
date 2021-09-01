# -*- coding: utf-8 -*-
"""

Kaitlin Frani
CPSC 223P-01
Mon Feb 22, 2021
kaitlinfrani@csu.fullerton.edu

"""

import lists

sports_teams = [lists.football_teams, lists.baseball_teams, lists.basketball_teams]
sports_teams = lists.football_teams + lists.baseball_teams + lists.basketball_teams
# Print out all the school lunches on the menu, but substitute bratwurst 
# wherever you see hot dogs
# Use list comprehension. Just print the list directly so the output will
# include the brackets and quotations (['item 1', item 2' ... and so on])
newSchoolLunch = [x if x != "hot dogs" else "bratwurst" for x in lists.school_lunches]
print(newSchoolLunch)

# Use zip to iterate over two lists at the same time
# Print out questions and answers in a loop
# Format them: "What is your <question>? My <question> is <answer>."
for q, a in zip(lists.questions, lists.answers):
    print("What is your {}? My {} is {}".format(q, q, a))

# Manipulate the nested lists of sports teams to print all teams from New York
# and all teams from Los Angeles.  Just print the lists directly so the output will
# include the brackets and quotations (['team 1', team 2' ... and so on])
CheckNewYork = ['New York']
NewYorkList = [x for x in sports_teams for y in CheckNewYork if str(y) in x]
print(NewYorkList)

CheckLosAngeles = ['Los Angeles']
LosAngelesList = [x for x in sports_teams for y in CheckLosAngeles if str(y) in x ]
print(LosAngelesList)