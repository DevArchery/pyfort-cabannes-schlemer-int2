#This script is the main script that will be run to start the program
import utility_functions as utils
def game():
    utils.introduction()
    team=utils.compose_team()
    utils.choose_player(team)
    utils.challenge_menu()

if __name__ == "__main__":
    game()