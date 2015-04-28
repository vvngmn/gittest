def func():
	ffrom=open("Mail_Fusion.txt")
	origin_cnt = ffrom.read()
	print 'origin is :----------------'
	print origin_cnt
	fto=open("FUSION-mail.txt","r")
	l = fto.readline()
	while l:
		l = fto.readline()
		case_name = l.split(":")
		if len(case_name) == 2:
			print 'case name is :--------'
			print case_name
			print l
			origin_cnt = origin_cnt.replace(case_name[1], l)
	print origin_cnt
	f = open('test.txt', 'w')
	f.write(origin_cnt)
	ffrom.close()
	fto.close()

if __name__ == "__main__":
	func()