#!/usr/bin/env python
# coding=utf-8
'''
 * @File    :  test_sirna_util.py
 * @Time    :  2020/04/28 16:31:15
 * @Author  :  Hanielxx
 * @Version :  1.0
 * @Desc    :  测试sirna_util构件
'''

import sys
sys.path.append("../spl_sirna")
from spl_sirna import sirna_util
import numpy as np


def test_get_idx_base():
    '''
    Desc：
        测试get_idx_base function 获取idx_to_word和word_to_idx
    '''
    flag = True
    try:
        idx_to_base, base_to_idx = sirna_util.get_idx_base(motif=2)
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: get_idx_base {}".format('is OK' if flag else 'has bugs'))
    return flag


def test_idx_to_seq():
    '''
    Desc：
        测试idx_to_seq function 获取idx_to_word和word_to_idx
    '''
    flag = True
    try:
        s = sirna_util.idx_to_seq(np.array([1, 2, 3, 4, 0, 0, 4, 3, 2, 1]))
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: idx_to_seq {}".format('is OK' if flag else 'has bugs'))
    return flag


def test_get_seq_motif():
    '''
    Desc：
        测试get_seq_motif 获取序列的各个motif的编码
    '''
    flag = True
    try:
        s = ['UUUGUUUUCCUGAUAAAGCtg']
        m = sirna_util.get_seq_motif(s)
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: get_seq_motif {}".format('is OK' if flag else 'has bugs'))
    return flag


def test_filter_sirna():
    '''
    Desc：
        测试filter_sirna 对序列进行过滤，筛选出只包含A/a, G/g, U/u, C/c, T/t的长度为21的部分
    '''
    flag = True
    try:
        a = ['sdfa', 'UUUGUUUUCCUGAUAAAGCtg', 'UUUGUUUUCCUGAUA']
        b = sirna_util.filter_sirna(a)
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: get_seq_motif {}".format('is OK' if flag else 'has bugs'))
    return flag


if __name__ == "__main__":
    test_idx_to_seq()
    test_get_idx_base()
    test_get_seq_motif()
    test_filter_sirna()