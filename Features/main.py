from Preprocess import *
from HighLevelFeatures import *

p = Preprocess('./test3')
p.allWorks()
h = HighLevelFeatures(p)
h.getCallType()
h.excludeFunction()
h.displayFunction()
