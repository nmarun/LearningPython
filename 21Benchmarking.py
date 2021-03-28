# Benchmarking interlude

"""Test the relative speed of iteration tool alternatives."""
import sys, timeit # Import timer functions
reps = 1000000
repslist = list(range(reps)) # Hoist out, list in both 2.X/3.X
def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return list(map(abs, repslist)) # Use list() here in 3.X only!

# return map(abs, repslist)
def genExpr():
    return list(abs(x) for x in repslist) # list() required to force results

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen()) # list() required to force results

stmtForLoop = "forLoop"
# the interactive namespace is a module called __main__
setupForLoop = """
from __main__ import forLoop
"""

stmtListComp = "listComp"
setupListComp = """
from __main__ import listComp
"""

stmtMapCall = "mapCall"
setupMapCall = """
from __main__ import mapCall
"""

stmtGenExpr = "genExpr"
setupGenExpr = """
from __main__ import genExpr
"""

stmtGenFunc = "genFunc"
setupGenFunc = """
from __main__ import genFunc
"""

timesForLoop = timeit.repeat(stmt=stmtForLoop, setup=setupForLoop, number=10000, repeat=8)
timesListComp = timeit.repeat(stmt=stmtListComp, setup=setupListComp, number=10000, repeat=8)
timesMapCall = timeit.repeat(stmt=stmtMapCall, setup=setupMapCall, number=10000, repeat=8)
timesGenExpr = timeit.repeat(stmt=stmtGenExpr, setup=setupGenExpr, number=10000, repeat=8)
timesGenFunc = timeit.repeat(stmt=stmtGenFunc, setup=setupGenFunc, number=10000, repeat=8)

print(f"Time taken by forLoop is {min(timesForLoop)*100000}")
print(f"Time taken by listComp is {min(timesListComp)*100000}")
print(f"Time taken by mapCall is {min(timesMapCall)*100000}")
print(f"Time taken by genExpr is {min(timesGenExpr)*100000}")
print(f"Time taken by genFunc is {min(timesGenFunc)*100000}")
