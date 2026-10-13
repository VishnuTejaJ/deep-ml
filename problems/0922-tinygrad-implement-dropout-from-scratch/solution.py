from tinygrad import Tensor

def dropout(x, p, training):
    if training==False:
        return x
    drop_mask = (Tensor.rand(*x.shape)>=p).cast(x.dtype) * (1/(1-p))
    return x*drop_mask