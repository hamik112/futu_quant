import playsound
import time
import threading

STOP = 0


class PlaySound(threading.Thread):
    def __init__(self):
        super(PlaySound, self).__init__()
        self.fail_times = 0

        self.start_bear =        STOP
        self.stop_lossing_bear = STOP
        self.stop_lossing_bear_inst= STOP
        self.start_bull =        STOP
        self.stop_lossing_bull = STOP
        self.burst_down =        STOP
        self.burst_up =          STOP
        self.morning_warn =      STOP
        self.no_trend =          STOP
        self.warn_bull_revover = STOP
        self.bull_recover_down_trend= STOP
        self.warn_bogus_break =  STOP
        self.warn_low_amplitude = STOP
        self.general_warn = STOP
        self.warn_ma_low = STOP
        self.zma10_decrease = STOP

        self.start_bear_path =        r"D:\quant\\test0\\futu_quant\\sounds\start_bear.wav"
        self.start_bull_path =        r"D:\quant\\test0\\futu_quant\\sounds\start_bull.wav"
        self.stop_lossing_bear_path = r"D:\quant\\test0\\futu_quant\\sounds\stop_lossing_bear.wav"
        self.stop_lossing_bear_inst_path = r"D:\quant\\test0\\futu_quant\\sounds\stop_lossing_bear_inst.wav"
        self.stop_lossing_bull_path = r"D:\quant\\test0\\futu_quant\\sounds\stop_lossing_bull.wav"
        self.burst_down_path =        r"D:\quant\\test0\\futu_quant\\sounds\burst_down.wav"
        self.burst_up_path =          r"D:\quant\\test0\\futu_quant\\sounds\burst_up.wav"
        self.morning_warn_path =      r"D:\quant\\test0\\futu_quant\\sounds\morning_warn.wav"
        self.no_trend_path =          r"D:\quant\\test0\\futu_quant\\sounds\no_trend.wav"
        self.warn_bull_revover_path = r"D:\quant\\test0\\futu_quant\\sounds\warn_bull_revover.wav"
        self.bull_recover_down_trend_path= r"D:\quant\\test0\\futu_quant\\sounds\bull_recover_down_trend.wav"
        self.warn_bogus_break_path =  r"D:\quant\\test0\\futu_quant\\sounds\warn_bogus_break.wav"
        self.warn_low_amplitude_path = r"D:\quant\\test0\\futu_quant\\sounds\warn_low_amplitude.wav"
        self.general_warn_path =      r"D:\quant\\test0\\futu_quant\\sounds\general_warn.wav"
        self.warn_ma_low_path =       r"D:\quant\\test0\\futu_quant\\sounds\warn_ma_low.wav"
        self.zma10_decrease_path =    r"D:\quant\\test0\\futu_quant\\sounds\zma10_decrease.wav"

# PLAY Signal
    def play_burst_up(self):
        self.burst_up += 1

    def play_burst_down(self):
        self.burst_down += 1

    def play_stop_lossing_bull(self):
        self.stop_lossing_bull += 1

    def play_stop_lossing_bear(self):
        self.stop_lossing_bear += 1

    def play_stop_lossing_bear_inst(self):
        self.stop_lossing_bear_inst += 1

    def play_start_bear(self):
        self.start_bear += 1

    def play_start_bull(self):
        self.start_bull += 1

    def play_morning_warn(self):
        self.morning_warn += 1

    def play_no_trend(self):
        self.no_trend += 1

    def play_warn_bull_recover(self):
        self.warn_bull_revover += 1

    def play_bull_recover_down_trend(self):
        self.bull_recover_down_trend += 1

    def play_warn_bogus_break(self):
        self.warn_bogus_break += 1

    def play_warn_low_amplitude(self):
        self.warn_low_amplitude += 1

    def play_general_warn(self):
        self.general_warn += 1

    def play_warn_ma_low(self):
        self.warn_ma_low += 1

    def play_zma10_decrease(self):
        self.zma10_decrease += 1

# STOP Signal
    def stop_play_stop_lossing_bull(self):
        self.stop_lossing_bull = STOP

    def stop_play_stop_lossing_bear(self):
        self.stop_lossing_bear = STOP
        self.stop_lossing_bear_inst = STOP

    def stop_play_start_bear(self):
        self.start_bear = STOP

    def stop_play_start_bull(self):
        self.start_bull = STOP

    def stop_burst_up(self):
        self.burst_up = STOP

    def stop_burst_down(self):
        self.burst_down = STOP

    def stop_play_morning_warn(self):
        self.morning_warn = STOP

    def stop_play_no_trend(self):
        self.no_trend = STOP

    def stop_play_warn_bull_recover(self):
        self.warn_bull_revover = STOP

    def stop_play_bull_recover_down_trend(self):
        self.bull_recover_down_trend = STOP

    def stop_play_warn_bogus_break(self):
        self.warn_bogus_break = STOP

    def stop_play_warn_low_amplitude(self):
        self.warn_low_amplitude = STOP

    def stop_play_general_warn(self):
        self.general_warn = STOP

    def stop_play_warn_ma_low(self):
        self.warn_ma_low = STOP

    def stop_play_zma10_decrease(self):
        self.zma10_decrease = STOP


    def play_sound(self, path):
        try:
            #playsound.playsound(path)
            x=1
            #print("skip play")
        except:
            #print("WARN: Play Sound Fail")
            self.fail_times += 1
            return
        self.fail_times = 0
        return

    def run(self):
        while(1):
            if self.burst_up != STOP:
                self.play_sound(self.burst_up_path)
                self.burst_up -= 1

            if self.burst_down != STOP:
                self.play_sound(self.burst_down_path)
                self.burst_down -= 1

            if self.stop_lossing_bear != STOP:
                self.play_sound(self.stop_lossing_bear_path)
                self.stop_lossing_bear -= 1

            if self.stop_lossing_bear_inst != STOP:
                self.play_sound(self.stop_lossing_bear_inst_path)
                self.stop_lossing_bear_inst -= 1

            if self.zma10_decrease != STOP:
                self.play_sound(self.zma10_decrease_path)
                self.zma10_decrease -= 1

            if self.stop_lossing_bull != STOP:
                self.play_sound(self.stop_lossing_bull_path)
                self.stop_lossing_bull -= 1

            if self.start_bear != STOP:
                self.play_sound(self.start_bear_path)
                self.start_bear -= 1

            if self.start_bull != STOP:
                self.play_sound(self.start_bull_path)
                self.start_bull -= 1

            if self.no_trend != STOP:
                self.play_sound(self.no_trend_path)
                self.no_trend -= 1

            if self.morning_warn != STOP:
                self.play_sound(self.morning_warn_path)
                self.morning_warn -= 1

            if self.warn_bull_revover != STOP:
                self.play_sound(self.warn_bull_revover_path)
                self.warn_bull_revover -= 1

            if self.bull_recover_down_trend != STOP:
                self.play_sound(self.bull_recover_down_trend_path)
                self.bull_recover_down_trend -= 1

            if self.warn_bogus_break != STOP:
                self.play_sound(self.warn_bogus_break_path)
                self.warn_bogus_break -= 1

            if self.warn_low_amplitude != STOP:
                self.play_sound(self.warn_low_amplitude_path)
                self.warn_low_amplitude -= 1

            if self.general_warn != STOP:
                self.play_sound(self.general_warn_path)

            if self.warn_ma_low != STOP:
                self.play_sound(self.warn_ma_low_path)

            if self.fail_times > 20:
                break

            time.sleep(0.2)
