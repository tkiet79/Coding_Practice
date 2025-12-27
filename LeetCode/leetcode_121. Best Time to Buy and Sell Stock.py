
prices = [7,1,5,3,6,4]
buy_price = prices[0] # giả sử giá mua = 7
profit = 0 # đặt lợi nhuận ban đầu là 0

for p in prices[1:]: # xét từ idx 1 trở đi
    if buy_price > p: # nếu 7 > giá trị nào đó từ 1:
        buy_price = p # thì giá trị đó chính là giá mua
    profit = max(profit, p - buy_price) # p - buy_price là nó sẽ thử từng giá trị từ 1: và gán vô thằng profit
                                        # sau đó so sánh giữa profit cũ và cái vừa mới gán để tìm ra cái lớn nhất

print(profit)

    
     

    
