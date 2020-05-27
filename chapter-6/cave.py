#!/usr/bin/python3

from random import choice, shuffle

class Cave(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.here = []
        self.tunnels = {}
        for direction in self.directions.keys():
            self.tunnels[direction] = None
    
    directions = {'north' : 'south', 'east' : 'west', 'south' : 'north', 'west' : 'east'}

    def exits(self):
        return [direction for direction, cave in self.tunnels.items() if cave is not None]
    
    def can_tunnel_to(self):
        return [v for v in self.tunnels.values() if v is None] != []
    
    def tunnel_to(self, direction, cave):
        """Create a two-way tunnel"""
        if direction not in self.directions:
            raise ValueError(direction + " is not a valid direction!")
        reverse_direction = self.directions[direction]
        
        if cave.tunnels[reverse_direction] is not None:
            raise ValueError("Cave " + str(cave) + " already has a cave to the " + reverse_direction + "!")
        
        self.tunnels[direction]=cave
        cave.tunnels[reverse_direction]=self
    
    def look(self, player, noun):
        if noun == "":
            result = [self.name, self.description]
            if len(self.here) > 0:
                result += ["Items here:"]
                result += ["  "+x.name for x in self.here if 'name' in dir(x)]
            if len(self.exits()) > 0:
                result += ["Exits:"]
                for direction in self.exits():
                    result += ["  "+direction + ": " + self.tunnels[direction].name]
            else:
                result += ["Exists: none"]
        else:
            result = [noun + "? I can't see that."]

        return result
    
    def go(self, player, noun):
        if noun not in self.directions:
            return [noun + "? I don't know that direction."]
        if self.tunnels[noun] is None:
            return ["Can't go " + noun + " from here."]
        self.here.remove(player)
        self.tunnels[noun].here.append(player)
        player.location = self.tunnels[noun]
        return (['You go ' + noun] + self.tunnels[noun].look(player, ''))
    
    def north(self, player, noun):
        return self.go(player, 'north')
    def south(self, player, noun):
        return self.go(player, 'south')
    def east(self, player, noun):
        return self.go(player, 'east')
    def west(self, player, noun):
        return self.go(player, 'west')
    n = north
    s = south
    e = east
    w = west
    l = look
    
    actions = ['look', 'go', 'north', 'south', 'east', 'west', 'n', 's', 'e', 'w', 'l']
    
    def __repr__(self):
        return "<Cave " + self.name + ">"
