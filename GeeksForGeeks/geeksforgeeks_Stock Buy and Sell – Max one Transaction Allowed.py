class Solution:
    def maximumProfit(self, prices):
        n = len(prices)
        if n < 2:
            return 0
            
        # Giả sử giá mua thấp nhất ban đầu là vô cực
        min_price = float('inf') 
        max_profit = 0
        
        for price in prices:
            # 1. Cập nhật giá thấp nhất nếu gặp giá rẻ hơn
            if price < min_price:
                min_price = price
            
            # 2. Nếu bán hôm nay có lời hơn kỷ lục cũ thì cập nhật
            # (Lợi nhuận = Giá hôm nay - Giá thấp nhất đã từng gặp)
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
