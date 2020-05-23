**Monsters-Game**

The following program is a game that allows you to pick the characteristics of two monsters that you will make. Every monster will start out with only the “wait” attack. You can add attacks to the monster, but the monster can only have a max of four attacks at a time. If you add an attack when the monster already has four, the weakest one is dropped automatically. If there is a tie for weakest attack, the weakest attack that comes first alphabetically is dropped. If all of a monster’s attacks are removed, “wait” will automatically be added again, so that every monster always has at least 1 attack. In addition, there are two monster types: Dragon and Ghost, both which inherit all of the properties of the Monster class. Both should have their “type” attribute updated to ‘dragon’ or ‘ghost’ respectively. Initially a monster’s type is set to “Normal”. You only need to do the following if you would like to change the “type”, of the monster to Dragon or Ghost.

Getting Started

Prerequisites 

No prerequisites.

Installing
Download the .ZIP file
Click on download and download the zip file and unzip on your computer.


Open File
Open the file “problem1.py” in your desired IDE


Input test cases to run.
Copy and paste a sample input or your own input on line 194

Running the tests
Now what happens when our monsters fight:

1) The monster entered as the first function parameter always goes first.
2) Each monster takes a turn using one attack move.
3) The attacks are looped from most powerful to least powerful attack until there is a winner. 
4) If there is a tie in hit points for an attack, an attack is selected using alphabetical order.
DON’T FORGET TO PASTE SAMPLE INPUT INTO LINE 194 IN THE SAME FORMAT.

Sample Tests

Sample Input 1:
'''

a = Monster("a", 9)
b = Monster("b",9)
a.add_attack("ice_storm")
b.add_attack("ice_storm")
b.remove_attack("wait")
a.remove_attack("wait")
round1, winner, moves = monster_fight(a, b)
print(round1)
print(winner.name)
print(moves)
'''

Sample Output 1:
3
a
['ice_storm', 'ice_storm', 'ice_storm']

Sample Input 2:
a = Dragon("a", 18)
b = Ghost("b",18)
a.add_attack("ice_storm")
b.add_attack("double_hit")
a.remove_attack("wait")
round1, winner, moves = monster_fight(a, b)
print(round1)
print(winner.name)
print(winner.attacks)
print(winner.exp)
print(winner.max_hp)
print(moves)
round1, winner, moves = monster_fight(a, b)
print(round1)
print(winner.name)
print(winner.attacks)
print(winner.exp)
print(winner.max_hp)
print(moves)


Sample Output 2:
6
A
{'ice_storm': 3}
5
18
['ice_storm', 'ice_storm', 'ice_storm', 'ice_storm', 'ice_storm', 'ice_storm']
6
A
{'ice_storm': 4}
10
18
['ice_storm', 'ice_storm', 'ice_storm', 'ice_storm', 'ice_storm', 'ice_storm']

Sample Input 3:
a = Dragon("a", 18)
b = Ghost("b", 18)
a.add_attack("ice_storm")
b.add_attack("double_hit")
b.remove_attack("wait")
round1, winner, moves = monster_fight(a, b)
print(round1)
print(winner.name)
print(winner.attacks)
print(winner.exp)
print(winner.max_hp)
print(moves)
round1, winner, moves = monster_fight(a, b)
print(round1)
print(winner.name)
print(winner.attacks)
print(winner.exp)
print(winner.max_hp)
print(moves)


Sample Output 3:
5
b
{'double_hit': 4}
5
18
['double_hit', 'double_hit', 'double_hit', 'double_hit', 'double_hit']
5
b
{'double_hit': 4}
10
23
['double_hit', 'double_hit', 'double_hit', 'double_hit', 'double_hit']


