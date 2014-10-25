#coding:utf-8
import random

class sgPlayer:
    def __init__(self):
        self.is_active = True
        self.stage_history = []
        self.bored_limit = 5
        self.stage_counter = 0
        self.charactor_power = 5
        self.dice_power = lambda : random.randint(1, 6) + random.randint(1, 6)

    def active_check(self):
        while len(self.stage_history) > self.bored_limit:
            self.stage_history.pop(0)

        if self.stage_history.count(True) == self.bored_limit:
            self.is_active = False
        if self.stage_history.count(False) == self.bored_limit:
            self.is_active = False


    def try_stage(self, stage_level):
        if self.is_active == False:
            return

        score = self.charactor_power + self.dice_power()
        if score >= stage_level:
            self.stage_history.append(True)
            self.next_stage()
        else:
            self.stage_history.append(False)

        self.active_check()

    def next_stage():
        self.charactor_power += 1
        self.stage_counter = 1


