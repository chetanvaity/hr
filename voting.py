#!/bin/python

import sys
import os

def electionWinner(votes):
    candidates = {}
    for v in votes:
        if candidates.get(v) is None:
            candidates[v] = 1
        else:
            candidates[v] = candidates[v] + 1
    cKeys = candidates.keys()
    wVoteCandidate = cKeys[0]
    wScore = candidates[wVoteCandidate]
    for k in candidates.keys():
        if candidates[k] > wScore:
            wVoteCandidate = k
    wScore = candidates[wVoteCandidate]
    for k in candidates.keys():
        if (candidates[k] == wScore) and (k > wVoteCandidate):
            wVoteCandidate = k
    return wVoteCandidate

    
if __name__ == "__main__":
    f = open('./aaa', 'w')
    votes_cnt = 0
    votes_cnt = int(raw_input())
    votes_i = 0
    votes = []
    while votes_i < votes_cnt:
        try:
            votes_item = raw_input()
        except:
            votes_item = None
        votes.append(votes_item)
        votes_i += 1


    res = electionWinner(votes);
    f.write(res + "\n")

    f.close()
