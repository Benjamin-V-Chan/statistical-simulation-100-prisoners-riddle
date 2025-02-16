# Main script to run the 100 prisoners simulation for each strategy and track results

import random
from strategies.loop_follow_strategy import run_loop_follow_strategy
from strategies.random_choice_strategy import run_random_choice_strategy
from config import NUM_TRIALS, NUM_PRISONERS, BOX_LIMIT
from utils import calculate_statistics

strategies = [
    ("Random Choice Strategy", run_random_choice_strategy),
    ("Loop Follow Strategy", run_loop_follow_strategy)
]

boxes = list(range(NUM_PRISONERS)) # 0-99 because of natural list indexing start at 0

for strategy_name, strategy_function in strategies:
    results = {'success': [], 'attempts': []}
    for _ in range(NUM_TRIALS):
        random.shuffle(boxes)

        trial_success, trial_total_attempts = strategy_function(boxes, BOX_LIMIT)
        results['success'].append(trial_success)
        results['attempts'].append(trial_total_attempts)

    calculate_statistics(strategy_name, results, NUM_TRIALS, NUM_PRISONERS, BOX_LIMIT)