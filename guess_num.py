import random
r = random.randint(1, 100)
count = 0 #必須寫在 while 外面, 才不會每次進 while 都被歸零
while True:
    num = input('請輸入數字: ')
    num = int(num)
    count += 1 # 等於 count = count + 1
    if num == r:
        print('終於猜對了')
        print('這是你猜的第', count, '次') #如此才會在猜對時也顯示出猜第幾次
        break
    elif num > r:
        print('比答案小喔')
    elif num < r:
        print('比答案大喔')
    print('這是你猜的第', count, '次')