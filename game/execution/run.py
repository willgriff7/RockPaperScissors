from game.utils import functions


def main():
    functions.beginning_prompt()
    wins = 0
    loses = 0
    ties = 0
    while(True):
        val = input("Input: ")
        moded_val = functions.shape_input(val)
        comp_val = functions.get_rps()
        win_val = functions.check_if_winner(moded_val, comp_val)
        functions.print_check_if_play_again()
        functions.check_if_play_again()
        if win_val == 0:
            ties+=1
        elif win_val < 0:
            loses+=1
        else:
            wins+=1
        functions.tally_score(wins, loses, ties)
        functions.beginning_prompt()

if __name__ == '__main__':
    main()


