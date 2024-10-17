from flask_limiter import limiter 
from flask_limiter.util import get_remote_address


limiter = Limiter(
    key_func=get_remote_address,  
    default_limits=["100 per hour"]  
)