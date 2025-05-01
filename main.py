import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions

    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    print(S)
    print(T)
    if (S, T) in MED:
        return MED[(S, T)]
    if S == "":
        return len(T)
    elif T == "":
        return len(S)


    if S[0] == T[0]:

        result = fast_MED(S[1:], T[1:], MED)
    else:

        insert = fast_MED(S, T[1:], MED)
        delete = fast_MED(S[1:], T, MED)
        substitute = fast_MED(S[1:], T[1:], MED)

        result = 1 + min(insert, delete, substitute)


    MED[(S, T)] = result

    return result

def fast_align_MED(S, T, MED = {}):
    len_S = len(S)
    len_T = len(T)


    MED = [[0 for _ in range(len_T + 1)] for _ in range(len_S + 1)]
    for i in range(len_S + 1):
        MED[i][0] = i
    for j in range(len_T + 1):
        MED[0][j] = j

    # Calculate edit distances
    for i in range(1, len_S + 1):
        for j in range(1, len_T + 1):
            cost = 0 if S[i - 1] == T[j - 1] else 1
            MED[i][j] = min(
                MED[i - 1][j] + 1,      # Deletion
                MED[i][j - 1] + 1,      # Insertion
                MED[i - 1][j - 1] + cost  # Substitution
            )

    # Traceback for alignment
    alignment_S = ""
    alignment_T = ""
    i = len_S
    j = len_T
    while i > 0 or j > 0:
        if i > 0 and j > 0 and MED[i][j] == MED[i - 1][j - 1] + (0 if S[i - 1] == T[j - 1] else 1):
            alignment_S = S[i - 1] + alignment_S
            alignment_T = T[j - 1] + alignment_T
            i -= 1
            j -= 1
        elif i > 0 and MED[i][j] == MED[i - 1][j] + 1:
            alignment_S = S[i - 1] + alignment_S
            alignment_T = "-" + alignment_T
            i -= 1
        else:
            alignment_S = "-" + alignment_S
            alignment_T = T[j - 1] + alignment_T
            j -= 1
    print(alignment_S)
    print(alignment_T)

    return MED[len_S][len_T], alignment_S, alignment_T


print(fast_align_MED('kookaburra', 'kookybird'))