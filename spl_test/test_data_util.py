#!/usr/bin/env python
# coding=utf-8
'''
 * @File    :  test_data_util.py
 * @Time    :  2020/04/28 14:24:55
 * @Author  :  Hanielxx
 * @Version :  1.0
 * @Desc    :  测试data_util构件
'''

import sys
sys.path.append("../spl_sirna")
from spl_sirna import data_util
import numpy as np
import pandas as pd
import time
import torch.utils.data as tud


def test_char_remove():
    '''
    Desc：
        测试char_remove function 移除部分字符构件
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    try:
        chrList = ['a', 'b']
        myStringList = ["abcd", "absdggef"]
        myStringArray = np.array(myStringList)
        myStringSeries = pd.Series(myStringArray)

        resList = data_util.char_remove(myStringList, chrList)
        resArray = data_util.char_remove(myStringArray, chrList)
        resSeries = data_util.char_remove(myStringSeries, chrList)
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: char_remove {}".format('is OK' if flag else 'has bugs'))


def test_cal_time():
    '''
    Desc：
        测试calculate time function 计算时间
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    try:
        st = time.time()
        for i in range(1000):
            for j in range(10000):
                a = i * j
        end = time.time()
        h, m, s = data_util.cal_time(st, end)
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: cal_time {}".format('is OK' if flag else 'has bugs'))


def test_copy_part_of_data():
    '''
    Desc：
        测试copy_part_of_data function 对文本进行部分复制增多
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    try:
        x = np.arange(100)
        y = np.linspace(0, 3, 100)
        x_, y_ = data_util.copy_part_of_data(x,
                                             y,
                                             yrange=(1.0, 2.0),
                                             copytimes=1)
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: copy_part_of_data {}".format('is OK' if flag else 'has bugs'))


def test_truncate_part_of_data():
    '''
    Desc：
        测试truncate_part_of_data function 截断部分数据
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    try:
        x = np.arange(100)
        y = np.linspace(0, 3, 100)
        x_, y_ = data_util.truncate_part_of_data(x, y, yrange=[])
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: cal_time {}".format('is OK' if flag else 'has bugs'))


def test_get_sample_freq():
    '''
    Desc：
        测试get_sample_freq function 统计频次
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    try:
        d = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
        f = data_util.get_sample_freq(d)
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: get_sample_freq {}".format('is OK' if flag else 'has bugs'))


def test_standardize_data():
    '''
    Desc：
        测试standardize_data function 通用的标准化构件
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    try:
        x = np.random.rand(8)
        x_ = data_util.standardize_data(x)
        npx = (x - np.mean(x)) / np.std(x)
        res = np.sum(abs(npx - x_))
        if res > 0.1:
            raise Exception
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: standardize_data {}".format('is OK' if flag else 'has bugs'))


def test_normlize_data():
    '''
    Desc：
        测试normlize_data function 通用的归一化构件
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    try:
        print("===Test data_util.normlize_data function===")
        x = input("请输入待归一化数据：")
        x = x.split(",")
        x = [int(i) for i in x]
        y = data_util.normalize_data(x)
        print("输入为：", x)
        print("输出为：", y)
        # x = np.random.rand(8)
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: normlize_data {}".format('is OK' if flag else 'has bugs'))
        print("==================End Test=================")


def test_split_dataset():
    '''
    Desc：
        测试 split_dataset function 通用的分割数据集构件
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    try:
        x = np.arange(100)
        y = np.random.rand(100)
        x_train, x_valid, x_test, y_train, y_valid, y_test = data_util.split_dataset(
            x, y, valid_size=0.1, test_size=0.1)
        if len(x_train) != 80 or len(x_test) != 10 or len(x_valid) != 10:
            raise Exception
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: split_dataset {}".format('is OK' if flag else 'has bugs'))


def test_EmbeddedTextDataset():
    '''
    Desc：
        测试 EmbeddedTextDataset function 通用的文本处理Dataset封装
    Returns：
        flag:boolean   --  正常为True，出错为False
    '''
    flag = True
    try:
        x_train = ['a', 'b', 'c', 'd', 'e']
        y_train = [1, 2, 3, 4, 5]
        train_data = data_util.EmbeddedTextDataset(x_train, y_train)
    except Exception as e:
        flag = False
        print(e)
    finally:
        print("RSC: EmbeddedTextDataet {}".format('is OK' if flag else 'has bugs'))


if __name__ == "__main__":
    test_char_remove()
    test_cal_time()
    test_copy_part_of_data()
    test_truncate_part_of_data()
    test_get_sample_freq()
    test_standardize_data()
    test_normlize_data()
    test_split_dataset()
    test_EmbeddedTextDataset()