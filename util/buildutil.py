from ..type.type import FieldType as Type
from ..error.buildError import WrongArgumentError, create_error_message

VALUE_RELATIONSHIP = {
    Type.SINGLE_LINE_TEXT.value: "str",
    Type.MULTI_LINE_TEXT.value: "str",
    Type.CHECK_BOX.value: "str",
    Type.DROP_DOWN.value: "str",
    Type.LINK.value: "str",
    Type.NUMBER.value: "int",
    Type.SUBTABLE.value: "list",
    Type.RECORD_NUMBER.value: "int"
}

def verification_with_type(field_type:Type, value ):
    
    if( not ( type(value).__name__ == VALUE_RELATIONSHIP[field_type.value]) ):
        error_message = create_error_message(f"Argument of value appear to be wrong. [{field_type.value} : {VALUE_RELATIONSHIP[field_type.value]}] not {type(value).__name__}")
        raise WrongArgumentError(error_message)
    

    if( field_type == Type.SUBTABLE ):
        for record in value:

            if not (type(record).__name__ == 'dict' ):
                error_message = create_error_message("A element of SUBTABLE must be 'dict'.")
                raise WrongArgumentError(error_message)


            try:
                sub_field_type = record['type']
                sub_value = record['value']
                
            except KeyError as e:
                error_message = create_error_message("Argument of value appear to be wrong.\ntype or value field could not be found.")
                raise WrongArgumentError(error_message)