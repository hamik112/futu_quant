from db.db_basic import *
import time

class dbop_ma_trand:
    def __init__(self):
        self.count = 0
        self.position = 0
        self.insert_ct = 0

    def dbop_store_ma_dur2(self, db_basic, ma10_val, ma20_val,cur_val, ask_val, bid_val, ask_p_val, bid_p_val):
        sql = "insert into dur2_trend(ma10,ma20,cur,ask,bid, p_ask, p_bid) values(" + str(ma10_val) + "," + str(ma20_val) + "," + str(cur_val)  + "," + str(ask_val)  + "," + str(bid_val) + "," + str(ask_p_val) + "," + str(bid_p_val) + ");"
        db_basic.insertMysql(sql)

    def dbop_store_ma_dur5(self, db_basic, ma10_val, ma20_val, cur_val, ask_val, bid_val, ask_p_val, bid_p_val):
        sql = "insert into dur5_trend(ma10,ma20,cur,ask,bid, p_ask, p_bid) values(" + str(ma10_val) + "," + str(ma20_val) + "," + str(cur_val)  + "," + str(ask_val)  + "," + str(bid_val) + "," + str(ask_p_val) + "," + str(bid_p_val) + ");"
        db_basic.insertMysql(sql)

    def dbop_read_ma_dur2(self, db_basic, time_start, time_end):
        sql = "select * from dur2_trend where time > '" + time_start + "' and time < '" + time_end + "';"
        self.count = db_basic.queryMysql(sql)
        return self.count

    def dbop_read_ma_dur_next(self, db_basic):
        if self.position >= self.count:
            return ""
        try:
            ret = db_basic.cursor.fetchone()
        except:
            print("fetchone fail")
            return ""
        self.position += 1
        return ret

    ###
    #  Table day_data_new2
    ###
    # "No.", "cur", "time", "zma10", "zma20", "zma10_ratio", "zma20_ratio", "zma20_ratio_ratio", "zma_gap", "zma_gap_ratio", "zma_gap_ratio_ratio",
    # "No.", "cur", "time", "zma10", "ma20", "zma10_ratio", "zma10_ratio_ratio", "zma10_ratio_ratio_ratio", "trade_mark", "ma20_ratio", "zma10_ratio_ratio_short"
    def dbop_add_day_data(self, db_basic, id, cur, time, zma10, ma20, zma10_ratio, zma10_ratio_ratio, zma10_ratio_ratio_ratio, trade_mark, ma20_ratio, zma10_ratio_ratio_short):
        sql = "insert into day_data_new_a(id,cur,time, zma10,ma20, zma10_ratio, zma10_ratio_ratio, zma10_ratio_ratio_ratio, trade_mark, ma20_ratio, zma10_ratio_ratio_short) values(" + \
              str(id) + "," + str(cur) + ", '" + str(time) + "' ," + str(zma10) + "," + str(ma20) + "," + \
              str(zma10_ratio) + "," + str(zma10_ratio_ratio) + "," + str(zma10_ratio_ratio_ratio) + "," + str(trade_mark) + "," + \
              str(ma20_ratio) + "," + str(zma10_ratio_ratio_short) + ");"
        db_basic.insertMysql(sql)


    def dbop_read_day_data(self, db_basic, time_start, time_end):
        sql = "select * from day_data_new_a where time > '" + str(time_start) + "' and time < '" + str(time_end) + "';"
        self.count = db_basic.queryMysql(sql)
        self.position = 0
        return self.count


    def dbop_update_day_data_trade_mark(self, db_basic, id, trade_mark):
        sql = "update day_data_new2 set trade_mark = " + str(trade_mark) + "where id = " + str(id) + ";"
        db_basic.insertMysql(sql)

    def dbop_read_day_data_next(self, db_basic):
        if self.position >= self.count:
            return ""
        try:
            ret = db_basic.cursor.fetchone()
        except:
            print("fetchone fail")
            return ""
        self.position += 1
        return ret

########### NEW TEST
    def dbop_read_day_data_standard(self, db_basic, time_start, time_end):
        sql = "select * from standard_quo where time > '" + time_start + "' and time < '" + time_end + "';"
        self.count = db_basic.queryMysql(sql)
        self.position = 0
        return self.count

    def dbop_read_day_data_standard_next(self, db_basic):
        if self.position >= self.count:
            return ""
        try:
            ret = db_basic.cursor.fetchone()
        except:
            print("fetchone fail")
            return ""
        self.position += 1
        return ret

    ###
    ## Table adjust_parameters
    ###
    def dbop_read_adj_paras(self, db_basic):
        sql = "select * from adjust_parameters ;"
        self.count = db_basic.queryMysql(sql)
        self.position = 0
        return self.count

    def dbop_read_adj_paras_next(self, db_basic):
        if self.position >= self.count:
            return "Error"
        try:
            ret = db_basic.cursor.fetchone()
        except:
            print("fetchone fail")
            return "Error"
        self.position += 1
        return ret

######## TBD
    def dbop_add_adj_paras(self, db_basic, zma20_r, zma10_r_r, cur_r):
        sql = "insert into adjust_parameters( zma20_ratio, zma10_ratio_ratio, cur_ratio) values(" + \
              str(zma20_r) + "," + str(zma10_r_r) + ", " + str(cur_r) + ");"
        db_basic.insertMysql(sql)

    ###
    ## Table trade_mark
    ###
    def dbop_read_mark_trade(self, db_basic):
        sql = "select * from trade_mark ;"
        self.count = db_basic.queryMysql(sql)
        self.position = 0
        return self.count

    def dbop_read_mark_trade_next(self, db_basic):
        if self.position >= self.count:
            return ""
        try:
            ret = db_basic.cursor.fetchone()
        except:
            print("fetchone fail")
            return ""
        self.position += 1
        return ret

    def dbop_add_mark_trade(self, db_basic, time_no, para_index, trade_mark):
        if self.insert_ct == 30000:
            print("REST!!!!")
            time.sleep(20)
            self.insert_ct = 0
        sql = "insert into trade_mark(id, para_index, trade_mark) values(" + \
            str(time_no) + "," + str(para_index) + "," + str(trade_mark) + ");"
        db_basic.insertMysql(sql)
        self.insert_ct += 1

    ####
    ## Table judge_result
    ####
    def dbop_add_judge_result(self, db_basic, No, action, passive_gap, turn_pos, turn_gap, index):
        sql = "insert into judge_result(id, action, result, turn_pos, turn_gap, para_index) values(" + \
            str(No) + "," + str(action) + "," + str(passive_gap) + "," + str(turn_pos) + "," + str(turn_gap) + "," + str(index) + ");"
        db_basic.insertMysql(sql)

    def dbop_add_ch_rates(self, db_basic, cur, cur_gap_5s, cur_gap_10s, cur_gap_20s):
        sql = "insert into ch_rates(cur, cur_gap_5s, cur_gap_10s, cur_gap_20s) values(" + \
            str(cur) + "," + str(cur_gap_5s) + "," + str(cur_gap_10s) + "," + str(cur_gap_20s) + ");"
        db_basic.insertMysql(sql)

    def dbop_add_standard_quo(self, db_basic, cur, MA10_cur, MA20_cur, deltaMA10_ma3, deltaMA20_ma3):
        sql = "insert into standard_quo(cur, MA10, MA20, delta_ma10_ma3, delta_ma20_ma3) values(" + \
            str(cur) + "," + str(MA10_cur) + "," + str(MA20_cur) + "," + str(deltaMA10_ma3) + "," + str(deltaMA20_ma3) + ");"
        db_basic.insertMysql(sql)

