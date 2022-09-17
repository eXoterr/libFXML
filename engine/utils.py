import re
from uuid import getnode

def clear_styles(text):
    text = re.sub(r'(<style .?\>|.+<\/style>)|(<.*?>)', ' ', text, flags=re.S) 
    text = re.sub(r' +', ' ', text)
    return text

def get_mac():
    return ''.join(re.findall('..', '%012x' % getnode()))