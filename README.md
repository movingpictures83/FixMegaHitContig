# FixMegaHitContig
# Language: Python
# Input: TXT
# Output: FASTA
# Tested with: PluMA 1.1, Python 3.6

PluMA plugin that fixes MegaHit output contigs (Uritsky et al, 2018).

Contains a slightly modified version of the script from MegaWrap.

Accepts a tab-delimited file of keyword value pairs:
fasta: Input FASTA file
minlen: Minimum length

Outputs contigs as a FASTA file
