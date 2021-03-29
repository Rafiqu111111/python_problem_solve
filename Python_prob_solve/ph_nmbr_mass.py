def nm():
    nmbr = ['0170350058','0155739311','0191564601']
    for i in range(3):
        m_numbr = input("enter your number: " )
        numbr2 = []
        numbr2 = m_numbr
        if numbr2 in nmbr:
            print("number match",numbr2)
        else:
            print("hello loser")

nm()