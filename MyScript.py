#my_script_1

DNA_length= input("Enter your DNA sample?:")
print("Your sample is",len(DNA_length),"bases long.")

#######################################################

def reverse_complement(DNA):
    DNA = DNA.upper()
    
    complement = str()
    
    complement_dictionary = {
    "A":"T", 
    "T":"A", 
    "G":"C",
    "C":"G"
    }
    
    for base in DNA:
        complement+=complement_dictionary.get(base,"N")
        
    return complement
    

DNA = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
#DNA = raw_input('Enter your DNA: ')
print(reverse_complement(DNA))


########################################


file_SPATA31 = open('/Users/uerso/OneDrive/Masaüstü/gene.txt', encoding='utf-8' )
file_SPATA31.read()

########################################

# myscript2

my_seq2 = input("Enter your seq:")
print("Your sample GC% is", GC(my_seq2))


########################################

#myscript2

MutableSeq

from Bio.Seq import MutableSeq

my_seq3 = input("Enter your seq:")
mutable_seq3 = MutableSeq(my_seq3)
print("Your mutable sequence is", mutable_seq3.reverse(), mutable_seq3)
