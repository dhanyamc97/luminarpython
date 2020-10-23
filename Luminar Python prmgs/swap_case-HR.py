# s=input()
# str=""
# for elem in s:
#     if(elem.isupper()):
#         print()
#         str+=elem.lower()
#     else:
#         print(elem.upper())
#         str += elem.upper()
#
# print(str)

# a= "dhanya"
# b="mc"
# str = "Hello {} {} lastname! You just delved into python.".format(a, b)
# print(str)

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)

# #Top Pillars
# for i in range(thickness+1):
#     print (c*thickness).______(thickness*2)+(c*thickness).______(thickness*6)
#
# #Middle Belt
# for i in range((thickness+1)/2):
#     print (c*thickness*5).______(thickness*6)
#
# #Bottom Pillars
# for i in range(thickness+1):
#     print (c*thickness).______(thickness*2)+(c*thickness).______(thickness*6)
#
# #Bottom Cone
# for i in range(thickness):
#     print ((c*(thickness-i-1)).______(thickness)+c+(c*(thickness-i-1)).______(thickness)).______(thickness*6)
#







