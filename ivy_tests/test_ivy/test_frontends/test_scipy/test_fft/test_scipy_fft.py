# # TODO: uncomment after frontend is not required
# # global
# from hypothesis import strategies as st

# # local
# import ivy_tests.test_ivy.helpers as helpers
# from ivy_tests.test_ivy.helpers import handle_frontend_test


# ### Helpers ###

# @st.composite
# def x_and_fft(draw, dtypes):
#     min_fft_points = 2
#     dtype = draw(dtypes)
#     x_dim = draw(
#         helpers.get_shape(
#             min_dim_size=2, max_dim_size=100, min_num_dims=1, max_num_dims=4
#         )
#     )
#     x = draw(
#         helpers.array_values(
#             dtype=dtype[0],
#             shape=tuple(x_dim),
#         )
#     )
#     dim = draw(
#         helpers.get_axis(shape=x_dim, allow_neg=True, allow_none=False, max_size=1)
#     )
#     norm = draw(st.sampled_from(["backward", "forward", "ortho"]))
#     n = draw(st.integers(min_fft_points, 256))
#     return dtype, x, dim, norm, n


# @st.composite
# def x_and_ifft(draw):
#     min_fft_points = 2
#     dtype = draw(helpers.get_dtypes("complex"))
#     x_dim = draw(
#         helpers.get_shape(
#             min_dim_size=2, max_dim_size=100, min_num_dims=1, max_num_dims=4
#         )
#     )
#     x = draw(
#         helpers.array_values(
#             dtype=dtype[0],
#             shape=tuple(x_dim),
#             min_value=-1e-10,
#             max_value=1e10,
#         )
#     )
#     dim = draw(st.integers(1 - len(list(x_dim)), len(list(x_dim)) - 1))
#     norm = draw(st.sampled_from(["backward", "forward", "ortho"]))
#     n = draw(st.integers(min_fft_points, 256))
#     return dtype, x, dim, norm, n


# @st.composite
# def valid_dct(draw):
#     dtype, x = draw(
#         helpers.dtype_and_values(
#             available_dtypes=helpers.get_dtypes("numeric"),
#             max_value=65280,
#             min_value=-65280,
#             min_num_dims=1,
#             max_num_dims=5,
#             min_dim_size=2,
#             max_dim_size=10,
#             shared_dtype=True,
#         )
#     )
#     dims_len = len(x[0].shape)
#     n = draw(st.sampled_from([None, "int"]))
#     axis = draw(helpers.ints(min_value=-dims_len, max_value=dims_len))
#     norm = draw(st.sampled_from([None, "ortho"]))
#     type = draw(helpers.ints(min_value=1, max_value=4))
#     if n == "int":
#         n = draw(helpers.ints(min_value=1, max_value=20))
#         if n <= 1 and type == 1:
#             n = 2
#     if norm == "ortho" and type == 1:
#         norm = None
#     return dtype, x, type, n, axis, norm


# @st.composite
# def valid_idct(draw):
#     dtype, x = draw(
#         helpers.dtype_and_values(
#             available_dtypes=["float32", "float64"],
#             max_value=65280,
#             min_value=-65280,
#             min_num_dims=1,
#             max_num_dims=5,
#             min_dim_size=2,
#             max_dim_size=10,
#             shared_dtype=True,
#         )
#     )
#     n = None
#     axis = -1
#     norm = draw(st.sampled_from([None, "ortho"]))
#     type = draw(helpers.ints(min_value=1, max_value=4))
#     if norm == "ortho" and type == 1:
#         norm = None
#     return dtype, x, type, n, axis, norm


# ### Tests ###

# # fft
# @handle_frontend_test(
#     fn_tree="scipy.fft.fft",
#     d_x_d_n_n=x_and_fft(helpers.get_dtypes("complex")),
#     test_with_out=st.just(False),
# )
# def test_fft(
#     d_x_d_n_n,
#     frontend,
#     test_flags,
#     fn_tree,
#     on_device,
# ):
#     dtype, x, dim, norm, n = d_x_d_n_n
#     helpers.test_frontend_function(
#         input_dtypes=dtype,
#         frontend=frontend,
#         test_flags=test_flags,
#         fn_tree=fn_tree,
#         on_device=on_device,
#         x=x,
#         dim=dim,
#         norm=norm,
#         n=n,
#     )


# # ifft
# @handle_frontend_test(
#     fn_tree="scipy.fft.ifft",
#     d_x_d_n_n=x_and_ifft(),
#     test_with_out=st.just(False),
# )
# def test_ifft(
#     d_x_d_n_n,
#     frontend,
#     test_flags,
#     fn_tree,
#     on_device,
# ):
#     dtype, x, dim, norm, n = d_x_d_n_n
#     helpers.test_frontend_function(
#         input_dtypes=dtype,
#         frontend=frontend,
#         test_flags=test_flags,
#         fn_tree=fn_tree,
#         on_device=on_device,
#         x=x,
#         dim=dim,
#         norm=norm,
#         n=n,
#     )


# # dct
# @handle_frontend_test(
#     fn_tree="scipy.fft.dct",
#     dtype_x_and_args=valid_dct(),
#     test_with_out=st.just(False),
# )
# def test_dct(
#     dtype_x_and_args,
#     frontend,
#     test_flags,
#     fn_tree,
#     on_device,
# ):
#     input_dtype, x, _type, n, axis, norm = dtype_x_and_args
#     helpers.test_frontend_function(
#         input_dtypes=input_dtype,
#         frontend=frontend,
#         test_flags=test_flags,
#         fn_tree=fn_tree,
#         on_device=on_device,
#         x=x[0],
#         type=_type,
#         n=n,
#         axis=axis,
#         norm=norm,
#         rtol_=1e-3,
#         atol_=1e-1,
#     )


# # idct
# @handle_frontend_test(
#     fn_tree="scipy.fft.idct",
#     dtype_x_and_args=valid_idct(),
#     test_with_out=st.just(False),
# )
# def test_idct(
#     dtype_x_and_args,
#     frontend,
#     test_flags,
#     fn_tree,
#     on_device,
# ):
#     input_dtype, x, _type, n, axis, norm = dtype_x_and_args
#     helpers.test_frontend_function(
#         input_dtypes=input_dtype,
#         frontend=frontend,
#         test_flags=test_flags,
#         fn_tree=fn_tree,
#         on_device=on_device,
#         x=x[0],
#         type=_type,
#         n=n,
#         axis=axis,
#         norm=norm,
#         rtol_=1e-3,
#         atol_=1e-1,
#     )
