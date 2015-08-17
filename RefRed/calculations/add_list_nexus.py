from mantid.simpleapi import *
from RefRed.calculations.load_list_nexus import LoadListNexus
from RefRed.calculations.load_nexus import LoadNexus
from RefRed.calculations.check_if_same_nxs_property import CheckIfSameNxsProperty

class AddListNexus(object):
    
    wks = None
    addition_worked = True
    
    def __init__(self, list_nexus=None, list_run=None, metadata_only=False, check_nexus_compatibility=True):
        if list_nexus is None:
            return
        
        self.wks = None
        self.addition_worked = True
        
        if len(list_nexus) == 1:
            _filename = list_nexus[0]
            _run = list_run[0]
            _ws_name = "_data_file_%s" %_run
            wks_object = LoadNexus(filename=_filename,
                                   output_wks = _ws_name,
                                   metadata_only = metadata_only)
            
            self.wks = wks_object
            
        else:
            load_list_object = LoadListNexus(list_nexus=list_nexus, 
                                             list_run=list_run,
                                             metadata_only=metadata_only)
            _list_wks = load_list_object.list_wks_loaded
            if len(_list_wks) > 1:
                if check_nexus_compatibility:
                    check_same_property = CheckIfSameNxsProperty(list_wks = _list_wks,
                                                                 property_name = 'LambdaRequest')
                else: #we force true
                    check_same_property.is_same_property = True

                if check_same_property.is_same_property:
                    lwks = _list_wks[0]
                    for i in range(1,len(_list_wks)):
                        rwks = _list_wks[1]
                        lwks = Plus(LHSWorkspace=lwks,
                                    RHSWorkspace=rwks,
                                    OutputWorkspace=lwks)
                    self.wks = lwks
                
                else:
                    self.wks = None
                    self.addition_worked = False
                
            else:
                self.wks = _list_wks
                