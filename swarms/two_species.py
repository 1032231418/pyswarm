#!/usr/bin/env python

from swarm import Agent, World
from random import random, shuffle

class Victim(Agent):

    def init(self, world):
        self.world  = world
        self.color  = 'FF00FFFF'

    def act(self):
        for agent in self.world.Predator:
            dist = self.distance(agent)
            if dist < 8:
                v = [x/15 for x in self.vector_to(agent, 1)]
                self.move(*v)
                return
        for agent in self.world.Victim:
            if self == agent:
                continue
            dist = self.distance(agent)
            if dist < 15:
                v = [x/25 for x in self.vector_to(agent)]
                self.move(*v)
                return
        self.move((random()-0.5)/2, (random()-0.5)/2, (random()-0.5)/2)

class Predator(Agent):

    def init(self, world):
        self.world  = world
        self.color  = '00FFFFFF'


    def act(self):
        shuffle(self.world.Victim)
        for agent in self.world.Victim:
            if self == agent:
                continue
            dist = self.distance(agent)
            if dist < 18 and dist > 1:
                v = [x/25 for x in self.vector_to(agent)]
                self.move(*v)
                return
        self.move((random()-0.5)/2, (random()-0.5)/2, (random()-0.5)/2)


if __name__ == '__main__':
    world = World()
    [world.add(Victim(world=world)) for x in range(1000)]
    [world.add(Predator(world=world)) for x in range(100)]
    print world
    for i in range(1000):
        print world.genNext()


