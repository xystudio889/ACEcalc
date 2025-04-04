'''
ACECalculator
====
Fast calculate the cyclone ACE.
'''
__all__ = []

TROPICAL = 0
SUBTROPICAL = 1
ETROTRO = 2

__version__ = "0.0.1.dev0"

ACE_list = []
now_mode = None

def add_knot(knots:int, mode=None,index:int = None):
    '''
    Add the knots.

    :example:  
    >>> import ACE_calc
    >>> ACE_calc.set_mode(ACE_calc.TROPICAL)
    >>> ACE_calc.add_knot(50)
    >>> ACE_calc.add_knot(45, 2)
    >>> ACE_calc.add_knot(35, 2, 1)
    >>> ACE_calc.output_knot()
    >>> """index = 1, knots = 50, mode = tropical
    index = 2, knots = 35, mode = subtropical
    index = 3, knots = 45, mode = subtropical
    """
    
    :param int knots: The knots you want to add.
    :param mode=now_mode: The mode you want to add.
    :param index=len(ACE_list): The index you want to insert in the after.

    :raises ValueError: Your input or mode is invalid.

    '''
    mode = now_mode if mode is None else mode
    index = len(ACE_list) if index is None else index

    if mode is None:
        raise ValueError('Variable now_mode is not defined.')
    elif mode not in [i for i in range(3)]:
        raise ValueError('This mode is not defined.')
    elif knots < 0:
        raise ValueError('Variable knots connot < 0.')
    elif index < 0:
        raise ValueError('Variable index connot < 0.')
    else:
        ACE_list.insert(index,[knots,mode])

def add_knots(knots:int, length:int, start:int=None, mode=None):
    '''
    Add the some knots.

    :example:  
    >>> import ACE_calc
    >>> ACE_calc.set_mode(ACE_calc.TROPICAL)
    >>> ACE_calc.add_knots(50, 3)
    >>> ACE_calc.output_knot()
    >>> """index = 1, knots = 50, mode = tropical
    index = 2, knots = 50, mode = tropical
    index = 3, knots = 50, mode = tropical
    """
    
    :param int knots: The knots you want to add.
    :param mode=now_mode: The mode you want to add.
    :param index=len(ACE_list): The index you want to insert in the after.

    :raises ValueError: Your input or mode is invalid.
    '''
    mode = now_mode if mode is None else mode
    start = len(ACE_list) if start is None else start
    for i in range(length):
        add_knot(knots, mode, start + i)

def del_knot():
    raise NotImplementedError

def del_knots():
    raise NotImplementedError

def calc_ACE():
    raise NotImplementedError

def upload():
    raise NotImplementedError

def download():
    raise NotImplementedError

def output_knots():
    '''
    Format print your knot list.

    :exmanple: 
    >>> import ACE_calc
    >>> ACE_calc.set_mode(ACE_calc.TROPICAL)
    >>> ACE_calc.add_knot(50)
    >>> ACE_calc.output_knot()
    "index = 1, knots = 50, mode = tropical"
    '''
    out_texts = []
    index = 1
    for i in ACE_list:
        if i[1] == TROPICAL:
            mode_text = 'tropical'
        elif i[1] == SUBTROPICAL:
            mode_text = 'subtropical'
        elif i[1] == ETROTRO:
            mode_text = 'etrotro'
        else:
            mode_text = None

        out_texts.append(f'index = {index}, knots = {i[0]}, mode = {mode_text}')
        index += 1
    print('\n'.join(out_texts))

def get_knots_indexes(knots) -> list[int]:
    '''
    Get all the ACE indexes (index starts from 1).

    :exmanple: 
    >>> ACE_calc.add_knot(50)
    >>> ACE_calc.add_knot(45, 2)
    >>> ACE_calc.add_knot(50, 2, 1)
    >>> get_ACE_indexes(50)
    "[1, 2]"

    :param int knots: The knots you want to search.

    :return list[int]: All the knots list.
    '''
    indexes = []
    for index in range(len(ACE_list)):
        if ACE_list[index][0] == knots:
            indexes.append(index + 1)
    return indexes

def set_mode(mode):
    '''
    Set the cyclone mode.

    *If you not setting,you cannot add the knots.*
    
    :param mode: The cyclone mode.
    :raises ValueError: Your input is invalid.
    '''
    global now_mode

    if mode in [i for i in range(3)]:
        now_mode = mode
    else:
        raise ValueError('This mode is not defined.')

def clear():
    global ACE_list

    ACE_list = []

class ACEList:
    pass