# code that raise an error
import logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
try:
    recycle()
except (NameError,TypeError):
    logging.error('Something went wrong but we handle it')
