from d2l import mxnet as d2l
from mxnet import np,npx 
import random
npx.set_np()
f=[1.0/6]*6
for i in range(1,100):
    print(np.random.multinomial(1,f))
