#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: WBFM Transmitter
# Author: Scott Jordan
# Description: Transmits WBFM from pc audio
# Generated: Tue Sep 10 22:05:49 2019
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

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import baz
import time
import wx


class WBFM_Transmitter(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="WBFM Transmitter")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.rf_gain = rf_gain = 64
        self.if_gain = if_gain = 50
        self.freq = freq = 96100000
        self.bb_gain = bb_gain = 50
        self.audio_deci = audio_deci = 1
        self.aud_gain = aud_gain = 3
        self.adj = adj = 0

        ##################################################
        # Blocks
        ##################################################
        _bb_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._bb_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_bb_gain_sizer,
        	value=self.bb_gain,
        	callback=self.set_bb_gain,
        	label='BB Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._bb_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_bb_gain_sizer,
        	value=self.bb_gain,
        	callback=self.set_bb_gain,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_bb_gain_sizer, 5, 1, 1, 1)
        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
        	",".join(('serial=30C7E1D', "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0_0.set_samp_rate(1000000)
        self.uhd_usrp_sink_0_0.set_center_freq(433.893e6, 0)
        self.uhd_usrp_sink_0_0.set_gain(bb_gain, 0)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0_0.set_bandwidth(1000000, 0)
        _rf_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rf_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	label='RF Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rf_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_rf_gain_sizer, 3, 1, 1, 1)
        _if_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._if_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_if_gain_sizer,
        	value=self.if_gain,
        	callback=self.set_if_gain,
        	label='IF Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._if_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_if_gain_sizer,
        	value=self.if_gain,
        	callback=self.set_if_gain,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_if_gain_sizer, 4, 1, 1, 1)
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label='Transmit Frequency',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=88100000,
        	maximum=108100000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_freq_sizer, 1, 1, 1, 1)
        self.baz_file_source_0 = baz.file_source((0 if 0 > 0 else gr.sizeof_gr_complex)*1, '', True, 0, '', False, 0, True, [])
        _audio_deci_sizer = wx.BoxSizer(wx.VERTICAL)
        self._audio_deci_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_audio_deci_sizer,
        	value=self.audio_deci,
        	callback=self.set_audio_deci,
        	label='Input Audio Decimation',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._audio_deci_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_audio_deci_sizer,
        	value=self.audio_deci,
        	callback=self.set_audio_deci,
        	minimum=0,
        	maximum=20,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_audio_deci_sizer, 7, 1, 1, 1)
        _aud_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._aud_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_aud_gain_sizer,
        	value=self.aud_gain,
        	callback=self.set_aud_gain,
        	label='Audio Input Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._aud_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_aud_gain_sizer,
        	value=self.aud_gain,
        	callback=self.set_aud_gain,
        	minimum=1,
        	maximum=100,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_aud_gain_sizer, 6, 1, 1, 1)
        _adj_sizer = wx.BoxSizer(wx.VERTICAL)
        self._adj_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_adj_sizer,
        	value=self.adj,
        	callback=self.set_adj,
        	label='Fine Transmit Adj.',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._adj_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_adj_sizer,
        	value=self.adj,
        	callback=self.set_adj,
        	minimum=-200000,
        	maximum=200000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_adj_sizer, 2, 1, 1, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.baz_file_source_0, 0), (self.uhd_usrp_sink_0_0, 0))

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self._rf_gain_slider.set_value(self.rf_gain)
        self._rf_gain_text_box.set_value(self.rf_gain)

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        self._if_gain_slider.set_value(self.if_gain)
        self._if_gain_text_box.set_value(self.if_gain)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        self._bb_gain_slider.set_value(self.bb_gain)
        self._bb_gain_text_box.set_value(self.bb_gain)
        self.uhd_usrp_sink_0_0.set_gain(self.bb_gain, 0)


    def get_audio_deci(self):
        return self.audio_deci

    def set_audio_deci(self, audio_deci):
        self.audio_deci = audio_deci
        self._audio_deci_slider.set_value(self.audio_deci)
        self._audio_deci_text_box.set_value(self.audio_deci)

    def get_aud_gain(self):
        return self.aud_gain

    def set_aud_gain(self, aud_gain):
        self.aud_gain = aud_gain
        self._aud_gain_slider.set_value(self.aud_gain)
        self._aud_gain_text_box.set_value(self.aud_gain)

    def get_adj(self):
        return self.adj

    def set_adj(self, adj):
        self.adj = adj
        self._adj_slider.set_value(self.adj)
        self._adj_text_box.set_value(self.adj)


def main(top_block_cls=WBFM_Transmitter, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
