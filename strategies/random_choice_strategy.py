# Implements the random choice strategy for the 100 prisoners riddle

import random

def run_random_choice_strategy(boxes, BOX_LIMIT):
    total_prisoner_attempts = 0
    trial_success = True # PROVE FALSE

    for prisoner in range(len(boxes)): # ITERATE THROUGH EACH PRISONER
        prisoner_attempts = 0
        available_boxes_indexes = list(range(len(boxes))) # INDEXES OF UNSELECTED BOXES
        
        while True: # PRISONER CHOICE LOOP
            prisoner_attempts += 1

            # PRISONER MAKING DECISION
            selected_box_index = random.choice(available_boxes_indexes) # SIMULATE PICKING INDEX OF BOX RATHER THEN VALUE
            available_boxes_indexes.remove(selected_box_index) # SIMULATE REMOVAL OF BOX INDEX FROM AVAILABLE BOXES INDEXES

            # CHECKS
            if boxes[selected_box_index] == prisoner: # ESCAPED!
                break
            elif prisoner_attempts >= BOX_LIMIT: # TOO MANY ATTEMPTS. PRISONER FAILED
                trial_success = False

        total_prisoner_attempts += prisoner_attempts

    return [trial_success, total_prisoner_attempts]