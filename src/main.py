import numpy as np
import youtube
import ui
import vidinput
import sentAnalysis

query_dict = {
    'rock' : 1,
    'classical' : 1,
    'pop' : 1,
    'blues' : 1,
    'edm' : 1,
    'alternative' : 1
}

def main():
    effective = True
    if effective:
        query_dict['rock'] += 1

    # List of things to do tada
    print(list(query_dict.keys()))
    print([x/sum(query_dict.values()) for x in query_dict.values()])

    print(np.random.choice(list(query_dict.keys()), 1, p = [x/sum(query_dict.values()) for x in query_dict.values()]))

main()