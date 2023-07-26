# global
import ivy
from ivy.func_wrapper import with_unsupported_dtypes, with_supported_dtypes
from ivy.functional.frontends.paddle import promote_types_of_paddle_inputs
from ivy.functional.frontends.paddle.func_wrapper import (
    to_ivy_arrays_and_back,
)


@with_supported_dtypes(
    {"2.4.2 and below": ("float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def cross(x, y, /, *, axis=9, name=None):
    x, y = promote_types_of_paddle_inputs(x, y)
    return ivy.cross(x, y, axis=axis)


# matmul
@with_unsupported_dtypes({"2.4.2 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def matmul(x, y, transpose_x=False, transpose_y=False, name=None):
    x, y = promote_types_of_paddle_inputs(x, y)
    return ivy.matmul(x, y, transpose_a=transpose_x, transpose_b=transpose_y)


# norm
@with_supported_dtypes({"2.4.2 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def norm(x, p="fro", axis=None, keepdim=False, name=None):
    if axis is None and p is not None:
        if p == "fro":
            p = 2
        ret = ivy.vector_norm(x.flatten(), ord=p, axis=-1)
        if keepdim:
            ret = ret.reshape([1] * len(x.shape))
        if len(ret.shape) == 0:
            return ivy.array([ret])
        return ret

    if isinstance(axis, tuple):
        axis = list(axis)
    if isinstance(axis, list) and len(axis) == 1:
        axis = axis[0]

    if isinstance(axis, int):
        if p == "fro":
            p = 2
        if p in [0, 1, 2, ivy.inf, -ivy.inf]:
            ret = ivy.vector_norm(x, ord=p, axis=axis, keepdims=keepdim)
        elif isinstance(p, (int, float)):
            ret = ivy.pow(
                ivy.sum(ivy.pow(ivy.abs(x), p), axis=axis, keepdims=keepdim),
                float(1.0 / p),
            )

    elif isinstance(axis, list) and len(axis) == 2:
        if p == 0:
            raise ValueError
        elif p == 1:
            ret = ivy.sum(ivy.abs(x), axis=axis, keepdims=keepdim)
        elif p == 2 or p == "fro":
            ret = ivy.matrix_norm(x, ord="fro", axis=axis, keepdims=keepdim)
        elif p == ivy.inf:
            ret = ivy.max(ivy.abs(x), axis=axis, keepdims=keepdim)
        elif p == -ivy.inf:
            ret = ivy.min(ivy.abs(x), axis=axis, keepdims=keepdim)
        elif isinstance(p, (int, float)) and p > 0:
            ret = ivy.pow(
                ivy.sum(ivy.pow(ivy.abs(x), p), axis=axis, keepdims=keepdim),
                float(1.0 / p),
            )
        else:
            raise ValueError

    else:
        raise ValueError

    if len(ret.shape) == 0:
        ret = ivy.array(
            [ret]
        )  # this is done so as to match shape of output from paddle
    return ret


# eig
@to_ivy_arrays_and_back
def eig(x, name=None):
    return ivy.eig(x)


# eigvals
@to_ivy_arrays_and_back
def eigvals(x, name=None):
    return ivy.eigvals(x)


# eigvalsh
@to_ivy_arrays_and_back
def eigvalsh(x, UPLO="L", name=None):
    return ivy.eigvalsh(x, UPLO=UPLO)


# eigh
@to_ivy_arrays_and_back
def eigh(x, UPLO="L", name=None):
    return ivy.eigh(x, UPLO=UPLO)


# pinv
@with_unsupported_dtypes({"2.4.2 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def pinv(x, rcond=1e-15, hermitian=False, name=None):
    # TODO: Add hermitian functionality
    return ivy.pinv(x, rtol=rcond)


# solve
@with_unsupported_dtypes({"2.4.2 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def solve(x1, x2, name=None):
    return ivy.solve(x1, x2)


# cholesky
@with_supported_dtypes({"2.4.2 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def cholesky(x, /, *, upper=False, name=None):
    return ivy.cholesky(x, upper=upper)


# bmm
@with_unsupported_dtypes({"2.4.2 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def bmm(x, y, transpose_x=False, transpose_y=False, name=None):
    if len(ivy.shape(x)) != 3 or len(ivy.shape(y)) != 3:
        raise RuntimeError("input must be 3D matrices")
    x, y = promote_types_of_paddle_inputs(x, y)
    return ivy.matmul(x, y, transpose_a=transpose_x, transpose_b=transpose_y)


# matrix_power
@with_unsupported_dtypes({"2.4.2 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def matrix_power(x, n, name=None):
    return ivy.matrix_power(x, n)
