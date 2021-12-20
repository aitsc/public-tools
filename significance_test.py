from scipy import stats
import random


def significance_test(x, y):
    '''
    t检验, 判断x是否等于y
    :param x: list; 一个总体, 比如对比算法
    :param y: list; 一个总体, 比如本算法
    :return:
    '''
    x_N = len(x)
    x_µ = sum(x) / x_N
    y_N = len(y)
    y_µ = sum(y) / y_N
    out = {'x-mean': x_µ, 'y-mean': y_µ}
    if x_N == y_N:
        xy = [i - j for i, j in zip(x, y)]  # 差值
        xy_µ = sum(xy) / x_N
        xy_D = sum([(xy_µ - i) ** 2 for i in xy]) / (x_N - 1)  # 样本方差
        if xy_D == 0:
            t_v = float('nan')
            tp_v = 1. if x_µ == y_µ else 0.
        else:
            t_v = (xy_µ - 0) / (xy_D / x_N) ** 0.5
            tp_v = min(1., (1 - stats.t.cdf(x=abs(t_v), df=x_N - 1)) * 2)
        out['t-value'] = t_v
        out['p-value'] = tp_v
        if tp_v > 0.05:
            out['describe'] = 'x和y没有显著性差异'
        else:
            if tp_v <= 0.001:
                p = 99.9
            elif tp_v <= 0.005:
                p = 99.5
            elif tp_v <= 0.01:
                p = 99
            elif tp_v <= 0.025:
                p = 97.5
            else:
                p = 95
            if x_µ > y_µ:
                out['describe'] = 'x大于y的置信度在' + str(p) + '%以上'
            else:
                out['describe'] = 'x小于y的置信度在' + str(p) + '%以上'
    return out


x = [82.3, 80.3, ] * 10
y = [i + random.random() * 1.5 + 0.5 for i in x]
print(significance_test(x, y))
