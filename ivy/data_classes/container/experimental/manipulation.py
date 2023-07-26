# global
from typing import (
    Optional,
    Union,
    List,
    Dict,
    Sequence,
    Tuple,
    Literal,
    Any,
    Callable,
    Iterable,
)
from numbers import Number

# local
import ivy
from ivy.data_classes.container.base import ContainerBase


class _ContainerWithManipulationExperimental(ContainerBase):
    @staticmethod
    def static_moveaxis(
        a: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        source: Union[int, Sequence[int]],
        destination: Union[int, Sequence[int]],
        /,
        *,
        copy: Optional[bool] = None,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.moveaxis. This method simply wraps
        the function, and so the docstring for ivy.moveaxis also applies to this method
        with minimal changes.

        Parameters
        ----------
        a
            The container with the arrays whose axes should be reordered.
        source
            Original positions of the axes to move. These must be unique.
        destination
            Destination positions for each of the original axes.
            These must also be unique.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        out
            optional output container, for writing the result to.

        Returns
        -------
        ret
            Container including arrays with moved axes.

        Examples
        --------
        With one :class:`ivy.Container` input:
        >>> x = ivy.Container(a=ivy.zeros((3, 4, 5)), b=ivy.zeros((2,7,6)))
        >>> ivy.Container.static_moveaxis(x, 0, -1).shape
        {
            a: (4, 5, 3)
            b: (7, 6, 2)
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "moveaxis",
            a,
            source,
            destination,
            copy=copy,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def moveaxis(
        self: ivy.Container,
        source: Union[int, Sequence[int]],
        destination: Union[int, Sequence[int]],
        /,
        *,
        copy: Optional[bool] = None,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.moveaxis. This method simply wraps
        the function, and so the docstring for ivy.flatten also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            The container with the arrays whose axes should be reordered.
        source
            Original positions of the axes to move. These must be unique.
        destination
            Destination positions for each of the original axes.
            These must also be unique.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        out
            optional output container, for writing the result to.

        Returns
        -------
        ret
            Container including arrays with moved axes.

        Examples
        --------
        With one :class:`ivy.Container` input:
        >>> x = ivy.Container(a=ivy.zeros((3, 4, 5)), b=ivy.zeros((2,7,6)))
        >>> x.moveaxis(, 0, -1).shape
        {
            a: (4, 5, 3)
            b: (7, 6, 2)
        }
        """
        return self.static_moveaxis(self, source, destination, copy=copy, out=out)

    @staticmethod
    def static_heaviside(
        x1: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        x2: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        /,
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.heaviside. This method simply wraps
        the function, and so the docstring for ivy.heaviside also applies to this method
        with minimal changes.

        Parameters
        ----------
        x1
            input container including the arrays.
        x2
            values to use where the array is zero.
        out
            optional output container array, for writing the result to.

        Returns
        -------
        ret
            output container with element-wise Heaviside step function of each array.

        Examples
        --------
        With :class:`ivy.Array` input:
        >>> x1 = ivy.Container(a=ivy.array([-1.5, 0, 2.0]), b=ivy.array([3.0, 5.0])
        >>> x2 = ivy.Container(a=0.5, b=[1.0, 2.0])
        >>> ivy.Container.static_heaviside(x1, x2)
        {
            a: ivy.array([ 0. ,  0.5,  1. ])
            b: ivy.array([1.0, 1.0])
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "heaviside",
            x1,
            x2,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def heaviside(
        self: ivy.Container,
        x2: ivy.Container,
        /,
        *,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.heaviside. This method simply wraps
        the function, and so the docstring for ivy.heaviside also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            input container including the arrays.
        x2
            values to use where the array is zero.
        out
            optional output container array, for writing the result to.

        Returns
        -------
        ret
            output container with element-wise Heaviside step function of each array.

        Examples
        --------
        With :class:`ivy.Array` input:
        >>> x1 = ivy.Container(a=ivy.array([-1.5, 0, 2.0]), b=ivy.array([3.0, 5.0])
        >>> x2 = ivy.Container(a=0.5, b=[1.0, 2.0])
        >>> x1.heaviside(x2)
        {
            a: ivy.array([ 0. ,  0.5,  1. ])
            b: ivy.array([1.0, 1.0])
        }
        """
        return self.static_heaviside(self, x2, out=out)

    @staticmethod
    def static_flipud(
        m: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        /,
        *,
        copy: Optional[bool] = None,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.flipud. This method simply wraps the
        function, and so the docstring for ivy.flipud also applies to this method with
        minimal changes.

        Parameters
        ----------
        m
            the container with arrays to be flipped.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        out
            optional output container, for writing the result to.

        Returns
        -------
        ret
            container including arrays corresponding to the input container's array
            with elements order reversed along axis 0.

        Examples
        --------
        With one :class:`ivy.Container` input:

        >>> m = ivy.Container(a=ivy.diag([1, 2, 3]), b=ivy.arange(4))
        >>> ivy.Container.static_flipud(m)
        {
            a: ivy.array(
                [[ 0.,  0.,  3.],
                 [ 0.,  2.,  0.],
                 [ 1.,  0.,  0.]]
            )
            b: ivy.array([3, 2, 1, 0])
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "flipud",
            m,
            copy=copy,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def flipud(
        self: ivy.Container,
        /,
        *,
        copy: Optional[bool] = None,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.flipud. This method simply wraps
        the function, and so the docstring for ivy.flipud also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            the container with arrays to be flipped.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        out
            optional output container, for writing the result to.

        Returns
        -------
        ret
            container including arrays corresponding to the input container's array
            with elements order reversed along axis 0.

        Examples
        --------
        With one :class:`ivy.Container` input:

        >>> m = ivy.Container(a=ivy.diag([1, 2, 3]), b=ivy.arange(4))
        >>> m.flipud()
        {
            a: ivy.array(
                [[ 0.,  0.,  3.],
                 [ 0.,  2.,  0.],
                 [ 1.,  0.,  0.]]
            )
            b: ivy.array([3, 2, 1, 0])
        }
        """
        return self.static_flipud(self, copy=copy, out=out)

    def vstack(
        self: ivy.Container,
        /,
        xs: Union[
            Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
            List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        ],
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.stack. This method simply wraps the
        function, and so the docstring for ivy.stack also applies to this method with
        minimal changes.

        Examples
        --------
        >>> x = ivy.Container(a=ivy.array([[0, 1], [2,3]]), b=ivy.array([[4, 5]]))
        >>> y = ivy.Container(a=ivy.array([[3, 2], [1,0]]), b=ivy.array([[1, 0]]))
        >>> x.vstack([y])
        {
            a: ivy.array([[[0, 1],
                        [2, 3]],
                        [[3, 2],
                        [1, 0]]]),
            b: ivy.array([[[4, 5]],
                        [[1, 0]]])
        }
        """
        new_xs = xs.cont_copy() if ivy.is_ivy_container(xs) else xs.copy()
        new_xs.insert(0, self.cont_copy())
        return self.static_vstack(
            new_xs,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    @staticmethod
    def static_vstack(
        xs: Union[
            Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
            List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        ],
        /,
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.stack. This method simply wraps the
        function, and so the docstring for ivy.vstack also applies to this method with
        minimal changes.

        Examples
        --------
        With one :class:`ivy.Container` input:

        >>> c = ivy.Container(a=[ivy.array([1,2,3]), ivy.array([0,0,0])],
                              b=ivy.arange(3))
        >>> y = ivy.Container.static_vstack(c)
        >>> print(y)
        {
            a: ivy.array([[1, 2, 3],
                          [0, 0, 0]]),
            b: ivy.array([[0],
                          [1],
                          [2]])
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "vstack",
            xs,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def hstack(
        self: ivy.Container,
        /,
        xs: Union[
            Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
            List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        ],
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.hstack. This method simply wraps
        the function, and so the docstring for ivy.hstack also applies to this method
        with minimal changes.

        Examples
        --------
        >>> x = ivy.Container(a=ivy.array([[0, 1], [2,3]]), b=ivy.array([[4, 5]]))
        >>> y = ivy.Container(a=ivy.array([[3, 2], [1,0]]), b=ivy.array([[1, 0]]))
        >>> z = x.hstack([y])
        >>> print(z)
        {
            a: ivy.array([[0, 1, 3, 2],
                          [2, 3, 1, 0]]),
            b: ivy.array([[4, 5, 1, 0]])
        }
        """
        new_xs = xs.cont_copy() if ivy.is_ivy_container(xs) else xs.copy()
        new_xs.insert(0, self.cont_copy())
        return self.static_hstack(
            new_xs,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    @staticmethod
    def static_hstack(
        xs: Union[
            Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
            List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        ],
        /,
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.hstack. This method simply wraps the
        function, and so the docstring for ivy.hstack also applies to this method with
        minimal changes.

        Examples
        --------
        With one :class:`ivy.Container` input:
        >>> c = ivy.Container(a=[ivy.array([1,2,3]), ivy.array([0,0,0])])
        >>> ivy.Container.static_hstack(c)
        {
            a: ivy.array([1, 2, 3, 0, 0, 0])
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "hstack",
            xs,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    @staticmethod
    def static_rot90(
        m: Union[ivy.Container, ivy.Array, ivy.NativeArray],
        /,
        *,
        copy: bool = None,
        k: int = 1,
        axes: Tuple[int, int] = (0, 1),
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.rot90. This method simply wraps the
        function, and so the docstring for ivy.rot90 also applies to this method with
        minimal changes.

        Parameters
        ----------
        m
            Input array of two or more dimensions.
        k
            Number of times the array is rotated by 90 degrees.
        axes
            The array is rotated in the plane defined by the axes. Axes must be
            different.
        key_chains
            The key-chains to apply or not apply the method to. Default is None.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is True.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is False.
        map_sequences
            Whether to also map method to sequences (lists, tuples). Default is False.
        out
            optional output container, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            Container with a rotated view of m.
            
        Examples
        --------
        >>> m = ivy.Container(a=ivy.array([[1,2], [3,4]]),\
                        b=ivy.array([[1,2,3,4],\
                                    [7,8,9,10]]))
        >>> n = ivy.Container.static_rot90(m)
        >>> print(n)
        {
            a: ivy.array([[2, 4],
                          [1, 3]]),
            b: ivy.array([[4, 10],
                          [3, 9],
                          [2, 8],
                          [1, 7]])
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "rot90",
            m,
            copy=copy,
            k=k,
            axes=axes,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def rot90(
        self: Union[ivy.Container, ivy.Array, ivy.NativeArray],
        /,
        *,
        copy: bool = None,
        k: int = 1,
        axes: Tuple[int, int] = (0, 1),
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.rot90. This method simply wraps the
        function, and so the docstring for ivy.rot90 also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            Input array of two or more dimensions.
        k
            Number of times the array is rotated by 90 degrees.
        axes
            The array is rotated in the plane defined by the axes. Axes must be
            different.
        key_chains
            The key-chains to apply or not apply the method to. Default is None.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is True.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is False.
        map_sequences
            Whether to also map method to sequences (lists, tuples). Default is False.
        out
            optional output container, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            Container with a rotated view of input array.

        Examples
        --------
        >>> m = ivy.Container(a=ivy.array([[1,2], [3,4]]),\
        ...                   b=ivy.array([[1,2,3,4],[7,8,9,10]]))
        >>> n = m.rot90()
        >>> print(n)
        {
            a: ivy.array([[2, 4],
                          [1, 3]]),
            b: ivy.array([[4, 10],
                          [3, 9],
                          [2, 8],
                          [1, 7]])
        }
        """
        return self.static_rot90(
            self,
            copy=copy,
            k=k,
            axes=axes,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    @staticmethod
    def static_top_k(
        x: Union[ivy.Container, ivy.Array, ivy.NativeArray],
        k: int,
        /,
        *,
        axis: int = -1,
        largest: bool = True,
        sorted: bool = True,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[Tuple[ivy.Container, ivy.Container]] = None,
    ) -> Tuple[ivy.Container, ivy.Container]:
        """
        ivy.Container static method variant of ivy.top_k. This method simply wraps the
        function, and so the docstring for ivy.top_k also applies to this method with
        minimal changes.

        Parameters
        ----------
        x
            The container to compute top_k for.
        k
            Number of top elements to retun must not exceed the array size.
        axis
            The axis along which we must return the top elements default value is 1.
        largest
            If largest is set to False we return k smallest elements of the array.
        sorted
            If sorted is set to True we return the elements in sorted order.
        key_chains
            The key-chains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``
        out:
            Optional output tuple, for writing the result to. Must have two Container,
            with a shape that the returned tuple broadcast to.

        Returns
        -------
        ret
            a container with indices and values.

        Examples
        --------
        With :class:`ivy.Container` input:

        >>> x = ivy.Container(a=ivy.array([-1, 2, -4]), b=ivy.array([4., 5., 0.]))
        >>> y = ivy.Container.static_top_k(x, 2)
        >>> print(y)
        {
            a: [
                values = ivy.array([ 2, -1]),
                indices = ivy.array([1, 0])
            ],
            b: [
                values = ivy.array([5., 4.]),
                indices = ivy.array([1, 0])
            ]
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "top_k",
            x,
            k,
            axis=axis,
            largest=largest,
            sorted=sorted,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def top_k(
        self: ivy.Container,
        k: int,
        /,
        *,
        axis: int = -1,
        largest: bool = True,
        sorted: bool = True,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[Tuple[ivy.Container, ivy.Container]] = None,
    ) -> Tuple[ivy.Container, ivy.Container]:
        """
        ivy.Container instance method variant of ivy.top_k. This method simply wraps the
        function, and so the docstring for ivy.top_k also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            The container to compute top_k for.
        k
            Number of top elements to retun must not exceed the array size.
        axis
            The axis along which we must return the top elements default value is 1.
        largest
            If largest is set to False we return k smallest elements of the array.
        sorted
            If sorted is set to True we return the elements in sorted order.
        key_chains
            The key-chains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``
        out:
            Optional output tuple, for writing the result to. Must have two Container,
            with a shape that the returned tuple broadcast to.

        Returns
        -------
        ret
            a container with indices and values.

        Examples
        --------
        With :class:`ivy.Container` input:

        >>> x = ivy.Container(a=ivy.array([-1, 2, -4]), b=ivy.array([4., 5., 0.]))
        >>> y = x.top_k(2)
        >>> print(y)
        {
            a: [
                values = ivy.array([ 2, -1]),
                indices = ivy.array([1, 0])
            ],
            b: [
                values = ivy.array([5., 4.]),
                indices = ivy.array([1, 0])
            ]
        }
        """
        return self.static_top_k(
            self,
            k,
            axis=axis,
            largest=largest,
            sorted=sorted,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    @staticmethod
    def static_fliplr(
        m: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        /,
        *,
        copy: Optional[bool] = None,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.fliplr. This method simply wraps the
        function, and so the docstring for ivy.fliplr also applies to this method with
        minimal changes.

        Parameters
        ----------
        m
            the container with arrays to be flipped. Arrays must be at least 2-D.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        key_chains
            The key-chains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``
        out
            optional output container, for writing the result to.

        Returns
        -------
        ret
            container including arrays corresponding to the input container's array
            with elements order reversed along axis 1.

        Examples
        --------
        With one :class:`ivy.Container` input:
        >>> m = ivy.Container(a=ivy.diag([1, 2, 3]),\
        ...                    b=ivy.array([[1, 2, 3],[4, 5, 6]]))
        >>> ivy.Container.static_fliplr(m)
        {
            a: ivy.array([[0, 0, 1],
                          [0, 2, 0],
                          [3, 0, 0]]),
            b: ivy.array([[3, 2, 1],
                          [6, 5, 4]])
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "fliplr",
            m,
            copy=copy,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def fliplr(
        self: ivy.Container,
        /,
        *,
        copy: Optional[bool] = None,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.fliplr. This method simply wraps
        the function, and so the docstring for ivy.fliplr also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            the container with arrays to be flipped. Arrays must be at least 2-D.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        out
            optional output container, for writing the result to.

        Returns
        -------
        ret
            container including arrays corresponding to the input container's array
            with elements order reversed along axis 1.

        Examples
        --------
        With one :class:`ivy.Container` input:

        >>> m = ivy.Container(a=ivy.diag([1, 2, 3]),\
        ...                    b=ivy.array([[1, 2, 3],[4, 5, 6]]))
        >>> m.fliplr()
        {
            a: ivy.array([[0, 0, 1],
                          [0, 2, 0],
                          [3, 0, 0]]),
            b: ivy.array([[3, 2, 1],
                          [6, 5, 4]])
        }
        """
        return self.static_fliplr(self, copy=copy, out=out)

    @staticmethod
    def static_i0(
        x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        /,
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.i0. This method simply wraps the
        function, and so the docstring for ivy.i0 also applies to this method with
        minimal changes.

        Parameters
        ----------
        x
            the container with array inputs.
        out
            optional output container, for writing the result to.

        Returns
        -------
        ret
            container including arrays with the modified Bessel
            function evaluated at each of the elements of x.

        Examples
        --------
        With one :class:`ivy.Container` input:

        >>> x = ivy.Container(a=ivy.array([1, 2, 3]), b=ivy.array(4))
        >>> ivy.Container.static_i0(x)
        {
            a: ivy.array([1.26606588, 2.2795853 , 4.88079259])
            b: ivy.array(11.30192195)
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "i0",
            x,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def i0(
        self: ivy.Container,
        /,
        *,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.i0. This method simply wraps the
        function, and so the docstring for ivy.i0 also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            the container with array inputs.
        out
            optional output container, for writing the result to.

        Returns
        -------
        ret
            container including arrays with the modified Bessel
            function evaluated at each of the elements of x.

        Examples
        --------
        With one :class:`ivy.Container` input:

        >>> x = ivy.Container(a=ivy.array([1, 2, 3]), b=ivy.array(4))
        >>> x.i0()
        {
            a: ivy.array([1.26606588, 2.2795853 , 4.88079259])
            b: ivy.array(11.30192195)
        }
        """
        return self.static_i0(self, out=out)

    @staticmethod
    def static_flatten(
        x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        /,
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        copy: Optional[bool] = None,
        start_dim: int = 0,
        end_dim: int = -1,
        order: str = "C",
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.flatten. This method simply wraps the
        function, and so the docstring for ivy.flatten also applies to this method with
        minimal changes.

        Parameters
        ----------
        x
            input container to flatten at leaves.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        start_dim
            first dim to flatten. If not set, defaults to 0.
        end_dim
            last dim to flatten. If not set, defaults to -1.
        order
            Read the elements of the input container using this index order,
            and place the elements into the reshaped array using this index order.
            ‘C’ means to read / write the elements using C-like index order,
            with the last axis index changing fastest, back to the first axis index
            changing slowest.
            ‘F’ means to read / write the elements using Fortran-like index order, with
            the first index changing fastest, and the last index changing slowest.
            Note that the ‘C’ and ‘F’ options take no account of the memory layout
            of the underlying array, and only refer to the order of indexing.
            Default order is 'C'

        Returns
        -------
        ret
            Container with arrays flattened at leaves.

        Examples
        --------
        With one :class:`ivy.Container` input:

        >>> x = ivy.Container(a=ivy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]),
        ...                   b=ivy.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]]))
        >>> ivy.flatten(x)
        [{
            a: ivy.array([1, 2, 3, 4, 5, 6, 7, 8])
            b: ivy.array([9, 10, 11, 12, 13, 14, 15, 16])
        }]

        >>> x = ivy.Container(a=ivy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]),
        ...                   b=ivy.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]]))
        >>> ivy.flatten(x, order="F")
        [{
            a: ivy.array([1, 5, 3, 7, 2, 6, 4, 8])
            b: ivy.array([9, 13, 11, 15, 10, 14, 12, 16])
        }]
        """
        return ContainerBase.cont_multi_map_in_function(
            "flatten",
            x,
            copy=copy,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            start_dim=start_dim,
            end_dim=end_dim,
            order=order,
            out=out,
        )

    def flatten(
        self: ivy.Container,
        *,
        copy: Optional[bool] = None,
        start_dim: int = 0,
        end_dim: int = -1,
        order: str = "C",
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.flatten. This method simply wraps
        the function, and so the docstring for ivy.flatten also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            input container to flatten at leaves.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        start_dim
            first dim to flatten. If not set, defaults to 0.
        end_dim
            last dim to flatten. If not set, defaults to -1.
        order
            Read the elements of the input container using this index order,
            and place the elements into the reshaped array using this index order.
            ‘C’ means to read / write the elements using C-like index order,
            with the last axis index changing fastest, back to the first axis index
            changing slowest.
            ‘F’ means to read / write the elements using Fortran-like index order, with
            the first index changing fastest, and the last index changing slowest.
            Note that the ‘C’ and ‘F’ options take no account of the memory layout
            of the underlying array, and only refer to the order of indexing.
            Default order is 'C'

        Returns
        -------
        ret
            Container with arrays flattened at leaves.

        Examples
        --------
        With one :class:`ivy.Container` input:

        >>> x = ivy.Container(a=ivy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]),
        ...                   b=ivy.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]]))
        >>> x.flatten()
        [{
            a: ivy.array([1, 2, 3, 4, 5, 6, 7, 8])
            b: ivy.array([9, 10, 11, 12, 13, 14, 15, 16])
        }]

        >>> x = ivy.Container(a=ivy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]),
        ...                   b=ivy.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]]))
        >>> x.flatten(order="F")
        [{
            a: ivy.array([1, 5, 3, 7, 2, 6, 4, 8])
            b: ivy.array([9, 13, 11, 15, 10, 14, 12, 16])
        }]
        """
        return self.static_flatten(
            self, copy=copy, start_dim=start_dim, end_dim=end_dim, out=out, order=order
        )

    @staticmethod
    def static_pad(
        input: ivy.Container,
        pad_width: Union[Iterable[Tuple[int]], int],
        /,
        *,
        mode: Union[
            Literal[
                "constant",
                "dilated",
                "edge",
                "linear_ramp",
                "maximum",
                "mean",
                "median",
                "minimum",
                "reflect",
                "symmetric",
                "wrap",
                "empty",
            ],
            Callable,
        ] = "constant",
        stat_length: Union[Iterable[Tuple[int]], int] = 1,
        constant_values: Union[Iterable[Tuple[Number]], Number] = 0,
        end_values: Union[Iterable[Tuple[Number]], Number] = 0,
        reflect_type: Literal["even", "odd"] = "even",
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
        **kwargs: Optional[Any],
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.pad.

        This method simply wraps the function, and so the docstring for
        ivy.pad also applies to this method with minimal changes.
        """
        return ContainerBase.cont_multi_map_in_function(
            "pad",
            input,
            pad_width,
            mode=mode,
            stat_length=stat_length,
            constant_values=constant_values,
            end_values=end_values,
            reflect_type=reflect_type,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
            **kwargs,
        )

    def pad(
        self: ivy.Container,
        pad_width: Union[Iterable[Tuple[int]], int],
        /,
        *,
        mode: Union[
            Literal[
                "constant",
                "dilated",
                "edge",
                "linear_ramp",
                "maximum",
                "mean",
                "median",
                "minimum",
                "reflect",
                "symmetric",
                "wrap",
                "empty",
            ],
            Callable,
        ] = "constant",
        stat_length: Union[Iterable[Tuple[int]], int] = 1,
        constant_values: Union[Iterable[Tuple[Number]], Number] = 0,
        end_values: Union[Iterable[Tuple[Number]], Number] = 0,
        reflect_type: Literal["even", "odd"] = "even",
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
        **kwargs: Optional[Any],
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.pad.

        This method simply wraps the function, and so the docstring for
        ivy.pad also applies to this method with minimal changes.
        """
        return self.static_pad(
            self,
            pad_width,
            mode=mode,
            stat_length=stat_length,
            constant_values=constant_values,
            end_values=end_values,
            reflect_type=reflect_type,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
            **kwargs,
        )

    @staticmethod
    def static_vsplit(
        ary: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        indices_or_sections: Union[int, Sequence[int], ivy.Array, ivy.NativeArray],
        /,
        *,
        copy: Optional[bool] = None,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> List[ivy.Container]:
        """
        ivy.Container static method variant of ivy.vsplit. This method simply wraps the
        function, and so the docstring for ivy.vsplit also applies to this method with
        minimal changes.

        Parameters
        ----------
        ary
            the container with array inputs.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        indices_or_sections
            If indices_or_sections is an integer n, the array is split into n
            equal sections, provided that n must be a divisor of the split axis.
            If indices_or_sections is a sequence of ints or 1-D array,
            then input is split at each of the indices.
        key_chains
            The key-chains to apply or not apply the method to. Default is None.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is True.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is False.
        map_sequences
            Whether to also map method to sequences (lists, tuples). Default is False.

        Returns
        -------
        ret
            list of containers holding arrays split vertically from the input

        Examples
        --------
        >>> ary = ivy.Container(
                a = ivy.array(
                        [[[0.,  1.],
                          [2.,  3.]],
                          [[4.,  5.],
                          [6.,  7.]]]
                    ),
                b=ivy.array(
                        [[ 0.,  1.,  2.,  3.],
                         [ 4.,  5.,  6.,  7.],
                         [ 8.,  9., 10., 11.],
                         [12., 13., 14., 15.]]
                    )
                )
        >>> ivy.Container.static_vsplit(ary, 2)
        [{
            a: ivy.array([[[0., 1.],
                           [2., 3.]]]),
            b: ivy.array([[0., 1., 2., 3.],
                          [4., 5., 6., 7.]])
        }, {
            a: ivy.array([[[4., 5.],
                           [6., 7.]]]),
            b: ivy.array([[8., 9., 10., 11.],
                          [12., 13., 14., 15.]])
        }]
        """
        return ContainerBase.cont_multi_map_in_function(
            "vsplit",
            ary,
            indices_or_sections,
            copy=copy,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )

    def vsplit(
        self: ivy.Container,
        indices_or_sections: Union[int, Sequence[int], ivy.Array, ivy.NativeArray],
        /,
        *,
        copy: Optional[bool] = None,
    ) -> List[ivy.Container]:
        """
        ivy.Container instance method variant of ivy.vsplit. This method simply wraps
        the function, and so the docstring for ivy.vsplit also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            the container with array inputs.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        indices_or_sections
            If indices_or_sections is an integer n, the array is split into n
            equal sections, provided that n must be a divisor of the split axis.
            If indices_or_sections is a sequence of ints or 1-D array,
            then input is split at each of the indices.

        Returns
        -------
        ret
            list of containers holding arrays split vertically from the input

        Examples
        --------
        >>> ary = ivy.Container(
                a = ivy.array(
                        [[[0.,  1.],
                          [2.,  3.]],
                          [[4.,  5.],
                          [6.,  7.]]]
                    ),
                b=ivy.array(
                        [[ 0.,  1.,  2.,  3.],
                         [ 4.,  5.,  6.,  7.],
                         [ 8.,  9., 10., 11.],
                         [12., 13., 14., 15.]]
                    )
                )
        >>> ary.vsplit(2)
        [{
            a: ivy.array([[[0., 1.],
                           [2., 3.]]]),
            b: ivy.array([[0., 1., 2., 3.],
                          [4., 5., 6., 7.]])
        }, {
            a: ivy.array([[[4., 5.],
                           [6., 7.]]]),
            b: ivy.array([[8., 9., 10., 11.],
                          [12., 13., 14., 15.]])
        }]
        """
        return self.static_vsplit(self, indices_or_sections, copy=copy)

    @staticmethod
    def static_dsplit(
        ary: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        indices_or_sections: Union[int, Sequence[int], ivy.Array, ivy.NativeArray],
        /,
        *,
        copy: Optional[bool] = None,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> List[ivy.Container]:
        """
        ivy.Container static method variant of ivy.dsplit. This method simply wraps the
        function, and so the docstring for ivy.dsplit also applies to this method with
        minimal changes.

        Parameters
        ----------
        ary
            the container with array inputs.
        indices_or_sections
            If indices_or_sections is an integer n, the array is split into n
            equal sections, provided that n must be a divisor of the split axis.
            If indices_or_sections is a sequence of ints or 1-D array,
            then input is split at each of the indices.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        key_chains
            The key-chains to apply or not apply the method to. Default is None.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is True.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is False.
        map_sequences
            Whether to also map method to sequences (lists, tuples). Default is False.

        Returns
        -------
        ret
            list of containers holding arrays split from the input at the 3rd axis

        Examples
        --------
        >>> ary = ivy.Container(
            a = ivy.array(
                    [[[0.,  1.],
                      [2.,  3.]],
                      [[4.,  5.],
                      [6.,  7.]]]
                ),
            b=ivy.array(
                    [[[ 0.,  1.,  2.,  3.],
                      [ 4.,  5.,  6.,  7.],
                      [ 8.,  9., 10., 11.],
                      [12., 13., 14., 15.]]]
                )
            )
        >>> ivy.Container.static_dsplit(ary, 2)
        [{
            a: ivy.array([[[0.], [2.]],
                          [[4.], [6.]]]),
            b: ivy.array([[[0., 1.], [4., 5.], [8., 9.], [12., 13.]]])
        }, {
            a: ivy.array([[[1.], [3.]],
                          [[5.], [7.]]]),
            b: ivy.array([[[2., 3.], [6., 7.], [10., 11.], [14., 15.]]])
        }]
        """
        return ContainerBase.cont_multi_map_in_function(
            "dsplit",
            ary,
            indices_or_sections,
            copy=copy,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )

    def dsplit(
        self: ivy.Container,
        indices_or_sections: Union[int, Sequence[int], ivy.Array, ivy.NativeArray],
        /,
        *,
        copy: Optional[bool] = None,
    ) -> List[ivy.Container]:
        """
        ivy.Container instance method variant of ivy.dsplit. This method simply wraps
        the function, and so the docstring for ivy.dsplit also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            the container with array inputs.
        indices_or_sections
            If indices_or_sections is an integer n, the array is split into n
            equal sections, provided that n must be a divisor of the split axis.
            If indices_or_sections is a sequence of ints or 1-D array,
            then input is split at each of the indices.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.

        Returns
        -------
        ret
            list of containers holding arrays split from the input at the 3rd axis

        Examples
        --------
        >>> ary = ivy.Container(
            a = ivy.array(
                    [[[0.,  1.],
                      [2.,  3.]],
                      [[4.,  5.],
                      [6.,  7.]]]
                ),
            b=ivy.array(
                    [[[ 0.,  1.,  2.,  3.],
                      [ 4.,  5.,  6.,  7.],
                      [ 8.,  9., 10., 11.],
                      [12., 13., 14., 15.]]]
                )
            )
        >>> ary.dsplit(2)
        [{
            a: ivy.array([[[0.], [2.]],
                          [[4.], [6.]]]),
            b: ivy.array([[[0., 1.], [4., 5.], [8., 9.], [12., 13.]]])
        }, {
            a: ivy.array([[[1.], [3.]],
                          [[5.], [7.]]]),
            b: ivy.array([[[2., 3.], [6., 7.], [10., 11.], [14., 15.]]])
        }]
        """
        return self.static_dsplit(self, indices_or_sections, copy=copy)

    @staticmethod
    def static_atleast_1d(
        *arys: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        copy: Optional[bool] = None,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> List[ivy.Container]:
        """
        ivy.Container static method variant of ivy.atleast_1d. This method simply wraps
        the function, and so the docstring for ivy.atleast_1d also applies to this
        method with minimal changes.

        Parameters
        ----------
        arys
            one or more container with array inputs.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        key_chains
            The keychains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.

        Returns
        -------
        ret
            container or list of container where each elements within container is
            atleast 1d. Copies are made only if necessary.

        Examples
        --------
        >>> ary = ivy.Container(a=ivy.array(1), b=ivy.array([3,4,5]),\
                        c=ivy.array([[3]]))
        >>> ivy.Container.static_atleast_1d(ary)
        {
            a: ivy.array([1]),
            b: ivy.array([3, 4, 5]),
            c: ivy.array([[3]]),
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "atleast_1d",
            *arys,
            copy=copy,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )

    def atleast_1d(
        self: Union[ivy.Container, ivy.Array, ivy.NativeArray],
        *arys: Union[ivy.Container, ivy.Array, ivy.NativeArray, bool, Number],
        copy: Optional[bool] = None,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> List[ivy.Container]:
        """
        ivy.Container instance method variant of ivy.atleast_1d. This method simply
        wraps the function, and so the docstring for ivy.atleast_1d also applies to this
        method with minimal changes.

        Parameters
        ----------
        self
            the container with array inputs.
        arys
            one or more container with array inputs.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        key_chains
            The keychains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.

        Returns
        -------
        ret
            container or list of container where each elements within container is
            atleast 1d. Copies are made only if necessary.

        Examples
        --------
        >>> ary1 = ivy.Container(a=ivy.array(1), b=ivy.array([3,4]),\
                            c=ivy.array([[5]]))
        >>> ary2 = ivy.Container(a=ivy.array(9), b=ivy.array(2),\
                            c=ivy.array(3))
        >>> ary1.atleast_1d(ary2)
        [{
            a: ivy.array([1]),
            b: ivy.array([3, 4]),
            c: ivy.array([[5]])
        }, {
            a: ivy.array([9]),
            b: ivy.array([2]),
            c: ivy.array([3])
        }]
        """
        return self.static_atleast_1d(
            self,
            *arys,
            copy=copy,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )

    def dstack(
        self: ivy.Container,
        /,
        xs: Union[
            Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
            List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        ],
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.stack. This method simply wraps the
        function, and so the docstring for ivy.stack also applies to this method with
        minimal changes.

        Examples
        --------
        >>> x = ivy.Container(a=ivy.array([[0, 1], [2,3]]), b=ivy.array([[4, 5]]))
        >>> y = ivy.Container(a=ivy.array([[3, 2], [1,0]]), b=ivy.array([[1, 0]]))
        >>> x.dstack([y])
        {
            a: ivy.array([[[0, 3],
                           [1, 2]],
                          [[2, 1],
                           [3, 0]]]),
            b: ivy.array([[[4, 1]],
                           [[5, 0]]])
        }
        """
        new_xs = xs.cont_copy() if ivy.is_ivy_container(xs) else xs.copy()
        new_xs.insert(0, self.cont_copy())
        return self.static_dstack(
            new_xs,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    @staticmethod
    def static_dstack(
        xs: Union[
            Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
            List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        ],
        /,
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.stack. This method simply wraps the
        function, and so the docstring for ivy.dstack also applies to this method with
        minimal changes.

        Examples
        --------
        With one :class:`ivy.Container` input:
        >>> c = ivy.Container(a=[ivy.array([1,2,3]), ivy.array([0,0,0])],
                              b=ivy.arange(3))
        >>> ivy.Container.static_dstack(c)
        {
            a: ivy.array([[1, 0],
                          [2, 0]
                          [3,0]]),
            b: ivy.array([[0, 1, 2])
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "dstack",
            xs,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    @staticmethod
    def static_atleast_2d(
        *arys: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        copy: Optional[bool] = None,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> List[ivy.Container]:
        """
        ivy.Container static method variant of ivy.atleast_2d. This method simply wraps
        the function, and so the docstring for ivy.atleast_2d also applies to this
        method with minimal changes.

        Parameters
        ----------
        arys
            one or more container with array inputs.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        key_chains
            The keychains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.

        Returns
        -------
        ret
            container or list of container where each elements within container is
            atleast 2D. Copies are made only if necessary.

        Examples
        --------
        >>> ary = ivy.Container(a=ivy.array(1), b=ivy.array([3,4,5]),\
                        c=ivy.array([[3]]))
        >>> ivy.Container.static_atleast_2d(ary)
        {
            a: ivy.array([[1]]),
            b: ivy.array([[3, 4, 5]]),
            c: ivy.array([[3]])
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "atleast_2d",
            *arys,
            copy=copy,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )

    def atleast_2d(
        self: Union[ivy.Container, ivy.Array, ivy.NativeArray],
        *arys: Union[ivy.Container, ivy.Array, ivy.NativeArray],
        copy: Optional[bool] = None,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> List[ivy.Container]:
        """
        ivy.Container instance method variant of ivy.atleast_2d. This method simply
        wraps the function, and so the docstring for ivy.atleast_2d also applies to this
        method with minimal changes.

        Parameters
        ----------
        self
            container with array inputs.
        arys
            one or more container with array inputs.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        key_chains
            The keychains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.

        Returns
        -------
        ret
            container or list of container where each elements within container is
            atleast 2D. Copies are made only if necessary.

        Examples
        --------
        >>> ary1 = ivy.Container(a=ivy.array(1), b=ivy.array([3,4]),\
                            c=ivy.array([[5]]))
        >>> ary2 = ivy.Container(a=ivy.array(9), b=ivy.array(2),\
                            c=ivy.array(3))
        >>> ary1.atleast_2d(ary2)
        [{
            a: ivy.array([[1]]),
            b: ivy.array([[3, 4]]),
            c: ivy.array([[5]])
        }, {
            a: ivy.array([[9]]),
            b: ivy.array([[2]]),
            c: ivy.array([[3]])
        }]
        """
        return self.static_atleast_2d(
            self,
            *arys,
            copy=copy,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )

    @staticmethod
    def static_atleast_3d(
        *arys: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        copy: Optional[bool] = None,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> List[ivy.Container]:
        """
        ivy.Container static method variant of ivy.atleast_3d. This method simply wraps
        the function, and so the docstring for ivy.atleast_3d also applies to this
        method with minimal changes.

        Parameters
        ----------
        arys
            one or more container with array inputs.
        copy
            boolean indicating whether or not to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
        key_chains
            The keychains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.

        Returns
        -------
        ret
            container or list of container where each elements within container is
            atleast 3D. Copies are made only if necessary. For example, a 1-D array
            of shape (N,) becomes a view of shape (1, N, 1), and a 2-D array of shape
            (M, N) becomes a view of shape (M, N, 1).

        Examples
        --------
        >>> ary = ivy.Container(a=ivy.array(1), b=ivy.array([3,4,5]),\
                        c=ivy.array([[3]]))
        >>> ivy.Container.static_atleast_3d(ary)
        {
            a: ivy.array([[[1]]]),
            b: ivy.array([[[3],
                           [4],
                           [5]]]),
            c: ivy.array([[[3]]])
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "atleast_3d",
            *arys,
            copy=copy,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )

    def atleast_3d(
        self: Union[ivy.Container, ivy.Array, ivy.NativeArray],
        *arys: Union[ivy.Container, ivy.Array, ivy.NativeArray, bool, Number],
        copy: Optional[bool] = None,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> List[ivy.Container]:
        """
        ivy.Container instance method variant of ivy.atleast_3d. This method simply
        wraps the function, and so the docstring for ivy.atleast_3d also applies to this
        method with minimal changes.

        Parameters
        ----------
        self
            container with array inputs.
        arys
            one or more container with array inputs.
            
        key_chains
            The keychains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.

        Returns
        -------
        ret
            container or list of container where each elements within container is
            atleast 3D. Copies are made only if necessary. For example, a 1-D array
            of shape (N,) becomes a view of shape (1, N, 1), and a 2-D array of shape
            (M, N) becomes a view of shape (M, N, 1).

        Examples
        --------
        >>> ary1 = ivy.Container(a=ivy.array(1), b=ivy.array([3,4]),\
                            c=ivy.array([[5]]))
        >>> ary2 = ivy.Container(a=ivy.array(9), b=ivy.array(2),\
                            c=ivy.array(3))
        >>> ary1.atleast_3d(ary2)
        [{
            a: ivy.array([[[1]]]),
            b: ivy.array([[[3],
                           [4]]]),
            c: ivy.array([[[5]]])
        }, {
            a: ivy.array([[[9]]]),
            b: ivy.array([[[2]]]),
            c: ivy.array([[[3]]])
        }]
        """
        return self.static_atleast_3d(
            self,
            *arys,
            copy=copy,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )

    @staticmethod
    def static_take_along_axis(
        arr: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        indices: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        axis: int,
        mode: str = "fill",
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.take_along_axis. This method simply
        wraps the function, and so the docstring for ivy.take_along_axis also applies to
        this method with minimal changes.

        Parameters
        ----------
        arr
            container with array inputs.
        indices
            container with indices of the values to extract.
        axis
            The axis over which to select values. If axis is None, then arr and indices
            must be 1-D sequences of the same length.
        mode
            One of: 'clip', 'fill', 'drop'. Parameter controlling how out-of-bounds
            indices will be handled.
        key_chains
            The keychains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.
        out
            optional output container, for writing the result to.

        Returns
        -------
        ret
            a container with arrays of the same shape as those in indices.

        Examples
        --------
        >>> arr = ivy.Container(a=ivy.array([[1, 2], [3, 4]]),\
                                b=ivy.array([[5, 6], [7, 8]]))
        >>> indices = ivy.Container(a=ivy.array([[0, 0], [1, 1]]),\
                                    b=ivy.array([[1, 0], [1, 0]]))
        >>> ivy.Container.static_take_along_axis(arr, indices, axis=1)
        {
            a: ivy.array([[1, 1],
                          [4, 4]]),
            b: ivy.array([[6, 5],
                          [8, 7]])
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "take_along_axis",
            arr,
            indices,
            axis,
            mode=mode,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def take_along_axis(
        self: Union[ivy.Container, ivy.Array, ivy.NativeArray],
        indices: Union[ivy.Container, ivy.Array, ivy.NativeArray],
        axis: int,
        mode: str = "fill",
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.take_along_axis. This method simply
        wraps the function, and so the docstring for ivy.take_along_axis also applies to
        this method with minimal changes.

        Parameters
        ----------
        self
            container with array inputs.
        indices
            container with indices of the values to extract.
        axis
            The axis over which to select values. If axis is None, then arr and indices
            must be 1-D sequences of the same length.
        mode
            One of: 'clip', 'fill', 'drop'. Parameter controlling how out-of-bounds
            indices will be handled.
        key_chains
            The keychains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.
        out
            optional output container, for writing the result to.

        Returns
        -------
        ret
            a container with arrays of the same shape as those in indices.

        Examples
        --------
        >>> arr = ivy.Container(a=ivy.array([[1, 2], [3, 4]]),\
                                b=ivy.array([[5, 6], [7, 8]]))
        >>> indices = ivy.Container(a=ivy.array([[0, 0], [1, 1]]),\
                                    b=ivy.array([[1, 0], [1, 0]]))
        >>> arr.take_along_axis(indices, axis=1)
        [{
            a: ivy.array([[1, 1],
                          [4, 4]]),
            b: ivy.array([[6, 5],
                            [8, 7]])
        }]
        """
        return self.static_take_along_axis(
            self,
            indices,
            axis,
            mode=mode,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    @staticmethod
    def static_hsplit(
        ary: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        indices_or_sections: Union[int, Sequence[int], ivy.Array, ivy.NativeArray],
        /,
        *,
        copy: Optional[bool] = None,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> List[ivy.Container]:
        """
        ivy.Container static method variant of ivy.hsplit. This method simply wraps the
        function, and so the docstring for ivy.hsplit also applies to this method with
        minimal changes.

        Parameters
        ----------
        ary
            the container with array inputs.
        indices_or_sections
            If indices_or_sections is an integer n, the array is split into n
            equal sections, provided that n must be a divisor of the split axis.
            If indices_or_sections is a sequence of ints or 1-D array,
            then input is split at each of the indices.
        key_chains
            The keychains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.

        Returns
        -------
        ret
            list of containers split horizontally from input array.

        Examples
        --------
        >>> ary = ivy.Container(
            a = ivy.array(
                    [[[0.,  1.],
                      [2.,  3.]],
                      [[4.,  5.],
                      [6.,  7.]]]
                ),
            b=ivy.array(
                    [0.,  1.,  2.,  3.,
                     4.,  5.,  6.,  7.,
                     8.,  9.,  10., 11.,
                     12., 13., 14., 15.]
                )
            )
        >>> ivy.Container.static_hsplit(ary, 2)
        [{
            a: ivy.array([[[0., 1.]],
                          [[4., 5.]]]),
            b: ivy.array([0., 1., 2., 3., 4., 5., 6., 7.])
        }, {
            a: ivy.array([[[2., 3.]],
                          [[6., 7.]]]),
            b: ivy.array([8., 9., 10., 11., 12., 13., 14., 15.])
        }]
        """
        return ContainerBase.cont_multi_map_in_function(
            "hsplit",
            ary,
            indices_or_sections,
            copy=copy,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )

    def hsplit(
        self: ivy.Container,
        indices_or_sections: Union[int, Sequence[int], ivy.Array, ivy.NativeArray],
        copy: Optional[bool] = None,
        /,
    ) -> List[ivy.Container]:
        """
        ivy.Container instance method variant of ivy.hsplit. This method simply wraps
        the function, and so the docstring for ivy.hsplit also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            the container with array inputs.
        indices_or_sections
            If indices_or_sections is an integer n, the array is split into n
            equal sections, provided that n must be a divisor of the split axis.
            If indices_or_sections is a sequence of ints or 1-D array,
            then input is split at each of the indices.

        Returns
        -------
        ret
            list of containers split horizontally from input container

        Examples
        --------
        >>> ary = ivy.Container(
            a = ivy.array(
                    [[[0.,  1.],
                      [2.,  3.]],
                      [[4.,  5.],
                      [6.,  7.]]]
                ),
            b=ivy.array(
                    [0.,  1.,  2.,  3.,
                     4.,  5.,  6.,  7.,
                     8.,  9.,  10., 11.,
                     12., 13., 14., 15.]
                )
            )
        >>> ary.hsplit(2)
        [{
            a: ivy.array([[[0., 1.]],
                          [[4., 5.]]]),
            b: ivy.array([0., 1., 2., 3., 4., 5., 6., 7.])
        }, {
            a: ivy.array([[[2., 3.]],
                          [[6., 7.]]]),
            b: ivy.array([8., 9., 10., 11., 12., 13., 14., 15.])
        }]
        """
        return self.static_hsplit(self, indices_or_sections, copy=copy)

    @staticmethod
    def static_broadcast_shapes(
        shapes: Union[ivy.Container, List[Tuple[int]]],
        /,
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.broadcast_shapes. This method simply
        wraps the function, and so the docstring for ivy.hsplit also applies to this
        method with minimal changes.

        Parameters
        ----------
        shapes
            the container with shapes to broadcast.
        key_chains
            The keychains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.

        Returns
        -------
        ret
            Container with broadcasted shapes.

        Examples
        --------
        >>> shapes = ivy.Container(a = [(2, 3), (2, 1)],
        ...                        b = [(2, 3), (1, 3)],
        ...                        c = [(2, 3), (2, 3)],
        ...                        d = [(2, 3), (2, 1), (1, 3), (2, 3)])
        >>> z = ivy.Container.static_broadcast_shapes(shapes)
        >>> print(z)
        {
            a: (2, 3),
            b: (2, 3),
            c: (2, 3),
            d: (2, 3)
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "broadcast_shapes",
            shapes,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def broadcast_shapes(
        self: ivy.Container,
        /,
        *,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.broadcast_shapes. This method
        simply wraps the function, and so the docstring for ivy.broadcast_shapes also
        applies to this method with minimal changes.

        Parameters
        ----------
        self
            the container with shapes to broadcast.

        Returns
        -------
        ret
            Container with broadcasted shapes.

        Examples
        --------
        >>> shapes = ivy.Container(a = [(2, 3), (2, 1)],
        ...                        b = [(2, 3), (1, 3)],
        ...                        c = [(2, 3), (2, 3)],
        ...                        d = [(2, 3), (2, 1), (1, 3), (2, 3)])
        >>> z = shapes.broadcast_shapes()
        >>> print(z)
        {
            a: (2, 3),
            b: (2, 3),
            c: (2, 3),
            d: (2, 3)
        }
        """
        return self.static_broadcast_shapes(self, out=out)

    @staticmethod
    def static_expand(
        x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        shape: Union[ivy.Shape, ivy.NativeShape],
        /,
        *,
        copy: Optional[bool] = None,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """

        Parameters
        ----------
        x
            input container.
        shape
            A 1-D Array indicates the shape you want to expand to,
            following the broadcast rule.
        copy
            boolean indicating whether to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
            device
        key_chains
            The keychains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.
        out
            optional output array, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            An output Container with the results.
        """
        return ContainerBase.cont_multi_map_in_function(
            "expand",
            x,
            shape,
            copy=copy,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def expand(
        self: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        shape: Union[ivy.Shape, ivy.NativeShape],
        /,
        *,
        copy: Optional[bool] = None,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """

        Parameters
        ----------
        self
            input container.
        shape
            A 1-D Array indicates the shape you want to expand to,
            following the broadcast rule.
        copy
            boolean indicating whether to copy the input array.
            If True, the function must always copy.
            If False, the function must never copy and must
            raise a ValueError in case a copy would be necessary.
            If None, the function must reuse existing memory buffer if possible
            and copy otherwise. Default: ``None``.
            device
        out
            optional output array, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            An output Container with the results.


        """
        return self.static_expand(self, shape, copy=copy, out=out)

    @staticmethod
    def static_as_strided(
        x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        shape: Union[ivy.Shape, ivy.NativeShape, Sequence[int]],
        strides: Sequence[int],
        /,
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.as_strided. This method simply
        wraps the function, and so the docstring for ivy.as_strided also applies to this
        method with minimal changes.

        Parameters
        ----------
        x
            Input container.
        shape
            The shape of the new arrays.
        strides
            The strides of the new arrays (specified in bytes).
        key_chains
            The keychains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.

        Returns
        -------
        ret
            Output container.
        """
        return ContainerBase.cont_multi_map_in_function(
            "as_strided",
            x,
            shape,
            strides,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )

    def as_strided(
        self: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        shape: Union[ivy.Shape, ivy.NativeShape, Sequence[int]],
        strides: Sequence[int],
        /,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.as_strided. This method simply
        wraps the function, and so the docstring for ivy.as_strided also applies to this
        method with minimal changes.

        Parameters
        ----------
        self
            Input container.
        shape
            The shape of the new arrays.
        strides
            The strides of the new arrays (specified in bytes).

        Returns
        -------
        ret
            Output container.
        """
        return self.static_as_strided(self, shape, strides)

    @staticmethod
    def static_concat_from_sequence(
        input_sequence: Union[
            Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
            List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        ],
        /,
        *,
        new_axis: int = 0,
        axis: int = 0,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.concat_from_sequence. This method
        simply wraps the function, and so the docstring for ivy.concat_from_sequence
        also applies to this method with minimal changes.

        Parameters
        ----------
        input_sequence
            Container with leaves to join. Each array leave must have the same shape.
        new_axis
            Insert and concatenate on a new axis or not,
            default 0 means do not insert new axis.
            new_axis = 0: concatenate
            new_axis = 1: stack
        axis
            axis along which the array leaves will be concatenated. More details
            can be found in the docstring for ivy.concat_from_sequence.

        key_chains
            The key-chains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.
        out
            optional output array, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            an output container with the results.

        Examples
        --------
        >>> x = ivy.Container(a=ivy.array([[0, 1], [2,3]]), b=ivy.array([[4, 5]]))
        >>> z = ivy.Container.static_concat_from_sequence(x,new_axis = 1, axis = 1)
        >>> print(z)
        {
            a: ivy.array([[0, 2],
                        [1, 3]]),
            b: ivy.array([[4],
                        [5]])
        }

        >>> x = ivy.Container(a=ivy.array([[0, 1], [2,3]]), b=ivy.array([[4, 5]]))
        >>> y = ivy.Container(a=ivy.array([[3, 2], [1,0]]), b=ivy.array([[1, 0]]))
        >>> z = ivy.Container.static_concat_from_sequence([x,y])
        >>> print(z)
        {
            a: ivy.array([[0, 1],
                          [2, 3],
                          [3, 2],
                          [1, 0]]),
            b: ivy.array([[4, 5],
                          [1, 0]])
        }

        >>> x = ivy.Container(a=ivy.array([[0, 1], [2,3]]), b=ivy.array([[4, 5]]))
        >>> y = ivy.Container(a=ivy.array([[3, 2], [1,0]]), b=ivy.array([[1, 0]]))
        >>> z = ivy.Container.static_concat_from_sequence([x,y],new_axis=1, axis=1)
        >>> print(z)
        {
            a: ivy.array([[[0, 1],
                        [3, 2]],
                        [[2, 3],
                        [1, 0]]]),
            b: ivy.array([[[4, 5],
                        [1, 0]]])
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "concat_from_sequence",
            input_sequence,
            new_axis=new_axis,
            axis=axis,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def concat_from_sequence(
        self: ivy.Container,
        /,
        input_sequence: Union[
            Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
            List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        ],
        *,
        new_axis: int = 0,
        axis: int = 0,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.stack. This method simply wraps the
        function, and so the docstring for ivy.stack also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            Container with leaves to join with leaves of other arrays/containers.
             Each array leave must have the same shape.
        input_sequence
            Container with other leaves to join.
            Each array leave must have the same shape.
        new_axis
            Insert and concatenate on a new axis or not,
            default 0 means do not insert new axis.
            new_axis = 0: concatenate
            new_axis = 1: stack
        axis
            axis along which the array leaves will be concatenated. More details can
            be found in the docstring for ivy.stack.
        key_chains
            The key-chains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.
        out
            optional output array, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            an output container with the results.

        Examples
        --------
        >>> x = ivy.Container(a=ivy.array([[0, 1], [2,3]]), b=ivy.array([[4, 5]]))
        >>> y = ivy.Container(a=ivy.array([[3, 2], [1,0]]), b=ivy.array([[1, 0]]))
        >>> z = ivy.Container.static_concat_from_sequence([x,y],axis=1)
        >>> print(z)
        {
            a: ivy.array([[[0, 1],
                        [3, 2]],
                        [[2, 3],
                        [1, 0]]]),
            b: ivy.array([[[4, 5],
                        [1, 0]]])
        }
        """
        new_input_sequence = (
            input_sequence.cont_copy()
            if ivy.is_ivy_container(input_sequence)
            else input_sequence.copy()
        )
        new_input_sequence.insert(0, self.cont_copy())
        return self.concat_from_sequence(
            new_input_sequence,
            new_axis=new_axis,
            axis=axis,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def associative_scan(
        self: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        fn: Callable,
        /,
        *,
        reverse: bool = False,
        axis: int = 0,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.associative_scan. This method
        simply wraps the function, and so the docstring for ivy.associative_scan also
        applies to this method with minimal changes.

        Parameters
        ----------
        self
            The Container to scan over.
        fn
            The associative function to apply.
        reverse
            Whether to scan in reverse with respect to the given axis.
        axis
            The axis to scan over.

        Returns
        -------
        ret
            The result of the scan.
        """
        return ivy.associative_scan(self, fn, reverse=reverse, axis=axis)

    @staticmethod
    def _static_unique_consecutive(
        x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        /,
        *,
        axis: Optional[int] = None,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.unique_consecutive.

        This method simply wraps the function, and so the docstring for
        ivy.unique_consecutive also applies to this method with minimal
        changes.
        """
        return ContainerBase.cont_multi_map_in_function(
            "unique_consecutive",
            x,
            axis=axis,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )

    def unique_consecutive(
        self: ivy.Container,
        /,
        *,
        axis: Optional[int] = None,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.unique_consecutive.

        This method simply wraps the function, and so the docstring for
        ivy.unique_consecutive also applies to this method with minimal
        changes.
        """
        return self._static_unique_consecutive(
            self,
            axis=axis,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )
