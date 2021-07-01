# Collection을 사용하면 if나 switch의 분기보다 힙 메모리는 더 사용하지만 더 좋은 성능을 얻을 수 있다.
# 아래 코드를 collection을 사용하는 방법으로 바꾸어보자
# JavaScript 코드
# const date = new Date()
# const year = date.getFullYear()
# const month = date.getMonth()
#
# var days = null
#
# switch(month){
#     case 0:
#     case 2:
#     case 4:
#     case 6:
#     case 7:
#     case 9:
#     case 11:
#         days = 31
#         break
#
#     case 3:
#     case 5:
#     case 8:
#     case 10:
#         days = 30
#         break
#
#     case 1:
#         if((year % 4 == 0) && (year % 100 != 0) || (year % 400) == 0)
#             days = 29
#         else
#             days = 28
#         break
# }
#
# console.log(days + ' days for ' + year + '-' + (month + 1))


from datetime import date


today = date.today()
year = today.year
month = today.month
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = days[month - 1]
if (month == 2 and year % 4 == 0 and year % 100 != 0) or (month == 2 and year % 400 == 0):
    day += 1

print('%d days for %d-%d' % (day, year, month))