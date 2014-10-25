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

    def create_stats_map(self):
        max_power_range = max([player.charactor_power for player in self.players])

        fp = open('stat_result.csv', "w")

        header = ["stage_id"]
        for i in xrange(max_power_range):
            header.append("status_%.4d" % i)
        print >>fp, ",".join(header)

        for stage_id in xrange(len(self.stages_result)):
            out = [stage_id]
            for charactor_power in xrange(max_power_range):
                if charactor_power in self.stages_result[stage_id]:
                    win = self.stages_result[stage_id][charactor_power][1]
                    lose =  self.stages_result[stage_id][charactor_power][0]
                    try_num = win + lose
                    if try_num:
                        win_rate = float(win) / try_num
                        out.append(win_rate)
                    else:
                        out.append('')
                else:
                    out.append('')
            print >>fp, ",".join(map(str, out))
        fp.close()

if __name__ == "__main__":
    stage = sgStage()
    stage.create_stage()
    stage.create_player()

    for i in xrange(50):
        stage.simulate()
        active_user = stage.get_active_user_count()
        average_power = stage.get_user_average_status()
        print i, active_user, average_power
    stage.create_stats_map()