"""
This is the Model class the super class of all Models 
"""
from tkinter.constants import S
from model.data.data_scan import DataManager


class Model():
    def __init__(self, data_source = None) -> None:
        self.record_set = None
        self.values = None
        self.field_names = None
        self.data_manager = DataManager()

        if data_source != None:
            csv_file_obj = self.data_manager.get_file(data_source)
            self.record_set, self.values = self.data_manager.scan(csv_file=csv_file_obj, has_header=True)
            self.data_manager.close_file(csv_file_obj)
            self.field_names = [ key for key in self.record_set[0]]
        
    def merge(self, source, target):
        self.data_manager.append(target, source)
        
    def get_column(self,column_name):
        if self.record_set and column_name in self.field_names:
            return [record[column_name] for record in self.record_set]

    