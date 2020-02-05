# Inspired by:
# https://codereview.stackexchange.com/questions/42359/condorcet-voting-method-in-oop-python
# and https://github.com/bradbeattie/python-vote-core/tree/master/pyvotecore

import sys
import os
import itertools


def main():
    file = sys.argv[1]

    if not os.path.isfile(file):
        print("File path {} does not exist. Exiting...".format(file))
        sys.exit()
    vote_results = get_data_from_file(file)
    print("The votes are {}.".format(vote_results))
    choices, scores = build_dict(vote_results)
    results = matches_choices(choices, scores)
    print("Pairwise results are {}.".format(results))
    # return elect_winner(choices, results)
    print("The winner is {}.".format(elect_winner(choices, results)))


def get_data_from_file(filepath):
    """
    Parses data from input file
    """
    vote_results = []
    with open(filepath, encoding='utf-8') as file:
        for lines in file:
            if lines.startswith('#'):
                pass
            elif lines in ['\n', '\r\n']:
                pass
            else:
                (one, two, three, four) = lines.split(None, 4)
                vote_results.append((one, two, three, four))
    return vote_results


def build_dict(votes):
    """
    Builds a dictionary of scores
    for each permutation of two choices
    """
    choices = set()
    scores = dict()
    for voting in votes:
        for choice in voting:
            choices.add(choice)
        for pair in list(itertools.permutations(voting, 2)):
            if pair not in scores:
                scores[pair] = 0
            if voting.index(pair[0]) < voting.index(pair[1]):
                scores[pair] += 1
    return choices, scores


def matches_choices(choices, scores):
    """
    Analyzes dictionary of scores and
    gives the winner of each pair of choices
    """
    results = dict()
    for match in list(itertools.combinations(choices, 2)):
        reverse = tuple(reversed(match))
        if scores[match] > scores[reverse]:
            results[match] = match[0]
        else:
            results[match] = match[1]
    return results


def elect_winner(choices, results):
    """
    If a choice is a winner against
    every other choice, declares winner.
    Does not detect Condorcet cycles
    """
    for choice in choices:
        choice_score = 0
        for result in results:
            if choice in result and results[result] == choice:
                choice_score += 1
        if choice_score == len(choices) - 1:
            return choice


if __name__ == '__main__':
    main()
