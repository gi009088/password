times = 4
while times > 0:
	password = 'a123456'
	print('請輸入密碼：')
	user_enter = input()
	
	if user_enter == password:
		print('登入成功')
		break
	elif times > 1:
		times = times - 1
		print('密碼錯誤!還有', times, '次機會')
	else:
		print('你沒有機會了!')
		break
raise SystemExit

