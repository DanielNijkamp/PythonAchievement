import math

trees = 333                                        #totaal aantal bomen
shadedTrees1 = trees / 3
shadedTrees = math.ceil(shadedTrees1 * 2)          #hoeveel er in de shadow staan

sunnyTrees = trees / 3                             #hoeveel er in de zon zitten


shadeOutputModifier = 0.8     #procent productie shaduwboom

sunnyTreeOutput = 146                              #hoeveel appels geeft 1 zonnige boom
shadedTreeOutput = sunnyTreeOutput *  shadeOutputModifier         #hoeveel appels geeft 1 shaduw boom

sunnyOutputTotal = sunnyTrees * 146                #hoeveel appels geven alle zon bomen
shadedOutputTotal2 = sunnyOutputTotal / 10
shadedOutputTotal = shadedOutputTotal2 * 8         #hoeveel appels geven alle shaduw bomen
totalOutput = sunnyOutputTotal + shadedOutputTotal 

owners = 3                                         #met hoeveel mensen verdelen we de appels

eatcount = totalOutput % owners
sellableOutput = totalOutput - eatcount
cut = sellableOutput

print(cut)

