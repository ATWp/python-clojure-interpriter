

def normal_split(line, sep):
    out_split = []
    s = ''
    for symbol in line:
        if symbol in sep['all']:
            if s != '':
                out_split.append(s)
                s = ''
            if symbol in sep['not-delete']:
                out_split.append(symbol)
        else:
            s += symbol
            
    return out_split