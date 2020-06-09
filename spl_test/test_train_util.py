#!/usr/bin/env python
# coding=utf-8
'''
 * @File    :  test_train_util.py
 * @Time    :  2020/04/28 16:41:05
 * @Author  :  Hanielxx
 * @Version :  1.0
 * @Desc    :  测试train_util构件
'''

import sys
sys.path.append("../spl_sirna")
from spl_sirna import train_util
from spl_sirna import model_util
from spl_sirna import data_util
from spl_sirna import file_util
from spl_sirna import sirna_util
import numpy as np
import torch
import torch.nn as nn
import torch.utils.data as tud
import torch.optim as optim


def test_train_evaluate_predict():
    '''
    Desc：
        测试train function
    '''
    flag = True
    try:
        seq, seq_freq = file_util.get_data_from_file(
            './input.csv',
            xname='Guide strand',
            yname='Normalized inhibitory activity',
            upper=True)
        x_train, x_valid, x_test, y_train, y_valid, y_test = data_util.split_dataset(
            seq, seq_freq, valid_size=0.1, test_size=0.1)
        idx_to_word, word_to_idx = sirna_util.get_idx_base()
        train_data = data_util.EmbeddedTextDataset(x_train, y_train,
                                                   word_to_idx, idx_to_word)
        valid_data = data_util.EmbeddedTextDataset(x_valid, y_valid,
                                                   word_to_idx, idx_to_word)
        train_dataloader = tud.DataLoader(train_data,
                                          batch_size=10,
                                          shuffle=True,
                                          num_workers=0)
        valid_dataloader = tud.DataLoader(valid_data,
                                          batch_size=10,
                                          shuffle=True,
                                          num_workers=0)
        model = model_util.EmbeddingLSTMModel(5,
                                              100,
                                              100,
                                              1,
                                              1,
                                              False,
                                              dropout=0.5,
                                              avg_hidden=False,
                                              device='cuda')
        model = model.to('cuda')
        optimizer = optim.Adam(model.parameters(), lr=0.001)
        criterion = nn.MSELoss().to('cuda')
        train_epoch_loss = []
        valid_epoch_loss = []
        valid_r = []
        for epoch in range(2):
            train_loss = train_util.train(model,
                                          train_dataloader,
                                          optimizer,
                                          criterion,
                                          device='cuda')

            valid_loss, r = train_util.evaluate(model,
                                                valid_dataloader,
                                                criterion,
                                                device='cuda',
                                                pcc=True,
                                                acc=False)

            train_epoch_loss.append(train_loss)
            valid_epoch_loss.append(valid_loss)
            valid_r.append(r)
        p = train_util.predict_samples(
            model,
            sirna_util.get_seq_motif(['UUUGUUUUCCUGAUAAAGCtg'])[0])
    except Exception as e:
        print(e)
        flag = False
    finally:
        print("RSC: train, evaluate and predict samples {}".format(
            'is OK' if flag else 'has bugs'))
    return flag


if __name__ == "__main__":
    test_train_evaluate_predict()
