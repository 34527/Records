Lottery
import random


class LottoNumbers:
    def __init__(self):
        self.lotto_1 = int(random.randint(1,49))
        self.lotto_2 = int(random.randint(1,49))
        self.lotto_3 = int(random.randint(1,49))
        self.lotto_4 = int(random.randint(1,49))
        self.lotto_5 = int(random.randint(1,49))
        self.lotto_6 = int(random.randint(1,49))

def lotto_lists():
    lotto_list = LottoNumbers()
    return lotto_list

def display(lotto_list):
    for each in lotto_list:
        print("{0}".format(each.lotto_1))
        
        

def main():
    lotto_list = lotto_lists()
    display(lotto_list)
              
              


main()
    
    



