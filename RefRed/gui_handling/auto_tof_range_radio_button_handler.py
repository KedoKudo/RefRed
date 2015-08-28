from RefRed.gui_handling.gui_utility import GuiUtility
from RefRed.plot.display_plots import DisplayPlots

class AutoTofRangeRadioButtonHandler(object):

    parent = None
    row = -1
    col = -1
    is_data = True

    def __init__(self, parent = None):
        self.parent = parent
        o_gui_utility = GuiUtility(parent = self.parent)
        self.row = o_gui_utility.get_current_table_reduction_check_box_checked()
        self.col = o_gui_utility.get_data_norm_tab_selected()
        self.is_data = True if self.col == 0 else False

    def radio_button_handler(self):
        if self.row == -1:
            return
        
        o_gui_utility = GuiUtility(parent = self.parent)
        is_auto_tof_selected = o_gui_utility.is_auto_tof_range_radio_button_selected()
        self.widgets_handler(is_auto_tof_selected)
        
        big_table_data = self.parent.big_table_data
        _data = big_table_data[self.row, self.col]
        if _data is None:
            return
        
        if is_auto_tof_selected:
            new_tof_range = _data.tof_range_auto
            self.save_manual_tof_range()            
        else:
            new_tof_range = _data.tof_range_manual
        
        self.replace_tof_range_displayed(new_tof_range)
        self.refresh_plot()
        
    def line_edit_validation(self):
        if self.row == -1:
            return
        
        self.save_manual_tof_range()
        self.refresh_plot()

    def refresh_plot(self):
        DisplayPlots(parent = self.parent,
                     row = self.row,
                     is_data = self.is_data,
                     plot_yt = True,
                     plot_yi = False,
                     plot_it = True,
                     plot_ix = False,
                     refresh_reduction_table = False)
        
    def save_manual_tof_range(self):
        big_table_data = self.parent.big_table_data
        _data = big_table_data[self.row, self.col]
        _data.tof_range_manual = self.retrieve_tof_range_defined_by_user()
        big_table_data[self.row, self.col] = _data
        self.big_table_data = big_table_data
        
    def retrieve_tof_range_defined_by_user(self):
        tof1 = float(self.parent.ui.TOFmanualFromValue.text()) * 1000.
        tof2 = float(self.parent.ui.TOFmanualToValue.text()) * 1000
        return [tof1, tof2]
    
    def replace_tof_range_displayed(self, tof_range):
        tof1 = "%.2f" %(tof_range[0] / 1000.)
        tof2 = "%.2f" %(tof_range[1] / 1000.)
        
        self.parent.ui.TOFmanualFromValue.setText(tof1)
        self.parent.ui.TOFmanualToValue.setText(tof2)

    def widgets_handler(self, is_auto_tof_selected):
        self.parent.ui.TOFmanualFromLabel.setEnabled(not is_auto_tof_selected)
        self.parent.ui.TOFmanualFromValue.setEnabled(not is_auto_tof_selected)
        self.parent.ui.TOFmanualFromUnitsValue.setEnabled(not is_auto_tof_selected)
        self.parent.ui.TOFmanualToValue.setEnabled(not is_auto_tof_selected)
        self.parent.ui.TOFmanualToLabel.setEnabled(not is_auto_tof_selected)
        self.parent.ui.TOFmanualToUnitsValue.setEnabled(not is_auto_tof_selected)
