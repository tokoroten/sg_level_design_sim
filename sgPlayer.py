#coding:utf-8
import random

class sgPlayer:
    def __init__(self):
        self.is_active = True
        self.stage_history = []
        self.bored_limit = 5
        self.stage_counter = 0
        self.character_power = 5
        self.dice_power = lambda : random.randint(1, 20) + random.randint(1, 20)

    def active_check(self):
        while len(self.stage_history) > self.bored_limit:
            self.stage_history.pop(0)

        # bored check
        if self.stage_history.count(True) == self.bored_limit or self.stage_history.count(False) == self.bored_limit:
            if random.random() < 0.001:
                self.is_active = False


    def try_stage(self, stage_level):
        if self.is_active == False:
            return None

        score = self.character_power + self.dice_power()
        if score >= stage_level:
            self.stage_history.append(True)
            self.next_stage()
        else:
            self.stage_history.append(False)

        self.active_check()

        return self.get_last_challenge_result()

    def get_last_challenge_result(self):
        return self.stage_history[-1]

    def next_stage(self):
        self.character_power += random.randint(0, 10)
        self.stage_counter += 1


if __name__ == "__main__":
    player = sgPlayer()

    for i in xrange(20):
        player.try_stage(14)
        print player.is_active, player.stage_counter, player.stage_history, player.character_power
        if player.is_active == False:
            break