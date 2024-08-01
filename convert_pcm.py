import numpy as np
import sys
if not len(sys.argv) == 3:
    print("command filename maxcount")
    print("maxcount is the number that will be multiplied against every specific probability to get integer counts. E.g. 1000")
    exit(-1)
motif_file = open(f"{sys.argv[1]}", "r")
lines = [l.rstrip() for l in motif_file]
header = lines[0]
data = lines[1:]
motif_file.close()
rows = len(data)
to_parse = "\t".join(data)
data = np.fromstring(to_parse, sep='\t')
data = (lambda t: t * int(sys.argv[2]))(data) 
data = data.reshape(rows, 4).astype("i4").T
# Change this to have a different output filename
out_file_name = header.split("\t")[1].split("/")[0]
np.savetxt(f"{out_file_name}.pwm", data, fmt="%i")
