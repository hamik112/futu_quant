from trade_api.hk_trade_api import *
import time

class hk_trade_opt:
    def __init__(self, hk_trade_api):
        self.hk_trade_api = hk_trade_api

# envtype == 1 stands simulation
# envtype == 0 stands real trade
        self.envtype = 1
        self.place_time = 0

# Buy return:
# {'SvrResult': '0', 'Cookie': '888888', 'EnvType': '1', 'LocalID': '1425263522639675'}
    def buy(self, price, qty, strcode):
        cookie = "333"
        ret_code, ret_data = self.hk_trade_api.place_order(cookie, price, qty, strcode, 0, 0, self.envtype)
        if ret_code == -1:
            print("place order fail")
            return -1
        if ret_data["SvrResult"] == -1:
            print("buy fail")
            return -1
        if ret_data["Cookie"] != cookie:
            print("cookie check fail")
            return -1
        self.place_time = time.time()
        return ret_data["LocalID"]

    def sell(self,  price, qty, strcode):
        cookie = "444"
        ret_code, ret_data = self.hk_trade_api.place_order(cookie, price, qty, strcode, 1, 0, self.envtype)
        if ret_code == -1:
            print("place order fail")
            return -1, ""
        if ret_data["SvrResult"] == -1:
            print("sell fail")
            return -1, ""
        if ret_data["Cookie"] != cookie:
            print("cookie check fail")
            return -1, ""
        return 0, ret_data["LocalID"]



# order_list_query:
#  stock_code  stock_name dealt_avg_price dealt_qty localid orderid order_type  price status submited_time updated_time
# 0   67541  恒指法兴七八熊O.P   0.0  0  0  575219   0   0  0.06  7   1492965026   1492965026
# 1   67541  恒指法兴七八熊O.P   0.0  0  0  575220   0   1  0.06  7   1492965071   1492965071
    def get_order_id(self, localid):
        position = -1
        count = 0
        ret_code, ret_data = self.hk_trade_api.order_list_query("123", self.envtype)
        if ret_code == -1:
            return -1
        for i in ret_data["localid"]:
            if i == localid:
                position = count
                break
            count += 1

        if position == -1:
            print("warn: localid index fail")
            len = 0
            for index in ret_data.iterrows():
                len += 1

            if float(ret_data["submited_time"][len - 1]) - self.place_time < 10:
                position = len - 1
            else:
                position = -1
        if position == -1:
            print("check order id fail")
            return -1

        orderid = ret_data["orderid"][position]
        return orderid

    def clear_stock_code(self, stock_code, price):
        pos_qty = 0
        pos_qty = self.query_position_stock_qty(stock_code)
        if int(pos_qty) == 0 or int(pos_qty) == -1:
            return
        else:
            print(pos_qty, "!!!!!!!!!!")
            ret = self.sell(price, pos_qty, stock_code)
        return

    def modify_order_price(self, localid, price, qty, direction):
        position = -1
        count = 0
        ret_code, ret_data = self.hk_trade_api.order_list_query("777777", self.envtype)
        if ret_code == -1:
            return -1
        for i in ret_data["localid"]:
            if str(i) == str(localid):
                position = count
                print("Find Order")
                break
            count += 1

        if position == -1:
            print("No Such Order")
            return -1
        else:
            orderid = ret_data["orderid"][position]
            stock_code = ret_data["stock_code"][position]
            dealt_qty = ret_data["dealt_qty"][position]
            new_qty = qty - dealt_qty
            if new_qty <= 0:
                print("Already Dealt")
                return -1
            self.delete_order(orderid)
            if direction == 1:
                localid = self.sell(price, new_qty, stock_code)
            else:
                localid = self.buy(price, new_qty, stock_code)
        return localid

    def disble_order_stock_code(self, stock_code):
        position = -1
        count = 0
        ret_code, ret_data = self.hk_trade_api.order_list_query("123", self.envtype)
        if ret_code == -1:
            return -1
        #print(ret_data)
        for i in ret_data["stock_code"]:
            if str(i) == str(stock_code) and (int(ret_data["status"][count]) == 1 or int(ret_data["status"][count]) == 2):
                position = count
                print("Find Order")
                break
            count += 1
        if position == -1:
            print("No Such Order")
            return -1
        else:
            print("Disable Order")
            orderid = ret_data["orderid"][position]
            self.disable_order(orderid)
        return orderid

    def query_position_stock_qty(self, stock_code):
        position = -1
        count = 0
        pos_qty = 0
        ret_code, ret_data = self.hk_trade_api.position_list_query("456", self.envtype)
        if ret_code == -1:
            return -1
        print(ret_data)
        for i in ret_data["stock_code"]:
            if str(i) == str(stock_code):
                position = count
                print("Find Position")
                break
            count += 1
        if position == -1:
            print("No Such stock position")
        else:
            pos_qty = ret_data["can_sell_qty"][position]
        return pos_qty


    def check_order_status(self, orderid):
        cookie = "123"
        position = -1
        count = 0
        ret_code, ret_data = self.hk_trade_api.order_list_query(cookie, self.envtype)
        if ret_code == -1:
            return -1
        order_list = ret_data["orderid"]
        for i in order_list:
            if i == orderid:
                position = count
                break
            count += 1
        if position == -1:
            return -1
        return ret_data["status"][position]

    def disable_order(self, orderid):
        cookie = "555"
        ret_code, ret_data = self.hk_trade_api.set_order_status(cookie, 1, 0, orderid, self.envtype)
        if ret_code == -1:
            return -1
        if ret_data["SvrResult"] == -1:
            print("disable_order fail")
            return -1
        if ret_data["Cookie"] != cookie:
            print("cookie check fail")
            return -1
        return 1

    def delete_order(self, orderid):
        cookie = "444"
        ret_code, ret_data = self.hk_trade_api.set_order_status(cookie, 3, 0, orderid, self.envtype)
        if ret_code == -1:
            return -1
        if ret_data["SvrResult"] == -1:
            print("delete_order fail")
            return -1
        if ret_data["Cookie"] != cookie:
            print("delete_order check fail")
            return -1
        return 1

    def check_dealt_all(self, localid):
        position = -1
        count = 0
        status = 0
        ret_code, ret_data = self.hk_trade_api.order_list_query("97864", self.envtype)
        if ret_code == -1:
            return -1
        for i in ret_data["localid"]:
            if str(i) == str(localid):
                position = count
                print("Find Order")
                break
            count += 1
        if position == -1:
            print("No Such stock position")
            return 0
        else:
            status = ret_data["status"][position]
        if status == 3:
            return 1
        else:
            return 0

    def get_dealt_qty(self, orderid):
        cookie = "654"
        position = -1
        count = 0
        dealt_qty = 0
        ret_code, ret_data = self.hk_trade_api.order_list_query(cookie, self.envtype)
        if ret_code == -1:
            return -1

        for i in ret_data["orderid"]:
            if i == orderid:
                position = count
                break
            count += 1

        if position == -1:
            print("get_dealt qty fail")
            return -1

        dealt_qty = ret_data["dealt_qty"][position]
        return dealt_qty

# Usage Examples
#    hk_trade = hk_trade_api()
#    hk_trade.initialize()
#    hk_trade.unlock_trade('88888888', '584679')
#    opt = hk_trade_opt(hk_trade)
#    localid = opt.buy(0.06, 10000, "67541")
#    orderid = opt.get_order_id(localid)
#    status = opt.check_order_status(orderid)
#    dealt = opt.get_dealt_qty(orderid)
#    print(dealt)
#    opt.disable_order(orderid)
