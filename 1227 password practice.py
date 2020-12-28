pwd = 'a123456'
count = 3
while True:
    pw = input ('Please enter your password: ')
    if pw == pwd:
        print ('Logged in successfully!')
        break
    else :
        count = count - 1 
        print ('Password error remian' , count  , 'chance(s) ')
        if count == 0 :
            print ('Please contact admin!') 
            break




pwd = 'yuyu5438'
c = 3
while True :
    pw = input ('Please enter your password:')
    if pw == pwd :
        print ('Logged in successfully!')
        break
    else :
        c = c - 1
        print ('Password incorrect, please try again' , c , ' chance(s) remain ')
        if c == 0 :
            print ('Please contact admin !')
            break


pwd = 'yuyu5438'
c = 3
while c > 0:
    c = c - 1 #Moved from "else" under "While" indicates "每輸入一次密碼，就用掉一次機會"
    pw = input ('pleae enter your password: ')
    if pw == pwd :
        print ('Logged in successfully!')
    else :
        print ('Password incorrect! Please try again')
        if c > 0 :    #為了不顯示剩餘0次機會
            print(c , 'chance(s) remain' )
        else :
           print ('please contact admin!')