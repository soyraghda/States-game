import pandas


class Answer:
    def __init__(self, state_name):
        self.state_name = state_name

    def is_correct(self):
        csv = pandas.read_csv("50_states.csv")
        return self.state_name in csv['state'].values

    def get_coordinate(self):
        xy_coordinate = []
        csv = pandas.read_csv("50_states.csv")
        state_values = csv[csv['state'] == self.state_name]
        x = int(state_values.x)
        y = int(state_values.y)
        xy_coordinate.append(x)
        xy_coordinate.append(y)
        return xy_coordinate

    def get_missing(self, all_states):
        csv = pandas.read_csv("50_states.csv")
        missing=[ i for i in csv['state'].values if i not in all_states]
        df = pandas.DataFrame(missing)
        df.to_csv("./not guessed/missing_states.csv")
