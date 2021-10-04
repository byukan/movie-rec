#!/usr/bin/env python3
"""
:file: h.py
:author: Brant Yukan
:date: 10/3/21
:brief: This header file contains function definitions for models.
"""

from transformers import AutoTokenizer, AutoModel
import torch


def calculate_sentence_embedding(s):
    """
    This function computes a dense vector representation of the input text using pytorch transformers library.
    :param: s is the string 
    :return: vector of length 768
    """
    