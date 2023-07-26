from enum import Enum

class FieldType( Enum ):
    NUMBER = 'NUMBER'
    SINGLE_LINE_TEXT = 'SINGLE_LINE_TEXT'
    MULTI_LINE_TEXT = 'MULTI_LINE_TEXT'
    MULTI_SELECT = 'MULTI_SELECT'
    CHECK_BOX = 'CHECK_BOX'
    DROP_DOWN = 'DROP_DOWN'
    LINK = 'LINK'
    SUBTABLE = 'SUBTABLE'