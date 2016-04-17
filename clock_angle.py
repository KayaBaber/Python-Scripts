#-*-coding:utf8;-*-
#qpy:2
#qpy:console
def clock_angle(hours, minutes):
    hourAngle=((hours%12) + (minutes/60.0))*30
    minAngle = minutes * 6
    return minAngle-hourAngle
for i in range(60):
    print clock_angle(12,i)