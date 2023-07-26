# global
import abc
from typing import Optional, Union, Tuple, Literal, Sequence, Callable

# local
import ivy


class _ArrayWithLayersExperimental(abc.ABC):
    def max_pool1d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int]],
        strides: Union[int, Tuple[int]],
        padding: str,
        /,
        *,
        data_format: str = "NWC",
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of `ivy.max_pool1d`. This method simply wraps
        the function, and so the docstring for `ivy.max_pool1d` also applies to this
        method with minimal changes.

        Parameters
        ----------
        self
            Input image *[batch_size,w,d_in]*.
        kernel
            The size of the window for each dimension of the input tensor.
        strides
            The stride of the sliding window for each dimension of input.
        padding
            "SAME" or "VALID" indicating the algorithm, or list indicating
            the per-dimension paddings.
        data_format
            "NWC" or "NCW". Defaults to "NWC".
        out
            optional output array, for writing the result to. It must have a shape that
            the inputs broadcast to.

        Returns
        -------
        ret
            The result of the max pooling operation.

        Examples
        --------
        >>> x = ivy.arange(0, 24.).reshape((2, 3, 4))
        >>> print(x.max_pool1d(2, 2, 'SAME'))
        ivy.array([[[ 4.,  5.,  6.,  7.],
                [ 8.,  9., 10., 11.]],
               [[16., 17., 18., 19.],
                [20., 21., 22., 23.]]])
        >>> x = ivy.arange(0, 24.).reshape((2, 3, 4))
        >>> print(x.max_pool1d(2, 2, 'VALID'))
        ivy.array([[[ 4.,  5.,  6.,  7.]],
           [[16., 17., 18., 19.]]])
        """
        return ivy.max_pool1d(
            self,
            kernel,
            strides,
            padding,
            data_format=data_format,
            out=out,
        )

    def max_pool2d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int], Tuple[int, int]],
        strides: Union[int, Tuple[int], Tuple[int, int]],
        padding: str,
        /,
        *,
        data_format: str = "NHWC",
        dilation: Union[int, Tuple[int], Tuple[int, int]] = 1,
        ceil_mode: bool = False,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of `ivy.max_pool2d`. This method simply wraps
        the function, and so the docstring for `ivy.max_pool2d` also applies to this
        method with minimal changes.

        Parameters
        ----------
        self
            Input image *[batch_size,h,w,d_in]*.
        kernel
            The size of the window for each dimension of the input tensor.
        strides
            The stride of the sliding window for each dimension of input.
        padding
            "SAME" or "VALID" indicating the algorithm, or list indicating
            the per-dimension paddings.
        data_format
            "NHWC" or "NCHW". Defaults to "NHWC".
        out
            optional output array, for writing the result to. It must have a shape that
            the inputs broadcast to.

        Returns
        -------
        ret
            The result of the max pooling operation.

        Examples
        --------
        >>> x = ivy.arange(12.).reshape((2, 1, 3, 2))
        >>> print(x.max_pool2d((2, 2), (1, 1), 'SAME'))
        ivy.array([[[[ 2,  3],
                 [ 4,  5],
                 [ 4,  5]]],
               [[[ 8,  9],
                 [10, 11],
                 [10, 11]]]])

        >>> x = ivy.arange(48.).reshape((2, 4, 3, 2))
        >>> print(x.max_pool2d(3, 1, 'VALID'))
        ivy.array([[[[16, 17]],
                [[22, 23]]],
               [[[40, 41]],
                [[46, 47]]]])
        """
        return ivy.max_pool2d(
            self,
            kernel,
            strides,
            padding,
            data_format=data_format,
            dilation=dilation,
            ceil_mode=ceil_mode,
            out=out,
        )

    def max_pool3d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int], Tuple[int, int, int]],
        strides: Union[int, Tuple[int], Tuple[int, int, int]],
        padding: str,
        /,
        *,
        data_format: str = "NDHWC",
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        Compute a 3-D max pool given 5-D input x.

        Parameters
        ----------
        self
            Input volume *[batch_size,d,h,w,d_in]*.
        kernel
            Convolution filters *[d,h,w]*.
        strides
            The stride of the sliding window for each dimension of input.
        padding
            SAME" or "VALID" indicating the algorithm, or list indicating
            the per-dimension paddings.
        data_format
            NDHWC" or "NCDHW". Defaults to "NDHWC".
        out
            optional output array, for writing the result to. It must have
            a shape that the inputs broadcast to.

        Returns
        -------
        ret
            The result of the pooling operation.

        Examples
        --------
        >>> x = ivy.arange(48.).reshape((2, 3, 2, 2, 2))
        >>> print(x.max_pool3d(2, 2, 'VALID'))
        ivy.array([[[[[14., 15.]]]],
           [[[[38., 39.]]]]])
        >>> print(x.max_pool3d(2, 2, 'SAME'))
        ivy.array([[[[[14., 15.]]],
            [[[22., 23.]]]],
           [[[[38., 39.]]],
            [[[46., 47.]]]]])
        """
        return ivy.max_pool3d(
            self,
            kernel,
            strides,
            padding,
            data_format=data_format,
            out=out,
        )

    def avg_pool1d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int]],
        strides: Union[int, Tuple[int]],
        padding: str,
        /,
        *,
        data_format: str = "NWC",
        count_include_pad: bool = False,
        ceil_mode: bool = False,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of `ivy.avg_pool1d`. This method simply wraps
        the function, and so the docstring for `ivy.avg_pool1d` also applies to this
        method with minimal changes.

        Parameters
        ----------
        self
            Input image *[batch_size,w,d_in]*.
        kernel
            The size of the window for each dimension of the input tensor.
        strides
            The stride of the sliding window for each dimension of input.
        padding
            "SAME" or "VALID" indicating the algorithm, or list indicating
            the per-dimension paddings.
        data_format
            "NWC" or "NCW". Defaults to "NWC".
        count_include_pad
            Whether to include padding in the averaging calculation.
        ceil_mode
            Whether to use ceil or floor for creating the output shape.
        out
            optional output array, for writing the result to. It must have a shape that
            the inputs broadcast to.

        Returns
        -------
        ret
            The result of the max pooling operation.

        Examples
        --------
        >>> x = ivy.arange(0, 24.).reshape((2, 3, 4))
        >>> print(x.avg_pool1d(2, 2, 'SAME'))
        ivy.array([[[ 2.,  3.,  4.,  5.],
                [ 8.,  9., 10., 11.]],
               [[14., 15., 16., 17.],
                [20., 21., 22., 23.]]])

        >>> x = ivy.arange(0, 24.).reshape((2, 3, 4))
        >>> print(x.avg_pool1d(2, 2, 'VALID'))
        ivy.array([[[ 2.,  3.,  4.,  5.]],
               [[14., 15., 16., 17.]]])
        """
        return ivy.avg_pool1d(
            self,
            kernel,
            strides,
            padding,
            data_format=data_format,
            count_include_pad=count_include_pad,
            ceil_mode=ceil_mode,
            out=out,
        )

    def avg_pool2d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int], Tuple[int, int]],
        strides: Union[int, Tuple[int], Tuple[int, int]],
        padding: str,
        /,
        *,
        data_format: str = "NHWC",
        count_include_pad: bool = False,
        ceil_mode: bool = False,
        divisor_override: Optional[int] = None,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of `ivy.avg_pool2d`. This method simply wraps
        the function, and so the docstring for `ivy.avg_pool2d` also applies to this
        method with minimal changes.

        Parameters
        ----------
        x
            Input image *[batch_size,h,w,d_in]*.
        kernel
            The size of the window for each dimension of the input tensor.
        strides
            The stride of the sliding window for each dimension of input.
        padding
            "SAME" or "VALID" indicating the algorithm, or list indicating
            the per-dimension paddings.
        data_format
            "NHWC" or "NCHW". Defaults to "NHWC".
        count_include_pad
            Whether to include padding in the averaging calculation.
        ceil_mode
            Whether to use ceil or floor for creating the output shape.
        divisor_override
            If given, it will be used as the divisor,
            otherwise kernel_size will be used.
        out
            optional output array, for writing the result to. It must have a shape that
            the inputs broadcast to.

        Returns
        -------
        ret
            The result of the max pooling operation.

        Examples
        --------
        >>> x = ivy.arange(12.).reshape((2, 1, 3, 2))
        >>> print(x.max_pool2d((2, 2), (1, 1), 'SAME'))
        ivy.array([[[[ 2,  3],
        [ 4,  5],
        [ 4,  5]]],
        [[[ 8,  9],
        [10, 11],
        [10, 11]]]])

        >>> x = ivy.arange(48.).reshape((2, 4, 3, 2))
        >>> print(x.max_pool2d(3, 1, 'VALID'))
        ivy.array([[[[16, 17]],
        [[22, 23]]],
        [[[40, 41]],
        [[46, 47]]]])
        """
        return ivy.avg_pool2d(
            self,
            kernel,
            strides,
            padding,
            data_format=data_format,
            count_include_pad=count_include_pad,
            ceil_mode=ceil_mode,
            divisor_override=divisor_override,
            out=out,
        )

    def avg_pool3d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int], Tuple[int, int, int]],
        strides: Union[int, Tuple[int], Tuple[int, int, int]],
        padding: str,
        /,
        *,
        data_format: str = "NDHWC",
        count_include_pad: bool = False,
        ceil_mode: bool = False,
        divisor_override: Optional[int] = None,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        Compute a 3-D max pool given 5-D input x.

        Parameters
        ----------
        self
            Input volume *[batch_size,d,h,w,d_in]*.
        kernel
            Convolution filters *[d,h,w]*.
        strides
            The stride of the sliding window for each dimension of input.
        padding
            SAME" or "VALID" indicating the algorithm, or list indicating
            the per-dimension paddings.
        data_format
            NDHWC" or "NCDHW". Defaults to "NDHWC".
        count_include_pad
            Whether to include padding in the averaging calculation.
        ceil_mode
            Whether to use ceil or floor for creating the output shape.
        divisor_override
            If specified, it will be used as divisor,
            otherwise kernel_size will be used.
        out
            optional output array, for writing the result to. It must have
            a shape that the inputs broadcast to.

        Returns
        -------
        ret
            The result of the pooling operation.

        Examples
        --------
        >>> x = ivy.arange(48.).reshape((2, 3, 2, 2, 2))
        >>> print(x.avg_pool3d(2, 2, 'VALID'))
        ivy.array([[[[[ 7.,  8.]]]],
               [[[[31., 32.]]]]])
        >>> print(x.avg_pool3d(2, 2, 'SAME'))
        ivy.array([[[[[ 7.,  8.]]],
                [[[19., 20.]]]],
               [[[[31., 32.]]],
                [[[43., 44.]]]]])
        """
        return ivy.avg_pool3d(
            self,
            kernel,
            strides,
            padding,
            data_format=data_format,
            count_include_pad=count_include_pad,
            ceil_mode=ceil_mode,
            divisor_override=divisor_override,
            out=out,
        )

    def dct(
        self: ivy.Array,
        /,
        *,
        type: Literal[1, 2, 3, 4] = 2,
        n: Optional[int] = None,
        axis: int = -1,
        norm: Optional[Literal["ortho"]] = None,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.dct. This method simply wraps the
        function, and so the docstring for ivy.dct also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            The input signal.
        type
            The type of the dct. Must be 1, 2, 3 or 4.
        n
            The lenght of the transform. If n is less than the input signal lenght,
            then x is truncated, if n is larger than x is zero-padded.
        norm
            The type of normalization to be applied. Must be either None or "ortho".
        out
            optional output array, for writing the result to.

        Returns
        -------
        ret
            Array containing the transformed input.

        Examples
        --------
        >>> x = ivy.array([8., 16., 24., 32., 40., 48., 56., 64.])
        >>> x.dct(type=2, norm="ortho")
        ivy.array([ 102.,  -51.5,   0.,  -5.39,   0.,  -1.61,   0., -0.406])
        """
        return ivy.dct(
            self._data,
            type=type,
            n=n,
            axis=axis,
            norm=norm,
            out=out,
        )

    def idct(
        self: ivy.Array,
        /,
        *,
        type: Literal[1, 2, 3, 4] = 2,
        n: Optional[int] = None,
        axis: int = -1,
        norm: Optional[Literal["ortho"]] = None,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.idct. This method simply wraps the
        function, and so the docstring for ivy.idct also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            The input signal.
        type
            The type of the idct. Must be 1, 2, 3 or 4.
        n
            The length of the transform. If n is less than the input signal length,
            then x is truncated, if n is larger than x is zero-padded.
        norm
            The type of normalization to be applied. Must be either None or "ortho".
        out
            optional output array, for writing the result to.

        Returns
        -------
        ret
            Array containing the transformed input.

        Examples
        --------
        >>> x = ivy.array([8., 16., 24., 32., 40., 48., 56., 64.])
        >>> x.idct(type=2, norm="ortho")
        ivy.array([ 79.49862671, -70.37691498,  30.00390816, -23.58938599,
            13.92713165, -10.078475  ,   5.19664812,  -1.95411837])
        """
        return ivy.idct(
            self._data,
            type=type,
            n=n,
            axis=axis,
            norm=norm,
            out=out,
        )

    def fft(
        self: ivy.Array,
        dim: int,
        /,
        *,
        norm: str = "backward",
        n: Optional[Union[int, Tuple[int]]] = None,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.ifft. This method simply wraps the
        function, and so the docstring for ivy.ifft also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            Input volume *[...,d_in,...]*,
            where d_in indicates the dimension that needs FFT.
        dim
            The dimension along which to take the one dimensional FFT.
        norm
            Optional argument, "backward", "ortho" or "forward". Defaults to be
            "backward".
            "backward" indicates no normalization.
            "ortho" indicates normalization by 1/sqrt(n).
            "forward" indicates normalization by 1/n.
        n
            Optional argument indicating the sequence length, if given, the input
            would be padded with zero or truncated to length n before performing FFT.
            Should be a integer greater than 1.
        out
            Optional output array, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            Array containing the transformed input.

        Examples
        --------
        >>> a = ivy.array((np.exp(2j * np.pi * np.arange(8) / 8)))
        >>> a.fft(0)
        ivy.array([-3.44509285e-16+1.14423775e-17j,  8.00000000e+00-8.11483250e-16j,
                    2.33486982e-16+1.22464680e-16j,  0.00000000e+00+1.22464680e-16j,
                    9.95799250e-17+2.33486982e-16j,  0.00000000e+00+7.66951701e-17j,
                    1.14423775e-17+1.22464680e-16j,  0.00000000e+00+1.22464680e-16j])
        """
        return ivy.fft(
            self._data,
            dim,
            norm=norm,
            n=n,
            out=out,
        )

    def ifft(
        self: ivy.Array,
        dim: int,
        *,
        norm: str = "backward",
        n: Optional[Union[int, Tuple[int]]] = None,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.ifft. This method simply wraps the
        function, and so the docstring for ivy.ifft also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            Input volume *[...,d_in,...]*,
            where d_in indicates the dimension that needs IFFT.
        dim
            The dimension along which to take the one dimensional IFFT.
        norm
            Optional argument, "backward", "ortho" or "forward". Defaults to be
            "backward".
            "backward" indicates no normalization.
            "ortho" indicates normalization by 1/sqrt(n).
            "forward" indicates normalization by 1/n.
        n
            Optional argument indicating the sequence length, if given, the input
            would be padded with zero or truncated to length n before performing IFFT.
            Should be a integer greater than 1.
        out
            Optional output array, for writing the result to. It must have a shape that
            the inputs broadcast to.

        Returns
        -------
        ret
            Array containing the transformed input.

        Examples
        --------
        >>> a = ivy.array((np.exp(2j * np.pi * np.arange(8) / 8)))
        >>> a.ifft(0)
        ivy.array([-4.30636606e-17+1.43029718e-18j,  0.00000000e+00+1.53080850e-17j,
                    1.43029718e-18+1.53080850e-17j,  0.00000000e+00+9.58689626e-18j,
                    1.24474906e-17+2.91858728e-17j,  0.00000000e+00+1.53080850e-17j,
                    2.91858728e-17+1.53080850e-17j,  1.00000000e+00-1.01435406e-16j])
        """
        return ivy.ifft(
            self._data,
            dim,
            norm=norm,
            n=n,
            out=out,
        )

    def embedding(
        self: ivy.Array,
        indices: ivy.Array,
        /,
        *,
        max_norm: Optional[int] = None,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        return ivy.embedding(self._data, indices, max_norm=max_norm, out=out)

    def dft(
        self,
        /,
        *,
        axis: int = 1,
        inverse: bool = False,
        onesided: bool = False,
        dft_length: Optional[Union[int, Tuple[int]]] = None,
        norm: str = "backward",
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        Compute the discrete Fourier transform of input.

        Parameters
        ----------
        self
            Input volume *[...,d_in,...]*,
            where d_in indicates the dimension that needs FFT.
        axis
            The axis on which to perform the DFT. By default this
            value is  set to 1, which corresponds to the first dimension
            after the batch index.
        inverse
            Whether to perform the inverse discrete fourier transform.
            By default this value is set to False.
        onesided
            If onesided is True, only values for w in [0, 1, 2, …, floor(n_fft/2) + 1]
            are returned because the real-to-complex Fourier transform satisfies the
            conjugate symmetry, i.e., X[m, w] = X[m,w]=X[m,n_fft-w]*. Note if the
            input or window tensors are complex, then onesided output is not possible.
            Enabling onesided with real inputs performs a Real-valued fast Fourier
            transform (RFFT). When invoked with real or complex valued input, the
            default value is False. Values can be True or False.
        dft_length
            The length of the signal.If greater than the axis dimension,
            the signal will be zero-padded up to dft_length. If less than
            the axis dimension, only the first dft_length values will be
            used as the signal. It’s an optional value.
        norm
            Optional argument, "backward", "ortho" or "forward". Defaults to be
            "backward".
            "backward" indicates no normalization.
            "ortho" indicates normalization by 1/sqrt(n).
            "forward" indicates normalization by 1/n.
        out
            Optional output array, for writing the result to. It must
            have a shape that the inputs broadcast to.

        Returns
        -------
        ret
            The Fourier Transform of the input vector.If onesided is False,
            the following shape is expected: [batch_idx][signal_dim1][signal_dim2]
            …[signal_dimN][2]. If axis=0 and onesided is True, the following shape
            is expected: [batch_idx][floor(signal_dim1/2)+1][signal_dim2]
            …[signal_dimN][2]. If axis=1 and onesided is True, the following
            shape is expected: [batch_idx][signal_dim1] [floor(signal_dim2/2)+1]
            …[signal_dimN][2]. If axis=N-1 and onesided is True, the following
            shape is expected: [batch_idx][signal_dim1][signal_dim2]…
            [floor(signal_dimN/2)+1][2]. The signal_dim at the specified axis
            is equal to the dft_length.
        """
        return ivy.dft(
            self._data,
            axis=axis,
            inverse=inverse,
            onesided=onesided,
            dft_length=dft_length,
            norm=norm,
            out=out,
        )

    def interpolate(
        self,
        size: Union[Sequence[int], int],
        /,
        *,
        mode: Union[
            Literal[
                "linear",
                "bilinear",
                "trilinear",
                "nearest",
                "area",
                "nearest_exact",
                "tf_area",
                "bicubic",
            ]
        ] = "linear",
        scale_factor: Optional[Union[Sequence[int], int]] = None,
        recompute_scale_factor: Optional[bool] = None,
        align_corners: Optional[bool] = None,
        antialias: bool = False,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        Down/up samples the input to the given size. The algorithm used for
        interpolation is determined by mode.

        Parameters
        ----------
        self
            Input array, Must have the shape
            [batch x channels x [optional depth] x [optional height] x width].
        size
            Output size.
        mode
            Interpolation mode. Can be one of the following:
            - linear
            - bilinear
            - trilinear
            - nearest
            - area
            - tf_area
            - bicubic
            - mitchellcubic
            - lanczos3
            - lanczos5
            - gaussian
        scale_factor
            Multiplier for spatial size that defines the output size
            (overwriting `size`).
        align_corners
            If True, the corner pixels of the input and output tensors are aligned,
            and thus preserving the values at the corner pixels. If False, the corner
            pixels are not aligned, and the interpolation uses edge value padding for
            out-of-boundary values.
            only has an effect when mode is 'linear', 'bilinear',
            'bicubic' or 'trilinear'. Default: False
        antialias
            If True, antialiasing is applied when downsampling an image.
            Supported modes: 'bilinear', 'bicubic'.
        out
            Optional output array, for writing the result to. It must
            have a shape that the inputs broadcast to.

        Returns
        -------
            resized array
        """
        return ivy.interpolate(
            self._data,
            size,
            mode=mode,
            scale_factor=scale_factor,
            recompute_scale_factor=recompute_scale_factor,
            align_corners=align_corners,
            antialias=antialias,
            out=out,
        )

    def adaptive_avg_pool1d(
        self: ivy.Array,
        output_size: int,
    ) -> ivy.Array:
        """
        Apply a 1D adaptive average pooling over an input signal composed of several
        input planes.

        Parameters
        ----------
        self
            Input array. Must have shape (N, C, L_in) or (C, L_in) where N is
            the batch dimension, C is the feature dimension, and L_in is the spatial
            dimension.
        output_size
            Spatial output size.

        Returns
        -------
            The result of the pooling operation. Will have shape (N, C, L_out) or
            (C, L_out), where L_out = `output_size`
        """
        return ivy.adaptive_avg_pool1d(
            self._data,
            output_size,
        )

    def adaptive_avg_pool2d(
        self: ivy.Array,
        output_size: Union[Sequence[int], int],
    ) -> ivy.Array:
        """
        Apply a 2D adaptive average pooling over an input signal composed of several
        input planes.

        Parameters
        ----------
        self
            Input array. Must have shape (N, C, H_in, W_in) or (C, H_in, W_in) where N
            is the batch dimension, C is the feature dimension, and H_in and W_in are
            the 2 spatial dimensions.
        output_size
            Spatial output size.

        Returns
        -------
            The result of the pooling operation. Will have shape (N, C, S_0, S_1) or
            (C, S_0, S_1), where S = `output_size`
        """
        return ivy.adaptive_avg_pool2d(
            self._data,
            output_size,
        )

    def reduce_window(
        self: ivy.Array,
        init_value: Union[int, float],
        computation: Callable,
        window_dimensions: Union[int, Sequence[int]],
        /,
        *,
        window_strides: Union[int, Sequence[int]] = 1,
        padding: Union[str, int, Sequence[Tuple[int, int]]] = "VALID",
        base_dilation: Union[int, Sequence[int]] = 1,
        window_dilation: Union[int, Sequence[int]] = 1,
    ) -> ivy.Array:
        """
        Apply a reduction function to all elements in each window of an array.

        Parameters
        ----------
        self
            An array representing the base area on which the window is going to slide
            over.
        init_value
            The starting value for the reduction.
        computation
            The reduction function to apply to elements in each window.
        window_dimensions
            A sequence containing the window dimensions.
        window_strides
            A sequence containing the window strides.
        padding
            Either the string ‘SAME’ (padding with zeros evenly), the string ‘VALID’ (no
            padding), or a sequence of n (low, high) integer pairs that give the padding
            to apply before and after each spatial dimension.
        base_dilation
            A sequence containing the base dilation values.
        window_dilation
            A sequence containing the window dilation values.

        Returns
        -------
        ret
            The result of the pooling-like operation.

        Examples
        --------
        >>> x = ivy.array([[1, 2, 3, 4],
        >>>                [5, 6, 7, 8],
        >>>                [9, 10, 11, 12]])
        >>> x.reduce_window(0, ivy.sum, (2, 2))
        ivy.array([[32.]])
        """
        return ivy.reduce_window(
            self._data,
            init_value,
            computation,
            window_dimensions,
            window_strides=window_strides,
            padding=padding,
            base_dilation=base_dilation,
            window_dilation=window_dilation,
        )

    def fft2(
        self: ivy.Array,
        *,
        s: Sequence[int] = None,
        dim: Sequence[int] = (-2, -1),
        norm: str = "backward",
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        Compute the 2-dimensional discrete Fourier Transform.

        Parameters
        ----------
        x
            Input volume *[...,d_in,...]*,
            where d_in indicates the dimension that needs FFT2.
        s
            sequence of ints, optional
            Shape (length of each transformed axis) of the output (s[0] refers
            to axis 0, s[1] to axis 1, etc.). This corresponds to n for fft(x, n).
            Along each axis, if the given shape is smaller than that of the input,
            the input is cropped. If it is larger, the input is padded with zeros.
            If s is not given, the shape of the input along the axes specified by
            axes is used.
        dim
            Axes over which to compute the FFT2. If not given, the last two axes are
            used. A repeated index in axes means the transform over that axis is
            performed multiple times. A one-element sequence means that a
            one-dimensional FFT is performed.
        norm
            Optional argument, "backward", "ortho" or "forward". Defaults to be
            "backward".
            "backward" indicates no normalization.
            "ortho" indicates normalization by 1/sqrt(n).
            "forward" indicates normalization by 1/n.
        out
            Optional output array, for writing the result to. It must have a shape that
            the inputs broadcast to.

        Returns
        -------
        ret
            The result of the FFT2 operation.

        Examples
        --------
        >>> a = ivy.array([[0, 0, 0, 0, 0],
                        [1, 1, 1, 1, 1],
                        [2, 2, 2, 2, 2],
                        [3, 3, 3, 3, 3],
                        [4, 4, 4, 4, 4]])
        >>> ivy.fft2(a)
        array([[ 50.  +0.j        ,   0.  +0.j        ,   0.  +0.j        , # may vary
                0.  +0.j        ,   0.  +0.j        ],
            [-12.5+17.20477401j,   0.  +0.j        ,   0.  +0.j        ,
                0.  +0.j        ,   0.  +0.j        ],
            [-12.5 +4.0614962j ,   0.  +0.j        ,   0.  +0.j        ,
                0.  +0.j        ,   0.  +0.j        ],
            [-12.5 -4.0614962j ,   0.  +0.j        ,   0.  +0.j        ,
                0.  +0.j        ,   0.  +0.j        ],
            [-12.5-17.20477401j,   0.  +0.j        ,   0.  +0.j        ,
                0.  +0.j        ,   0.  +0.j        ]])
        """
        return ivy.fft2(self._data, s=s, dim=dim, norm=norm, out=out)
