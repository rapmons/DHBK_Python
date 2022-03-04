#already used function with outputs


def format_name(f_name,l_name):
    """ 
    take a first and lát name and format it to retuen the title case vesion of the name.
    """
    if f_name=="" and l_name=="":
        return
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return f"{formated_f_name} {formated_l_name}"

format_name("hehe","haha")