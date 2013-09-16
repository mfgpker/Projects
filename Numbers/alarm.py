import winsound, sys
import time
import threading

class Timer(threading.Thread):
	def __init__(self, seconds):
		self.runTime = seconds
		threading.Thread.__init__(self)

	def run(self):
		time.sleep(self.runTime)
		print("BEEP BEEEEP")
		beep("alarm")
		
class CountDownTimer(Timer):
	def run(self):
		counter = self.runTime
		for sec in range(self.runTime):
			print counter
			time.sleep(1.0)
			counter -= 1
		print("BEEP BEEEEP")
		beep("alarm")


def beep(sound):
	winsound.PlaySound('%s.wav' % sound, winsound.SND_FILENAME)

def main():
	time = int(raw_input("insert (sec): "))
	t = CountDownTimer(time)
	t.start()
	

if __name__ == '__main__':
	main()