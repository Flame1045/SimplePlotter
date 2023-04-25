import matplotlib.pyplot as plt
import numpy as np
import os
import argparse
from yacs.config import CfgNode as CN

def get_default_config_per_plot():
    cfg = CN()
    cfg.Plot = CN()
    cfg.Plot.Filename = './output/query.txt'
    cfg.Plot.Xstart = [1, 2]
    cfg.Plot.Xend = [2, 3]
    cfg.Plot.Ystart = [1, 2]
    cfg.Plot.Yend = [2, 3]
    cfg.Plot.Splitchar = ' '
    cfg.Plot.Legend = 'legend'
    return cfg.clone()

def get_default_config():
    cfg = CN()
    cfg.Plot = CN()
    cfg.Plot.Title = 'Title'
    cfg.Plot.Xaxis = 'x'
    cfg.Plot.Yaxis = 'y'
    cfg.Plot.Legendpos = 'best'
    return cfg.clone()

def get_data(filename: str, xstart: list, xend: list, ystart, yend, 
             split_char: str) -> np.array:
    
    with open(filename, 'r') as f:
        data = f.readlines()
    
    # xstart [2, 4], xend [100, 4]
    if xstart[1] == xend[1]:
        # numpy list to store x data
        x = np.array([])
        for i in range(xstart[0]-1, xend[0]):
            x = np.append(x, float(data[i].split(split_char)[xstart[1]-1]))
            continue
    # xstart [2, 4], xend [2, 100]
    elif xstart[0] == xend[0]:
        # numpy list to store x data
        x = np.array([])
        for j in range(xstart[1]-1, xend[1]):
            x = np.append(x, float(data[xstart[0]-1].split(split_char)[j]))
            continue
    else:
        print('Error: xstart and xend are not in the same row or column')

    # ystart [2, 5], yend [100, 5]
    if ystart[1] == yend[1]:
        # numpy list to store y data
        y = np.array([])
        for i in range(ystart[0]-1, yend[0]):
            y = np.append(y, float(data[i].split(split_char)[ystart[1]-1]))
            continue
    # ystart [3, 4], yend [3, 100],
    elif ystart[0] == yend[0]:
        # numpy list to store y data
        y = np.array([])
        for j in range(ystart[1]-1, yend[1]):
            y = np.append(y, float(data[ystart[0]-1].split(split_char)[j]))
            continue
    else:
        print('Error: ystart and yend are not in the same row or column')

    return x, y



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--exper_dir', type=str, default='./test1', help='path to the file to be plotted')
    dir = parser.parse_args()

    for _, _, files in os.walk(dir.exper_dir):
        nums = len(files)
        for num in range(0, nums):
            cfg = get_default_config_per_plot()
            cfg.merge_from_file(dir.exper_dir + '/' + files[num])
            cfg.freeze()
            X, Y = get_data(cfg.Plot.Filename, cfg.Plot.Xstart, cfg.Plot.Xend, 
                            cfg.Plot.Ystart, cfg.Plot.Yend, cfg.Plot.Splitchar)
            order = np.argsort(X) 
            X = np.array(X)[order] 
            Y = np.array(Y)[order]
            plt.plot(X, Y, label=cfg.Plot.Legend)

    config = get_default_config()
    config.merge_from_file('CONFIG.yaml')
    plt.title(config.Plot.Title)
    plt.xlabel(config.Plot.Xaxis)
    plt.ylabel(config.Plot.Yaxis)
    plt.legend(loc=config.Plot.Legendpos)
    plt.show()