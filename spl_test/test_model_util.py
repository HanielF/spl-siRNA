#!/usr/bin/env python
# coding=utf-8
'''
 * @File    :  test_model_util.py
 * @Time    :  2020/04/28 15:44:23
 * @Author  :  Hanielxx
 * @Version :  1.0
 * @Desc    :  测试model_util构件
'''

import sys
sys.path.append("../spl_sirna")
from spl_sirna import data_util
from spl_sirna import model_util


def test_Word2vecModel():
    '''
    Desc：
        测试通用的word2vec模型
    '''
    flag = True
    try:
        model = model_util.Word2vecModel(10, 10)
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: Word2vecModel {}".format('is OK' if flag else 'has bugs'))
    return flag


def test_MultiMotifLSTMModel():
    '''
    Desc：
        测试MultiMotifLSTMModel模型
    '''
    flag = True
    try:
        model = model_util.MultiMotifLSTMModel([10, 10, 10], [10, 10, 10],
                                               10,
                                               1,
                                               1,
                                               True,
                                               dropout=0.5,
                                               avg_hidden=False,
                                               motif=3,
                                               loadvec=False,
                                               device='cuda')
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: MultiMotifLSTMModel {}".format(
            'is OK' if flag else 'has bugs'))
    return flag


def test_EmbeddingLSTMModel():
    '''
    Desc：
        测试EmbeddingLSTMModel模型
    '''
    flag = True
    try:
        model = model_util.EmbeddingLSTMModel(10, 10, 10, 1, 1)
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: EmbeddingLSTMModel {}".format(
            'is OK' if flag else 'has bugs'))
    return flag


def test_count_parameters():
    '''
    Desc：
        测试count_parameters函数
    '''
    flag = True
    try:
        model = model_util.EmbeddingLSTMModel(10, 10, 10, 1, 1)
        para = model_util.count_parameters(model)
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: count_parameters {}".format(
            'is OK' if flag else 'has bugs'))
    return flag


if __name__ == "__main__":
    test_Word2vecModel()
    test_MultiMotifLSTMModel()
    test_EmbeddingLSTMModel()
    test_count_parameters()