# dessert.py
# 參考網址:(python 函數的可變參數 *args 和 **kwargs)http://blog.maxkit.com.tw/2018/12/python-args-kwargs.html

def ice_cream(*ingredients):
    print("冰淇淋 材料如下:")
    n = 0
    for i in ingredients:
        n += 1
        print(str(n) + "," + i)
        
def pudding(brand,taste):
    print("布丁 規格如下:")
    print("品牌:",brand)
    print("口味:",taste)
    
    
    
#a = ice_cream("香蕉","巧克力","哈根達斯")
#print("\n")
#b = pudding("統一","牛奶")