# -*- coding: utf-8 -*-
# @Time       : 2020/1/8 12:00
# @Author     : SMnRa
# @Email      : smnra@163.com
# @File       : readData.py
# @Software   : PyCharm
# @description: 本脚本的作用为  读取数据



import sys, time
import numpy as np
import pandas as pd


def readCsv(fileName):
    names = ["enb_id", "starttime", "endtime", "reporttime", "period", "eci", "mr_ripprb_00", "mr_ripprb_01",
             "mr_ripprb_02", "mr_ripprb_03", "mr_ripprb_04", "mr_ripprb_05", "mr_ripprb_06", "mr_ripprb_07",
             "mr_ripprb_08", "mr_ripprb_09", "mr_ripprb_10", "mr_ripprb_11", "mr_ripprb_12", "mr_ripprb_13",
             "mr_ripprb_14", "mr_ripprb_15", "mr_ripprb_16", "mr_ripprb_17", "mr_ripprb_18", "mr_ripprb_19",
             "mr_ripprb_20", "mr_ripprb_21", "mr_ripprb_22", "mr_ripprb_23", "mr_ripprb_24", "mr_ripprb_25",
             "mr_ripprb_26", "mr_ripprb_27", "mr_ripprb_28", "mr_ripprb_29", "mr_ripprb_30", "mr_ripprb_31",
             "mr_ripprb_32", "mr_ripprb_33", "mr_ripprb_34", "mr_ripprb_35", "mr_ripprb_36", "mr_ripprb_37",
             "mr_ripprb_38", "mr_ripprb_39", "mr_ripprb_40", "mr_ripprb_41", "mr_ripprb_42", "mr_ripprb_43",
             "mr_ripprb_44", "mr_ripprb_45", "mr_ripprb_46", "mr_ripprb_47", "mr_ripprb_48", "mr_ripprb_49",
             "mr_ripprb_50", "mr_ripprb_51", "mr_ripprb_52"]

    csvDf = pd.read_csv(fileName,
                        index_col=None,
                        names=names,
                        parse_dates = [1,2,3],
                        # dtype={'starttime': np.int32},
                        nrows=30

    )

    eci = csvDf['eci'].str.split(":|'", expand=True) # 多名字分列
    eci = eci[[1,2,3,4]] # 筛选2,3,4,5列
    eci.columns = ['eci', 'arfcn', 'rip', 'prb']  # 添加列名
    del csvDf['eci']     # 删除df 中的 列
    csvDf = csvDf.join(eci)  # 把 df 添加到 df 中
    print(csvDf['starttime'])
    pass

if __name__=="__main__":
    readCsv('./csv/MRS_RIPPRB_15MI.csv')