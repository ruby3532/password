password = 'a123456' #先將答案存起來了
i = 3 #剩餘機會

while True:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('成功登入')
		break
	else:
		i = i - 1
		print('密碼錯誤! 還有', i,'次機會') # 要拆開，字串、整數、字串
		if i == 0:
			break