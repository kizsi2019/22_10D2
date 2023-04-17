from hiresek_alap import Hires

hires1 = Hires(input("Add meg egy híres nő nevét! "), input("Add meg a foglalkozását! "), input("Add meg a nemzetiségét (a/n)! "))
hires2 = Hires(input("Add meg egy híres nő nevét! "), input("Add meg a foglalkozását! "), input("Add meg a nemzetiségét (a/n)! "))
hires3 = Hires(input("Add meg egy híres nő nevét! "), input("Add meg a foglalkozását! "), input("Add meg a nemzetiségét (a/n)! "))

print(hires1.get_prefix(), hires1.get_name(), "egy híres", hires1.get_job())
print(hires2.get_prefix(), hires2.get_name(), "egy híres", hires2.get_job())
print(hires3.get_prefix(), hires3.get_name(), "egy híres", hires3.get_job())
