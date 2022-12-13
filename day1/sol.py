


class Solution:

    def __init__(self,input_string: str):
        self.input_string = input_string


    def clean_input(self):
        contents = [i.replace('\n','').strip() if len(i) > 1 else '0' for i in self.input_string]
        contents = [int(i) for i in contents]
        return contents

    def return_stacked_elf(
        self,
        second_star: bool = False
        ):

        numeric_list = self.clean_input()

        current_elf = 0
        stacked_elf_cals = 0
        tmp_cals = 0
        num_list = []
        for val in numeric_list:
            tmp_cals += val

            if val == 0:
                num_list.append(tmp_cals)
                current_elf+=1
                if stacked_elf_cals < tmp_cals:
                    stacked_elf_cals = tmp_cals
                    stacked_elf = current_elf

                tmp_cals = 0
        if second_star:
            num_list.sort()
            return sum(num_list[-3:])
        else:
            return stacked_elf_cals


if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        input_string = f.readlines()

    solution_finder = Solution(input_string)

    print(solution_finder.return_stacked_elf(second_star=True))
