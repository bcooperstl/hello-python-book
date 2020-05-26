#!/usr/bin/python3

from random import choice, shuffle

class Cave(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.here = []
        self.tunnels = []
    
    def tunnel_to(self, cave):
        """Create a two-way tunnel"""
        self.tunnels.append(cave)
        cave.tunnels.append(self)
    
    def __repr__(self):
        return "<Cave " + self.name + ">"

cave_names = [ "Arched cavern", "Twisty passages", "Dripping cave", "Dusty crawlspace", "Underground lake",
               "Black pit", "Fallen cave", "Shallow pool", "Icy underground river", "Sandy hollow",
               "Old firepit", "Tree root cave", "Narrow ledge", "Winding steps", "Echoing chamber",
               "Musty cave", "Gloomy cave", "Low ceilinged cave", "Wumpus lair", "Sppoky Chasm" ]

def create_caves():
    shuffle(cave_names)
    caves = [Cave(cave_names[0],cave_names[0])]
    for name in cave_names[1:]:
        new_cave = Cave(name, name)
        eligible_caves = [cave for cave in caves
                          if len(cave.tunnels) < 3]
        new_cave.tunnel_to(choice(eligible_caves))
        caves.append(new_cave)
    return caves

if __name__ == '__main__':
    for cave in create_caves():
        print(cave.name,"=>",cave.tunnels)
