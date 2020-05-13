from datetime import datetime

import time
import random

odds = [ 1, 3, 5, 7, 9 ,11 ,13 ,15 ,22 ,33]

for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("this minute seems a little odd.")
    else:
        print("not an odd minute.")
    wait_time = random.randint(1,10)
    time.sleep(wait_time)
