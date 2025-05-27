def vacuum_cleaner(env, location):
    for room in ['A', 'B']:
        if env[room] == 'Dirty':
            print(f"Vacuum in {room}: Cleaning")
            env[room] = 'Clean'
        else:
            print(f"Vacuum in {room}: Already clean")
    print("Final Environment:", env)

# Input
environment = {'A': 'Dirty', 'B': 'Dirty'}
vacuum_cleaner(environment, 'A')
