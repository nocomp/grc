#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: UHD FFT
# Author: Example
# Description: UHD FFT Waveform Plotter
# Generated: Tue Sep 10 21:54:12 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import sip
import sys
import threading
import time
from gnuradio import qtgui


class uhd_fft(gr.top_block, Qt.QWidget):

    def __init__(self, antenna='RX2', args='', fft_size=1024, freq=466.05e6, gain=20, samp_rate=1e6, spec='', stream_args='', update_rate=.1, wire_format=''):
        gr.top_block.__init__(self, "UHD FFT")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("UHD FFT")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "uhd_fft")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Parameters
        ##################################################
        self.antenna = antenna
        self.args = args
        self.fft_size = fft_size
        self.freq = freq
        self.gain = gain
        self.samp_rate = samp_rate
        self.spec = spec
        self.stream_args = stream_args
        self.update_rate = update_rate
        self.wire_format = wire_format

        ##################################################
        # Variables
        ##################################################
        self.freq_c = freq_c = freq
        self.chan0_lo_locked = chan0_lo_locked = uhd.sensor_value("", False, "")
        self.usrp_device_info = usrp_device_info = uhd.get_version_string()
        self.uhd_version_info = uhd_version_info = uhd.get_version_string()
        self.samp_rate_ = samp_rate_ = samp_rate
        self.lo_locked_probe = lo_locked_probe = chan0_lo_locked.to_bool()
        self.gain_ = gain_ = gain
        self.current_freq_c = current_freq_c = freq_c
        self.ant = ant = antenna

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate__tool_bar = Qt.QToolBar(self)
        self._samp_rate__tool_bar.addWidget(Qt.QLabel('Sampling Rate'+": "))
        self._samp_rate__line_edit = Qt.QLineEdit(str(self.samp_rate_))
        self._samp_rate__tool_bar.addWidget(self._samp_rate__line_edit)
        self._samp_rate__line_edit.returnPressed.connect(
        	lambda: self.set_samp_rate_(eng_notation.str_to_num(str(self._samp_rate__line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._samp_rate__tool_bar, 3, 2, 1, 2)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._gain__range = Range(0, 31.5, .5, gain, 200)
        self._gain__win = RangeWidget(self._gain__range, self.set_gain_, 'RX Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain__win, 2, 0, 1, 4)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_c_tool_bar = Qt.QToolBar(self)
        self._freq_c_tool_bar.addWidget(Qt.QLabel('RX Tune Frequency'+": "))
        self._freq_c_line_edit = Qt.QLineEdit(str(self.freq_c))
        self._freq_c_tool_bar.addWidget(self._freq_c_line_edit)
        self._freq_c_line_edit.returnPressed.connect(
        	lambda: self.set_freq_c(eng_notation.str_to_num(str(self._freq_c_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._freq_c_tool_bar, 3, 0, 1, 2)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join((args, "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate_)
        self.uhd_usrp_source_0.set_center_freq(float(freq_c), 0)
        self.uhd_usrp_source_0.set_gain(gain_, 0)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_source_0.set_bandwidth(samp_rate, 0)
        self.uhd_usrp_source_0.set_auto_dc_offset("", 0)
        self.uhd_usrp_source_0.set_auto_iq_balance("", 0)
        self.display = Qt.QTabWidget()
        self.display_widget_0 = Qt.QWidget()
        self.display_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.display_widget_0)
        self.display_grid_layout_0 = Qt.QGridLayout()
        self.display_layout_0.addLayout(self.display_grid_layout_0)
        self.display.addTab(self.display_widget_0, 'Spectrum')
        self.display_widget_1 = Qt.QWidget()
        self.display_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.display_widget_1)
        self.display_grid_layout_1 = Qt.QGridLayout()
        self.display_layout_1.addLayout(self.display_grid_layout_1)
        self.display.addTab(self.display_widget_1, 'Waterfall')
        self.display_widget_2 = Qt.QWidget()
        self.display_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.display_widget_2)
        self.display_grid_layout_2 = Qt.QGridLayout()
        self.display_layout_2.addLayout(self.display_grid_layout_2)
        self.display.addTab(self.display_widget_2, 'Scope')
        self.top_grid_layout.addWidget(self.display, 0, 0, 1, 4)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._usrp_device_info_tool_bar = Qt.QToolBar(self)

        if None:
          self._usrp_device_info_formatter = None
        else:
          self._usrp_device_info_formatter = lambda x: repr(x)

        self._usrp_device_info_tool_bar.addWidget(Qt.QLabel('Device Information'+": "))
        self._usrp_device_info_label = Qt.QLabel(str(self._usrp_device_info_formatter(self.usrp_device_info)))
        self._usrp_device_info_tool_bar.addWidget(self._usrp_device_info_label)
        self.top_grid_layout.addWidget(self._usrp_device_info_tool_bar, 1, 2, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._uhd_version_info_tool_bar = Qt.QToolBar(self)

        if None:
          self._uhd_version_info_formatter = None
        else:
          self._uhd_version_info_formatter = lambda x: str(x)

        self._uhd_version_info_tool_bar.addWidget(Qt.QLabel('UHD Version'+": "))
        self._uhd_version_info_label = Qt.QLabel(str(self._uhd_version_info_formatter(self.uhd_version_info)))
        self._uhd_version_info_tool_bar.addWidget(self._uhd_version_info_label)
        self.top_grid_layout.addWidget(self._uhd_version_info_tool_bar, 1, 0, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	samp_rate_, #bw
        	'', #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(update_rate)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.display_grid_layout_1.addWidget(self._qtgui_waterfall_sink_x_0_win, 0, 0, 1, 4)
        for r in range(0, 1):
            self.display_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.display_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate_, #samp_rate
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(update_rate)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.display_grid_layout_2.addWidget(self._qtgui_time_sink_x_0_win, 0, 0, 1, 4)
        for r in range(0, 1):
            self.display_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.display_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	fft_size, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	samp_rate_, #bw
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(update_rate)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.1)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)

        if not False:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.display_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 1, 4)
        for r in range(0, 1):
            self.display_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 4):
            self.display_grid_layout_0.setColumnStretch(c, 1)
        self.low_pass_filter_0 = filter.fir_filter_ccf(25, firdes.low_pass(
        	1, samp_rate, 7500, 5000, firdes.WIN_HAMMING, 6.76))
        self._lo_locked_probe_tool_bar = Qt.QToolBar(self)

        if None:
          self._lo_locked_probe_formatter = None
        else:
          self._lo_locked_probe_formatter = lambda x: str(x)

        self._lo_locked_probe_tool_bar.addWidget(Qt.QLabel('LO locked'+": "))
        self._lo_locked_probe_label = Qt.QLabel(str(self._lo_locked_probe_formatter(self.lo_locked_probe)))
        self._lo_locked_probe_tool_bar.addWidget(self._lo_locked_probe_label)
        self.top_grid_layout.addWidget(self._lo_locked_probe_tool_bar, 4, 0, 1, 2)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)

        def _current_freq_c_probe():
            while True:
                val = self.uhd_usrp_source_0.get_sensor('lo_locked')
                try:
                    self.set_current_freq_c(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _current_freq_c_thread = threading.Thread(target=_current_freq_c_probe)
        _current_freq_c_thread.daemon = True
        _current_freq_c_thread.start()


        def _chan0_lo_locked_probe():
            while True:
                val = self.uhd_usrp_source_0.get_sensor('lo_locked')
                try:
                    self.set_chan0_lo_locked(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _chan0_lo_locked_thread = threading.Thread(target=_chan0_lo_locked_probe)
        _chan0_lo_locked_thread.daemon = True
        _chan0_lo_locked_thread.start()

        self.audio_sink_0 = audio.sink(48000, '', True)
        self._ant_options = ('RX2', 'TX/RX', 'J1', 'J2', )
        self._ant_labels = ('RX2', 'TX/RX', 'J1', 'J2', )
        self._ant_tool_bar = Qt.QToolBar(self)
        self._ant_tool_bar.addWidget(Qt.QLabel('Antenna'+": "))
        self._ant_combo_box = Qt.QComboBox()
        self._ant_tool_bar.addWidget(self._ant_combo_box)
        for label in self._ant_labels: self._ant_combo_box.addItem(label)
        self._ant_callback = lambda i: Qt.QMetaObject.invokeMethod(self._ant_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._ant_options.index(i)))
        self._ant_callback(self.ant)
        self._ant_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_ant(self._ant_options[i]))
        self.top_grid_layout.addWidget(self._ant_tool_bar, 4, 2, 1, 2)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=32000,
        	quad_rate=32000,
        	tau=75e-6,
        	max_dev=5e3,
          )



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.qtgui_freq_sink_x_0, 'freq'), (self.qtgui_freq_sink_x_0, 'freq'))
        self.msg_connect((self.qtgui_freq_sink_x_0, 'freq'), (self.uhd_usrp_source_0, 'command'))
        self.connect((self.analog_nbfm_rx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "uhd_fft")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_antenna(self):
        return self.antenna

    def set_antenna(self, antenna):
        self.antenna = antenna
        self.set_ant(self.antenna)

    def get_args(self):
        return self.args

    def set_args(self, args):
        self.args = args

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_freq_c(self.freq)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq, self.samp_rate_)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq, self.samp_rate_)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.set_gain_(self.gain)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_rate_(self.samp_rate)
        self.uhd_usrp_source_0.set_bandwidth(self.samp_rate, 0)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 7500, 5000, firdes.WIN_HAMMING, 6.76))

    def get_spec(self):
        return self.spec

    def set_spec(self, spec):
        self.spec = spec

    def get_stream_args(self):
        return self.stream_args

    def set_stream_args(self, stream_args):
        self.stream_args = stream_args

    def get_update_rate(self):
        return self.update_rate

    def set_update_rate(self, update_rate):
        self.update_rate = update_rate
        self.qtgui_waterfall_sink_x_0.set_update_time(self.update_rate)
        self.qtgui_time_sink_x_0.set_update_time(self.update_rate)
        self.qtgui_freq_sink_x_0.set_update_time(self.update_rate)

    def get_wire_format(self):
        return self.wire_format

    def set_wire_format(self, wire_format):
        self.wire_format = wire_format

    def get_freq_c(self):
        return self.freq_c

    def set_freq_c(self, freq_c):
        self.freq_c = freq_c
        Qt.QMetaObject.invokeMethod(self._freq_c_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.freq_c)))
        self.uhd_usrp_source_0.set_center_freq(float(self.freq_c), 0)
        self.set_current_freq_c(self.freq_c)

    def get_chan0_lo_locked(self):
        return self.chan0_lo_locked

    def set_chan0_lo_locked(self, chan0_lo_locked):
        self.chan0_lo_locked = chan0_lo_locked

    def get_usrp_device_info(self):
        return self.usrp_device_info

    def set_usrp_device_info(self, usrp_device_info):
        self.usrp_device_info = usrp_device_info
        Qt.QMetaObject.invokeMethod(self._usrp_device_info_label, "setText", Qt.Q_ARG("QString", self.usrp_device_info))

    def get_uhd_version_info(self):
        return self.uhd_version_info

    def set_uhd_version_info(self, uhd_version_info):
        self.uhd_version_info = uhd_version_info
        Qt.QMetaObject.invokeMethod(self._uhd_version_info_label, "setText", Qt.Q_ARG("QString", self.uhd_version_info))

    def get_samp_rate_(self):
        return self.samp_rate_

    def set_samp_rate_(self, samp_rate_):
        self.samp_rate_ = samp_rate_
        Qt.QMetaObject.invokeMethod(self._samp_rate__line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate_)))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate_)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq, self.samp_rate_)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate_)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq, self.samp_rate_)

    def get_lo_locked_probe(self):
        return self.lo_locked_probe

    def set_lo_locked_probe(self, lo_locked_probe):
        self.lo_locked_probe = lo_locked_probe
        Qt.QMetaObject.invokeMethod(self._lo_locked_probe_label, "setText", Qt.Q_ARG("QString", self.lo_locked_probe))

    def get_gain_(self):
        return self.gain_

    def set_gain_(self, gain_):
        self.gain_ = gain_
        self.uhd_usrp_source_0.set_gain(self.gain_, 0)


    def get_current_freq_c(self):
        return self.current_freq_c

    def set_current_freq_c(self, current_freq_c):
        self.current_freq_c = current_freq_c

    def get_ant(self):
        return self.ant

    def set_ant(self, ant):
        self.ant = ant
        self._ant_callback(self.ant)


def argument_parser():
    description = 'UHD FFT Waveform Plotter'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "-A", "--antenna", dest="antenna", type="string", default='RX2',
        help="Set Antenna [default=%default]")
    parser.add_option(
        "-a", "--args", dest="args", type="string", default='',
        help="Set UHD device address args [default=%default]")
    parser.add_option(
        "", "--fft-size", dest="fft_size", type="intx", default=1024,
        help="Set Set number of FFT bins [default=%default]")
    parser.add_option(
        "-f", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(466.05e6),
        help="Set Default Frequency [default=%default]")
    parser.add_option(
        "-g", "--gain", dest="gain", type="eng_float", default=eng_notation.num_to_str(20),
        help="Set Set gain in dB (default is midpoint) [default=%default]")
    parser.add_option(
        "-s", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(1e6),
        help="Set Sample Rate [default=%default]")
    parser.add_option(
        "", "--spec", dest="spec", type="string", default='',
        help="Set Subdev [default=%default]")
    parser.add_option(
        "", "--stream-args", dest="stream_args", type="string", default='',
        help="Set Set additional stream args [default=%default]")
    parser.add_option(
        "", "--update-rate", dest="update_rate", type="eng_float", default=eng_notation.num_to_str(.1),
        help="Set Set GUI widget update rate [default=%default]")
    parser.add_option(
        "", "--wire-format", dest="wire_format", type="string", default='',
        help="Set Wire format [default=%default]")
    return parser


def main(top_block_cls=uhd_fft, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(antenna=options.antenna, args=options.args, fft_size=options.fft_size, freq=options.freq, gain=options.gain, samp_rate=options.samp_rate, spec=options.spec, stream_args=options.stream_args, update_rate=options.update_rate, wire_format=options.wire_format)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
