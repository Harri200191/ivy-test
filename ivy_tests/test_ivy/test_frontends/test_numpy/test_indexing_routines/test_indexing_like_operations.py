# Testing Function
# global
from hypothesis import strategies as st

# local
import ivy_tests.test_ivy.helpers as helpers
import ivy_tests.test_ivy.test_frontends.test_numpy.helpers as np_frontend_helpers
from ivy_tests.test_ivy.helpers import handle_frontend_test


@handle_frontend_test(
    fn_tree="numpy.take_along_axis",
    dtype_x_indices_axis=helpers.array_indices_axis(
        array_dtypes=helpers.get_dtypes("numeric"),
        indices_dtypes=["int32", "int64"],
        min_num_dims=1,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=10,
        indices_same_dims=True,
    ),
    test_with_out=st.just(False),
)
def test_numpy_take_along_axis(
    *,
    dtype_x_indices_axis,
    test_flags,
    frontend,
    fn_tree,
    on_device,
):
    dtypes, x, indices, axis, _ = dtype_x_indices_axis
    helpers.test_frontend_function(
        input_dtypes=dtypes,
        test_flags=test_flags,
        frontend=frontend,
        fn_tree=fn_tree,
        on_device=on_device,
        arr=x,
        indices=indices,
        axis=axis,
    )


@handle_frontend_test(
    fn_tree="numpy.diag",
    dtype_and_x=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("valid"),
        min_num_dims=1,
        max_num_dims=2,
        min_dim_size=2,
    ),
    k=st.integers(min_value=-1, max_value=1),
    test_with_out=st.just(False),
)
def test_numpy_diag(
    dtype_and_x,
    k,
    test_flags,
    frontend,
    fn_tree,
    on_device,
):
    input_dtype, x = dtype_and_x
    np_frontend_helpers.test_frontend_function(
        input_dtypes=input_dtype,
        test_flags=test_flags,
        on_device=on_device,
        frontend=frontend,
        fn_tree=fn_tree,
        v=x[0],
        k=k,
    )


@handle_frontend_test(
    fn_tree="numpy.diagonal",
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("numeric"),
        min_num_dims=2,
        min_axes_size=2,
        max_axes_size=2,
        valid_axis=True,
    ),
    offset=st.integers(min_value=-1, max_value=1),
    test_with_out=st.just(False),
)
def test_numpy_diagonal(
    dtype_x_axis,
    offset,
    on_device,
    fn_tree,
    frontend,
    test_flags,
):
    input_dtype, x, axis = dtype_x_axis
    np_frontend_helpers.test_frontend_function(
        input_dtypes=input_dtype,
        on_device=on_device,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        a=x[0],
        offset=offset,
        axis1=axis[0],
        axis2=axis[1],
    )


@handle_frontend_test(
    fn_tree="numpy.put_along_axis",
    dtype_x_indices_axis=helpers.array_indices_put_along_axis(
        array_dtypes=helpers.get_dtypes("numeric"),
        indices_dtypes=["int32", "int64"],
        min_num_dims=1,
        max_num_dims=5,
        min_dim_size=1,
        max_dim_size=10,
    ),
    test_with_out=st.just(False),
)
def test_numpy_put_along_axis(
    *,
    dtype_x_indices_axis,
    test_flags,
    frontend,
    fn_tree,
    on_device,
):
    dtypes, x, indices, axis, values, _ = dtype_x_indices_axis
    helpers.test_frontend_function(
        input_dtypes=dtypes,
        test_flags=test_flags,
        frontend=frontend,
        fn_tree=fn_tree,
        on_device=on_device,
        arr=x,
        indices=indices,
        axis=axis,
        values=values,
    )
