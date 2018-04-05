"""Dataset with 'Influenza A virus [segment 7]' sequences.

A dataset with 25333 'Influenza A virus [segment 7]' sequences.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom

__author__ = 'Hayden Metsky <hayden@mit.edu>'


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/influenza_a_segment7.fasta.gz", relative=True)
sys.modules[__name__] = ds
