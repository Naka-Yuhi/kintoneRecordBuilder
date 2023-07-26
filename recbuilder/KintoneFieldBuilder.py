from ..type.type import FieldType

class KintoneFieldBase:
    def __init__(self,name, field_type: FieldType , value):
        if not ( field_type.__class__.__name__ == 'FieldType' ):
            raise TypeError("Estimated type is FieldType")

        if ( type(name).__name__ != 'str' ):
            error_message = f"name must be str. not {type(name).__name__}"
            raise TypeError(error_message)

        self.__type = field_type
        self.__value = value
        self.__name = name
    
    def set_value(self,value):
        self.__value = value

    def set_type(self, field_type):
        self.__type = field_type

    def get_name(self):
        return self.__name
    
    def build_dict(self):
        record_dict = {
                "type":self.__type.value,
                "value":self.__value
        }
        return record_dict

    def __str__(self):
        info = f"[FieldName={self.__name}, FieldType={self.__type}, Value={self.__value}]"
        return info

class KintoneNormalField( KintoneFieldBase ):
    def __init__(self,name: str, field_type: FieldType, value):

        if ( type(value).__name__ == 'int' ):
            value = str(value)
        elif( type(value).__name__ != 'str' ):
            error_message = f"Argument of value must be str. not {type(value).__name__}"
            raise TypeError()
        

        super().__init__(name, field_type, value)

class KintoneTableField( KintoneFieldBase ):
    def __init__( self, table_name: str, table_index: int):
        self.__table_index = table_index
        self.__table_fields = []
        super().__init__( table_name, FieldType.SUBTABLE , [] )

    def appendTable(self, fields ):
        if( type(fields).__name__ != 'list' ):
            raise TypeError('This Argument must be list')
        
        if( len(fields) > self.__table_index ):
            raise IndexError("Length of the argument is out of table size.")
        
        self.__table_fields.append( fields )

    def __convert_table_fields2value(self):
        #print("start to convert")
        values = []
        for fields in self.__table_fields:
            value = {}
            for field in fields:
                value[field.get_name()] = field.build_dict()
                #print(value)
            
            values.append(value)
        #print(values)
        return values
    
    def build_dict(self):
        super().set_value( self.__convert_table_fields2value() )
        return super().build_dict()
        
class KintoneMultiSelectionField( KintoneFieldBase ):
    def __init__( self, selection_name ):
        self.__selected_value = []
        super().__init__(name=selection_name, field_type=FieldType.MULTI_SELECT, value= [] )
    
    def append(self,value):
        
        value = str(value) if type(value).__name__ == 'int' else value

        if( type(value).__name__ != 'str' ):
            raise TypeError("This argument must be 'str' or 'int'.")

        self.__selected_value.append(value)
    
    def appendAll(self,values):
        if( type(values).__name__ != 'list' ):
            raise TypeError("This argument must be 'list'.")

        for value in values:
            self.append( value )

    def build_dict(self):
        super().set_value(self.__selected_value)
        return super().build_dict()