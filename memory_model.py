import actr
import random


# Define a more complex chunk type for declarative memory facts
actr.chunk_type("fact", "cue response last_reviewed")
actr.chu
# Function to add facts to declarative memory with time stamp
def add_fact(cue, response):
    current_time = actr.get_time()
    fact = actr.make_chunk("fact", "cue", cue, "response", response, "last_reviewed", current_time)
    actr.add_dm(fact)

# Function to simulate learning facts with different intervals (spaced vs. massed)
def learn_facts(facts, learning_style='spaced'):
    if learning_style == 'spaced':
        interval = 5
    else:
        interval = 1

    for fact in facts:
        add_fact(fact['cue'], fact['response'])
        actr.run(interval)  # Simulate time passing between learning different facts

# Define a recall function that checks for forgetting
def recall_fact(cue):
    # Retrieval attempt
    fact = actr.recall("fact", "cue", cue)
    if fact:
        # Calculate time since last reviewed
        time_since_reviewed = actr.get_time() - fact['last_reviewed']
        forgetting_threshold = 10  # Time after which forgetting is more likely

        if time_since_reviewed > forgetting_threshold:
            if random.random() > 0.5:  # 50% chance of forgetting after the threshold
                print(f"Failed to recall: {cue}")
                return
        print(f"Recalled response: {fact['response']}")
    else:
        print("No memory found for cue:", cue)

# Example facts to learn
facts_to_learn = [
    {'cue': 'apple', 'response': 'fruit'},
    {'cue': 'dog', 'response': 'animal'},
    {'cue': 'rose', 'response': 'flower'}
]

# Learning session
learn_facts(facts_to_learn, learning_style='spaced')

# Simulate a period of time (to model forgetting effects)
actr.run(20)

# Recall session
for fact in facts_to_learn:
    recall_fact(fact['cue'])
