def max_kereso(x, *args):
	    max = x
	    for szam in args:
		    if szam > max:
			        max = szam
	    return max


print(max_kereso(1, 19, 11, 7, 17))
