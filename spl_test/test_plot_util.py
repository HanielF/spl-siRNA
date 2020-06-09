#!/usr/bin/env python
# coding=utf-8
'''
 * @File    :  test_plot_util.py
 * @Time    :  2020/04/28 16:23:25
 * @Author  :  Hanielxx
 * @Version :  1.0
 * @Desc    :  测试plot_util构件
'''

import sys
sys.path.append("../spl_sirna")
from spl_sirna import plot_util
import numpy as np


def test_make_plot():
    '''
    Desc：
        测试make_plot function 通用的绘制折线图构件
    '''
    flag = True
    try:
        x1 = np.random.rand(10)
        x2 = np.random.rand(10)
        x3 = np.random.rand(10)
        plot_util.make_plot([[x1, x2], [x3]], [['x1', 'x2'], ['x3']],
                            titles=['x1 and x2', 'x3'])
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: make_plot {}".format('is OK' if flag else 'has bugs'))


def test_make_scatter():
    '''
    Desc：
        测试make_scatter function 通用的绘制折线图构件
    '''
    flag = True
    try:
        a = np.random.rand(100)
        b = np.random.rand(100)
        plot_util.make_scatter(a,
                               b,
                               xlabel='a',
                               ylabel='b',
                               title='a and b',
                               error=True,
                               pcc=True,
                               yxline=True)
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: make_scatter {}".format('is OK' if flag else 'has bugs'))


if __name__ == "__main__":
    test_make_plot()
    test_make_scatter()