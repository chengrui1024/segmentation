import numpy as np
from PIL import Image

ar = np.ones((32, 32), dtype=np.uint16)
im = Image.fromarray(ar)
im.save('foo.png')