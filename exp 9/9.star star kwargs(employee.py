def employee(**details):
    for k,v in details.items():
        print(k,":",v)
employee(ame="ashish",id=101,dept="it")