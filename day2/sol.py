



class StrategyGuide:

    def __init__(
        self,
    ):
        self.strategy = {
            # Rock
            # Lose
            'X': {
                'value':1,
                'defeats':'C',
                'outcome':'loss'
            },
            'A': {
                'value': 1
            },
            # Paper
            # Draw
            'Y': {
                'value':2,
                'defeats':'A',
                'outcome':'draw'
            },
            'B':{
                'value': 2
            },
            # Scissors
            # Win
            'Z': {
                'value':3,
                'defeats':'B',
                'outcome':'win'
            },
            'C':{
                'value': 3
            },
        }

        self.theirs = 0
        self.mine = -1

    def read_input(
        self,
        input_path:str):

        with open(input_path, 'r' ) as f:
            content = [
                i.replace('\n','')
                for i
                in f.readlines()
            ]
        return content

    def solve(
        self,
        input_path: str):

        content = self.read_input(input_path)

        theirs = self.theirs
        mine = self.mine

        my_choice_points = [
            self.strategy[i[mine]]['value']
            for i in content
        ]

        outcome_score = [
            # tie
            3 if (self.strategy[i[mine]]['value'] == self.strategy[i[theirs]]['value'])
            # win
            else 6 if (self.strategy[i[mine]]['defeats'] == i[theirs])
            # loss
            else 0 for i in content
        ]
        # breakpoint()
        return sum(outcome_score) + sum(my_choice_points)

    def outcome(self, string):

        # not stoked about how this turned out
        # did not want to refactor the setup from part 1, i.e. edit the strategy dict
        # resulted in hard to decifer code for part 2


        theirs = string[self.theirs]
        mine = string[self.mine]

        sub_dict = {k:v for (k,v) in self.strategy.items() if 'defeats' in v.keys()}

        # these update the self.strategy.. not only sub_dict
        # which is a behavior I did not expect
        [
            v.update({'theirs':theirs})
            for (k,v),theirs
            in zip(sub_dict.items(), [theirs]* 3)
            if 'defeats' in v.keys()
        ]

        [
            v.update({'theirs_val':theirs_val})
            for (k,v),theirs_val
            in zip(sub_dict.items(), [self.strategy[theirs]['value']]* 3)
            if 'defeats' in v.keys()
        ]

        # if a draw I need their string & so I grab theirs and take the value
        if self.strategy[mine]['outcome'] == 'draw':
            return self.strategy[theirs]['value']

        # if a win I need to defeats theirs
        if self.strategy[mine]['outcome'] == 'win':
            return [v['value'] for (k,v) in sub_dict.items() if v['defeats'] == v['theirs']][0]

        # if a loss I need to choose not the one that defeats & not the tie
        else:
            return [v['value'] for (k,v) in sub_dict.items() if (v['defeats'] != v['theirs']) and (v['value'] != v['theirs_val'])][0]


    def solve_p2(
        self,
        input_path: str):

        content = self.read_input(input_path)

        # breakpoint()

        my_choice_points = [self.outcome(input) for input in content]

        outcome_score = [
            # tie
            3 if (self.strategy[i[self.mine]]['outcome']  == 'draw')
            # win
            else 6 if (self.strategy[i[self.mine]]['outcome'] == 'win')
            # loss
            else 0 for i in content
        ]

        return sum(outcome_score) + sum(my_choice_points)


if __name__ == "__main__":

    path = 'input.txt'
    rps = StrategyGuide()

    print(rps.solve(path))
    print(rps.solve_p2(path))
