#https://xueqiu.com/1444657641/116722499
#先引入后面可能用到的包（package）
import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt
# %matplotlib inline
#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

#获取上证综指1998年至今的日交易数据
sh=ts.get_k_data('sh',start='1998-1-1')
sh.index=pd.to_datetime(sh.date)

sh['close'].plot(figsize=(16,8))
# 设置刻度字体大小
plt.xticks(pd.date_range('1998-01-01','2020-6-18',freq='Y'))
plt.yticks(range(1000,6100,420))
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('时间',fontsize=15)
plt.title('上证综指走势与大事记',fontsize=18)
############A股牛市转折大事记
#事件1：
plt.annotate('5.19行情:\n 1999年经济通缩\n政策推动股市\n为经济服务',
    xy=('1999-1-1',1500),xytext=('1999-3-30',2000),
    bbox = dict(boxstyle = 'round,pad=0.5',
    fc = 'yellow', alpha = 0.5),
    arrowprops=dict(facecolor='red',
    shrink=0.05),fontsize=12)
#事件2：
plt.annotate('股权分置改革\n人民币升值\n基金大规模发行\n流动性过剩\n全民炒股',
    xy=('2005-5-1',1400),
    xytext=('2005-6-30',2000),
    bbox = dict(boxstyle = 'round,pad=0.5',
    fc = 'yellow', alpha = 0.5),
    arrowprops=dict(facecolor='red',
    shrink=0.05),fontsize=12)
#事件3：
plt.annotate('四万亿刺激计划\n十大产业振兴规划',
    xy=('2008-11-1',2200),
    xytext=('2009-1-1',3580),
    bbox = dict(boxstyle = 'round,pad=0.5',
    fc = 'yellow', alpha = 0.5),
    arrowprops=dict(facecolor='red',
    shrink=0.05),fontsize=12)
#事件4：
plt.annotate('全面深化改革\n资本洼地\n杠杆资金',
    xy=('2014-7-1',2054),
    xytext=('2014-3-1',2500),
    bbox = dict(boxstyle = 'round,pad=0.5',
    fc = 'yellow', alpha = 0.5),
    arrowprops=dict(facecolor='red',
    shrink=0.05),fontsize=12)
############A股熊市转折大事记
#事件1：
plt.annotate('国有股市价减持',
    xy=('2001-6-1',2260),
    xytext=('2001-10-30',3000),
    bbox = dict(boxstyle = 'round,pad=0.5',
    fc = 'grey', alpha = 0.5),
    arrowprops=dict(facecolor='g',
    shrink=0.05),fontsize=12)
#事件2：
plt.annotate('通胀、基金暂停发行\n次贷危机、大小非减持',
    xy=('2007-10-1',6100),
    xytext=('2008-1-30',5000),
    bbox = dict(boxstyle = 'round,pad=0.5',
    fc = 'grey', alpha = 0.5),
    arrowprops=dict(facecolor='g',
    shrink=0.05),fontsize=12)
#事件3：
plt.annotate('IPO重启、收紧的货币\n地产调控政策、不断解禁的大小非',
    xy=('2009-8-1',3500),
    xytext=('2010-1-1',1500),
    bbox = dict(boxstyle = 'round,pad=0.5',
    fc = 'grey', alpha = 0.5),
    arrowprops=dict(facecolor='g',
    shrink=0.05),fontsize=12)
#事件4：
plt.annotate('场外配资清理\n场内融资\n分级基金去杠杆',
    xy=('2015-8-15',4000),
    xytext=('2015-6-15',5200),
    bbox = dict(boxstyle = 'round,pad=0.5',
    fc = 'grey', alpha = 0.5),
    arrowprops=dict(facecolor='g',
    shrink=0.05),fontsize=12)
############未来路在何方？
plt.annotate('金融去杠杆\n严监管\n中美贸易战\n路在何方？',
    xy=('2017-12-15',3200),
    xytext=('2018-1-1',1600),
    bbox = dict(boxstyle = 'round,pad=0.5',
    fc = 'blue', alpha = 0.5),
    arrowprops=dict(facecolor='k',
    shrink=0.05),fontsize=12)
#    肺炎爆发
plt.annotate('武汉封城',
    xy=('2020-1-23',3200),
    xytext=('2020-1-23',4600),
    bbox = dict(boxstyle = 'round,pad=0.5',
    fc = 'blue', alpha = 0.5),
    arrowprops=dict(facecolor='k',
    shrink=0.05),fontsize=12)
#保存图片到本地
#plt.savefig('D:/CuteHand/sh.jpg')
plt.show()
