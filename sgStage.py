#coding:utf-8
import sgPlayer
import random

class sgStage:
    def __init__(self):
        self.players = []
        self.stages_difficult = []
        self.stages_result = []
        self.stat_round_num = 5

    def create_player(self):
        for i in xrange(100000):
            self.players.append(sgPlayer.sgPlayer())

    def create_stage(self):
        for i in xrange(100):
            self.stages_difficult.append(10 + i * 5 + random.randint(1,10))
            self.stages_result.append({})

    def simulate(self):
        for player in self.players:
            stage_id = player.stage_counter
            if len(self.stages_difficult) < stage_id:
                continue

            stage_level = self.stages_difficult[stage_id]
            player_power = int(player.character_power / self.stat_round_num) * self.stat_round_num

            result = player.try_stage(stage_level)

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
                total_power += player.character_power

        if active_count:
            return float(total_power) / active_count
        else:
            return 0.0

    def create_stats_map(self):
        max_power_range = max([player.character_power for player in self.players])

        fp = open('stat_result.csv', "w")

        header = ["stage_id", "drop_user_num", "stage_difficult"]
        for character_power in xrange(0, max_power_range, self.stat_round_num):
            header.append("status_%.4d" % character_power)
        print >>fp, ",".join(header)

        for stage_id in xrange(len(self.stages_result)):
            out = ["stage_id_%.4d" % stage_id]
            drop_user_num = [player.stage_counter for player in self.players if player.is_active == False].count(stage_id)
            out.append(drop_user_num)
            out.append(self.stages_difficult[stage_id])
            for character_power in xrange(0, max_power_range, self.stat_round_num):
                if character_power in self.stages_result[stage_id]:
                    win = self.stages_result[stage_id][character_power][1]
                    lose =  self.stages_result[stage_id][character_power][0]
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

    for i in xrange(100):
        stage.simulate()
        active_user = stage.get_active_user_count()
        average_power = stage.get_user_average_status()
        print i, active_user, average_power
    stage.create_stats_map()