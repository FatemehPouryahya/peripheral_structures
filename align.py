#On ubuntu
import pandas as pd
import numpy as np
#gene family of 8


from Bio import SeqIO
from Bio.Align.Applications import MafftCommandline

for j  in range(1,7):
    filename="/mnt/e/sugerc/family of 8/f8y"+ str(j)+".fasta"
    output="/mnt/e/sugerc/family of 8 alignment/f8y"+ str(j)+"-aligned.fasta" 
    in_file =str(filename) 
    with open(filename) as f:
        mafft_cline =MafftCommandline(input =in_file)
        stdout, stderr =mafft_cline()
        with open(output, 'w') as handle:
            handle.write(stdout)   
  

#gene family of 7

from Bio import SeqIO
from Bio.Align.Applications import MafftCommandline

for j  in range(1,48):
    filename="/mnt/e/sugerc/family of 7/f7y"+ str(j)+".fasta"
    output="/mnt/e/sugerc/family of 7 alignment/f7y"+ str(j)+"-aligned.fasta" 
    in_file =str(filename) 
    with open(filename) as f:
        mafft_cline =MafftCommandline(input =in_file)
        stdout, stderr =mafft_cline()
        with open(output, 'w') as handle:
            handle.write(stdout)   
 

#gene family of 6

from Bio import SeqIO
from Bio.Align.Applications import MafftCommandline

for j  in range(1,234):
    filename="/mnt/e/sugerc/family of 6/f6y"+ str(j)+".fasta"
    output="/mnt/e/sugerc/family of 6 alignment/f6y"+ str(j)+"-aligned.fasta" 
    in_file =str(filename) 
    with open(filename) as f:
        mafft_cline =MafftCommandline(input =in_file)
        stdout, stderr =mafft_cline()
        with open(output, 'w') as handle:
            handle.write(stdout)   
  