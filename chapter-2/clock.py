## Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on the clock when the alarm goes off.


time_now = input("what is the current time now (in hours)?")
time_now_int = int (time_now)

set_alarm = input ("Number of hours you want to wait for the alarm")
set_alarm_int = int(set_alarm)

total_time = time_now_int + set_alarm_int

final_time = total_time % 24 

print (final_time)