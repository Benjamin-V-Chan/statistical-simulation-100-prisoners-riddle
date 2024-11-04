# Implements the known loop-following strategy for the 100 prisoners riddle

def run_loop_follow_strategy(boxes, BOX_LIMIT):
    total_prisoner_attempts = 0
    trial_success = True # PROVE FALSE

    for prisoner in range(len(boxes)): # ITERATE THROUGH EACH PRISONER
        prisoner_attempts = 0
        selected_box_index = prisoner # FIRST CHOICE (OWN PRISONERS NUMBER)
        
        while True: # PRISONER CHOICE LOOP
            prisoner_attempts += 1

            # CHECKS
            if boxes[selected_box_index] == prisoner: # ESCAPED!
                break
            elif prisoner_attempts >= BOX_LIMIT: # TOO MANY ATTEMPTS. PRISONER FAILED
                trial_success = False

            # PRISONER MAKING DECISION FOR NEXT ROUND
            selected_box_index = boxes[selected_box_index]

        total_prisoner_attempts += prisoner_attempts

    return [trial_success, total_prisoner_attempts]