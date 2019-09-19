from hamming import hamming
import pytest


def test_unequal_dna_strand_lengths():
    with pytest.raises(ValueError):
        hamming("GGAG", "CATCG")


def test_empty_dna_strands():
    with pytest.raises(Exception):
        hamming("", "")


def test_count_short_dna_strands():
    assert hamming("GAGCC", "CATCG") == 3


def test_count_medium_length_dna_strands():
    assert hamming("GAGCCTACT", "CATCGTAAT") == 4


def test_count_long_dna_strands():
    assert hamming("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7


def test_identical_dna_strands():
    assert hamming("GAGCC", "GAGCC") == 0


def test_one_dna_strand_difference():
    assert hamming("GAGCG", "GAGCC") == 1


def test_multiple_dna_strand_differences():
    assert hamming("CACGG", "GAGCC") == 4
