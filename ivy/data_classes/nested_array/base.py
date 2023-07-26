# global
import abc
from typing import List

# local
import ivy


class NestedArrayBase(abc.ABC):
    """Base class for nested array objects."""

    def __init__(self, data, dtype, device, internal=False):
        if not internal:
            raise RuntimeError(
                "NestedArray is an abstract class "
                "and should not be instantiated directly."
                "Please use one of the factory methods instead"
            )
        self._data = data
        self._shape = self._generate_shape()
        self._dtype = dtype
        self._device = device
        self._pre_repr = "ivy."

    @classmethod
    def nested_array(cls, data, dtype=None, device=None):
        dtype = ivy.default_dtype(dtype=dtype, item=data)
        device = ivy.default_device(device, item=data)
        if ivy.is_ivy_array(data):
            data = [data]
        elif isinstance(data, (list, tuple)):
            data = ivy.to_ivy(data)
        elif ivy.is_native_array(data):
            data = [ivy.to_ivy(data)]
        elif isinstance(data, cls):
            data = data._data
        else:
            raise TypeError(
                "Input data must be ivy.Array, ivy.NativeArray"
                " or a list of either, got: {}".format(type(data))
            )
        for i in range(len(data)):
            data[i] = ivy.astype(data[i], dtype)
            data[i] = ivy.to_device(data[i], device)
        return cls(data, dtype, device, internal=True)

    def _generate_shape(
        self,
    ):
        final_shape = [len(self._data)]
        shapes = list()
        ndims = list()
        for arr in self._data:
            shapes.append(arr.shape)
            ndims.append(arr.ndim)
        if ndims.count(ndims[0]) != len(ndims):
            raise RuntimeError(
                "All arrays in a nested array must have the same number of dimensions."
            )
        for i in range(ndims[0]):
            same_shape = True
            current_shape = shapes[0][i]
            for j in range(final_shape[0]):
                if shapes[j][i] != current_shape:
                    same_shape = False
                    break
            if same_shape:
                final_shape.append(current_shape)
            else:
                final_shape.append(None)
        return final_shape

    @staticmethod
    def nested_multi_map_in_static_method(fn_name, *args, **kwargs):
        arg_nest_idxs = ivy.nested_argwhere(
            args, ivy.is_ivy_nested_array, to_ignore=ivy.Container
        )
        kwarg_nest_idxs = ivy.nested_argwhere(
            kwargs, ivy.is_ivy_nested_array, to_ignore=ivy.Container
        )
        # retrieve all the nested_array in args and kwargs
        arg_nest = ivy.multi_index_nest(args, arg_nest_idxs)
        kwarg_nest = ivy.multi_index_nest(kwargs, kwarg_nest_idxs)
        num_nest = len(arg_nest) + len(kwarg_nest)
        fn = ivy.__dict__[fn_name]

        if num_nest == 1:
            return ivy.nested_map(
                fn,
            )

    def unbind(self):
        return tuple(ivy.copy_nest(self._data))

    def reshape(self, shape):
        assert shape[0] == self._shape[0], "batch dimension is not changeable"
        for i in range(0, shape[0]):
            new_shape = list()
            for j in range(1, len(shape)):
                if shape[j] == -1:
                    new_shape.append(self._data[i].shape[j - 1])
                else:
                    new_shape.append(shape[j])
            self._data[i] = self._data[i].reshape(new_shape)
            print(self._data[i].shape)
        self._shape = self._generate_shape()
        return self

    # Properties #
    # ---------- #

    @property
    def data(self) -> ivy.NativeArray:
        """The native array being wrapped in self."""
        return self._data

    @property
    def dtype(self) -> ivy.Dtype:
        """Data type of the array elements."""
        return self._dtype

    @property
    def device(self) -> ivy.Device:
        """Hardware device the array data resides on."""
        return self._device

    @property
    def shape(self) -> List:
        """Array dimensions."""
        return self._shape

    @property
    def ndim(self) -> int:
        """Number of array dimensions (axes)."""
        return len(tuple(self._shape))

    # Built-ins #
    # ----------#

    def __repr__(self):
        arrays_repr = "\t"
        for i in range(self._shape[0] - 1):
            arrays_repr += repr(self._data[i]) + "\n\t"
        arrays_repr += repr(self._data[-1])
        return self._pre_repr + self.__class__.__name__ + "([\n" + arrays_repr + "\n])"

    def __getitem__(self, query):
        return self._data[query]
