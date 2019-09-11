#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: UHD WBFM Receive
# Author: Example
# Description: WBFM Receive
# Generated: Wed May  3 09:58:34 2017
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

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
import time
from gnuradio import qtgui


class uhd_wbfm_receive(gr.top_block, Qt.QWidget):

    def __init__(self, address='addr=192.168.10.2', audio_output='', freq=104.2e6, gain=0, samp_rate=400e3):
        gr.top_block.__init__(self, "UHD WBFM Receive")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("UHD WBFM Receive")
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

        self.settings = Qt.QSettings("GNU Radio", "uhd_wbfm_receive")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.address = address
        self.audio_output = audio_output
        self.freq = freq
        self.gain = gain
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 1
        self.tun_gain = tun_gain = 10
        self.tun_freq = tun_freq = freq/1e6
        self.fine = fine = 0
        self.audio_decim = audio_decim = 10

        ##################################################
        # Blocks
        ##################################################
        self._volume_range = Range(0, 10, 0.1, 1, 200)
        self._volume_win = RangeWidget(self._volume_range, self.set_volume, 'Volume', "counter_slider", float)
        self.top_grid_layout.addWidget(self._volume_win, 1, 0, 1, 4)
        self._tun_gain_range = Range(0, 20, 1, 10, 200)
        self._tun_gain_win = RangeWidget(self._tun_gain_range, self.set_tun_gain, 'UHD Gain', "counter_slider", float)
        self.top_layout.addWidget(self._tun_gain_win)
        self._tun_freq_range = Range(87.9, 108.1, 1, freq/1e6, 200)
        self._tun_freq_win = RangeWidget(self._tun_freq_range, self.set_tun_freq, 'UHD Freq (MHz)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tun_freq_win, 0,0,1,2)
        self._fine_range = Range(-.1, .1, .01, 0, 200)
        self._fine_win = RangeWidget(self._fine_range, self.set_fine, 'Fine Freq (MHz)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._fine_win, 0,2,1,2)
        self.uhd_usrp_source_1 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_1.set_center_freq((tun_freq+fine)*1e6, 0)
        self.uhd_usrp_source_1.set_gain(tun_gain, 0)
        self.uhd_usrp_source_1.set_antenna('TX/RX', 0)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	512, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	(tun_freq+fine)*1e6, #fc
        	samp_rate, #bw
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 2,0,2,4)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 115e3, 30e3, firdes.WIN_HANN, 6.76))
        self.blocks_multiply_const_vxx = blocks.multiply_const_vff((volume, ))
        self.audio_sink = audio.sink(int(samp_rate/audio_decim), audio_output, True)
        self.analog_wfm_rcv = analog.wfm_rcv(
        	quad_rate=samp_rate,
        	audio_decimation=audio_decim,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv, 0), (self.blocks_multiply_const_vxx, 0))
        self.connect((self.blocks_multiply_const_vxx, 0), (self.audio_sink, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.low_pass_filter_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "uhd_wbfm_receive")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_audio_output(self):
        return self.audio_output

    def set_audio_output(self, audio_output):
        self.audio_output = audio_output

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_tun_freq(self.freq/1e6)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range((self.tun_freq+self.fine)*1e6, self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 115e3, 30e3, firdes.WIN_HANN, 6.76))

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx.set_k((self.volume, ))

    def get_tun_gain(self):
        return self.tun_gain

    def set_tun_gain(self, tun_gain):
        self.tun_gain = tun_gain
        self.uhd_usrp_source_1.set_gain(self.tun_gain, 0)


    def get_tun_freq(self):
        return self.tun_freq

    def set_tun_freq(self, tun_freq):
        self.tun_freq = tun_freq
        self.uhd_usrp_source_1.set_center_freq((self.tun_freq+self.fine)*1e6, 0)
        self.qtgui_freq_sink_x_0.set_frequency_range((self.tun_freq+self.fine)*1e6, self.samp_rate)

    def get_fine(self):
        return self.fine

    def set_fine(self, fine):
        self.fine = fine
        self.uhd_usrp_source_1.set_center_freq((self.tun_freq+self.fine)*1e6, 0)
        self.qtgui_freq_sink_x_0.set_frequency_range((self.tun_freq+self.fine)*1e6, self.samp_rate)

    def get_audio_decim(self):
        return self.audio_decim

    def set_audio_decim(self, audio_decim):
        self.audio_decim = audio_decim


def argument_parser():
    description = 'WBFM Receive'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "-a", "--address", dest="address", type="string", default='addr=192.168.10.2',
        help="Set IP Address [default=%default]")
    parser.add_option(
        "-O", "--audio-output", dest="audio_output", type="string", default='',
        help="Set Audio Output Device [default=%default]")
    parser.add_option(
        "-f", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(104.2e6),
        help="Set Default Frequency [default=%default]")
    parser.add_option(
        "-g", "--gain", dest="gain", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set Default Gain [default=%default]")
    parser.add_option(
        "-s", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(400e3),
        help="Set Sample Rate [default=%default]")
    return parser


def main(top_block_cls=uhd_wbfm_receive, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(address=options.address, audio_output=options.audio_output, freq=options.freq, gain=options.gain, samp_rate=options.samp_rate)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
