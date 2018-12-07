import numpy as np


def det(array):
    """
    行列式を計算する.

    Parameters
    ----------
    array : Iterable
        計算する行列.

    Returns
    -------
    det : int
        arrayのデタミナント.

    """
    try:
        return np.linalg.det(array)
    except np.linalg.linalg.LinAlgError:
        return None


def inv(array):
    """
    逆行列を計算する.

    Parameters
    ----------
    array : Iterable
        計算する行列.

    Returns
    -------
    inv : List
        arrayの逆行列.

    """
    try:
        return np.linalg.inv(array).tolist()
    except np.linalg.linalg.LinAlgError:
        return None


def rank(array):
    """
    ランクを計算する.

    Parameters
    ----------
    array : Iterable
        計算する行列.

    Returns
    -------
    rank : int
        arrayのランク.

    """
    try:
        return np.linalg.matrix_rank(array)
    except np.linalg.linalg.LinAlgError:
        return None
