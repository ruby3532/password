password = 'a123456' #先將答案存起來了
i = 3 #剩餘機會

while i > 0:  # 若不寫 true 可以怎麼寫？從剩餘機會思考  
	i = i - 1                  
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('成功登入')
		break
	else:
		print('密碼錯誤')
		if i > 0:
			print('還有', i,'次機會') # 要拆開，字串、整數、字串
		else:
			print('沒機會嘗試了，要鎖帳號了')