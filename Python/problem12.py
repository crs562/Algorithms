# Use Python 3

"""
HanoiTowers(n, fromPeg, toPeg):
    if n = 1:
        output "Move disk from peg fromPeg to peg toPeg"
        return
    unusedPeg <- 6 - fromPeg - toPeg
    HanoiTowers(n-1, fromPeg, unusedPeg)
    output "Move disk from peg fromPeg to peg toPeg"
    HanoiTowers(n-1, unusedPeg, toPeg)
"""

def HanoiTowers(n, fromPeg, toPeg):
    if n == 1:
        print("Move disk from peg " + str(fromPeg) + " to peg " + str(toPeg))
        return
    unusedPeg = 6 - fromPeg - toPeg
    HanoiTowers(n-1, fromPeg, unusedPeg)
    print("Move disk from peg " + str(fromPeg) + " to peg " + str(toPeg))
    HanoiTowers(n-1, unusedPeg, toPeg)

HanoiTowers(3, 1, 3)
