#coding:utf-8
import random

class sgPlayer:
    def __init__(self):
        self.is_active = True
        self.bored_counter = 0
        self.bored_limit = 5
        self.stage_count_max = 0
        self.stage_counter = 0
        self.character_power = 5
        self.dice_power = lambda : random.randint(1, 7) + random.randint(1, 7)

    def active_check(self):
        if self.bored_counter >= self.bored_limit:
            self.is_active = False


    def try_stage(self, stage_level):
        if self.is_active == False:
            return None

        score = self.character_power + self.dice_power()
        is_clear = score >= stage_level
        if is_clear:
            self.next_stage()
        else:
            if self.stage_counter > 0:
                self.stage_counter -= 1
            self.bored_counter += 1

        self.active_check()

        return is_clear

    def next_stage(self):
        self.character_power += random.randint(0, 7)
        self.stage_counter += 1
        if self.stage_counter > self.stage_count_max:
            self.stage_count_max = self.stage_counter
            self.bored_counter = 0


if __name__ == "__main__":
    player = sgPlayer()

    for i in xrange(20):
        player.try_stage(14)
        print player.is_active, player.stage_counter, player.stage_history, player.character_power
        if player.is_active == False:
            break