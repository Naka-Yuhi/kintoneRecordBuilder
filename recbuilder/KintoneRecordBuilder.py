from ..type.type import FieldType
from ..error.buildError import AppIDNoneError
from ..recbuilder.KintoneFieldBuilder import KintoneFieldBase

class KintoneRecordBuilder:
    def __init__(self, app_id = None):
        self.__record = {}
        self.__fields = []
        self.__app_id = app_id
        self.__body = {}

    def clear(self):
        self.__record = {}
        self.__fields = []
        self.__body = {}

    def build_record(self):
        for field in self.__fields:
            self.__record[field.get_name()] = field.build_dict()
        return self.__record
    
    def build_body(self):
        if( self.__app_id == None ):
            raise AppIDNoneError("AppID is set to be 'None'")
        self.__body['app'] = self.__app_id
        self.__body['record'] = self.build_record()
        return self.__body
    
    def append_field(self, kintone_field ):

        if( issubclass(kintone_field.__class__, KintoneFieldBase) ):
            self.__fields.append(kintone_field)
        else:
            raise TypeError("Argument must be a class that has 'KintoneFieldBase' class as parent.")
    
    def append_allFields(self, kintone_fields):
        if( type(kintone_fields).__name__ != 'list' ):
            raise TypeError("This argument must be 'list'")
        
        for kintone_field in kintone_fields:
            self.append_field(kintone_field)

    def __str__(self):
        return self.__record.__str__()
    
