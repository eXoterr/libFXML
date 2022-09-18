import re
from uuid import getnode


# Remove html tags from given text 
def clear_styles(text="") -> str:
    text = re.sub(r'(<style .?\>|.+<\/style>)|(<.*?>)', ' ', text, flags=re.S) 
    text = re.sub(r' +', ' ', text)
    return text

def get_mac() -> str:
    return ''.join(re.findall('..', '%012x' % getnode()))