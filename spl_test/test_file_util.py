#!/usr/bin/env python
# coding=utf-8
'''
 * @File    :  test_file_util.py
 * @Time    :  2020/04/28 14:07:04
 * @Author  :  Hanielxx
 * @Version :  1.0
 * @Desc    :  测试file_util构件
'''

import sys
sys.path.append("../spl_sirna")
from spl_sirna import file_util
import numpy as np
import pandas as pd


def test_get_data_from_file():
    '''
    Desc：
        测试read file 监督学习中通用的读csv/excel的构件
    Return:
        正常：True，出错：False
    '''
    flag = True
    try:
        seq, seq_freq = file_util.get_data_from_file(
            './input.csv',
            xname='Guide strand',
            yname='Normalized inhibitory activity')
        seq, seq_freq = file_util.get_data_from_file(
            './input.csv', xname=['NAS ID', 'Guide strand'], yname=[])
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: get_data_from_file {}".format('is OK' if flag else 'has bugs'))
    return flag


def test_write_csv_excel():
    '''
    Desc：
        write to file 通用的写csv/excel/txt文件构件
    Return:
        正常：True，出错：False
    '''
    flag = True
    try:
        a = pd.DataFrame(np.arange(10).reshape(2,5))
        file_util.write_csv_excel(a, './test.csv')
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: write_csv_excel is {}".format('is OK' if flag else 'has bugs'))
    return flag


if __name__ == "__main__":
    test_get_data_from_file()
    test_write_csv_excel()