import datetime
import akshare as ak
import concurrent.futures
import os

# 获取日期范围
def date_ranges():
    begin = datetime.datetime(2016, 2, 3)
    now = datetime.datetime.today()
    interv = datetime.timedelta(days=1)
    dates = []
    date = begin
    while True:
        if (date < now) and (date + interv < now):
            date = date + interv
            dates.append(date.strftime('%Y%m%d'))
        else:
            dates.append(now.strftime('%Y%m%d'))
            break
    return dates

# 下载新闻数据并保存
def download_data(date):
    news_cctv_df = ak.news_cctv(date=date)
    news_cctv_df.to_csv(f'cctv/{date}.csv', index=False, encoding='utf-8')
    print(f"Downloaded data for {date}")

# 使用线程池并行下载数据
if __name__ == "__main__":

    # 确保保存路径的文件夹存在
    if not os.path.exists('cctv'):
        os.makedirs('cctv')

    dates = date_ranges()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_data, dates)
