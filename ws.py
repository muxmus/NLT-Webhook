import websocket
import requests
import datetime
import json
import time

def on_message(ws, message):
	try:
		data = json.loads(message)
		if data != {"ping": True}:
			print('收到消息:', data)
			title = data['title']
			body = data['body']
			requests.get(f'https://5476.push.ft07.com/send/sctp5476tajelm94z28n58c4wts6ysr.send?title={title}&desp={body}%0D%0A[{datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S')}]')
	except json.JSONDecodeError:
		print('收到非JSON消息:', message)

def on_error(ws, error):
	print('发生错误:', error)

def on_close(ws, close_status_code, close_msg):
	print('连接关闭，尝试重连...')
	time.sleep(5)
	start_websocket()

def on_open(ws):
	print('连接已建立')
	# 发送认证消息（如果需要）
	# ws.send(json.dumps({'token': 'YOUR_TOKEN'}))

def start_websocket():
	ws = websocket.WebSocketApp('ws://localhost:5075', on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
	ws.run_forever(ping_interval=60)  # 每60秒发送心跳

if __name__ == '__main__':
	print('notice\n')
	start_websocket()