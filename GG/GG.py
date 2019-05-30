import time
from DavesLogger import Logs, Log

Error = Logs.Error
Warning = Logs.Warning
Debug = Logs.Debug
Default = Log ()

def __SendLog (_Log, _Function):
    Name = _Function.__name__
    ArgCount = _Function.__code__.co_argcount
    File = _Function.__code__.co_filename
    Line = _Function.__code__.co_firstlineno
    StartTime = time.time ()

    Result = _Function ()

    EndTime = time.time ()
    Time = EndTime - StartTime

    Header = '----- Log Result -----'
    HeaderLength = len (Header)
    if _Log != Default:
        HeaderLength += len (_Log.IPrefix) - 7

    Message = f'''
{Header}
Executed:           {Name}
Result:             {Result}
Result Type:        {type (Result).__name__}
Execution Time:     {Time} seconds
Arg Count:          {ArgCount}
File Path:          {File}
Start Line:         {Line}
{'-' * HeaderLength}'''

    _Log (Message)

def Log (_Type = None):
    if _Type == None:
        _Type = Default

    def Wrapper (_Callback):
        __SendLog (_Type, _Callback)

        return _Callback

    return Wrapper

def Print (_Callback):
    Value = _Callback ()

    if Value:
        print (Value)

def Check (_Callback, _Type):
    Returned = _Callback ()

    if not isinstance (Returned, _Type):
        Logs.Error ('Function doesn\'t return: ' + str (_Type.__name__))
        return

    return Returned

def Int (_Callback):
    Check (_Callback, int)

def Float (_Callback):
    Check (_Callback, float)

def String (_Callback):
    Check (_Callback, str)

def List (_Callback):
    Check (_Callback, list)

def Dict (_Callback):
    Check (_Callback, dict)

def Tuple (_Callback):
    Check (_Callback, tuple)

def Combine (*_Types):
    Types = (_Types)

    def Wrapper (_Callback):
        Check (_Callback, Types)
        return _Callback

    return Wrapper
