from sample_madlibs import madlibs, story, zombie, hunger_games
import random

if __name__ == "__main__":
    m = random.choice([madlibs, story, zombie, hunger_games])
    m.madlib()