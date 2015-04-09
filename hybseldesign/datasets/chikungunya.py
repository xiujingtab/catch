"""Dataset with Chikungunya sequences.

A dataset with 213 Chikungunya sequences. There are 181 complete
genomes from NCBI and 32 isolates from VBRC.
"""

import sys

from hybseldesign.datasets import GenomesDatasetSingleChrom

__author__ = 'Hayden Metsky <hayden@mit.edu>'

ds = GenomesDatasetSingleChrom(__name__, __file__)
ds.set_fasta_path("data/chikungunya.fasta", relative=True)
sys.modules[__name__] = ds

