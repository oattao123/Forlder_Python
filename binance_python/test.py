from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
api_key = 'j57Bf1YQSUXH570rSsLZWHVBrjS5MAKeyhFkmJLnIMUAGR3HzwHOY91ACOs7IjXx'
api_secret = 'oAio644qUQaLk6jNeIg2vnJpJtc31J60eNsfdmyIjRV8ZGUilwpz3gi6HjlGDk4N'
client = Client(api_key, api_secret)
#depth = client.get_order_book(symbol='BTCBUSD')
#print(depth)
prices = client.get_all_tickers()
for i in prices :
  if i['symbol'] == 'BTCBUSD':
     print(i)
     ic = float(i['price'])
     rate = 30.01
     cal = ic * rate
     print(cal)
     print(type(cal))