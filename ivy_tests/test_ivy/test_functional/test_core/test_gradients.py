"""Collection of tests for unified gradient functions."""

# global
from hypothesis import strategies as st
import pytest
import numpy as np

# local
import ivy
from ivy.functional.ivy.gradients import _variable
import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers import handle_test


@st.composite
def get_gradient_arguments_with_lr(
    draw,
    *,
    min_value=-1e20,
    max_value=1e20,
    abs_smallest_val=None,
    large_abs_safety_factor=2,
    small_abs_safety_factor=16,
    num_arrays=1,
    float_lr=False,
    no_lr=False,
):
    dtypes, arrays, shape = draw(
        helpers.dtype_and_values(
            available_dtypes=helpers.get_dtypes("float"),
            num_arrays=num_arrays,
            min_value=min_value,
            max_value=max_value,
            abs_smallest_val=abs_smallest_val,
            large_abs_safety_factor=large_abs_safety_factor,
            small_abs_safety_factor=small_abs_safety_factor,
            safety_factor_scale="log",
            min_num_dims=1,
            shared_dtype=True,
            ret_shape=True,
        )
    )
    dtype = dtypes[0]
    if no_lr:
        return dtypes, arrays
    if float_lr:
        lr = draw(
            helpers.floats(
                min_value=1e-2,
                max_value=1.0,
            )
        )
    else:
        lr = draw(
            st.one_of(
                helpers.floats(
                    min_value=1e-2,
                    max_value=1.0,
                ),
                helpers.array_values(
                    dtype=dtype,
                    shape=shape,
                    min_value=1e-2,
                    max_value=1.0,
                ),
            )
        )
    if isinstance(lr, list):
        dtypes += [dtype]
    return dtypes, arrays, lr


# stop_gradient
@handle_test(
    fn_tree="functional.ivy.stop_gradient",
    dtype_and_x=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("numeric")
    ),
    preserve_type=st.booleans(),
    test_instance_method=st.just(False),
    test_gradients=st.just(False),
)
def test_stop_gradient(
    *,
    dtype_and_x,
    preserve_type,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    dtype, x = dtype_and_x
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=dtype,
        test_flags=test_flags,
        fw=backend_fw,
        fn_name=fn_name,
        on_device=on_device,
        x=x[0],
        preserve_type=preserve_type,
    )


# execute_with_gradients
@handle_test(
    fn_tree="functional.ivy.execute_with_gradients",
    dtype_and_xs=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("float"),
        min_num_dims=1,
        min_dim_size=1,
        min_value=0,
        max_value=100,
    ),
    retain_grads=st.booleans(),
    test_instance_method=st.just(False),
    test_with_out=st.just(False),
    test_gradients=st.just(False),
)
def test_execute_with_gradients(
    *,
    dtype_and_xs,
    retain_grads,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    def func(xs):
        if isinstance(xs, ivy.Container):
            array_idxs = ivy.nested_argwhere(xs, ivy.is_array)
            array_vals = ivy.multi_index_nest(xs, array_idxs)
            if len(array_vals) == 0:
                final_array = None
            else:
                final_array = ivy.stack(array_vals)
        else:
            final_array = xs
        ret = ivy.mean(final_array)
        return ret

    dtype, xs = dtype_and_xs
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=dtype,
        test_flags=test_flags,
        fw=backend_fw,
        fn_name=fn_name,
        func=func,
        rtol_=1e-1,
        atol_=1e-1,
        on_device=on_device,
        xs=xs[0],
        retain_grads=retain_grads,
    )


# value_and_grad
@pytest.mark.parametrize(
    "x", [[[4.6, 2.1, 5], [2.8, 1.3, 6.2]], [[4.6, 2.1], [5, 2.8], [1.3, 6.2]]]
)
@pytest.mark.parametrize("dtype", ["float32", "float64"])
@pytest.mark.parametrize(
    "func", [lambda x: ivy.mean(ivy.square(x)), lambda x: ivy.mean(ivy.cos(x))]
)
def test_value_and_grad(x, dtype, func, backend_fw):
    fw = backend_fw.current_backend_str()
    if fw == "numpy":
        return
    ivy.set_backend(fw)
    var = _variable(ivy.array(x, dtype=dtype))
    fn = ivy.value_and_grad(func)
    value, grad = fn(var)
    value_np, grad_np = helpers.flatten_and_to_np(ret=value), helpers.flatten_and_to_np(
        ret=grad
    )
    ivy.previous_backend()
    ivy.set_backend("tensorflow")
    var = _variable(ivy.array(x, dtype=dtype))
    fn = ivy.value_and_grad(func)
    value_gt, grad_gt = fn(var)
    value_np_from_gt, grad_np_from_gt = helpers.flatten_and_to_np(
        ret=value_gt
    ), helpers.flatten_and_to_np(ret=grad_gt)
    for value, value_from_gt in zip(value_np, value_np_from_gt):
        assert value.shape == value_from_gt.shape
        assert np.allclose(value, value_from_gt)
    for grad, grad_from_gt in zip(grad_np, grad_np_from_gt):
        assert grad.shape == grad_from_gt.shape
        assert np.allclose(grad, grad_from_gt)


# jac
@pytest.mark.parametrize(
    "x", [[[4.6, 2.1, 5], [2.8, 1.3, 6.2]], [[4.6, 2.1], [5, 2.8], [1.3, 6.2]]]
)
@pytest.mark.parametrize("dtype", ["float32", "float64"])
@pytest.mark.parametrize(
    "func", [lambda x: ivy.mean(ivy.square(x)), lambda x: ivy.mean(ivy.cos(x))]
)
def test_jac(x, dtype, func, backend_fw):
    fw = backend_fw.current_backend_str()
    if fw == "numpy":
        return
    ivy.set_backend(fw)
    var = _variable(ivy.array(x, dtype=dtype))
    fn = ivy.jac(func)
    jacobian = fn(var)
    jacobian_np = helpers.flatten_and_to_np(ret=jacobian)
    ivy.previous_backend()
    ivy.set_backend("tensorflow")
    var = _variable(ivy.array(x, dtype=dtype))
    fn = ivy.jac(func)
    jacobian_gt = fn(var)
    jacobian_np_from_gt = helpers.flatten_and_to_np(ret=jacobian_gt)
    for jacobian, jacobian_from_gt in zip(jacobian_np, jacobian_np_from_gt):
        assert jacobian.shape == jacobian_from_gt.shape
        assert np.allclose(jacobian, jacobian_from_gt)

    # Test nested input
    func = lambda xs: (2 * xs[1]["x2"], xs[0])

    ivy.set_backend(fw)
    var1 = _variable(ivy.array(x[0], dtype=dtype))
    var2 = _variable(ivy.array(x[1], dtype=dtype))
    var = [var1, {"x2": var2}]
    fn = ivy.jac(func)
    jacobian = fn(var)
    jacobian_np = helpers.flatten_and_to_np(ret=jacobian)
    ivy.previous_backend()
    ivy.set_backend("tensorflow")
    var1 = _variable(ivy.array(x[0], dtype=dtype))
    var2 = _variable(ivy.array(x[1], dtype=dtype))
    var = [var1, {"x2": var2}]
    fn = ivy.jac(func)
    jacobian_gt = fn(var)
    jacobian_np_from_gt = helpers.flatten_and_to_np(ret=jacobian_gt)
    for jacobian, jacobian_from_gt in zip(jacobian_np, jacobian_np_from_gt):
        assert jacobian.shape == jacobian_from_gt.shape
        assert np.allclose(jacobian, jacobian_from_gt)


# grad
@pytest.mark.parametrize(
    "x", [[[4.6, 2.1, 5], [2.8, 1.3, 6.2]], [[4.6, 2.1], [5, 2.8], [1.3, 6.2]]]
)
@pytest.mark.parametrize("dtype", ["float32", "float64"])
@pytest.mark.parametrize(
    "func", [lambda x: ivy.mean(ivy.square(x)), lambda x: ivy.mean(ivy.cos(x))]
)
@pytest.mark.parametrize("nth", [1, 2, 3])
def test_grad(x, dtype, func, backend_fw, nth):
    fw = backend_fw.current_backend_str()

    # ToDo: Remove skipping for paddle and jax for nth > 1
    if fw == "numpy" or ((fw == "paddle" or fw == "jax") and nth > 1):
        return

    ivy.set_backend(fw)
    var = _variable(ivy.array(x, dtype=dtype))
    fn = ivy.grad(func)
    if nth > 1:
        for _ in range(1, nth):
            fn = ivy.grad(fn)
    grad = fn(var)
    grad_np = helpers.flatten_and_to_np(ret=grad)
    ivy.previous_backend()
    ivy.set_backend("tensorflow")
    var = _variable(ivy.array(x, dtype=dtype))
    fn = ivy.grad(func)
    if nth > 1:
        for _ in range(1, nth):
            fn = ivy.grad(fn)

    grad_gt = fn(var)
    grad_np_from_gt = helpers.flatten_and_to_np(ret=grad_gt)
    for grad, grad_from_gt in zip(grad_np, grad_np_from_gt):
        assert grad.shape == grad_from_gt.shape
        assert np.allclose(grad, grad_from_gt)


# adam_step
@handle_test(
    fn_tree="functional.ivy.adam_step",
    dtype_n_dcdw_n_mw_n_vw=get_gradient_arguments_with_lr(
        num_arrays=3,
        no_lr=True,
        min_value=1e-05,
        max_value=1e08,
        large_abs_safety_factor=2,
        small_abs_safety_factor=2,
    ),
    step=helpers.ints(min_value=1, max_value=3),
    beta1_n_beta2_n_epsilon=helpers.list_of_size(
        x=helpers.floats(min_value=1e-1, max_value=1),
        size=3,
    ),
)
def test_adam_step(
    *,
    dtype_n_dcdw_n_mw_n_vw,
    step,
    beta1_n_beta2_n_epsilon,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    input_dtypes, [dcdw, mw, vw] = dtype_n_dcdw_n_mw_n_vw
    (
        beta1,
        beta2,
        epsilon,
    ) = beta1_n_beta2_n_epsilon
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=input_dtypes,
        test_flags=test_flags,
        fw=backend_fw,
        fn_name=fn_name,
        on_device=on_device,
        rtol_=1e-1,
        atol_=1e-1,
        dcdw=dcdw,
        mw=mw,
        vw=vw,
        step=step,
        beta1=beta1,
        beta2=beta2,
        epsilon=epsilon,
    )


# optimizer_update
@handle_test(
    fn_tree="functional.ivy.optimizer_update",
    dtype_n_ws_n_effgrad_n_lr=get_gradient_arguments_with_lr(num_arrays=2),
    stop_gradients=st.booleans(),
)
def test_optimizer_update(
    *,
    dtype_n_ws_n_effgrad_n_lr,
    stop_gradients,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    input_dtypes, [w, effective_grad], lr = dtype_n_ws_n_effgrad_n_lr
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=input_dtypes,
        fw=backend_fw,
        test_flags=test_flags,
        fn_name=fn_name,
        on_device=on_device,
        rtol_=1e-2,
        atol_=1e-2,
        w=w,
        effective_grad=effective_grad,
        lr=lr,
        stop_gradients=stop_gradients,
    )


# gradient_descent_update
@handle_test(
    fn_tree="functional.ivy.gradient_descent_update",
    dtype_n_ws_n_dcdw_n_lr=get_gradient_arguments_with_lr(num_arrays=2),
    stop_gradients=st.booleans(),
)
def test_gradient_descent_update(
    *,
    dtype_n_ws_n_dcdw_n_lr,
    stop_gradients,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    input_dtypes, [w, dcdw], lr = dtype_n_ws_n_dcdw_n_lr
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=input_dtypes,
        test_flags=test_flags,
        fw=backend_fw,
        fn_name=fn_name,
        on_device=on_device,
        rtol_=1e-2,
        atol_=1e-2,
        w=w,
        dcdw=dcdw,
        lr=lr,
        stop_gradients=stop_gradients,
    )


# lars_update
@handle_test(
    fn_tree="functional.ivy.lars_update",
    dtype_n_ws_n_dcdw_n_lr=get_gradient_arguments_with_lr(
        num_arrays=2,
    ),
    decay_lambda=helpers.floats(min_value=1e-2, max_value=1),
    stop_gradients=st.booleans(),
)
def test_lars_update(
    *,
    dtype_n_ws_n_dcdw_n_lr,
    decay_lambda,
    stop_gradients,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    input_dtypes, [w, dcdw], lr = dtype_n_ws_n_dcdw_n_lr
    # ToDo: Add testing for bfloat16 back when it returns consistent gradients for jax
    if "bfloat16" in input_dtypes:
        return
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=input_dtypes,
        test_flags=test_flags,
        fw=backend_fw,
        fn_name=fn_name,
        on_device=on_device,
        rtol_=1e-1,
        atol_=1e-1,
        w=w,
        dcdw=dcdw,
        lr=lr,
        decay_lambda=decay_lambda,
        stop_gradients=stop_gradients,
    )


# adam_update
@handle_test(
    fn_tree="functional.ivy.adam_update",
    dtype_n_ws_n_dcdw_n_mwtm1_n_vwtm1_n_lr=get_gradient_arguments_with_lr(
        num_arrays=4,
        min_value=1e-05,
        max_value=1e08,
        large_abs_safety_factor=2.0,
        small_abs_safety_factor=2.0,
    ),
    step=st.integers(min_value=1, max_value=10),
    beta1_n_beta2_n_epsilon=helpers.list_of_size(
        x=helpers.floats(min_value=1e-2, max_value=1),
        size=3,
    ),
    stopgrad=st.booleans(),
)
def test_adam_update(
    *,
    dtype_n_ws_n_dcdw_n_mwtm1_n_vwtm1_n_lr,
    step,
    beta1_n_beta2_n_epsilon,
    stopgrad,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    input_dtypes, [w, dcdw, mw_tm1, vw_tm1], lr = dtype_n_ws_n_dcdw_n_mwtm1_n_vwtm1_n_lr
    beta1, beta2, epsilon = beta1_n_beta2_n_epsilon
    stop_gradients = stopgrad
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=input_dtypes,
        test_flags=test_flags,
        fw=backend_fw,
        fn_name=fn_name,
        on_device=on_device,
        rtol_=1e-2,
        atol_=1e-2,
        w=w,
        dcdw=dcdw,
        lr=lr,
        mw_tm1=mw_tm1,
        vw_tm1=vw_tm1,
        step=step,
        beta1=beta1,
        beta2=beta2,
        epsilon=epsilon,
        stop_gradients=stop_gradients,
    )


# lamb_update
@handle_test(
    fn_tree="functional.ivy.lamb_update",
    dtype_n_ws_n_dcdw_n_mwtm1_n_vwtm1_n_lr=get_gradient_arguments_with_lr(
        min_value=-1e5,
        max_value=1e5,
        num_arrays=4,
    ),
    step=helpers.ints(min_value=1, max_value=100),
    beta1_n_beta2_n_epsilon_n_lambda=helpers.list_of_size(
        x=helpers.floats(
            min_value=1e-2,
            max_value=1.0,
        ),
        size=4,
    ),
    mtr=st.one_of(
        helpers.ints(min_value=1, max_value=10),
        st.floats(min_value=1e-2, max_value=10, exclude_min=True),
    ),
    stopgrad=st.booleans(),
)
def test_lamb_update(
    *,
    dtype_n_ws_n_dcdw_n_mwtm1_n_vwtm1_n_lr,
    step,
    beta1_n_beta2_n_epsilon_n_lambda,
    mtr,
    stopgrad,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    input_dtypes, [w, dcdw, mw_tm1, vw_tm1], lr = dtype_n_ws_n_dcdw_n_mwtm1_n_vwtm1_n_lr
    (
        beta1,
        beta2,
        epsilon,
        decay_lambda,
    ) = beta1_n_beta2_n_epsilon_n_lambda
    max_trust_ratio, stop_gradients = mtr, stopgrad
    # ToDo: enable gradient tests for jax once the issue with jacrev is resolved
    if "jax" in backend_fw.__name__:
        test_flags.test_gradients = False
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=input_dtypes,
        test_flags=test_flags,
        fw=backend_fw,
        fn_name=fn_name,
        on_device=on_device,
        rtol_=1e-1,
        atol_=1e-1,
        w=w,
        dcdw=dcdw,
        lr=lr,
        mw_tm1=mw_tm1,
        vw_tm1=vw_tm1,
        step=step,
        beta1=beta1,
        beta2=beta2,
        epsilon=epsilon,
        max_trust_ratio=max_trust_ratio,
        decay_lambda=decay_lambda,
        stop_gradients=stop_gradients,
    )
