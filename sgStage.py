#coding:utf-8
import sgPlayer
import random

class sgStage:
    def __init__(self):
        self.players = []
        self.stages_difficult = []
        self.stages_result = []

    def create_player(self):
        for i in xrange(100):
            self.players.append(sgPlayer.sgPlayer())

    def create_stage(self):
        for i in xrange(100):
            self.stages_difficult.append(6 + i + random.randint(1,10))
            self.stages_result.append({})

    def simulate(self):
        for player in self.players:
            stage_id = player.stage_counter
            if len(self.stages_difficult) < stage_id:
                continue

            stage_level = self.stages_difficult[stage_id]
            result = player.try_stage(stage_level)

            player_power = player.charactor_power

            if player_power not in self.stages_result[stage_id]:
                self.stages_result[stage_id][player_power] = [0, 0]

            if result:
                # win
                self.stages_result[stage_id][player_power][1] += 1
            else:
                # lose
                self.stages_result[stage_id][player_power][0] += 1


    def get_active_user_count(self):
        count = [player.is_active for player in self.players].count(True)
        return count

    def get_user_average_status(self):
        total_power = 0
        active_count = 0
        for player in self.players:
            if player.is_active:
                active_count += 1
                total_power += player.charactor_power

        if active_count:
            return float(total_power) / active_count
        else:
            return 0.0

if __name__ == "__main__":
    stage = sgStage()
    stage.create_stage()
    stage.create_player()

    for i in xrange(50):
        stage.simulate()
        active_user = stage.get_active_user_count()
        average_power = stage.get_user_average_status()
        print i, active_user, average_power
