import pymarkov
import sys
import os

if len(sys.argv) < 3 :
    print "Usage python double_markov.py input_file output_file "
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]
temp_file = "temp.txt"

first_pass = pymarkov.Markov(open(input_file))
temp_store = open(temp_file,"a") # Open in append mode

for el in xrange(0,50): #Train markov for 50 lines
     temp_store.write(first_pass.generate_markov_text() + "\n")


temp_store.close() #Closes the buffer

## Perform a second pass

second_pass = pymarkov.Markov(open(temp_file))
final_store = open(output_file,"a") # Open in append mode

for el in xrange(0,50): #Train second markov for 50 lines
    final_store.write(second_pass.generate_markov_text() + "\n")

final_store.close() #Writes the output 


# Todo improve it to be cross platfrom
return_code = os.system("rm temp.txt")

if int(return_code) == 0:
    print "Temporary files cleaned up successfully"
else:
    print "Error cleaning up"



