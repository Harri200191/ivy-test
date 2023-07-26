# flake8: noqa
# global
import copy
import functools
import numpy as np
from operator import mul
from typing import Optional

# local
import ivy
from .conversions import args_to_native, to_ivy
from .activations import _ArrayWithActivations
from .creation import _ArrayWithCreation
from .data_type import _ArrayWithDataTypes
from .device import _ArrayWithDevice
from .elementwise import _ArrayWithElementwise
from .general import _ArrayWithGeneral
from .gradients import _ArrayWithGradients
from .image import _ArrayWithImage
from .layers import _ArrayWithLayers
from .linear_algebra import _ArrayWithLinearAlgebra
from .losses import _ArrayWithLosses
from .manipulation import _ArrayWithManipulation
from .norms import _ArrayWithNorms
from .random import _ArrayWithRandom
from .searching import _ArrayWithSearching
from .set import _ArrayWithSet
from .sorting import _ArrayWithSorting
from .statistical import _ArrayWithStatistical
from .utility import _ArrayWithUtility
from ivy.func_wrapper import handle_view_indexing
from .experimental import (
    _ArrayWithSearchingExperimental,
    _ArrayWithActivationsExperimental,
    _ArrayWithConversionsExperimental,
    _ArrayWithCreationExperimental,
    _ArrayWithData_typeExperimental,
    _ArrayWithDeviceExperimental,
    _ArrayWithElementWiseExperimental,
    _ArrayWithGeneralExperimental,
    _ArrayWithGradientsExperimental,
    _ArrayWithImageExperimental,
    _ArrayWithLayersExperimental,
    _ArrayWithLinearAlgebraExperimental,
    _ArrayWithLossesExperimental,
    _ArrayWithManipulationExperimental,
    _ArrayWithNormsExperimental,
    _ArrayWithRandomExperimental,
    _ArrayWithSetExperimental,
    _ArrayWithSortingExperimental,
    _ArrayWithStatisticalExperimental,
    _ArrayWithUtilityExperimental,
)


class Array(
    _ArrayWithActivations,
    _ArrayWithCreation,
    _ArrayWithDataTypes,
    _ArrayWithDevice,
    _ArrayWithElementwise,
    _ArrayWithGeneral,
    _ArrayWithGradients,
    _ArrayWithImage,
    _ArrayWithLayers,
    _ArrayWithLinearAlgebra,
    _ArrayWithLosses,
    _ArrayWithManipulation,
    _ArrayWithNorms,
    _ArrayWithRandom,
    _ArrayWithSearching,
    _ArrayWithSet,
    _ArrayWithSorting,
    _ArrayWithStatistical,
    _ArrayWithUtility,
    _ArrayWithActivationsExperimental,
    _ArrayWithConversionsExperimental,
    _ArrayWithCreationExperimental,
    _ArrayWithData_typeExperimental,
    _ArrayWithDeviceExperimental,
    _ArrayWithElementWiseExperimental,
    _ArrayWithGeneralExperimental,
    _ArrayWithGradientsExperimental,
    _ArrayWithImageExperimental,
    _ArrayWithLayersExperimental,
    _ArrayWithLinearAlgebraExperimental,
    _ArrayWithLossesExperimental,
    _ArrayWithManipulationExperimental,
    _ArrayWithNormsExperimental,
    _ArrayWithRandomExperimental,
    _ArrayWithSearchingExperimental,
    _ArrayWithSetExperimental,
    _ArrayWithSortingExperimental,
    _ArrayWithStatisticalExperimental,
    _ArrayWithUtilityExperimental,
):
    def __init__(self, data, dynamic_backend=None):
        _ArrayWithActivations.__init__(self)
        _ArrayWithCreation.__init__(self)
        _ArrayWithDataTypes.__init__(self)
        _ArrayWithDevice.__init__(self)
        _ArrayWithElementwise.__init__(self)
        _ArrayWithGeneral.__init__(self)
        _ArrayWithGradients.__init__(self)
        _ArrayWithImage.__init__(self)
        _ArrayWithLayers.__init__(self)
        _ArrayWithLinearAlgebra.__init__(self)
        _ArrayWithLosses.__init__(self)
        _ArrayWithManipulation.__init__(self)
        _ArrayWithNorms.__init__(self)
        _ArrayWithRandom.__init__(self)
        _ArrayWithSearching.__init__(self)
        _ArrayWithSet.__init__(self)
        _ArrayWithSorting.__init__(self)
        _ArrayWithStatistical.__init__(self)
        _ArrayWithUtility.__init__(self)
        _ArrayWithActivationsExperimental.__init__(self),
        _ArrayWithConversionsExperimental.__init__(self),
        _ArrayWithCreationExperimental.__init__(self),
        _ArrayWithData_typeExperimental.__init__(self),
        _ArrayWithDeviceExperimental.__init__(self),
        _ArrayWithElementWiseExperimental.__init__(self),
        _ArrayWithGeneralExperimental.__init__(self),
        _ArrayWithGradientsExperimental.__init__(self),
        _ArrayWithImageExperimental.__init__(self),
        _ArrayWithLayersExperimental.__init__(self),
        _ArrayWithLinearAlgebraExperimental.__init__(self),
        _ArrayWithLossesExperimental.__init__(self),
        _ArrayWithManipulationExperimental.__init__(self),
        _ArrayWithNormsExperimental.__init__(self),
        _ArrayWithRandomExperimental.__init__(self),
        _ArrayWithSearchingExperimental.__init__(self),
        _ArrayWithSetExperimental.__init__(self),
        _ArrayWithSortingExperimental.__init__(self),
        _ArrayWithStatisticalExperimental.__init__(self),
        _ArrayWithUtilityExperimental.__init__(self),
        self._init(data, dynamic_backend)
        self._view_attributes(data)

    def _init(self, data, dynamic_backend=None):
        if ivy.is_ivy_array(data):
            self._data = data.data
        elif ivy.is_native_array(data):
            self._data = data
        elif isinstance(data, np.ndarray):
            self._data = ivy.asarray(data)._data
        else:
            raise ivy.utils.exceptions.IvyException(
                "data must be ivy array, native array or ndarray"
            )
        self._size = None
        self._strides = None
        self._itemsize = None
        self._dtype = None
        self._device = None
        self._dev_str = None
        self._pre_repr = None
        self._post_repr = None
        self.backend = ivy.current_backend_str()
        if dynamic_backend is not None:
            self._dynamic_backend = dynamic_backend
        else:
            self._dynamic_backend = ivy.dynamic_backend
        self.weak_type = False  # to handle 0-D jax front weak typed arrays

    def _view_attributes(self, data):
        self._base = None
        self._view_refs = []
        self._manipulation_stack = []
        self._torch_base = None
        self._torch_view_refs = []
        self._torch_manipulation = None

    # Properties #
    # ---------- #

    @property
    def dynamic_backend(self):
        return self._dynamic_backend

    @dynamic_backend.setter
    def dynamic_backend(self, value):
        from ivy.functional.ivy.gradients import _variable
        from ivy.utils.backend.handler import _determine_backend_from_args

        if value == False:
            self._backend = _determine_backend_from_args(self)

        else:
            is_variable = self._backend.is_variable
            to_numpy = self._backend.to_numpy
            variable_data = self._backend.variable_data

            if is_variable(self.data) and not (
                str(self._backend).__contains__("jax")
                or str(self._backend).__contains__("numpy")
            ):
                native_data = variable_data(self.data)
                np_data = to_numpy(native_data)
                new_arr = ivy.array(np_data)
                self._data = _variable(new_arr).data

            else:
                np_data = to_numpy(self.data)
                self._data = ivy.array(np_data).data

        self._dynamic_backend = value

    @property
    def data(self) -> ivy.NativeArray:
        """The native array being wrapped in self."""
        return self._data

    @property
    def dtype(self) -> ivy.Dtype:
        """Data type of the array elements."""
        if self._dtype is None:
            self._dtype = ivy.dtype(self._data)
        return self._dtype

    @property
    def device(self) -> ivy.Device:
        """Hardware device the array data resides on."""
        if self._device is None:
            self._device = ivy.dev(self._data)
        return self._device

    @property
    def mT(self) -> ivy.Array:
        """
        Transpose of a matrix (or a stack of matrices).

        Returns
        -------
        ret
            array whose last two dimensions (axes) are permuted in reverse order
            relative to original array (i.e., for an array instance having shape
            ``(..., M, N)``, the returned array must have shape ``(..., N, M)``).
            The returned array must have the same data type as the original array.
        """
        ivy.utils.assertions.check_greater(
            len(self._data.shape), 2, allow_equal=True, as_array=False
        )
        return ivy.matrix_transpose(self._data)

    @property
    def ndim(self) -> int:
        """Number of array dimensions (axes)."""
        return len(tuple(self._data.shape))

    @property
    def shape(self) -> ivy.Shape:
        """Array dimensions."""
        return ivy.Shape(self._data.shape)

    @property
    def size(self) -> Optional[int]:
        """Number of elements in the array."""
        if self._size is None:
            self._size = (
                functools.reduce(mul, self._data.shape)
                if len(self._data.shape) > 0
                else 0
            )
        return self._size

    @property
    def itemsize(self) -> Optional[int]:
        """Size of array elements in bytes."""
        if self._itemsize is None:
            self._itemsize = ivy.itemsize(self._data)
        return self._itemsize

    @property
    def strides(self) -> Optional[int]:
        """Get strides across each dimension."""
        if self._strides is None:
            self._strides = ivy.strides(self._data)
        return self._strides

    @property
    def T(self) -> ivy.Array:
        """
        Transpose of the array.

        Returns
        -------
        ret
            two-dimensional array whose first and last dimensions (axes) are
            permuted in reverse order relative to original array.
        """
        ivy.utils.assertions.check_equal(len(self._data.shape), 2, as_array=False)
        return ivy.matrix_transpose(self._data)

    @property
    def base(self) -> ivy.Array:
        """Original array referenced by view."""
        return self._base

    # Setters #
    # --------#

    @data.setter
    def data(self, data):
        ivy.utils.assertions.check_true(
            ivy.is_native_array(data), "data must be native array"
        )
        self._init(data)

    # Built-ins #
    # ----------#

    @classmethod
    def __torch_function__(cls, func, types, args=(), kwargs={}):
        args, kwargs = args_to_native(*args, **kwargs)
        return func(*args, **kwargs)

    def __ivy_array_function__(self, func, types, args, kwargs):
        # Cannot handle items that have __ivy_array_function__ other than those of
        # ivy arrays or native arrays.
        for t in types:
            if (
                hasattr(t, "__ivy_array_function__")
                and (t.__ivy_array_function__ is not ivy.Array.__ivy_array_function__)
                or (
                    hasattr(ivy.NativeArray, "__ivy_array_function__")
                    and (
                        t.__ivy_array_function__
                        is not ivy.NativeArray.__ivy_array_function__
                    )
                )
            ):
                return NotImplemented

        # Arguments contain no overrides, so we can safely call the
        # overloaded function again.
        return func(*args, **kwargs)

    def __array__(self, *args, **kwargs):
        args, kwargs = args_to_native(*args, **kwargs)
        return self._data.__array__(*args, dtype=self.dtype, **kwargs)

    def __array_prepare__(self, *args, **kwargs):
        args, kwargs = args_to_native(*args, **kwargs)
        return self._data.__array_prepare__(*args, **kwargs)

    def __array_ufunc__(self, *args, **kwargs):
        args, kwargs = args_to_native(*args, **kwargs)
        return self._data.__array_ufunc__(*args, **kwargs)

    def __array_wrap__(self, *args, **kwargs):
        args, kwargs = args_to_native(*args, **kwargs)
        return self._data.__array_wrap__(*args, **kwargs)

    def __array_namespace__(self, api_version=None):
        return ivy

    def __repr__(self):
        if self._dev_str is None:
            self._dev_str = ivy.as_ivy_dev(self.device)
            self._pre_repr = "ivy.array"
            if "gpu" in self._dev_str:
                self._post_repr = ", dev={})".format(self._dev_str)
            else:
                self._post_repr = ")"
        sig_fig = ivy.array_significant_figures
        dec_vals = ivy.array_decimal_values
        if self.backend == "" or ivy.is_local():
            # If the array was constructed using implicit backend
            backend = ivy.current_backend()
        else:
            # Requirerd in the case that backend is different
            # from the currently set backend
            backend = ivy.with_backend(self.backend, cached=True)
        arr_np = backend.to_numpy(self._data)
        rep = ivy.vec_sig_fig(arr_np, sig_fig) if self.size > 0 else np.array(arr_np)
        with np.printoptions(precision=dec_vals):
            repr = rep.__repr__()[:-1].partition(", dtype")[0].partition(", dev")[0]
            return (
                self._pre_repr
                + repr[repr.find("(") :]
                + self._post_repr.format(ivy.current_backend_str())
            )

    def __dir__(self):
        return self._data.__dir__()

    def __getattribute__(self, item):
        return super().__getattribute__(item)

    def __getattr__(self, item):
        try:
            attr = self._data.__getattribute__(item)
        except AttributeError:
            attr = self._data.__getattr__(item)
        return to_ivy(attr)

    @handle_view_indexing
    def __getitem__(self, query):
        return ivy.get_item(self._data, query)

    def __setitem__(self, query, val):
        if ivy.current_backend_str() == "torch":
            self._data = self._data.detach()
        if ivy.is_ivy_array(val):
            val = val.data
        target = self.__getitem__(query)
        if not ivy.isscalar(target) and ivy.isscalar(val):
            val = ivy.ones_like(target) * val
        try:
            self._data.__setitem__(query, val)
        except:
            self._data = ivy.scatter_nd(query, val, reduction="replace", out=self)._data
            self._dtype = ivy.dtype(self._data)

    def __contains__(self, key):
        return self._data.__contains__(key)

    def __getstate__(self):
        data_dict = dict()

        # only pickle the native array
        data_dict["data"] = self.data

        # also store the local ivy framework that created this array
        data_dict["backend"] = self.backend
        data_dict["device_str"] = ivy.as_ivy_dev(self.device)

        return data_dict

    def __setstate__(self, state):
        # we can construct other details of ivy.Array
        # just by re-creating the ivy.Array using the native array

        # get the required backend
        (
            ivy.set_backend(state["backend"])
            if state["backend"] is not None and len(state["backend"]) > 0
            else ivy.current_backend(state["data"])
        )
        ivy_array = ivy.array(state["data"])
        ivy.previous_backend()

        self.__dict__ = ivy_array.__dict__

        # TODO: what about placement of the array on the right device ?
        # device = backend.as_native_dev(state["device_str"])
        # backend.to_device(self, device)

    def __pos__(self):
        return ivy.positive(self._data)

    def __neg__(self):
        return ivy.negative(self._data)

    def __pow__(self, power):
        """
        ivy.Array special method variant of ivy.pow. This method simply wraps the
        function, and so the docstring for ivy.pow also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            Input array or float.
        power
            Array or float power. Must be compatible with ``self``
            (see :ref:`broadcasting`). Should have a numeric data type.

        Returns
        -------
        ret
            an array containing the element-wise sums. The returned array must have a
            data type determined by :ref:`type-promotion`.

        Examples
        --------
        With :class:`ivy.Array` input:

        >>> x = ivy.array([1, 2, 3])
        >>> y = x ** 2
        >>> print(y)
        ivy.array([1, 4, 9])

        >>> x = ivy.array([1.2, 2.1, 3.5])
        >>> y = x ** 2.9
        >>> print(y)
        ivy.array([ 1.69678056,  8.59876156, 37.82660675])
        """
        return ivy.pow(self._data, power)

    def __rpow__(self, power):
        return ivy.pow(power, self._data)

    def __ipow__(self, power):
        return ivy.pow(self._data, power)

    def __add__(self, other):
        """
        ivy.Array special method variant of ivy.add. This method simply wraps the
        function, and so the docstring for ivy.add also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            first input array. Should have a numeric data type.
        other
            second input array. Must be compatible with ``self``
            (see :ref:`broadcasting`). Should have a numeric data type.

        Returns
        -------
        ret
            an array containing the element-wise sums. The returned array must have a
            data type determined by :ref:`type-promotion`.

        Examples
        --------
        >>> x = ivy.array([1, 2, 3])
        >>> y = ivy.array([4, 5, 6])
        >>> z = x + y
        >>> print(z)
        ivy.array([5, 7, 9])
        """
        return ivy.add(self._data, other)

    def __radd__(self, other):
        """
        ivy.Array reverse special method variant of ivy.add. This method simply wraps
        the function, and so the docstring for ivy.add also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            first input array. Should have a numeric data type.
        other
            second input array. Must be compatible with ``self``
            (see :ref:`broadcasting`). Should have a numeric data type.

        Returns
        -------
        ret
            an array containing the element-wise sums. The returned array must have a
            data type determined by :ref:`type-promotion`.

        Examples
        --------
        >>> x = 1
        >>> y = ivy.array([4, 5, 6])
        >>> z = x + y
        >>> print(z)
        ivy.array([5, 6, 7])
        """
        return ivy.add(other, self._data)

    def __iadd__(self, other):
        return ivy.add(self._data, other)

    def __sub__(self, other):
        """
        ivy.Array special method variant of ivy.subtract. This method simply wraps the
        function, and so the docstring for ivy.subtract also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            first input array. Should have a numeric data type.
        other
            second input array. Must be compatible with ``self``
            (see :ref:`broadcasting`). Should have a numeric data type.

        Returns
        -------
        ret
            an array containing the element-wise differences. The returned array must have a
            data type determined by :ref:`type-promotion`.

        Examples
        --------
        With :class:`ivy.Array` instances only:

        >>> x = ivy.array([1, 2, 3])
        >>> y = ivy.array([4, 5, 6])
        >>> z = x - y
        >>> print(z)
        ivy.array([-3, -3, -3])
        """
        return ivy.subtract(self._data, other)

    def __rsub__(self, other):
        """
        ivy.Array reverse special method variant of ivy.subtract. This method simply
        wraps the function, and so the docstring for ivy.subtract also applies to this
        method with minimal changes.

        Parameters
        ----------
        self
            first input array. Should have a numeric data type.
        other
            second input array. Must be compatible with ``self``
            (see :ref:`broadcasting`). Should have a numeric data type.

        Returns
        -------
        ret
            an array containing the element-wise differences. The returned array must have a
            data type determined by :ref:`type-promotion`.

        Examples
        --------
        >>> x = 1
        >>> y = ivy.array([4, 5, 6])
        >>> z = x - y
        >>> print(z)
        ivy.array([-3, -4, -5])
        """
        return ivy.subtract(other, self._data)

    def __isub__(self, other):
        return ivy.subtract(self._data, other)

    def __mul__(self, other):
        return ivy.multiply(self._data, other)

    def __rmul__(self, other):
        return ivy.multiply(other, self._data)

    def __imul__(self, other):
        return ivy.multiply(self._data, other)

    def __mod__(self, other):
        return ivy.remainder(self._data, other)

    def __rmod__(self, other):
        return ivy.remainder(other, self._data)

    def __imod__(self, other):
        return ivy.remainder(self._data, other)

    def __divmod__(self, other):
        return tuple([ivy.divide(self._data, other), ivy.remainder(self._data, other)])

    def __rdivmod__(self, other):
        return tuple([ivy.divide(other, self._data), ivy.remainder(other, self._data)])

    def __truediv__(self, other):
        """
        ivy.Array reverse special method variant of ivy.divide. This method simply wraps
        the function, and so the docstring for ivy.divide also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            first input array. Should have a numeric data type.
        other
            second input array. Must be compatible with ``self``
            (see :ref:`broadcasting`). Should have a numeric data type.

        Returns
        -------
        ret
            an array containing the element-wise results. The returned array must have a
            data type determined by :ref:`type-promotion`.

        Examples
        --------
        >>> x = ivy.array([1, 2, 3])
        >>> y = ivy.array([4, 5, 6])
        >>> z = x / y
        >>> print(z)
        ivy.array([0.25      , 0.40000001, 0.5       ])
        """
        return ivy.divide(self._data, other)

    def __rtruediv__(self, other):
        return ivy.divide(other, self._data)

    def __itruediv__(self, other):
        return ivy.divide(self._data, other)

    def __floordiv__(self, other):
        return ivy.floor_divide(self._data, other)

    def __rfloordiv__(self, other):
        return ivy.floor_divide(other, self._data)

    def __ifloordiv__(self, other):
        return ivy.floor_divide(self._data, other)

    def __matmul__(self, other):
        return ivy.matmul(self._data, other)

    def __rmatmul__(self, other):
        return ivy.matmul(other, self._data)

    def __imatmul__(self, other):
        return ivy.matmul(self._data, other)

    def __abs__(self):
        """
        ivy.Array special method variant of ivy.abs. This method simply wraps the
        function, and so the docstring for ivy.abs also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            input array. Should have a numeric data type.

        Returns
        -------
        ret
            an array containing the absolute value of each element
            in ``self``. The returned array must have the same data
            type as ``self``.

        Examples
        --------
        With :class:`ivy.Array` input:

        >>> x = ivy.array([6, -2, 0, -1])
        >>> print(abs(x))
        ivy.array([6, 2, 0, 1])

        >>> x = ivy.array([-1.2, 1.2])
        >>> print(abs(x))
        ivy.array([1.2, 1.2])
        """
        return ivy.abs(self._data)

    def __float__(self):
        res = self._data.__float__()
        if res is NotImplemented:
            return res
        return to_ivy(res)

    def __int__(self):
        if hasattr(self._data, "__int__"):
            res = self._data.__int__()
        else:
            res = int(ivy.to_scalar(self._data))
        if res is NotImplemented:
            return res
        return to_ivy(res)

    def __bool__(self):
        return self._data.__bool__()

    def __dlpack__(self, stream=None):
        return self._data.__dlpack__()

    def __dlpack_device__(self):
        return self._data.__dlpack_device__()

    def __lt__(self, other):
        """
        ivy.Array special method variant of ivy.less. This method simply wraps the
        function, and so the docstring for ivy.less also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            first input array. May have any data type.
        other
            second input array. Must be compatible with x1 (with Broadcasting). May have any
            data type.

        Returns
        -------
        ret
            an array containing the element-wise results. The returned array must have a
            data type of bool.

        Examples
        --------
        >>> x = ivy.array([6, 2, 3])
        >>> y = ivy.array([4, 5, 3])
        >>> z = x < y
        >>> print(z)
        ivy.array([ False, True, False])
        """
        return ivy.less(self._data, other)

    def __le__(self, other):
        """
        ivy.Array special method variant of ivy.less_equal. This method simply wraps the
        function, and so the docstring for ivy.less_equal also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            first input array. May have any data type.
        other
            second input array. Must be compatible with x1 (with Broadcasting). May have any
            data type.

        Returns
        -------
        ret
            an array containing the element-wise results. The returned array must have a
            data type of bool.

        Examples
        --------
        >>> x = ivy.array([6, 2, 3])
        >>> y = ivy.array([4, 5, 3])
        >>> z = x <= y
        >>> print(z)
        ivy.array([ False, True, True])
        """
        return ivy.less_equal(self._data, other)

    def __eq__(self, other):
        """
        ivy.Array special method variant of ivy.equal. This method simply wraps the
        function, and so the docstring for ivy.equal also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            first input array. May have any data type.
        other
            second input array. Must be compatible with x1 (with Broadcasting). May have any
            data type.

        Returns
        -------
        ret
            an array containing the element-wise results. The returned array must have a
            data type of bool.

        Examples
        --------
        With :class:`ivy.Array` instances:

        >>> x1 = ivy.array([1, 0, 1, 1])
        >>> x2 = ivy.array([1, 0, 0, -1])
        >>> y = x1 == x2
        >>> print(y)
        ivy.array([True, True, False, False])

        >>> x1 = ivy.array([1, 0, 1, 0])
        >>> x2 = ivy.array([0, 1, 0, 1])
        >>> y = x1 == x2
        >>> print(y)
        ivy.array([False, False, False, False])
        """
        return ivy.equal(self._data, other)

    def __ne__(self, other):
        """
        ivy.Array special method variant of ivy.not_equal. This method simply wraps the
        function, and so the docstring for ivy.not_equal also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            first input array. May have any data type.
        other
            second input array. Must be compatible with x1 (with Broadcasting). May have any
            data type.

        Returns
        -------
        ret
            an array containing the element-wise results. The returned array must have a
            data type of bool.

        Examples
        --------
        With :class:`ivy.Array` instances:

        >>> x1 = ivy.array([1, 0, 1, 1])
        >>> x2 = ivy.array([1, 0, 0, -1])
        >>> y = x1 != x2
        >>> print(y)
        ivy.array([False, False, True, True])

        >>> x1 = ivy.array([1, 0, 1, 0])
        >>> x2 = ivy.array([0, 1, 0, 1])
        >>> y = x1 != x2
        >>> print(y)
        ivy.array([True, True, True, True])
        """
        return ivy.not_equal(self._data, other)

    def __gt__(self, other):
        """
        ivy.Array special method variant of ivy.greater. This method simply wraps the
        function, and so the docstring for ivy.greater also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            first input array. May have any data type.
        other
            second input array. Must be compatible with x1 (with Broadcasting). May have any
            data type.

        Returns
        -------
        ret
            an array containing the element-wise results. The returned array must have a
            data type of bool.

        Examples
        --------
        With :class:`ivy.Array` instances:

        >>> x = ivy.array([6, 2, 3])
        >>> y = ivy.array([4, 5, 3])
        >>> z = x > y
        >>> print(z)
        ivy.array([True,False,False])

        With mix of :class:`ivy.Array` and :class:`ivy.Container` instances:

        >>> x = ivy.array([[5.1, 2.3, -3.6]])
        >>> y = ivy.Container(a=ivy.array([[4.], [5.1], [6.]]),b=ivy.array([[-3.6], [6.], [7.]]))
        >>> z = x > y
        >>> print(z)
        {
            a: ivy.array([[True, False, False],
                          [False, False, False],
                          [False, False, False]]),
            b: ivy.array([[True, True, False],
                          [False, False, False],
                          [False, False, False]])
        }
        """
        return ivy.greater(self._data, other)

    def __ge__(self, other):
        """
        ivy.Array special method variant of ivy.greater_equal. This method simply wraps
        the function, and so the docstring for ivy.bitwise_xor also applies to this
        method with minimal changes.

        Parameters
        ----------
        self
            first input array. May have any data type.
        other
            second input array. Must be compatible with x1 (with Broadcasting). May have any
            data type.

        Returns
        -------
        ret
            an array containing the element-wise results. The returned array must have a
            data type of bool.

        Examples
        --------
        With :class:`ivy.Array` instances:

        >>> x = ivy.array([6, 2, 3])
        >>> y = ivy.array([4, 5, 6])
        >>> z = x >= y
        >>> print(z)
        ivy.array([True,False,False])

        With mix of :class:`ivy.Array` and :class:`ivy.Container` instances:

        >>> x = ivy.array([[5.1, 2.3, -3.6]])
        >>> y = ivy.Container(a=ivy.array([[4.], [5.1], [6.]]),b=ivy.array([[5.], [6.], [7.]]))
        >>> z = x >= y
        >>> print(z)
        {
            a: ivy.array([[True, False, False],
                          [True, False, False],
                          [False, False, False]]),
            b: ivy.array([[True, False, False],
                          [False, False, False],
                          [False, False, False]])
        }
        """
        return ivy.greater_equal(self._data, other)

    def __and__(self, other):
        return ivy.bitwise_and(self._data, other)

    def __rand__(self, other):
        return ivy.bitwise_and(other, self._data)

    def __iand__(self, other):
        return ivy.bitwise_and(self._data, other)

    def __or__(self, other):
        return ivy.bitwise_or(self._data, other)

    def __ror__(self, other):
        return ivy.bitwise_or(other, self._data)

    def __ior__(self, other):
        return ivy.bitwise_or(self._data, other)

    def __invert__(self):
        return ivy.bitwise_invert(self._data)

    def __xor__(self, other):
        """
        ivy.Array special method variant of ivy.bitwise_xor. This method simply wraps
        the function, and so the docstring for ivy.bitwise_xor also applies to this
        method with minimal changes.

        Parameters
        ----------
        self
            first input array. Should have an integer or boolean data type.
        other
            second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`).
            Should have an integer or boolean data type.
        out
            optional output array, for writing the result to. It must have a shape that the
            inputs broadcast to.

        Returns
        -------
        ret
            an array containing the element-wise results. The returned array must have a
            data type determined by :ref:`type-promotion`.

        Examples
        --------
        With :class:`ivy.Array` instances:

        >>> a = ivy.array([1, 2, 3])
        >>> b = ivy.array([3, 2, 1])
        >>> y = a ^ b
        >>> print(y)
        ivy.array([2,0,2])

        With mix of :class:`ivy.Array` and :class:`ivy.Container` instances:

        >>> x = ivy.Container(a = ivy.array([-67, 21]))
        >>> y = ivy.array([12, 13])
        >>> z = x ^ y
        >>> print(z)
        {a: ivy.array([-79, 24])}
        """
        return ivy.bitwise_xor(self._data, other)

    def __rxor__(self, other):
        return ivy.bitwise_xor(other, self._data)

    def __ixor__(self, other):
        return ivy.bitwise_xor(self._data, other)

    def __lshift__(self, other):
        return ivy.bitwise_left_shift(self._data, other)

    def __rlshift__(self, other):
        return ivy.bitwise_left_shift(other, self._data)

    def __ilshift__(self, other):
        return ivy.bitwise_left_shift(self._data, other)

    def __rshift__(self, other):
        """
        ivy.Array special method variant of ivy.bitwise_right_shift. This method simply
        wraps the function, and so the docstring for ivy.bitwise_right_shift also
        applies to this method with minimal changes.

        Parameters
        ----------
        self
            first input array. Should have an integer data type.
        other
            second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`).
            Should have an integer data type. Each element must be greater than or equal
            to ``0``.

        Returns
        -------
        ret
            an array containing the element-wise results. The returned array must have
            a data type determined by :ref:`type-promotion`.

        Examples
        --------
        With :class:`ivy.Array` instances only:

        >>> a = ivy.array([2, 3, 4])
        >>> b = ivy.array([0, 1, 2])
        >>> y = a >> b
        >>> print(y)
        ivy.array([2, 1, 1])
        """
        return ivy.bitwise_right_shift(self._data, other)

    def __rrshift__(self, other):
        """
        ivy.Array reverse special method variant of ivy.bitwise_right_shift. This method
        simply wraps the function, and so the docstring for ivy.bitwise_right_shift also
        applies to this method with minimal changes.

        Parameters
        ----------
        self
            first input array. Should have an integer data type.
        other
            second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`).
            Should have an integer data type. Each element must be greater than or equal
            to ``0``.

        Returns
        -------
        ret
            an array containing the element-wise results. The returned array must have
            a data type determined by :ref:`type-promotion`.

        Examples
        --------
        >>> a = 32
        >>> b = ivy.array([0, 1, 2])
        >>> y = a >> b
        >>> print(y)
        ivy.array([32, 16,  8])
        """
        return ivy.bitwise_right_shift(other, self._data)

    def __irshift__(self, other):
        return ivy.bitwise_right_shift(self._data, other)

    def __deepcopy__(self, memodict={}):
        try:
            return to_ivy(self._data.__deepcopy__(memodict))
        except AttributeError:
            # ToDo: try and find more elegant solution to jax inability to
            #  deepcopy device arrays
            if ivy.current_backend_str() == "jax":
                np_array = copy.deepcopy(self._data)
                jax_array = ivy.array(np_array)
                return to_ivy(jax_array)
            return to_ivy(copy.deepcopy(self._data))

    def __len__(self):
        try:
            return len(self._data)
        except TypeError:
            return self._data.shape[0]

    def __iter__(self):
        if self.ndim == 0:
            raise TypeError("iteration over a 0-d ivy.Array not supported")
        if ivy.current_backend_str() == "paddle":
            if self.dtype in ["int8", "int16", "uint8", "float16"]:
                return iter([to_ivy(i) for i in ivy.unstack(self._data)])
            elif self.ndim == 1:
                return iter([to_ivy(i).squeeze(0) for i in self._data])
        return iter([to_ivy(i) for i in self._data])
