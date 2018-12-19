from os import path
from Bio import SeqIO
from Bio.Alphabet import generic_dna


# https://rody.blog/2015/11/14/orf-finder-for-fasta-files-with-dna-sequences-using-python/
#FUNCTION START
def orf_finder(dna,frame):

    stop_codons = ['tga', 'tag', 'taa']
    start_codon = ['atg']
    start_positions = []
    stop_positions = []
    num_starts=0
    num_stops=0


    for i in range(frame,len(dna),3):
        codon=dna[i:i+3].lower()
        if codon in start_codon:
            start_positions += str(i+1).splitlines()
        if codon in stop_codons:
            stop_positions += str(i+1).splitlines()

    for line in stop_positions:
        num_stops += 1

    for line in start_positions:
        num_starts += 1

    orffound = {}

    if num_stops >=1 and num_starts >=1: #first statment: the number of stop codons and start condos are greater than or equal to 1;

        orfs = True
        stop_before = 0
        start_before = 0

        if num_starts > num_stops:
            num_runs = num_starts
        if num_stops > num_starts:
            num_runs = num_stops
        if num_starts == num_stops:
            num_runs = num_starts

        position_stop_previous = 0
        position_start_previous = 0
        counter = 0

        for position_stop in stop_positions:

            position_stop = int(position_stop.rstrip()) + 2

            for position_start in start_positions:

                position_start = position_start.rstrip()

                if int(position_start) < int(position_stop) and int(position_stop) > int(position_stop_previous) and int(position_start) > int(position_stop_previous):

                    counter += 1
                    nameorf = "orf"+str(counter)
                    position_stop_previous += int(position_stop) - int(position_stop_previous)
                    position_start_previous += int(position_start) - int(position_start_previous)
                    sizeorf = int(position_stop) - int(position_start) + 1

                    orffound[nameorf] = position_start,position_stop,sizeorf,frame

                else:

                    pass

    else:

        orfs = False

    return orffound
#FUNCTION END





if __name__ == "__main__":
    FASTA_DIR_PATH = '../data/sequences'


    FASTA_FILE_PATH = path.join(FASTA_DIR_PATH, "Port.fsa")
    fsa_parse = [s for s in SeqIO.parse(FASTA_FILE_PATH, 'fasta',
                                        alphabet=generic_dna)]

    # for seq in fsa_parse:
    #     print(seq.id)
    #     print(repr(seq.seq))
    #     print(len(seq))

    
