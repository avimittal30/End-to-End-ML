d={'a':'value1', 'b':'value2'}

d['a']

d.a

# helps us access value using '.' instead of d['a']
from box import ConfigBox
d=ConfigBox({'a':'value1', 'b':'value2'})
d.a

from ensure import ensure_annotations

@ensure_annotations
def get_product(x:int, y:int)->int:
    return x*y
# Without ensure_annotations, this will not through any error and will give wierd output
get_product(2,"3")


from mlProject.utils.common import read_yaml
from mlProject.constants import *
read_yaml(CONFIG_FILE_PATH)