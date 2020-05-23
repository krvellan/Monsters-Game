class Monster:
    def __init__(self, name, hp=20):
        self.name = name
        self.exp = 0
        self.type = 'Normal'
        self.max_hp = int(hp)
        self.current_hp = self.max_hp
        self.attacks = {'wait': 0}
        self.possible_attacks = {
            "sneak_attack": 1,
            "slash": 2,
            "ice_storm": 3,
            "fire_storm": 3,
            "whirlwind": 3,
            "earthquake": 2,
            "double_hit": 4,
            "wait": 0
        }

    def remove_attack(self, attack_name):
        if str(attack_name) in self.attacks.keys():
            del self.attacks[str(attack_name)]
            if len(self.attacks) < 1:
                self.attacks['wait'] = 0
            return True
        else:
            return False

    def add_attack(self, attack_name):
        if str(attack_name) in self.attacks.keys():
            return False
        if len(self.attacks) < 4:
            if str(attack_name) in self.possible_attacks.keys():
                self.attacks[str(attack_name)] = self.possible_attacks.get(attack_name)
                return True
            else:
                return False
        else:
            lowest_hp = 20
            name = 'z'
            for key, value in self.attacks.items():
                if lowest_hp > value:
                    lowest_hp = value
                    name = key
                if lowest_hp == value:
                    if name > key:
                        name = key
            del self.attacks[str(name)]
            if str(attack_name) in self.possible_attacks.keys():
                self.attacks[str(attack_name)] = self.possible_attacks.get(attack_name)
                return True
            else:
                return False

    def win_fight(self):
        self.exp += 5
        self.current_hp = self.max_hp

    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp

class Ghost(Monster):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.type = 'ghost'
        self.now_exp = 0

    def win_fight(self):
        self.exp += 5
        self.now_exp += 5
        if self.now_exp > 9:
            self.max_hp += 5
            self.now_exp -= 10
        self.current_hp = self.max_hp


    def lose_fight(self):
        self.exp += 1
        self.now_exp += 1
        if self.now_exp > 9:
            self.now_exp -= 10
        self.current_hp = self.max_hp

class Dragon(Monster):

    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.type = 'Dragon'
        self.now_exp = 0

    def win_fight(self):
        self.exp += 5
        self.now_exp += 5
        if self.exp > 9:
            for key, value in self.attacks.items():
                self.attacks[key] += 1
            self.now_exp -= 10
        self.current_hp = self.max_hp

    def lose_fight(self):
        self.exp += 1
        self.now_exp += 1
        if self.now_exp > 9:
            for key, value in self.attacks.items():
                self.attacks[key] += 1
            self.now_exp -= 10
        self.current_hp = self.max_hp

def monster_fight(monster1, monster2):
    monster1_lst = sorted(monster1.attacks.items(), key=lambda x: x[1], reverse=True)
    monster2_lst = sorted(monster2.attacks.items(), key=lambda x: x[1], reverse=True)

    if (len(monster1_lst) == 1) and (len(monster2_lst) == 1):
        if ('wait',0) in monster1_lst:
            if ('wait',0) in monster2_lst:
                return(-1, None, None)

    '''function for ordering monster1's attacks'''
    for i in monster1_lst:
        for j in monster1_lst:
            if i[1] == j[1]:
                if i[0] == j[0]:
                    continue
                else:
                    if j[0] < i[0]:
                        temp = j
                        temp2 = i
                        loc1 = monster1_lst.index(j)
                        loc2 = monster1_lst.index(i)
                        monster1_lst.pop(loc2)
                        monster1_lst.insert(loc2, temp)
                        monster1_lst.pop(loc1)
                        monster1_lst.insert(loc1, temp2)
                    else:
                        continue

    '''function for ordering monster2's attacks'''
    for i in monster2_lst:
        for j in monster2_lst:
            if i[1] == j[1]:
                if i[0] == j[0]:
                    continue
                else:
                    if j[0] < i[0]:
                        temp = j
                        temp2 = i
                        loc1 = monster2_lst.index(j)
                        loc2 = monster2_lst.index(i)
                        monster2_lst.pop(loc2)
                        monster2_lst.insert(loc2, temp)
                        monster2_lst.pop(loc1)
                        monster2_lst.insert(loc1, temp2)
                    else:
                        continue

    monster1_moves = []
    monster2_moves = []

    counter1 = 0
    counter2 = 0
    a = 0

    while True:
        a += 1
        if counter1 == (len(monster1_lst)):
            counter1 = 0

        monster2.current_hp -= int(monster1_lst[counter1][1])
        monster1_moves.append(str(monster1_lst[counter1][0]))
        counter1 += 1

        if monster2.current_hp <= 0:
            monster1.win_fight()
            monster2.lose_fight()
            return(a, monster1, monster1_moves)


        if counter2 == (len(monster2_lst)):
            counter2 = 0

        monster1.current_hp -= int(monster2_lst[counter2][1])
        monster2_moves.append(str(monster2_lst[counter2][0]))
        counter2 += 1


        if monster1.current_hp <= 0:
            monster2.win_fight()
            monster1.lose_fight()
            return(a, monster2, monster2_moves)