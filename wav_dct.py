# coding:UTF-8

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from scipy.fftpack import dct, idct
import japanize_matplotlib

if __name__ == '__main__':
    fname = 'music_mono.wav' # 入力するWAVファイル
    basename=fname[0:fname.rfind('.')]
    cfname=basename+'_dct_miss.wav'

    # データ取得
    f, samplerate = sf.read(fname)
    N = len(f)

    print(u'原信号', f[:5])
    print(u'チャンネル = ', len(f.shape))
    print(u'サンプリング周波数[Hz] = ', samplerate)
    print(u'データ数 = ', len(f))
    print(u'時間[s] = ', len(f)/samplerate)

    # 原信号のプロット
    plt.plot(f)
    plt.title('原信号')
    plt.show()

    # DCT変換
    F=dct(f,norm='ortho')
    print(F[:5])

    plt.plot(F)
    plt.title('DCT係数')
    plt.show()

    g=idct(F, norm='ortho', n=N)
    plt.plot(g)
    plt.title('復元信号')
    plt.show()

    # カットポイントを動かしながらDCT逆変換
    # corrcoefs = []
    # abs = []
    # for a in range(0, 600000, 10000):
    #     gd=idct(F[:a],norm='ortho', n=N)
    #     corrcoefs.append(np.corrcoef(f, gd)[0][1])
    #     abs.append(np.sum(np.abs(f-gd)))
    
    # # 相関係数のプロット
    # plt.plot(corrcoefs)
    # xticks, strs = pylab.xticks()
    # pylab.xticks(xticks, ["%d" % x for x in 10000 * xticks])
    # plt.xlabel('CutPoint')
    # plt.ylabel('corrcoefs')
    # plt.title("相関係数")
    # plt.show()

    # # 絶対誤差のプロット
    # plt.plot(abs)
    # xticks, strs = pylab.xticks()
    # pylab.xticks(xticks, ["%d" % x for x in 10000 * xticks])
    # plt.xlabel('CutPoint')
    # plt.ylabel('abs')
    # plt.title("絶対誤差")
    # plt.show()

    # 適切なカットポイントを指定
    a = 200000
    gd=idct(F[:a],norm='ortho', n=N)
    print(gd[:5])

    # 復元信号のプロット
    plt.plot(gd, label='gd')
    plt.title("復元信号")
    plt.show()
    sf.write(cfname, gd, samplerate)
