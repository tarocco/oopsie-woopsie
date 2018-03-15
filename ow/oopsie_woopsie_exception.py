class OopsieWoopsieException(Exception):
    def __init__(self, fucky_wucky):
        fw_size = fucky_wucky.Size
        fw_type = type(fucky_wucky)
        fw_type_name = fw_type.__name__
        fw_super_type = fw_type.__bases__[0]
        fw_super_type_name = fw_super_type.__name__
        message_template = "OOPSIE WOOPSIE!! Uwu We made a {}!! A {} {}!\n"
        formatted_message = message_template.format(fw_super_type_name, fw_size, fw_type_name)
        details = "The code monkeys at our headquarters are working VEWY HAWD to fix this!"
        #error_code = None 
        super(OopsieWoopsieException, self).__init__(formatted_message + details)