from pyexpat.errors import messages

name="智力有限责任公司"
stock_price=19.99
stock_code=222023338082021
stock_price_daily_growth_factor=1.2
growth_days=7
price_1=stock_price_daily_growth_factor**growth_days
price_2=price_1*stock_price
message="每日增长系数是:%.1f,经过了%d天的增长后，股票达到了:%.2f"%(stock_price_daily_growth_factor,growth_days,price_2)

print(f"公司：{name},股票代码：{stock_code},当前股价{stock_price}")
print(message)
