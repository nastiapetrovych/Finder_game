"""
This is my game
"""
import sys


class Room:
    """
    The class which describes the room
    """

    def __init__(self, room):
        """
        :param room: list
        """
        self.room = room

    def __str__(self):

        if self.room == 'Kitchen':
            return 'A dank and dirty room buzzing with flies.\nThe dinning room is south'
        elif self.room == 'Dinner Hall':
            return 'A large room with ornate golden decorations on each wall\nThe Ballroom is west\nThe Kitchen is north'
        elif self.room == 'Ballroom':
            return 'A vast room with a shiny wooden floor.Huge candlesticks guard the entrance.\nThe Dining Hall is east'
        else:
            return 'Bye!'


class Enemy(Room):
    """
    The class which describes enemies and inherent a name of room
    """

    def __init__(self, room):
        super().__init__(room)
        if self.room == 'Dinner Hall':
            self.enemy_name = 'zombie'
        elif self.room == 'Ballroom':
            self.enemy_name = 'spider'
        else:
            self.enemy_name = None

    def __str__(self):
        if self.room == 'Dinner Hall':
            return 'A smelly zombie'
        elif self.room == 'Ballroom':
            return 'An enormous spider with countless eyes and furry legs.'
        else:
            return ''

    def get_enemy_name(self):
        """
        Only return enemy name
        :return: str
        """
        return self.enemy_name


class Friend(Room):
    """
    Gives info about friends. Also, inherent the room name of class 'Room'
    """

    def __init__(self, room):
        super().__init__(room)
        if self.room == 'Dinner Hall':
            self.friend_name = 'Dave'
        elif self.room == 'Ballroom':
            self.friend_name = 'Tabitha'
        else:
            self.friend_name = ''

    def __str__(self):
        if len(self.friend_name) != 0:
            return f'{self.friend_name} is here!'
        else:
            return ''

    def get_name(self):
        """
        Returns name for class Character
        :return: str
        """
        return self.friend_name


class Object:
    """
    Gives info about given object in the room
    """

    def __init__(self, room, ballroom_items, hall_items):
        self.room = room
        self.ballroom_items = ballroom_items
        self.hall_items = hall_items
        if self.room == 'Ballroom':
            if len(self.ballroom_items) != 0:
                self.item_name = self.ballroom_items[0]
            else:
                self.item_name = None
        elif self.room == 'Dinner Hall':
            if len(self.hall_items) != 0:
                self.item_name = self.hall_items[0]
        else:
            self.item_name = None

    def __str__(self):
        if self.item_name is not None:
            if self.item_name == 'cheese':
                return f'The [{self.item_name}] is here - A large and smelly block of cheese'
            elif self.item_name == 'book':
                return f'The [{self.item_name}] is here - A really good book entitled "Knitting for dummies"'
            else:
                return f'The [{self.item_name}] is here'
        else:
            return ''


class Character(Object):
    """
    Operate all character's action
    """

    def __init__(self, room_nam, item_name):
        self.item_name = item_name
        self.friend_name = Friend(room_nam).get_name()

    def talk(self):
        """
        Returns the speech of each friend
        :return: str
        """
        if self.friend_name == 'Tabitha':
            return f"[{self.friend_name} says]: Sssss....I'm so bored..."
        elif self.friend_name == 'Dave':
            return f"[{self.friend_name} says]: What's up, dude! I'm hungry."
        else:
            return ''

    def fight(self, enemy_name, items):
        """
        Fights with enemy if it exists
        :param enemy_name: str
        :param items: list
        :return: str
        """
        if len(items) == 0 and enemy_name is not None:
            return f'{self.friend_name} crushes you, puny adventurer!'
        if enemy_name is not None:
            print('What will you fight with?')
            take_input = input()
            if enemy_name == 'zombie':
                for stuff_name in items:
                    if stuff_name == take_input and take_input != 'cheese':
                        del items[items.index(stuff_name)]
                        return f'You fend {self.friend_name} off with the {stuff_name}.\nHooray, you won the fight!'
                    else:
                        return f'{self.friend_name} crushes you, puny adventurer!'
            elif enemy_name == 'spider':
                for stuff_name in items:
                    if stuff_name == take_input:
                        del items[items.index(stuff_name)]
                        return f'You fend {self.friend_name} off with the {stuff_name}.\nHooray, you won the fight!'
                else:
                    return f'{self.friend_name} crushes you, puny adventurer!'
        else:
            return 'There is no one here to fight with'

    def take(self, hall_items, ballroom_items):
        """
        Puts items in backpack
        :param hall_items: list
        :param ballroom_items: list
        :return: str
        """
        if self.item_name is None or len(self.item_name) == 0:
            return "There's nothing here to take!"
        elif self.item_name in hall_items:
            del hall_items[0]
            return f'You put the {self.item_name} in your backpack'
        elif self.item_name in ballroom_items:
            del ballroom_items[0]
            return f'You put the {self.item_name} in your backpack'
        else:
            return ''


if __name__ == '__main__':
    def introduction():
        """
        print the beginning of game
        """
        print('Hi, welcome to my game!')
        print('What room do you prefer to start?')
        room_name = input('Enter one from ["Ballroom", "Kitchen","Dinner Hall"]\n')
        launch(room_name)

    counter = []

    def operate(exact_room):
        """
        Function which control all proces with recursive function
        :param exact_room: str
        :return: None
        """
        while len(counter) < 2:
            direction = input('Enter the direction if u want to change room. If not push "Enter"\n')
            if direction == 'south':
                launch('Dinner Hall')
            elif direction == 'north':
                launch('Kitchen')
            elif direction == 'west':
                launch('Ballroom')
            else:
                launch(exact_room)

    backpack_lst = []
    ballroom_items_lst = ['cheese', 'shoes', 'cheese', 'flowers']
    hall_items_lst = ['book', 'dress']

    def launch(exact_room):
        """
        A recursive function
        :param exact_room: str
        :return: None
        """
        print(exact_room)
        print('----------------------------------------------------------------------------')
        print(Room(exact_room))
        print(Friend(exact_room))
        print(Enemy(exact_room))
        name_txt = Object(exact_room, ballroom_items_lst, hall_items_lst).__str__()
        print(name_txt)
        command_input = input('Enter a wished command ["fight", "talk", "take"]\n')
        enemy = Enemy(exact_room).get_enemy_name()
        if command_input == 'take':
            try:
                item_name = name_txt.split()
                item = Character(exact_room, item_name[1][1:-1]).take(hall_items_lst, ballroom_items_lst)
                print(item)
                backpack_lst.append(item_name[1][1:-1])
                print(f'The items in backpack are {backpack_lst}')
            except:
                item = Character(exact_room, name_txt).take(hall_items_lst, ballroom_items_lst)
                print(item)
            operate(exact_room)

        elif command_input == 'talk':
            try:
                item_name = name_txt.split()
                print(Character(exact_room, item_name[1][1:-1]).talk())
            except:
                print(Character(exact_room, name_txt).talk())
            operate(exact_room)
        elif command_input == 'fight':
            try:
                item_name = name_txt.split()
                length = Character(exact_room, item_name[1][1:-1]).fight(enemy, backpack_lst)
                print(length)
            except:
                length = Character(exact_room, name_txt).fight(enemy, backpack_lst)
                print(length)

            if length[-2:] == 'r!':
                print("Oh dear, you lost the fight.\nThat's the end of the game")
                sys.exit()
            elif length[-2:] == 't!':
                counter.append(1)
                operate(exact_room)
            else:
                operate(exact_room)

introduction()
