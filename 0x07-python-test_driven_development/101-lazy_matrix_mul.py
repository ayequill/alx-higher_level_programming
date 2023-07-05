#!/usr/bin/python3
"""
A module for matrix multiplication
"""
from numpy import matmul
"""
importing matmul from numpy    
"""
def lazy_matrix_mul(m_a, m_b):
    """
    Perform a matrix multiplication

    Args:
        m_a (list): a list of lists
        m_b (list): a list of lists

    Returns:
        list: list of lists
    """
    return matmul(m_a, m_b)
