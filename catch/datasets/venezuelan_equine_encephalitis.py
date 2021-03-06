"""Dataset with 'Venezuelan equine encephalitis virus' sequences.

A dataset with 132 'Venezuelan equine encephalitis virus' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/venezuelan_equine_encephalitis.fasta.gz", relative=True)
sys.modules[__name__] = ds
