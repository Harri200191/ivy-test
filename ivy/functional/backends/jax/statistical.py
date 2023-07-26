# global
import jax.numpy as jnp
import jax.lax as jlax
from typing import Union, Optional, Sequence, Tuple


# local
import ivy
from ivy.func_wrapper import with_unsupported_dtypes
from ivy.functional.backends.jax import JaxArray
from jaxlib.xla_extension import ArrayImpl
from . import backend_version

# Array API Standard #
# -------------------#


def min(
    x: JaxArray,
    /,
    *,
    axis: Optional[Union[int, Sequence[int]]] = None,
    keepdims: bool = False,
    out: Optional[JaxArray] = None,
) -> JaxArray:
    axis = tuple(axis) if isinstance(axis, list) else axis
    return jnp.min(a=jnp.asarray(x), axis=axis, keepdims=keepdims)


def max(
    x: JaxArray,
    /,
    *,
    axis: Optional[Union[int, Sequence[int]]] = None,
    keepdims: bool = False,
    out: Optional[JaxArray] = None,
) -> JaxArray:
    axis = tuple(axis) if isinstance(axis, list) else axis
    return jnp.max(a=jnp.asarray(x), axis=axis, keepdims=keepdims)


def mean(
    x: JaxArray,
    /,
    *,
    axis: Optional[Union[int, Sequence[int]]] = None,
    keepdims: bool = False,
    out: Optional[JaxArray] = None,
) -> JaxArray:
    axis = tuple(axis) if isinstance(axis, list) else axis
    return jnp.mean(x, axis=axis, keepdims=keepdims)


def _infer_dtype(dtype: jnp.dtype):
    default_dtype = ivy.infer_default_dtype(dtype)
    if ivy.dtype_bits(dtype) < ivy.dtype_bits(default_dtype):
        return default_dtype
    return dtype


def prod(
    x: JaxArray,
    /,
    *,
    axis: Optional[Union[int, Sequence[int]]] = None,
    dtype: Optional[jnp.dtype] = None,
    keepdims: bool = False,
    out: Optional[JaxArray] = None,
) -> JaxArray:
    dtype = ivy.as_native_dtype(dtype)
    if dtype is None:
        dtype = _infer_dtype(x.dtype)
    axis = tuple(axis) if isinstance(axis, list) else axis
    return jnp.prod(a=x, axis=axis, dtype=dtype, keepdims=keepdims)


def std(
    x: JaxArray,
    /,
    *,
    axis: Optional[Union[int, Sequence[int]]] = None,
    correction: Union[int, float] = 0.0,
    keepdims: bool = False,
    out: Optional[JaxArray] = None,
) -> JaxArray:
    axis = tuple(axis) if isinstance(axis, list) else axis
    return jnp.std(x, axis=axis, ddof=correction, keepdims=keepdims)


def sum(
    x: JaxArray,
    /,
    *,
    axis: Optional[Union[int, Sequence[int]]] = None,
    dtype: Optional[jnp.dtype] = None,
    keepdims: Optional[bool] = False,
    out: Optional[JaxArray] = None,
) -> JaxArray:
    dtype = ivy.as_native_dtype(dtype)
    if dtype is None:
        dtype = x.dtype
    if dtype != x.dtype and not ivy.is_bool_dtype(x):
        x = x.astype(dtype)
    axis = tuple(axis) if isinstance(axis, list) else axis
    return jnp.sum(a=x, axis=axis, dtype=dtype, keepdims=keepdims)


def var(
    x: JaxArray,
    /,
    *,
    axis: Optional[Union[int, Sequence[int]]] = None,
    correction: Union[int, float] = 0.0,
    keepdims: bool = False,
    out: Optional[JaxArray] = None,
) -> JaxArray:
    if axis is None:
        axis = tuple(range(len(x.shape)))
    axis = (axis,) if isinstance(axis, int) else tuple(axis)
    if isinstance(correction, int):
        ret = jnp.var(x, axis=axis, ddof=correction, keepdims=keepdims, out=out)
        return ivy.astype(ret, x.dtype, copy=False)
    if x.size == 0:
        return jnp.asarray(float("nan"))
    size = 1
    for a in axis:
        size *= x.shape[a]
    if size == correction:
        size += 0.0001  # to avoid division by zero in return
    return ivy.astype(
        jnp.multiply(
            jnp.var(x, axis=axis, keepdims=keepdims, out=out),
            size / jnp.abs(size - correction),
        ),
        x.dtype,
        copy=False,
    )


# Extra #
# ------#


@with_unsupported_dtypes({"0.4.12 and below": "bfloat16"}, backend_version)
def cumprod(
    x: JaxArray,
    /,
    *,
    axis: int = 0,
    exclusive: bool = False,
    reverse: bool = False,
    dtype: Optional[jnp.dtype] = None,
    out: Optional[JaxArray] = None,
) -> JaxArray:
    dtype = ivy.as_native_dtype(dtype)
    if dtype is None:
        if dtype is jnp.bool_:
            dtype = ivy.default_int_dtype(as_native=True)
        else:
            dtype = _infer_dtype(x.dtype)
    if not (exclusive or reverse):
        return jnp.cumprod(x, axis, dtype=dtype)
    elif exclusive and reverse:
        x = jnp.cumprod(jnp.flip(x, axis=(axis,)), axis=axis, dtype=dtype)
        x = jnp.swapaxes(x, axis, -1)
        x = jnp.concatenate((jnp.ones_like(x[..., -1:]), x[..., :-1]), -1)
        x = jnp.swapaxes(x, axis, -1)
        return jnp.flip(x, axis=(axis,))

    elif exclusive:
        x = jnp.swapaxes(x, axis, -1)
        x = jnp.concatenate((jnp.ones_like(x[..., -1:]), x[..., :-1]), -1)
        x = jnp.cumprod(x, -1, dtype=dtype)
        return jnp.swapaxes(x, axis, -1)
    else:
        x = jnp.cumprod(jnp.flip(x, axis=(axis,)), axis=axis, dtype=dtype)
        return jnp.flip(x, axis=axis)


@with_unsupported_dtypes({"0.4.12 and below": "bfloat16"}, backend_version)
def cummin(
    x: JaxArray,
    /,
    *,
    axis: int = 0,
    reverse: bool = False,
    dtype: Optional[jnp.dtype] = None,
    out: Optional[JaxArray] = None,
) -> JaxArray:
    if axis < 0:
        axis = axis + len(x.shape)
    dtype = ivy.as_native_dtype(dtype)
    if dtype is None:
        if dtype is jnp.bool_:
            dtype = ivy.default_int_dtype(as_native=True)
        else:
            dtype = _infer_dtype(x.dtype)
    return jlax.cummin(x, axis, reverse=reverse).astype(dtype)


def cumsum(
    x: JaxArray,
    axis: int = 0,
    exclusive: bool = False,
    reverse: bool = False,
    *,
    dtype: Optional[jnp.dtype] = None,
    out: Optional[JaxArray] = None,
) -> JaxArray:
    dtype = ivy.as_native_dtype(dtype)
    if dtype is None:
        if dtype is jnp.bool_:
            dtype = ivy.default_int_dtype(as_native=True)
        elif ivy.is_int_dtype(x.dtype):
            dtype = ivy.promote_types(x.dtype, ivy.default_int_dtype(as_native=True))
        else:
            dtype = _infer_dtype(x.dtype)
    if exclusive or reverse:
        if exclusive and reverse:
            x = jnp.cumsum(jnp.flip(x, axis=axis), axis=axis, dtype=dtype)
            x = jnp.swapaxes(x, axis, -1)
            x = jnp.concatenate((jnp.zeros_like(x[..., -1:]), x[..., :-1]), -1)
            x = jnp.swapaxes(x, axis, -1)
            res = jnp.flip(x, axis=axis)
        elif exclusive:
            x = jnp.swapaxes(x, axis, -1)
            x = jnp.concatenate((jnp.zeros_like(x[..., -1:]), x[..., :-1]), -1)
            x = jnp.cumsum(x, -1, dtype=dtype)
            res = jnp.swapaxes(x, axis, -1)
        elif reverse:
            x = jnp.cumsum(jnp.flip(x, axis=axis), axis=axis, dtype=dtype)
            res = jnp.flip(x, axis=axis)
        return res
    return jnp.cumsum(x, axis, dtype=dtype)


def cummax(
    x: JaxArray,
    axis: int = 0,
    exclusive: bool = False,
    reverse: bool = False,
    *,
    out: Optional[JaxArray] = None,
) -> Tuple[JaxArray, JaxArray]:
    if x.dtype in (jnp.bool_, jnp.float16):
        x = x.astype(jnp.float64)
    elif x.dtype in (jnp.int16, jnp.int8, jnp.uint8):
        x = x.astype(jnp.int64)
    elif x.dtype in (jnp.complex128, jnp.complex64):
        x = jnp.real(x).astype(jnp.float64)

    if exclusive or (reverse and exclusive):
        if exclusive and reverse:
            indices = __find_cummax_indices(jnp.flip(x, axis=axis), axis=axis)
            x = jlax.cummax(jnp.flip(x, axis=axis), axis=axis)
            x, indices = jnp.swapaxes(x, axis, -1), jnp.swapaxes(indices, axis, -1)
            x, indices = jnp.concatenate(
                (jnp.zeros_like(x[..., -1:]), x[..., :-1]), -1
            ), jnp.concatenate(
                (jnp.zeros_like(indices[..., -1:]), indices[..., :-1]), -1
            )
            x, indices = jnp.swapaxes(x, axis, -1), jnp.swapaxes(indices, axis, -1)
            res, indices = jnp.flip(x, axis=axis), jnp.flip(indices, axis=axis)
        elif exclusive:
            x = jnp.swapaxes(x, axis, -1)
            x = jnp.concatenate((jnp.zeros_like(x[..., -1:]), x[..., :-1]), -1)
            x = jnp.swapaxes(x, axis, -1)
            indices = __find_cummax_indices(x, axis=axis)
            res = jlax.cummax(x, axis=axis)
        return res, indices

    if reverse:
        y = jnp.flip(x, axis=axis)
        indices = __find_cummax_indices(y, axis=axis)
        indices = jnp.flip(indices, axis=axis)
    else:
        indices = __find_cummax_indices(x, axis=axis)
    return jlax.cummax(x, axis, reverse=reverse), indices


def __find_cummax_indices(
    x: JaxArray,
    axis: int = 0,
) -> JaxArray:
    n, indice, indices = 0, [], []

    if type(x[0]) == ArrayImpl and len(x[0].shape) >= 1:
        if axis >= 1:
            for ret1 in x:
                indice = __find_cummax_indices(ret1, axis=axis - 1)
                indices.append(indice)
        else:
            z_list = __get_index(x.tolist())
            indices, n1 = x.copy(), {}
            indices = jnp.zeros(jnp.asarray(indices.shape), dtype=x.dtype)
            z_list = sorted(z_list, key=lambda i: i[1])
            for y, y_index in z_list:
                multi_index = y_index
                if tuple(multi_index[1:]) not in n1:
                    n1[tuple(multi_index[1:])] = multi_index[0]
                    indices = indices.at[y_index].set(multi_index[0])
                elif (
                    y >= x[tuple([n1[tuple(multi_index[1:])]] + list(multi_index[1:]))]
                ):
                    n1[tuple(multi_index[1:])] = multi_index[0]
                    indices = indices.at[y_index].set(multi_index[0])
                else:
                    indices = indices.at[y_index].set(n1[tuple(multi_index[1:])])
    else:
        n, indices = 0, []
        for idx, y in enumerate(x):
            if idx == 0 or x[n] <= y:
                n = idx
            indices.append(n)

    return jnp.asarray(indices, dtype="int64")


def __get_index(lst, indices=None, prefix=None):
    if indices is None:
        indices = []
    if prefix is None:
        prefix = []

    if isinstance(lst, list):
        for i, sub_lst in enumerate(lst):
            sub_indices = prefix + [i]
            __get_index(sub_lst, indices, sub_indices)
    else:
        indices.append((lst, tuple(prefix)))
    return indices


def einsum(
    equation: str, *operands: JaxArray, out: Optional[JaxArray] = None
) -> JaxArray:
    return jnp.einsum(equation, *operands)


def igamma(
    a: JaxArray,
    /,
    *,
    x: JaxArray,
    out: Optional[JaxArray] = None,
) -> JaxArray:
    return jlax.igamma(a=a, x=x)
