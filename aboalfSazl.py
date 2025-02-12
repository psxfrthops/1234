hour = int(input("لطفا ساعت را وارد کنید: "))

if 0 <= hour < 6:
    print("نیمه شب بخیر")
elif 6 <= hour < 12:
    print("صبح بخیر")
elif 12 <= hour < 18:
    print("بعد از ظهر بخیر")
elif 18 <= hour <= 24:
    print("شب بخیر")
else:
    print("سارا خانم، لطفا عددی در بازه ی ۰ تا ۲۴ وارد کن")