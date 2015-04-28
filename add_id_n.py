def func():
	file=open("SBM-contact.txt",'r')
	origin_cnt = ffrom.read()
	# print 'origin is :----------------'
	# print origin_cnt
	
	fto=open("SBM-contact_id.txt","w")
	l = file.readlines()
	for line in l:
		case_name = line.split(": ")[1]
		print 'case name is :--------'
		print case_name
		new = origin_cnt.replace(case_name, line)
		fto.write(new)
	file.close()
	fto.close()

if __name__ == "__main__":
	func()