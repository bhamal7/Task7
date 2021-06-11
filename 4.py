class Time():

	def __init__(self, hours, minutes):
		self.hours = hours
		self.minutes = minutes

	def addTime(time1, time2):
		time3 = Time(0,0)
		time3.hours = time1.hours + time2.hours
		time3.minutes = time1.minutes + time2.minutes
		while time3.minutes >= 60:
			time3.hours+=1
			time3.minutes -=60
		return time3

	def displayTime(self):
		print("Time is {} hours and {} minutes".format(self.hours,self.minutes))

	def displayMinute(self):
		totalMin = (self.hours*60+self.minutes)
		print("Total minutes is: ",totalMin)

a = Time(2,50)
b = Time(1,20)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()