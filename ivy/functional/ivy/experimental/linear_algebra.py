# global
from typing import Union, Optional, Tuple, List, Sequence

# local
import ivy
from ivy.utils.backend import current_backend
from ivy.func_wrapper import (
    to_native_arrays_and_back,
    handle_out_argument,
    handle_nestable,
    handle_array_like_without_promotion,
    handle_array_function,
)
from ivy.utils.exceptions import handle_exceptions

# Helpers #
# ------- #


def _check_valid_dimension_size(std):
    ivy.utils.assertions.check_dimensions(std)


@handle_exceptions
@handle_nestable
@handle_array_like_without_promotion
@handle_array_function
def eigh_tridiagonal(
    alpha: Union[ivy.Array, ivy.NativeArray],
    beta: Union[ivy.Array, ivy.NativeArray],
    /,
    *,
    eigvals_only: bool = True,
    select: str = "a",
    select_range: Optional[
        Union[Tuple[int, int], List[int], ivy.Array, ivy.NativeArray]
    ] = None,
    tol: Optional[float] = None,
) -> Union[ivy.Array, Tuple[ivy.Array, ivy.Array]]:
    """
    Compute the eigenvalues and eigenvectors of a Hermitian tridiagonal matrix.

    Parameters
    ----------
    alpha
        A real or complex array of shape (n), the diagonal elements of the
        matrix. If alpha is complex, the imaginary part is ignored
        (assumed zero) to satisfy the requirement that the matrix be Hermitian.
    beta
        A real or complex array of shape (n-1), containing the elements of
        the first super-diagonal of the matrix. If beta is complex, the first
        sub-diagonal of the matrix is assumed to be the conjugate of beta to
        satisfy the requirement that the matrix be Hermitian.
    eigvals_only
        If False, both eigenvalues and corresponding eigenvectors are
        computed. If True, only eigenvalues are computed. Default is True.
    select
        Optional string with values in {'a', 'v', 'i'} (default is 'a') that
        determines which eigenvalues to calculate: 'a': all eigenvalues.
        'v': eigenvalues in the interval (min, max] given by select_range.
        'i': eigenvalues with indices min <= i <= max.
    select_range
        Size 2 tuple or list or array specifying the range of eigenvalues to
        compute together with select. If select is 'a', select_range is ignored.
    tol
        Optional scalar. Ignored when backend is not Tensorflow. The absolute
        tolerance to which each eigenvalue is required. An eigenvalue
        (or cluster) is considered to have converged if it lies in an interval
        of this width. If tol is None (default), the value eps*|T|_2 is used
        where eps is the machine precision, and |T|_2 is the 2-norm of the matrix T.

    Returns
    -------
    eig_vals
        The eigenvalues of the matrix in non-decreasing order.
    eig_vectors
        If eigvals_only is False the eigenvectors are returned in the second output
        argument.

    Both the description and the type hints above assumes an array input for
    simplicity, but this function is *nestable*, and therefore also accepts
    :class:`ivy.Container` instances in place of any of the arguments.

    Examples
    --------
    With :class:`ivy.Array` input:

    >>> alpha = ivy.array([0., 1., 2.])
    >>> beta = ivy.array([0., 1.])
    >>> y = ivy.eigh_tridiagonal(alpha, beta)
    >>> print(y)
    ivy.array([0., 0.38196, 2.61803])

    >>> alpha = ivy.array([0., 1., 2.])
    >>> beta = ivy.array([0., 1.])
    >>> y = ivy.eigh_tridiagonal(alpha,
    ...     beta, select='v',
    ...     select_range=[0.2,3.0])
    >>> print(y)
    ivy.array([0.38196, 2.61803])

    >>> ivy.set_backend("tensorflow")
    >>> alpha = ivy.array([0., 1., 2., 3.])
    >>> beta = ivy.array([2., 1., 2.])
    >>> y = ivy.eigh_tridiagonal(alpha,
    ...     beta,
    ...     eigvals_only=False,
    ...     select='i',
    ...     select_range=[1,2]
    ...     tol=1.)
    >>> print(y)
    (ivy.array([0.18749806, 2.81250191]), ivy.array([[ 0.350609  , -0.56713122],
        [ 0.06563006, -0.74146169],
        [-0.74215561, -0.0636413 ],
        [ 0.56742489,  0.35291126]]))

    With :class:`ivy.Container` input:

    >>> alpha = ivy.Container(a=ivy.array([0., 1., 2.]), b=ivy.array([2., 2., 2.]))
    >>> beta = ivy.array([0.,2.])
    >>> y = ivy.eigh_tridiagonal(alpha, beta)
    >>> print(y)
    {
        a: ivy.array([-0.56155, 0., 3.56155]),
        b: ivy.array([0., 2., 4.])
    }

    >>> alpha = ivy.Container(a=ivy.array([0., 1., 2.]), b=ivy.array([2., 2., 2.]))
    >>> beta = ivy.Container(a=ivy.array([0.,2.]), b=ivy.array([2.,2.]))
    >>> y = ivy.eigh_tridiagonal(alpha, beta)
    >>> print(y)
    {
        a: ivy.array([-0.56155, 0., 3.56155]),
        b: ivy.array([-0.82842, 2., 4.82842])
    }
    """
    x = ivy.diag(alpha)
    y = ivy.diag(beta, k=1)
    z = ivy.diag(beta, k=-1)
    w = x + y + z

    eigh_out = ivy.linalg.eigh(w)
    eigenvalues = eigh_out.eigenvalues
    eigenvectors = eigh_out.eigenvectors

    if select == "i":
        eigenvalues = eigenvalues[select_range[0] : select_range[1] + 1]
        eigenvectors = eigenvectors[:, select_range[0] : select_range[1] + 1]
    elif select == "v":
        condition = ivy.logical_and(
            eigenvalues.greater(select_range[0]),
            eigenvalues.less_equal(select_range[1]),
        )
        eigenvalues = eigenvalues[condition]
        eigenvectors = eigenvectors[:, condition]

    if eigvals_only:
        return eigenvalues
    return eigenvalues, eigenvectors


@handle_exceptions
@handle_nestable
@handle_array_like_without_promotion
@handle_out_argument
@to_native_arrays_and_back
def diagflat(
    x: Union[ivy.Array, ivy.NativeArray],
    /,
    *,
    offset: int = 0,
    padding_value: float = 0,
    align: str = "RIGHT_LEFT",
    num_rows: int = -1,
    num_cols: int = -1,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """
    Return a two-dimensional array with the flattened input as a diagonal.

    Parameters
    ----------
    x
        Input data, which is flattened and set as the k-th diagonal of the output.
    k
        Diagonal to set.
        Positive value means superdiagonal,
        0 refers to the main diagonal,
        and negative value means subdiagonal.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        The 2-D output array.

    Functional Examples
    ------------------

    With :class:`ivy.Array` inputs:

    >>> x = ivy.array([[1,2], [3,4]])
    >>> ivy.diagflat(x)
    ivy.array([[1, 0, 0, 0],
               [0, 2, 0, 0],
               [0, 0, 3, 0],
               [0, 0, 0, 4]])

    >>> x = ivy.array([1,2])
    >>> ivy.diagflat(x, k=1)
    ivy.array([[0, 1, 0],
               [0, 0, 2],
               [0, 0, 0]])
    """
    return current_backend(x).diagflat(
        x,
        offset=offset,
        padding_value=padding_value,
        align=align,
        num_rows=num_rows,
        num_cols=num_cols,
        out=out,
    )


@handle_exceptions
@handle_nestable
@handle_array_like_without_promotion
@handle_out_argument
@to_native_arrays_and_back
def kron(
    a: Union[ivy.Array, ivy.NativeArray],
    b: Union[ivy.Array, ivy.NativeArray],
    /,
    *,
    out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    Compute the Kronecker product, a composite array made of blocks of the second array
    scaled by the first.

    Parameters
    ----------
    a
        First input array.
    b
        Second input array
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        Array representing the Kronecker product of the input arrays.

    Examples
    --------
    >>> a = ivy.array([1,2])
    >>> b = ivy.array([3,4])
    >>> ivy.kron(a, b)
    ivy.array([3, 4, 6, 8])
    """
    return current_backend(a, b).kron(a, b, out=out)


@handle_exceptions
@handle_nestable
@handle_array_like_without_promotion
@handle_out_argument
@to_native_arrays_and_back
def matrix_exp(
    x: Union[ivy.Array, ivy.NativeArray],
    /,
    *,
    out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    Compute the matrix exponential of a square matrix.

    Parameters
    ----------
    a
        Square matrix.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        the matrix exponential of the input.

    Examples
    --------
        >>> x = ivy.array([[[1., 0.],
                            [0., 1.]],
                            [[2., 0.],
                            [0., 2.]]])
        >>> ivy.matrix_exp(x)
        ivy.array([[[2.7183, 1.0000],
                    [1.0000, 2.7183]],
                    [[7.3891, 1.0000],
                    [1.0000, 7.3891]]])
    """
    return current_backend(x).matrix_exp(x, out=out)


@handle_exceptions
@handle_nestable
@handle_array_like_without_promotion
@to_native_arrays_and_back
def eig(
    x: Union[ivy.Array, ivy.NativeArray],
    /,
) -> Tuple[ivy.Array]:
    """Compute eigenvalies and eigenvectors of x. Returns a tuple with two
    elements: first is the set of eigenvalues, second is the set of
    eigenvectors.

    Parameters
    ----------
    x
        An array of shape (..., N, N).

    Returns
    -------
    w
        Not necessarily ordered array(..., N) of eigenvalues in complex type.
    v
        An array(..., N, N) of normalized (unit “length”) eigenvectors,
        the column v[:,i] is the eigenvector corresponding to the eigenvalue w[i].

    This function conforms to the `Array API Standard
    <https://data-apis.org/array-api/latest/>`_.
    Both the description and the type hints above assumes an array input for simplicity,
    but this function is *nestable*, and therefore also accepts :class:`ivy.Container`
    instances in place of any of the arguments.

    Functional Examples
    ------------------
    With :class:`ivy.Array` inputs:
    >>> x = ivy.array([[1,2], [3,4]])
    >>> w, v = ivy.eig(x)
    >>> w; v
    ivy.array([-0.37228132+0.j,  5.37228132+0.j])
    ivy.array([[-0.82456484+0.j, -0.41597356+0.j],
               [ 0.56576746+0.j, -0.90937671+0.j]])

    >>> x = ivy.array([[[1,2], [3,4]], [[5,6], [5,6]]])
    >>> w, v = ivy.eig(x)
    >>> w; v
    ivy.array(
        [
            [-3.72281323e-01+0.j,  5.37228132e+00+0.j],
            [3.88578059e-16+0.j,  1.10000000e+01+0.j]
        ]
    )
    ivy.array([
            [
                [-0.82456484+0.j, -0.41597356+0.j], [0.56576746+0.j, -0.90937671+0.j]
            ],
            [
                [-0.76822128+0.j, -0.70710678+0.j], [0.6401844 +0.j, -0.70710678+0.j]
            ]
    ])
    """
    return current_backend(x).eig(x)


@handle_exceptions
@handle_nestable
@handle_array_like_without_promotion
@to_native_arrays_and_back
def eigvals(
    x: Union[ivy.Array, ivy.NativeArray],
    /,
) -> ivy.Array:
    """
    Compute eigenvalues of x. Returns a set of eigenvalues.

    Parameters
    ----------
    x
        An array of shape (..., N, N).

    Returns
    -------
    w
        Not necessarily ordered array(..., N) of eigenvalues in complex type.

    Functional Examples
    ------------------
    With :class:`ivy.Array` inputs:
    >>> x = ivy.array([[1,2], [3,4]])
    >>> w = ivy.eigvals(x)
    >>> w
    ivy.array([-0.37228132+0.j,  5.37228132+0.j])

    >>> x = ivy.array([[[1,2], [3,4]], [[5,6], [5,6]]])
    >>> w = ivy.eigvals(x)
    >>> w
    ivy.array(
        [
            [-0.37228132+0.j,  5.37228132+0.j],
            [ 0.        +0.j, 11.        +0.j]
        ]
    )
    """
    return current_backend(x).eigvals(x)


@handle_exceptions
@handle_nestable
@handle_array_like_without_promotion
@handle_out_argument
@to_native_arrays_and_back
def adjoint(
    x: Union[ivy.Array, ivy.NativeArray],
    /,
    *,
    out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    Compute the complex conjugate transpose of x.

    Parameters
    ----------
    x
        An array with more than one dimension.
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        the complex conjugate transpose of the input.

    Examples
    --------
        >>> x = np.array([[1.-1.j, 2.+2.j],
                          [3.+3.j, 4.-4.j]])
        >>> x = ivy.array(x)
        >>> ivy.adjoint(x)
        ivy.array([[1.+1.j, 3.-3.j],
                   [2.-2.j, 4.+4.j]])
    """
    return current_backend(x).adjoint(x, out=out)


@handle_nestable
@handle_out_argument
@to_native_arrays_and_back
@handle_exceptions
def multi_dot(
    x: Sequence[Union[ivy.Array, ivy.NativeArray]],
    /,
    *,
    out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    Compute the dot product of two or more matrices in a single function call, while
    selecting the fastest evaluation order.

    Parameters
    ----------
    x
        sequence of matrices to multiply.
    out
        optional output array, for writing the result to. It must have a valid
        shape, i.e. the resulting shape after applying regular matrix multiplication
        to the inputs.

    Returns
    -------
    ret
        dot product of the arrays.

    Examples
    --------
    With :class:`ivy.Array` input:

    >>> A = ivy.arange(2 * 3).reshape((2, 3))
    >>> B = ivy.arange(3 * 2).reshape((3, 2))
    >>> C = ivy.arange(2 * 2).reshape((2, 2))
    >>> ivy.multi_dot((A, B, C))
    ivy.array([[ 26,  49],
               [ 80, 148]])

    >>> A = ivy.arange(2 * 3).reshape((2, 3))
    >>> B = ivy.arange(3 * 2).reshape((3, 2))
    >>> C = ivy.arange(2 * 2).reshape((2, 2))
    >>> D = ivy.zeros((2, 2))
    >>> ivy.multi_dot((A, B, C), out=D)
    >>> print(D)
    ivy.array([[ 26,  49],
               [ 80, 148]])
    """
    return current_backend(x).multi_dot(x, out=out)


@handle_exceptions
@handle_nestable
@handle_array_like_without_promotion
@handle_out_argument
@to_native_arrays_and_back
def cond(
    x: Union[ivy.Array, ivy.NativeArray],
    /,
    *,
    p: Optional[Union[int, float, str]] = None,
    out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    Compute the condition number of x.

    Parameters
    ----------
    x
        An array with more than one dimension.
    p
        The order of the norm of the matrix (see :func:`ivy.norm` for details).
    out
        optional output array, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        the condition number of the input.

    Examples
    --------
        >>> x = ivy.array([[1., 2.],
                           [3., 4.]])
        >>> ivy.cond(x)
        ivy.array(14.933034)

        >>> x = ivy.array([[1., 2.],
                            [3., 4.]])
        >>> ivy.cond(x, p=ivy.inf)
        ivy.array(21.0)
    """
    return current_backend(x).cond(x, p=p, out=out)


@handle_exceptions
@handle_nestable
@handle_array_like_without_promotion
@to_native_arrays_and_back
def cov(
    x1: Union[ivy.Array, ivy.NativeArray],
    x2: Union[ivy.Array, ivy.NativeArray] = None,
    /,
    *,
    rowVar: bool = True,
    bias: bool = False,
    ddof: Optional[int] = None,
    fweights: Optional[ivy.Array] = None,
    aweights: Optional[ivy.Array] = None,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
) -> ivy.Array:
    """
    Compute the covariance of matrix x1, or variables x1 and x2.

    Parameters
    ----------
    x1
        a 1D or 2D input array, with a numeric data type.
    x2
        optional second 1D or 2D input array, with a numeric data type.
        Must have the same shape as ``self``.
    rowVar
        optional variable where each row of input is interpreted as a variable
        (default = True). If set to False, each column is instead interpreted
        as a variable.
    bias
        optional variable for normalizing input (default = False) by (N - 1) where
        N is the number of given observations. If set to True, then normalization
        is instead by N. Can be overridden by keyword ``ddof``.
    ddof
        optional variable to override ``bias`` (default = None). ddof=1 will return
        the unbiased estimate, even with fweights and aweights given. ddof=0 will
        return the simple average.
    fweights
        optional 1D array of integer frequency weights; the number of times each
        observation vector should be repeated.
    aweights
        optional 1D array of observation vector weights. These relative weights are
        typically large for observations considered "important" and smaller for
        observations considered less "important". If ddof=0 is specified, the array
        of weights can be used to assign probabilities to observation vectors.
    dtype
        optional variable to set data-type of the result. By default, data-type
        will have at least ``numpy.float64`` precision.
    out
        optional output array, for writing the result to. It must have a shape that
        the inputs broadcast to.

    Returns
    -------
    ret
        an array containing the covariance matrix of an input matrix, or the
        covariance matrix of two variables. The returned array must have a
        floating-point data type determined by Type Promotion Rules and must be
        a square matrix of shape (N, N), where N is the number of variables in the
        input(s).

    This function conforms to the `Array API Standard
    <https://data-apis.org/array-api/latest/>`_. This docstring is an extension of the
    `docstring <https://data-apis.org/array-api/latest/
    extensions/generated/signatures.linalg.cov.html>`_
    in the standard.
    Both the description and the type hints above assumes an array input for simplicity,
    but this function is *nestable*, and therefore also accepts :class:`ivy.Container`
    instances in place of any of the arguments.

    Examples
    --------
    With :class:`ivy.Array` input:
    >>> x = ivy.array([[1,2,3],
    ...                [4,5,6]])
    >>> y = x.cov()
    >>> print(y)
    ivy.array([[ 1.,  1.  ],
    ...        [ 1.,  1.  ]]
    With :class:`ivy.Container` inputs:
    >>> x = ivy.Container(a=ivy.array([1., 2., 3.]), b=ivy.array([1., 2., 3.]))
    >>> y = ivy.Container(a=ivy.array([3., 2., 1.]), b=ivy.array([3., 2., 1.]))
    >>> z = ivy.Container.static_cov(x, y)
    >>> print(z)
    {
        a: ivy.array([ 1., -1., -1., -1.]
                     [ 1.,  1., -1., -1.]),
        b: ivy.array([-1., -1.,  1.,  1.]
                     [-1.,  1.,  1.,  1.])
    }
    With a combination of :class:`ivy.Array` and :class:`ivy.Container` inputs:
    >>> x = ivy.array([1., 2., 3.])
    >>> y = ivy.Container(a=ivy.array([3. ,2. ,1.]), b=ivy.array([-1., -2., -3.]))
    >>> z = ivy.cov(x, y)
    >>> print(z)
    {
        a: ivy.array([ 1., -1.]
                     [-1.,  1.]),
        b: ivy.array([ 1., -1.]
                     [-1.,  1.])
    }
    With :class:`ivy.Array` input and rowVar flag set to False (True by default):
    >>> x = ivy.array([[1,2,3],
    ...                [4,5,6]])
    >>> y = x.cov(rowVar=False)
    >>> print(y)
    ivy.array([[ 4.5,  4.5, 4.5 ],
    ...        [ 4.5,  4.5, 4.5 ],
    ...        [ 4.5,  4.5, 4.5 ]])
    With :class:`ivy.Array` input and bias flag set to True (False by default):
    >>> x = ivy.array([[1,2,3],
    ...                [4,5,6]])
    >>> y = x.cov(bias=True)
    >>> print(y)
    ivy.array([[ 0.6667,  0.6667  ],
    ...        [ 0.6667,  0.6667  ]]
    With :class:`ivy.Array` input with both fweights and aweights given:
    >>> x = ivy.array([[1,2,3],
    ...                [4,5,6]])
    >>> fw = ivy.array([1,2,3])
    >>> aw = ivy.array([ 1.2, 2.3, 3.4 ])
    >>> y = x.cov(fweights=fw, aweights=aw)
    >>> print(y)
    ivy.array([[ 0.48447205,  0.48447205  ],
    ...        [ 0.48447205,  0.48447205  ]]
    With :class:`ivy.Array` input with both fweights and aweights given,
    and rowVar set to False:
    >>> x = ivy.array([[1,2,3],
    ...                [4,5,6]])
    >>> fw = ivy.array([1,3])
    >>> aw = ivy.array([ 1.5, 4 ])
    >>> y = x.cov(fweights=fw, aweights=aw, rowVar=False)
    >>> print(y)
    ivy.array([[ 1.22727273,  1.22727273, 1.22727273 ],
    ...        [ 1.22727273,  1.22727273, 1.22727273 ],
    ...        [ 1.22727273,  1.22727273, 1.22727273 ]])
    """
    return current_backend().cov(
        x1,
        x2,
        rowVar=rowVar,
        bias=bias,
        ddof=ddof,
        fweights=fweights,
        aweights=aweights,
        dtype=dtype,
    )
