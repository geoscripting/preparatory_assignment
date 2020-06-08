#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""__description__
"""

__author__ = "Christina Ludwig, GIScience Research Group, Heidelberg University"
__email__ = "christina.ludwig@uni-heidelberg.de"


import os
import nbimporter


def test_function_exists():
    """
    Test whether function list_sum was defined
    :return:
    """
    files_lowercase = [x.lower() for x in os.listdir("..")]
    assert "preparatory_assignment.ipynb" in files_lowercase


def test_sum_all_positive():
    """
    Test result if all numbers are positive
    :return:
    """
    os.chdir("..")
    from preparatory_assignment import list_sum

    # given
    numbers = [1,2,3,4]
    expected_result = 10

    # Execute
    result = list_sum(numbers)

    # Compare
    assert result == expected_result
