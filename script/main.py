from os import path
from Bio import SeqIO
from Bio.Alphabet import generic_dna
from pillars_parser import pillars_parser

if __name__ == "__main__":

    #FASTA_DIR_PATH = '../data/sequences'

    #FASTA_FILE_PATH = path.join(FASTA_DIR_PATH, "Port.fsa")
    #fsa_parse = [s for s in SeqIO.parse(FASTA_FILE_PATH, 'fasta',
    #                                    alphabet=generic_dna)]

    # for seq in fsa_parse:
    #     print(seq.id)
    #     print(repr(seq.seq))
    #     print(len(seq))

    # --------------------------------------------------------------------------

    PILLARS_PATH = '../data/Pillars.tab'

    pil = pillars_parser(PILLARS_PATH, ygob=[8,9,10,11,21,22,23,24])
