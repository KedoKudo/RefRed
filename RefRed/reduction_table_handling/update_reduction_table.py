from PyQt4 import QtGui

from RefRed.calculations.run_sequence_breaker import RunSequenceBreaker
from RefRed.calculations.check_list_run_compatibility_and_display_thread import CheckListRunCompatibilityAndDisplayThread
from RefRed.plot.display_reduction_table import DisplayReductionTable
import RefRed.colors 
from RefRed.lconfigdataset import LConfigDataset
from RefRed.plot.clear_plots import ClearPlots
from RefRed.calculations.locate_list_run import LocateListRun

class UpdateReductionTable(object):
    
    raw_runs = None
    is_data_displayed = True
    
    def __init__(self, parent=None, row=0, col=1, runs=None):
        self.parent= parent
        self.row = row
        self.col = col
        
        item = self.parent.ui.reductionTable.item(row, col)
        if item.text() == '':
            self.clear_cell()
            return
        
        data_type = 'data' if col == 1 else 'norm'
        self.is_data_displayed = True if (col == 1) else False

        self.raw_runs = str(runs)
        run_breaker = RunSequenceBreaker(run_sequence=self.raw_runs)
        list_run = run_breaker.final_list
        
        # check if nexus can be found
        list_run_object = LocateListRun(list_run = list_run)
        if list_run_object.list_run_not_found != []:
            str_list_run_not_found = [str(x) for x in list_run_object.list_run_not_found]
            runs_not_located = ', '.join(str_list_run_not_found)
            mess = "Can not locate %s run(s): %s" %(data_type, runs_not_located)
            self.parent.ui.reductionTable.item(row, 8).setText(mess)
            _color = QtGui.QColor(RefRed.colors.VALUE_BAD)
            self.parent.ui.reductionTable.item(row, 8).setBackground(_color)
        else:
            mess = "%s runs have been located!" %data_type
            self.parent.ui.reductionTable.item(row, 8).setText(mess)
            _color = QtGui.QColor(RefRed.colors.VALUE_OK)
            self.parent.ui.reductionTable.item(row, 8).setBackground(_color)
            
        list_run_found = list(list_run_object.list_run_found)

        if list_run_found == []:
            self.parent.ui.reductionTable.item(row, col).setText('')
            return
        str_list_run_found = [str(x) for x in list_run_found]
        final_list_run_found = ','.join(str_list_run_found)        
        self.parent.ui.reductionTable.item(row, col).setText(final_list_run_found)

        list_nexus_found = list_run_object.list_nexus_found
        self.parent.loading_nxs_thread = CheckListRunCompatibilityAndDisplayThread()
        self.parent.loading_nxs_thread.setup(parent=self.parent,
                       list_run = list_run_found,
                       list_nexus = list_nexus_found,
                       row = row,
                       col = col, 
                       is_working_with_data_column = self.is_data_displayed,
                       is_display_requested = self.display_of_this_row_checked())
        self.parent.loading_nxs_thread.start()

    def clear_cell(self):
        print('in clear cell')
        
    def display_of_this_row_checked(self):
        _button_status = self.parent.ui.reductionTable.cellWidget(self.row, 0).checkState()
        if _button_status == 2:
            return True
        return False
    