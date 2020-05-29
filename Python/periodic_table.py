#Just enter the correct name of element and know all about it 
#for example if you want to know about hydrogen just enter hydrogen as input.
#this periodic data contain only data till atomic number 118
try:
    import pandas as pd
    a = input().capitalize()
    a = " ".join(a.split())
    periodicdata = pd.read_csv("https://gist.githubusercontent.com/GoodmanSciences/c2dd862cd38f21b0ad36b8f96b4bf1ee/raw/1d92663004489a5b6926e944c1b3d9ec5c40900e/Periodic%2520Table%2520of%2520Elements.csv",index_col="Element")
    print(periodicdata.loc[a,:])
except KeyError:
    print("Ops ! No such element found. \nEnter the correct element. TRY AGAIN !!")
