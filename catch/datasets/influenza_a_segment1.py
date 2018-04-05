"""Dataset with 'Influenza A virus [segment 1]' sequences.

A dataset with 20571 'Influenza A virus [segment 1]' sequences.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom

__author__ = 'Hayden Metsky <hayden@mit.edu>'


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/influenza_a_segment1.fasta.gz", relative=True)
sys.modules[__name__] = ds
