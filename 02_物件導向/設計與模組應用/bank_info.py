class Bank():
    def __init__(self,user):
        self.user = user
        self.__total = 0 #設定私有的一開始存款金額
        self.title = "玉山銀行" #設定開戶銀行
        
    def save_money(self,save):
        self.__total += save
        print(self.user,"存入:",save,"元")
        
    def take_money(self,take):
        self.__total -= take
        print(self.user,"取出:",take,"元")
        
    def get_total(self):
        print("存款金額:",self.__total)

        
        
class Wu_Bank(Bank):
    def __init__(self):
        self.title = "吳氏銀行"
        
    def bank_title(self):
        print(self.title)