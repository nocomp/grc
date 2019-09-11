#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Airband
# Author: Tapio Valli
# Description: Simple airband scanner
# Generated: Mon Jun 27 13:34:23 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx


class airband(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Airband")
        _icon_path = "C:\gnuradio\share\icons\hicolor\48x48/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 500e-3
        self.samp_rate = samp_rate = 2.4e6
        self.offset_freq = offset_freq = -300e3
        self.freq_corr = freq_corr = 65
        self.base_freq = base_freq = 119.4e6

        ##################################################
        # Blocks
        ##################################################
        _volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	label="Volume",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_volume_sizer)
        self._offset_freq_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.offset_freq,
        	callback=self.set_offset_freq,
        	label="Frequency select",
        	choices=[-800e3,-550e3, -300e3,300e3,500e3],
        	labels=["meythet 118.2M","TWR2 118.85M", "APP1 119.1M","APP2 119.7M","APP3 119.9M"],
        	style=wx.RA_VERTICAL,
        )
        self.Add(self._offset_freq_chooser)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=512,
        	fft_rate=5,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(base_freq, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(50, (firdes.low_pass_2(1,samp_rate,25e3,10e3,40)), offset_freq, samp_rate)
        _freq_corr_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_corr_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_corr_sizer,
        	value=self.freq_corr,
        	callback=self.set_freq_corr,
        	label="Freq correction (ppm)",
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._freq_corr_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_corr_sizer,
        	value=self.freq_corr,
        	callback=self.set_freq_corr,
        	minimum=-127,
        	maximum=127,
        	num_steps=254,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_freq_corr_sizer)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.audio_sink_0 = audio.sink(48000, "pulse", True)
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=48e3,
        	audio_decim=1,
        	audio_pass=5000,
        	audio_stop=5500,
        )
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-5, 1, 0)
        self.analog_agc2_xx_0.set_max_gain(5)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.analog_am_demod_cf_0, 0))    
        self.connect((self.analog_am_demod_cf_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_agc2_xx_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.wxgui_fftsink2_0, 0))    

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self._volume_slider.set_value(self.volume)
        self._volume_text_box.set_value(self.volume)
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass_2(1,self.samp_rate,25e3,10e3,40)))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

    def get_offset_freq(self):
        return self.offset_freq

    def set_offset_freq(self, offset_freq):
        self.offset_freq = offset_freq
        self._offset_freq_chooser.set_value(self.offset_freq)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.offset_freq)

    def get_freq_corr(self):
        return self.freq_corr

    def set_freq_corr(self, freq_corr):
        self.freq_corr = freq_corr
        self._freq_corr_slider.set_value(self.freq_corr)
        self._freq_corr_text_box.set_value(self.freq_corr)

    def get_base_freq(self):
        return self.base_freq

    def set_base_freq(self, base_freq):
        self.base_freq = base_freq
        self.uhd_usrp_source_0.set_center_freq(self.base_freq, 0)


def main(top_block_cls=airband, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
