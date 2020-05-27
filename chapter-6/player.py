#!/usr/bin/python3

import shlex

class Player(object):
    def __init__(self, location):
        self.name = "Player"
        self.description = "The Player"
        self.location = location
        self.location.here.append(self)
        self.playing = True
        self.inventory = []
    
    def get_input(self):
        return input("> ")
    
    def update(self):
        self.result = self.process_input(self.input)
    
    def process_input(self, input):
        parts = shlex.split(input)
        if len(parts) == 0:
            return []
        if len(parts) == 1:
            parts.append("")
        verb = parts[0]
        noun = " ".join(parts[1:])
        
        handler = self.find_handler(verb, noun)
        if handler is None:
            return [input + "? I don't know how to do that!"]
        return handler(self, noun)
    
    def find_handler(self, verb, noun):
        if noun != "":
            object = [x for x in self.location.here + self.inventory
                      if x is not self and x.name == noun and verb in x.actions]
            if len(object) > 0:
                return getattr(object[0], verb)
        if verb.lower() in self.actions:
            return getattr(self, verb)
        elif verb.lower() in self.location.actions:
            return getattr(self.location, verb)
    
    def get(self, player, noun):
        return [noun + "? I can't see that here."]
    
    def drop(self, player, noun):
        return [noun + "? I don't have that."]
    
    def inv(self, player, noun):
        result = []
        if self.inventory:
            result += ["You have: "]
            result += ["  "+x.name for x in self.inventory]
        else:
            result += ["You have nothing!"]
        return result
    
    def quit(self, player, noun):
        self.playing = False
        return ["bye bye!"]
    
    actions = ['quit', 'inv', 'get', 'drop']
