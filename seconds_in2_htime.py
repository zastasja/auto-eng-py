#Электронные часы - 2
#Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов в диапазоне от 0 до 23, потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд. Количество минут и секунд при необходимости дополняются до двузначного числа нулями.

#Программа получает на вход число n - количество секунд, которое прошло с начала суток.

#Выведите показания часов, соблюдая формат - h:mm:ss


sec = int(input())
h = (sec//3600%24)
sec = sec%3600
m = sec//60
m = str(m).zfill(2)
s = sec%60
s = str(s).zfill(2)

print(h, m, s, sep=":")
