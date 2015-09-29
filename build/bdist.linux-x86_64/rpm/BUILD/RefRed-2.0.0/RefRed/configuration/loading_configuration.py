from PyQt4 import QtGui
from logging import info
import os
from xml.dom import minidom
from numpy import empty
from RefRed.lconfigdataset import LConfigDataset
from RefRed.configuration.populate_reduction_table_from_lconfigdataset import PopulateReductionTableFromLConfigDataSet as PopulateReductionTable
from RefRed.configuration.load_reduction_table_from_lconfigdataset import LoadReductionTableFromLConfigDataSet as LoadReductionTable
from RefRed.gui_handling.scaling_factor_widgets_handler import ScalingFactorWidgetsHandler


class LoadingConfiguration(object):
	
	parent = None
	load_config_worked = True
	filename = ''
	dom = None
	
	def __init__(self, parent = None):
		self.parent = parent
		self.filename = ''
		
	def run(self):
		_path = self.parent.path_config
		filename = QtGui.QFileDialog.getOpenFileName(self.parent, 
		                                             'Open Configuration File', 
		                                             _path)
		QtGui.QApplication.processEvents()
		if not (filename == ""):
			self.filename = str(filename)
			self.loading()
			
	def loading(self):
		self.parent.path_config = os.path.dirname(self.filename)
		self.clear_reductionTable()
		self.load_config_in_big_table_data()
		self.populate_reduction_table_from_lconfigdataset()
		self.load_reduction_table_from_lconfigdataset()
		
	def load_config_in_big_table_data(self):
		filename = self.filename
		try:
			self.dom = minidom.parse(filename)
		except:
			info('No configuration file loaded')
			self.load_config_worked = False
			return
		self.populate_big_table_data_with_lconfig()
		self.populate_main_gui_general_settings()
		
	def populate_big_table_data_with_lconfig(self):
		dom = self.dom
		RefLData = dom.getElementsByTagName('RefLData')
		nbrRowBigTable = len(RefLData)
		
		big_table_data = empty((self.parent.nbr_row_table_reduction, 3), dtype=object)
		_row = 0
		for node in RefLData:
			_metadataObject = self.getMetadataObject(node)
			big_table_data[_row, 2] = _metadataObject
			_row += 1
		
		self.parent.big_table_data = big_table_data
			
	def populate_main_gui_general_settings(self):
		dom = self.dom
		RefLData = dom.getElementsByTagName('RefLData')
		node_0 = RefLData[0]
		
		q_step = self.getNodeValue(node_0, 'q_step')
		self.parent.ui.qStep.setText(q_step)
		
		angle_offset = self.getNodeValue(node_0, 'angle_offset')
		self.parent.ui.angleOffsetValue.setText(angle_offset)
		
		angle_offset_error = self.getNodeValue(node_0, 'angle_offset_error')
		self.parent.ui.angleOffsetError.setText(angle_offset_error)
		
		scaling_factor_file = self.getNodeValue(node_0, 'scaling_factor_file')
		self.parent.full_scaling_factor_file_name = scaling_factor_file
		short_scaling_factor_file = os.path.basename(scaling_factor_file)
		self.parent.ui.scalingFactorFile.setText(short_scaling_factor_file)
		o_scaling_factor_widget = ScalingFactorWidgetsHandler(parent = self.parent)
		o_scaling_factor_widget.fill_incident_medium_list(scaling_factor_file)
		
	def getMetadataObject(parent, node):
		iMetadata = LConfigDataset()
		
		_peak_min = parent.getNodeValue(node, 'from_peak_pixels')
		_peak_max = parent.getNodeValue(node, 'to_peak_pixels')
		iMetadata.data_peak = [_peak_min, _peak_max]
		
		_back_min = parent.getNodeValue(node, 'back_roi1_from')
		_back_max = parent.getNodeValue(node, 'back_roi1_to')
		iMetadata.data_back = [_back_min, _back_max]
		
		_low_res_min = parent.getNodeValue(node, 'x_min_pixel')
		_low_res_max = parent.getNodeValue(node, 'x_max_pixel')
		iMetadata.data_low_res = [_low_res_min, _low_res_max]
		
		_back_flag = parent.getNodeValue(node, 'background_flag')
		iMetadata.data_back_flag = _back_flag
		
		_low_res_flag = parent.getNodeValue(node, 'x_range_flag')
		iMetadata.data_low_res_flag = _low_res_flag
		
		_tof_min = parent.getNodeValue(node, 'from_tof_range')
		_tof_max = parent.getNodeValue(node, 'to_tof_range')
		if float(_tof_min) < 500:  # ms
			_tof_min = str(float(_tof_min) * 1000)
			_tof_max = str(float(_tof_max) * 1000)
		iMetadata.tof_range = [_tof_min, _tof_max]
		
		_q_min = parent.getNodeValue(node, 'from_q_range')
		_q_max = parent.getNodeValue(node, 'to_q_range')
		iMetadata.q_range = [_q_min, _q_max]
		
		_lambda_min = parent.getNodeValue(node, 'from_lambda_range')
		_lambda_max = parent.getNodeValue(node, 'to_lambda_range')
		iMetadata.lambda_range = [_lambda_min, _lambda_max]
		
		iMetadata.tof_units = 'micros'
		
		_data_sets = parent.getNodeValue(node, 'data_sets')
		_data_sets = _data_sets.split(',')
		iMetadata.data_sets = [str(x) for x in _data_sets]
		
		_tof_auto = parent.getNodeValue(node, 'tof_range_flag')
		iMetadata.tof_auto_flag = _tof_auto
		
		_norm_flag = parent.getNodeValue(node, 'norm_flag')
		iMetadata.norm_flag = _norm_flag
		
		_peak_min = parent.getNodeValue(node, 'norm_from_peak_pixels')
		_peak_max = parent.getNodeValue(node, 'norm_to_peak_pixels')
		iMetadata.norm_peak = [_peak_min, _peak_max]
		
		_back_min = parent.getNodeValue(node, 'norm_from_back_pixels')
		_back_max = parent.getNodeValue(node, 'norm_to_back_pixels')
		iMetadata.norm_back = [_back_min, _back_max]
		
		_norm_sets = parent.getNodeValue(node, 'norm_dataset')
		_norm_sets = _norm_sets.split(',')
		iMetadata.norm_sets = [str(x) for x in _norm_sets]
	    
		_low_res_min = parent.getNodeValue(node, 'norm_x_min')
		_low_res_max = parent.getNodeValue(node, 'norm_x_max')
		iMetadata.norm_low_res = [_low_res_min, _low_res_max]
	    
		_back_flag = parent.getNodeValue(node, 'norm_background_flag')
		iMetadata.norm_back_flag = _back_flag
		
		_low_res_flag = parent.getNodeValue(node, 'norm_x_range_flag')
		iMetadata.norm_low_res_flag = _low_res_flag
		
		try:
			_data_full_file_name = parent.getNodeValue(node, 'data_full_file_name')
			_data_full_file_name = _data_full_file_name.split(',')
			_data_full_file_name = [str(x) for x in _data_full_file_name]
		except:
			_data_full_file_name = ['']
		iMetadata.data_full_file_name = _data_full_file_name
			
		try:
			_norm_full_file_name = parent.getNodeValue(node, 'norm_full_file_name')
			_norm_full_file_name = _norm_full_file_name.split(',')
			_norm_full_fil_name = [str(x) for x in _norm_full_file_name]
		except:
			_norm_full_file_name = ['']
		iMetadata.norm_full_file_name = _norm_full_file_name
	    
		return iMetadata
	
	def getNodeValue(parent,node,flag):
		try:
			_tmp = node.getElementsByTagName(flag)
			_value = _tmp[0].childNodes[0].nodeValue
		except:
			_value = ''
		return _value
	
	def clear_reductionTable(self):
		nbr_row = self.parent.ui.reductionTable.rowCount()
		nbr_col = self.parent.ui.reductionTable.columnCount()
		for _row in range(nbr_row):
			for _col in range(1, nbr_col):
				self.parent.ui.reductionTable.item(_row, _col).setText("")

	def populate_reduction_table_from_lconfigdataset(self):
		o_pop_reduction_table = PopulateReductionTable(parent = self.parent)
		QtGui.QApplication.processEvents()

	def load_reduction_table_from_lconfigdataset(self):
		o_load_reduction_table = LoadReductionTable(parent = self.parent)