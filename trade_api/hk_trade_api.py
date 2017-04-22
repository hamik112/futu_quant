from openft.open_quant_context import *
class hk_trade:
    def __init__(self, host = "127.0.0.1", sync_port = 11111):
        self.host = host
        self.sync_port = sync_port

    def initialize(self):
        self.tradehk_ctx = OpenHKTradeContext(host = "127.0.0.1", sync_port = 11111)

    def unlock_trade(self,cookie, passwd):
        ret_code, ret_data = self.tradehk_ctx.unlock_trade(cookie, passwd)
        if ret_code == RET_ERROR:
            print("Unlock fail")
            print(ret_data)
            return -1
        return 1

    def place_order(self,cookie, price, qty, strcode, orderside, ordertype, envtype):
        ret_code, ret_data = self.tradehk_ctx.place_order(cookie, price, qty, strcode, orderside, ordertype, envtype)
        if ret_code == RET_ERROR:
            print("place_order fail")
            print(ret_data)
            return -1
        return 1

    def set_order_status(self,cookie, status, localid, oderid, envtype):
    # order id and local id != 0 is ok.
        ret_code, ret_data = self.tradehk_ctx.set_order_status(cookie, status, localid, oderid, envtype)
        if ret_code == RET_ERROR:
            print("set_order_status fail")
            print(ret_data)
            return -1
        return 1

    def change_order(self, cookie, price, qty, localid, oderid, envtype):
        ret_code, ret_data = self.tradehk_ctx.change_order(cookie, price, qty, localid, oderid, envtype)
        if ret_code == RET_ERROR:
            print("change_order fail")
            print(ret_data)
            return -1
        return 1

    def accinfo_query(self, cookie, envtype):
        ret_code, ret_data = self.tradehk_ctx.accinfo_query(cookie, envtype)
        print(ret_code)
        print(ret_data)
        if ret_code == RET_ERROR:
            print("accinfo_query fail")
            print(ret_data)
            return -1
        return 1