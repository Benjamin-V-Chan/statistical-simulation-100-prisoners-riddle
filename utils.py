# Contains helper functions for logging, result tracking, and data processing for the simulation

def calculate_statistics(strategy_name, results, NUM_TRIALS, NUM_PRISONERS, BOX_LIMIT):

    trial_success_rate = results['success'].count(True) / NUM_TRIALS
    average_prisoner_attempts = sum(results['attempts']) / NUM_TRIALS / NUM_PRISONERS

    print('--------------------------------------------------------')
    print()
    print("STRATEGY")
    print(strategy_name)
    print()
    print("CONSTANTS")
    print(f"Number of Trials: {NUM_TRIALS}")
    print(f"Number of Prisoners: {NUM_PRISONERS}")
    print(f"Box Limit: {BOX_LIMIT}")
    print()
    print("STATISTICS")
    print(f"Trial Success Rate: {trial_success_rate}")
    print(f"Average Prisoner Attempts: {average_prisoner_attempts}")
    print()
    print('--------------------------------------------------------')