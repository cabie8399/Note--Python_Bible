#RC_7_3: 上網抓資料並畫K線圖
#需要pip install mpl_finance
import matplotlib.pyplot as plt
import matplotlib.dates as dts
import yfinance as yf
from mpl_finance import candlestick_ohlc
from pandas_datareader import data as pdr

#下載資料起迄日, 日期格式與股票代號
start = ('2016-4-1')
end = ('2016-4-25')
weekFormatter = dts.DateFormatter('%b %d')  # 例如, Jan 03 2016

yf.pdr_override() # <== that's all it takes :-)
#以pandas_datareader的get_data_yahoo抓取資料
quotes = pdr.get_data_yahoo('AAPL', start, end)
#轉成陣列
quotes = quotes.to_records(convert_datetime64=True).tolist()
#將陣列中，每個元素第一個欄位(日期)都改成數字型態，並縮成5個元素一組，以符合candlestick_ohlc
quotes = [ (dts.date2num(d), o, h, l, c) for d, o, h, l, c, adj, v in quotes]	

#若抓取的資料是空字串則離開系統
if len(quotes) == 0:
    raise SystemExit

#設定繪圖區域的格式化
fig, ax = plt.subplots()
ax.xaxis_date()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
#畫K線圖並顯示
candlestick_ohlc(ax, quotes, width=0.6)
plt.show()