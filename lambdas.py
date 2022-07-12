from startup import *

def admin_lambda(m):
    return m.from_user.id == admin_id