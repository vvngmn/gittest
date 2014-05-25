import time
import threading

class user(threading.Thread):
    def __init__(self,name,password='p'):
        threading.Thread.__init__(self)
        user.name=name
        user.password=password
        self.thread_stop = False
    
    def login(self):
        print 'login for user '+self.name
        
    def run(self):
        while not self.thread_stop:
            self.login()
            print 'send http request for user '+self.name
            time.sleep(1)
        
    def stop(self):
        self.thread_stop = True
 
 
def test():
    user1=user('user1')
    # user2=user('user2')
    user1.start()
    # user2.start()
    user1.stop()
    # user2.stop()
    
if __name__=='__main__':
    test()
    
