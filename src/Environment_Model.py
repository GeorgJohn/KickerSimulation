class Observation:

    def __init__(self):
        self.reward = 0
        self.state = []

    def get_reward(self):
        return self.reward

    def get_state(self, kicker, ball, human_gamer, computer_gamer):
        self.state = [kicker.get_score(),
                      ball.get_x_position(), ball.get_y_position(), ball.get_angle(), ball.get_speed(),
                      human_gamer.get_position(), computer_gamer.get_position]
        return self.state
