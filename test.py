import numpy as np
x =np.array([4,5,6,7])
with open("first.txt","w") as t:
    t.write("this is a etest fike")
    t.write("\n\n\n\n")
    print(type(x[0]))
    for element in x:

        t.write(str(element))
        t.write("\t")