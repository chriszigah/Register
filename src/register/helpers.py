import string
from random import choice
import uuid



def unique_id_generator(fixwd, digits):
    chars = string.digits
    random = "".join(choice(chars) for _ in range(digits))
    new_id = fixwd + random
    return new_id