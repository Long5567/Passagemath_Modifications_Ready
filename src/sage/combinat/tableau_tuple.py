# sage_setup: distribution = sagemath-combinat
r"""
TableauTuples

A :class:`TableauTuple` is a tuple of tableaux. These objects arise naturally
in representation theory of the wreath products of cyclic groups and the
symmetric groups where the standard tableau tuples index bases for the ordinary
irreducible representations. This generalises the well-known fact the ordinary
irreducible representations of the symmetric groups have bases indexed by the
standard tableaux of a given shape. More generally, :class:`TableauTuples`, or
multitableaux, appear in the representation theory of the degenerate and
non-degenerate cyclotomic Hecke algebras and in the crystal theory of the
integral highest weight representations of the affine special linear groups.

A :class:`TableauTuple` is an ordered tuple
`(t^{(1)}, t^{(2)}, \ldots, t^{(l)})` of tableaux. The length of the tuple is
its *level* and the tableaux `t^{(1)}, t^{(2)}, \ldots, t^{(l)}` are the
components of the :class:`TableauTuple`.

A tableau can be thought of as the labelled diagram of a partition.
Analogously, a :class:`TableauTuple` is the labelled diagram of a
:class:`PartitionTuple`. That is, a :class:`TableauTuple` is a tableau of
:class:`PartitionTuple` shape. As much as possible, :class:`TableauTuples`
behave in exactly the same way as :class:`Tableaux`. There are obvious
differences in that the cells of a partition are ordered pairs `(r, c)`,
where `r` is a row index and `c` a column index, whereas the cells of a
:class:`PartitionTuple` are ordered triples `(k, r, c)`, with `r` and `c` as
before and `k` indexes the component.

Frequently, we will call a :class:`TableauTuple` a tableau, or a tableau of
:class:`PartitionTuple` shape. If the shape of the tableau is known this
should not cause any confusion.

.. WARNING::

    In sage the convention is that the `(k, r, c)`-th entry of a tableau tuple
    `t` is the entry in row `r`, column `c` and component `k` of the tableau.
    This is because it makes much more sense to let ``t[k]`` be component of
    the tableau. In particular, we want ``t(k,r,c) == t[k][r][c]``. In the
    literature, the cells of a tableau tuple are usually written in the form
    `(r, c, k)`, where `r` is the row index, `c` is the column index, and
    `k` is the component index.

    The same convention applies to the cells of :class:`PartitionTuples`.

.. NOTE::

    As with partitions and tableaux, the cells are 0-based. For example, the
    (lexicographically) first cell in any non-empty tableau tuple is
    ``[0,0,0]``.

EXAMPLES::

    sage: TableauTuple([[1,2,3],[4,5]])
    [[1, 2, 3], [4, 5]]
    sage: t = TableauTuple([ [[6,7],[8,9]],[[1,2,3],[4,5]] ]); t
    ([[6, 7], [8, 9]], [[1, 2, 3], [4, 5]])
    sage: t.pp()
      6  7     1  2  3
      8  9     4  5
    sage: t(0,0,1)
    7
    sage: t(1,0,1)
    2
    sage: t.shape()
    ([2, 2], [3, 2])
    sage: t.size()
    9
    sage: t.level()
    2
    sage: t.components()
    [[[6, 7], [8, 9]], [[1, 2, 3], [4, 5]]]
    sage: t.entries()
    [6, 7, 8, 9, 1, 2, 3, 4, 5]
    sage: t.parent()
    Tableau tuples
    sage: t.category()
    Category of elements of Tableau tuples

One reason for implementing :class:`TableauTuples` is to be able to consider
:class:`StandardTableauTuples`. These objects arise in many areas of algebraic
combinatorics. In particular, they index bases for the Specht modules of the
cyclotomic Hecke algebras of type `G(r,1,n)`. A :class:`StandardTableauTuple`
of tableau whose entries are increasing along rows and down columns in each
component and which contain the numbers `1,2, \ldots, n`, where the shape of
the :class:`StandardTableauTuple` is a :class:`PartitionTuple` of `n`.

::

    sage: s = StandardTableauTuple([ [[1,2],[3]],[[4,5]]])
    sage: s.category()
    Category of elements of Standard tableau tuples
    sage: t = TableauTuple([ [[1,2],[3]],[[4,5]]])
    sage: t.is_standard(), t.is_column_strict(), t.is_row_strict()
    (True, True, True)
    sage: t.category()
    Category of elements of Tableau tuples
    sage: s == t
    True
    sage: s is t
    False
    sage: s == StandardTableauTuple(t)
    True
    sage: StandardTableauTuples([ [2,1],[1] ])[:]
    [([[1, 2], [3]], [[4]]),
     ([[1, 3], [2]], [[4]]),
     ([[1, 2], [4]], [[3]]),
     ([[1, 3], [4]], [[2]]),
     ([[2, 3], [4]], [[1]]),
     ([[1, 4], [2]], [[3]]),
     ([[1, 4], [3]], [[2]]),
     ([[2, 4], [3]], [[1]])]

As tableaux (of partition shape) are in natural bijection with 1-tuples of
tableaux  all of the :class:`TableauTuple` classes return an ordinary
:class:`Tableau` when given :class:`TableauTuple` of level 1.

::

    sage: TableauTuples( level=1 ) is Tableaux()
    True
    sage: TableauTuple([[1,2,3],[4,5]])
    [[1, 2, 3], [4, 5]]
    sage: TableauTuple([ [[1,2,3],[4,5]] ])
    [[1, 2, 3], [4, 5]]
    sage: TableauTuple([[1,2,3],[4,5]]) == Tableau([[1,2,3],[4,5]])
    True

There is one situation where a 1-tuple of tableau is not actually a
:class:`Tableau`; tableaux generated by the :func:`StandardTableauTuples()`
iterators must have the correct parents, so in this one case 1-tuples of
tableaux are different from :class:`Tableaux`::

    sage: StandardTableauTuples()[:10]                                                  # needs sage.libs.flint
    [(),
     ([[1]]),
     ([], []),
     ([[1, 2]]),
     ([[1], [2]]),
     ([[1]], []),
     ([], [[1]]),
     ([], [], []),
     ([[1, 2, 3]]),
     ([[1, 3], [2]])]

AUTHORS:

- Andrew Mathas (2012-10-09): Initial version -- heavily based on
  ``tableau.py`` by Mike Hansen (2007) and Jason Bandlow (2011).

- Andrew Mathas (2016-08-11): Row standard tableaux added

Element classes:

* :class:`TableauTuples`
* :class:`StandardTableauTuples`
* :class:`RowStandardTableauTuples`

Factory classes:

* :class:`TableauTuples`
* :class:`StandardTableauTuples`
* :class:`RowStandardTableauTuples`

Parent classes:

* :class:`TableauTuples_all`
* :class:`TableauTuples_level`
* :class:`TableauTuples_size`
* :class:`TableauTuples_level_size`
* :class:`StandardTableauTuples_all`
* :class:`StandardTableauTuples_level`
* :class:`StandardTableauTuples_size`
* :class:`StandardTableauTuples_level_size`
* :class:`StandardTableauTuples_shape`
* :class:`StandardTableaux_residue`
* :class:`StandardTableaux_residue_shape`
* :class:`RowStandardTableauTuples_all`
* :class:`RowStandardTableauTuples_level`
* :class:`RowStandardTableauTuples_size`
* :class:`RowStandardTableauTuples_level_size`
* :class:`RowStandardTableauTuples_shape`
* :class:`RowStandardTableauTuples_residue`
* :class:`RowStandardTableauTuples_residue_shape`

.. SEEALSO::

    * :class:`Tableau`
    * :class:`StandardTableau`
    * :class:`Tableaux`
    * :class:`StandardTableaux`
    * :class:`Partitions`
    * :class:`PartitionTuples`
    * :class:`ResidueSequence`

.. TODO::

    Implement semistandard tableau tuples as defined in [DJM1998]_.

Much of the combinatorics implemented here is motivated by this and
subsequent papers on the representation theory of these algebras.
"""

# ****************************************************************************
#       Copyright (C) 2012,2016 Andrew Mathas <andrew dot mathas at sydney dot edu dot au>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#                  http://www.gnu.org/licenses/
# ****************************************************************************

from sage.arith.misc import factorial
from sage.combinat.combinat import CombinatorialElement
from sage.combinat.words.word import Word
from sage.combinat.tableau import (Tableau, Tableaux, Tableaux_size, Tableaux_all,
                                   StandardTableau, RowStandardTableau,
                                   StandardTableaux, StandardTableaux_size,
                                   StandardTableaux_all, StandardTableaux_shape,
                                   RowStandardTableaux, RowStandardTableaux_size,
                                   RowStandardTableaux_all, RowStandardTableaux_shape)
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.categories.sets_cat import Sets
from sage.misc.classcall_metaclass import ClasscallMetaclass
from sage.misc.flatten import flatten
from sage.misc.lazy_attribute import lazy_attribute
from sage.misc.lazy_import import lazy_import
from sage.misc.misc_c import prod
from sage.misc.prandom import randint
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing
from sage.rings.integer import Integer
from sage.rings.semirings.non_negative_integer_semiring import NN
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets
from sage.sets.family import Family
from sage.sets.positive_integers import PositiveIntegers
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from sage.combinat import permutation

lazy_import('sage.combinat.posets.posets', 'Poset')
lazy_import('sage.groups.perm_gps.permgroup', 'PermutationGroup')


# -------------------------------------------------
# Tableau tuple - element class
# -------------------------------------------------
class TableauTuple(CombinatorialElement):
    """
    A class to model a tuple of tableaux.

    INPUT:

    - ``t`` -- list or tuple of :class:`Tableau`, a list or tuple of lists
      of lists

    OUTPUT: the Tableau tuple object constructed from ``t``

    A :class:`TableauTuple` is a tuple of tableau of shape a
    :class:`PartitionTuple`. These combinatorial objects are useful is
    several areas of algebraic combinatorics. In particular, they are
    important in:

    - the representation theory of the complex reflection groups of
      type `G(l,1,n)` and the representation theory of the associated
      (degenerate and non-degenerate) Hecke algebras. See, for example,
      [DJM1998]_

    - the crystal theory of (quantum) affine special linear groups and  its
      integral highest weight modules and their canonical bases. See, for
      example, [BK2009]_.

    These apparently different and unrelated contexts are, in fact, intimately
    related as in characteristic zero the cyclotomic Hecke algebras categorify
    the canonical bases of the integral highest weight modules of the quantum
    affine special linear groups.

    The :meth:`level` of a tableau tuple is the length of the tuples. This
    corresponds to the level of the corresponding highest weight module.

    In sage a :class:`TableauTuple` looks and behaves like a real tuple of
    (level 1) :class:`Tableaux`. Many of the operations which are defined
    on :class:`Tableau` extend to :class:`TableauTuples`. Tableau tuples of
    level 1 are just ordinary :class:`Tableau`.

    In sage, the entries of :class:`Tableaux` can be very general, including
    arbitrarily nested lists, so some lists can be interpreted either as a
    tuple of tableaux or simply as tableaux. If it is possible to interpret
    the input to :class:`TableauTuple` as a tuple of tableaux then
    :class:`TableauTuple` returns the corresponding tuple. Given a 1-tuple of
    tableaux the tableau itself is returned.

    EXAMPLES::

        sage: t = TableauTuple([ [[6,9,10],[11]], [[1,2,3],[4,5]], [[7],[8]] ]); t
        ([[6, 9, 10], [11]], [[1, 2, 3], [4, 5]], [[7], [8]])
        sage: t.level()
        3
        sage: t.size()
        11
        sage: t.shape()
        ([3, 1], [3, 2], [1, 1])
        sage: t.is_standard()
        True
        sage: t.pp() # pretty printing
         6  9 10     1  2  3     7
        11           4  5        8
        sage: t.category()
        Category of elements of Tableau tuples
        sage: t.parent()
        Tableau tuples

        sage: s = TableauTuple([ [['a','c','b'],['d','e']],[[(2,1)]]]); s
        ([['a', 'c', 'b'], ['d', 'e']], [[(2, 1)]])
        sage: s.shape()
        ([3, 2], [1])
        sage: s.size()
        6

        sage: TableauTuple([[],[],[]])  # The empty 3-tuple of tableaux
        ([], [], [])

        sage: TableauTuple([[1,2,3],[4,5]])
        [[1, 2, 3], [4, 5]]
        sage: TableauTuple([[1,2,3],[4,5]]) == Tableau([[1,2,3],[4,5]])
        True

    .. SEEALSO::

        - :class:`StandardTableauTuple`
        - :class:`StandardTableauTuples`
        - :class:`StandardTableau`
        - :class:`StandardTableaux`
        - :class:`TableauTuple`
        - :class:`TableauTuples`
        - :class:`Tableau`
        - :class:`Tableaux`

    TESTS::

        sage: TableauTuple( [[1,2,3],[4,5]] ).category()
        Category of elements of Tableaux
        sage: TableauTuple([[[1,2,3],[4,5]]]).category()
        Category of elements of Tableaux

        sage: TableauTuple([[1],[2,3]])
        Traceback (most recent call last):
        ...
        ValueError: a tableau must be a list of iterables

        sage: TestSuite( TableauTuple([ [[1,2],[3,4]], [[1,2],[3,4]] ]) ).run()
        sage: TestSuite( TableauTuple([ [[1,2],[3,4]], [], [[1,2],[3,4]] ]) ).run()
        sage: TestSuite( TableauTuple([[[1,1],[1]],[[1,1,1]],[[1],[1],[1]],[[1]]]) ).run()
    """
    Element = Tableau

    @staticmethod
    def __classcall_private__(self, t):
        r"""
        This ensures that a :class:`TableauTuples` is only ever constructed
        via an ``element_class()`` call of an appropriate parent.

        EXAMPLES::

            sage: t = TableauTuple([[[1,1],[1]],[[1,1,1]],[[1],[1],[1]],[[1]]])
            sage: t.parent()
            Tableau tuples
            sage: t.category()
            Category of elements of Tableau tuples
            sage: type(t)
            <class 'sage.combinat.tableau_tuple.TableauTuples_all_with_category.element_class'>
            sage: TableauTuples(level=4)(t).parent()
            Tableau tuples of level 4
        """
        if isinstance(t, (Tableau, TableauTuple)):
            return t

        # one way or another these two cases need to be treated separately
        if t == [] or t == [[]]:
            return Tableaux_all().element_class(Tableaux_all(), [])

        # The Tableau class is very general in that it allows the entries of a
        # tableau to be almost anything, including lists. For this reason we
        # first try and interpret t as a tuple of tableaux and if this fails we
        # then try to think of t as a tableau.
        try:
            t = [Tableau(s) for s in t]
        except (TypeError, ValueError):
            try:
                t = [Tableau(t)]
            except ValueError:
                pass

        if len(t) == 1:
            return Tableaux_all().element_class(Tableaux_all(), t[0])
        return TableauTuples_all().element_class(TableauTuples_all(), t)

    def __init__(self, parent, t, check=True):
        r"""
        Initialize a tableau.

        EXAMPLES::

            sage: t = TableauTuples( )([[[1,1],[1]],[[1,1,1]],[[1],[1],[1]]])
            sage: s = TableauTuples(3)([[[1,1],[1]],[[1,1,1]],[[1],[1],[1]]])
            sage: s == t
            True
            sage: t.parent()
            Tableau tuples
            sage: s.parent()
            Tableau tuples of level 3
            sage: r = TableauTuples()(s); r.parent()
            Tableau tuples
            sage: s is t # identical tableaux are distinct objects
            False
        """
        # By calling Tableau we implicitly check that the shape is a PartitionTuple
        t = [Tableau(s) for s in t]
        CombinatorialElement.__init__(self, parent, t)
        self._level = len(self._list)

    def _repr_(self):
        """
        The string representation of ``self``.

        EXAMPLES::

            sage: TableauTuple([[]])    # indirect doctest
            []
            sage: TableauTuple([[],[]])
            ([], [])
            sage: TableauTuple([[],[],[]])
            ([], [], [])
            sage: TableauTuple([[],[],[],[]])
            ([], [], [], [])
        """
        return self.parent().options._dispatch(self, '_repr_', 'display')

    def _repr_list(self):
        """
        Return a string representation of ``self`` as a list.

        EXAMPLES::

            sage: TableauTuple([[],[],[],[]])._repr_list()
            '([], [], [], [])'
        """
        return '(' + ', '.join('%s' % s for s in self) + ')'

    def _repr_compact(self):
        """
        Return a compact string representation of ``self``.

        EXAMPLES::

            sage: TableauTuple([[],[],[],[]])._repr_compact()
            '-|-|-|-'
            sage: TableauTuple([[[1,2,3],[4,5]],[],[[6]],[]])._repr_compact()
            '1,2,3/4,5|-|6|-'
        """
        return '|'.join('%s' % s._repr_compact() for s in self)

    def _repr_diagram(self):
        """
        Return a string representation of ``self`` as an array.

        EXAMPLES::

            sage: print(TableauTuple([[[2,3]],[[1]],[[4],[5]],[]])._repr_diagram())
              2  3     1     4     -
                             5
            sage: print(TableauTuple([[[2,3]],[],[[4],[5]],[]])._repr_diagram())
              2  3     -     4     -
                             5
            sage: TableauTuples.options(convention='French')
            sage: print(TableauTuple([[[2,3]],[[1]],[[4],[5]],[]])._repr_diagram())
                             5
              2  3     1     4     -
            sage: print(TableauTuple([[[2,3]],[],[[4],[5]],[]])._repr_diagram())
                             5
              2  3     -     4     -
            sage: TableauTuples.options._reset()

        TESTS:

        Check that :issue:`20768` is fixed::

            sage: T = TableauTuple([[[1,2,1],[1],[12345]], [], [[1523,1,2],[1,12341,-2]]])
            sage: T.pp()
                 1  2  1     -    1523     1  2
                 1                   1 12341 -2
             12345
        """
        str_tt = [T._repr_diagram().split('\n') for T in self]
        if TableauTuples.options('convention') == "French":
            for T_str in str_tt:
                T_str.reverse()
        widths = [len(T_str[0]) for T_str in str_tt]
        num_cols = max(len(T_str) for T_str in str_tt)

        diag = ['   '.join(' ' * widths[j] if i >= len(T_str) else
                           "{:<{width}}".format(T_str[i], width=widths[j])
                           for j, T_str in enumerate(str_tt))
                for i in range(num_cols)]

        if TableauTuples.options('convention') == "English":
            return '\n'.join(diag)
        else:
            return '\n'.join(diag[::-1])

    def _ascii_art_(self):
        """
        TESTS::

            sage: ascii_art(TableauTuple([[[2,3]],[],[[4],[5]],[]]))
              2  3     -     4     -
                             5
        """
        from sage.typeset.ascii_art import AsciiArt
        return AsciiArt(self._repr_diagram().splitlines())

    def _latex_(self):
        r"""
        Return a LaTeX version of ``self``.

        EXAMPLES::

            sage: t = TableauTuple([ [[1,2],[3]], [], [[4,5],[6,7]] ])
            sage: latex(t)    # indirect doctest
            \Bigg( {\def\lr#1{\multicolumn{1}{|@{\hspace{.6ex}}c@{\hspace{.6ex}}|}{\raisebox{-.3ex}{$#1$}}}
            \raisebox{-.6ex}{$\begin{array}[b]{*{2}c}\cline{1-2}
            \lr{1}&\lr{2}\\\cline{1-2}
            \lr{3}\\\cline{1-1}
            \end{array}$},\emptyset,\raisebox{-.6ex}{$\begin{array}[b]{*{2}c}\cline{1-2}
            \lr{4}&\lr{5}\\\cline{1-2}
            \lr{6}&\lr{7}\\\cline{1-2}
            \end{array}$}
            } \Bigg)
            sage: TableauTuples.options(convention='french')
            sage: latex(t)    # indirect doctest
            \Bigg( {\def\lr#1{\multicolumn{1}{|@{\hspace{.6ex}}c@{\hspace{.6ex}}|}{\raisebox{-.3ex}{$#1$}}}
            \raisebox{-.6ex}{$\begin{array}[t]{*{2}c}\cline{1-1}
            \lr{3}\\\cline{1-2}
            \lr{1}&\lr{2}\\\cline{1-2}
            \end{array}$},\emptyset,\raisebox{-.6ex}{$\begin{array}[t]{*{2}c}\cline{1-2}
            \lr{6}&\lr{7}\\\cline{1-2}
            \lr{4}&\lr{5}\\\cline{1-2}
            \end{array}$}
            } \Bigg)
            sage: TableauTuples.options._reset()
        """
        return self.parent().options._dispatch(self, '_latex_', 'latex')

    _latex_list = _repr_list

    def _latex_diagram(self):
        r"""
        Return a LaTeX representation of ``self`` as a Young diagram.

        EXAMPLES::

            sage: t = TableauTuple([ [[1,2],[3]], [], [[4,5],[6,7]] ])
            sage: print(t._latex_diagram())
            \Bigg( {\def\lr#1{\multicolumn{1}{|@{\hspace{.6ex}}c@{\hspace{.6ex}}|}{\raisebox{-.3ex}{$#1$}}}
            \raisebox{-.6ex}{$\begin{array}[b]{*{2}c}\cline{1-2}
            \lr{1}&\lr{2}\\\cline{1-2}
            \lr{3}\\\cline{1-1}
            \end{array}$},\emptyset,\raisebox{-.6ex}{$\begin{array}[b]{*{2}c}\cline{1-2}
            \lr{4}&\lr{5}\\\cline{1-2}
            \lr{6}&\lr{7}\\\cline{1-2}
            \end{array}$}
            } \Bigg)
        """
        from sage.combinat.output import tex_from_array_tuple
        return r'\Bigg( %s \Bigg)' % tex_from_array_tuple(self)

    def components(self):
        """
        Return a list of the components of tableau tuple ``self``.

        The `components` are the individual :class:`Tableau` which are
        contained in the tuple ``self``.

        For compatibility with :class:`TableauTuples` of :meth:`level` 1,
        :meth:`components` should be used to iterate over the components of
        :class:`TableauTuples`.

        EXAMPLES::

            sage: for t in TableauTuple([[1,2,3],[4,5]]).components(): t.pp()
              1  2  3
              4  5
            sage: for t in TableauTuple([ [[1,2,3],[4,5]], [[6,7],[8,9]] ]).components(): t.pp()
              1  2  3
              4  5
              6  7
              8  9
        """
        return list(self)

    def to_list(self):
        """
        Return the list representation of the tableaux tuple ``self``.

        EXAMPLES::

            sage: TableauTuple([ [[1,2,3],[4,5]], [[6,7],[8,9]] ]).to_list()
            [[[1, 2, 3], [4, 5]], [[6, 7], [8, 9]]]
        """
        return [t.to_list() for t in self]

    def __call__(self, *cell):
        r"""
        Get a cell in ``self``.

        INPUT:

        - ``self`` -- a tableau

        - ``cell`` -- a triple of integers, tuple, or list specifying a cell
          in ``self``

        OUTPUT: the value in the corresponding cell

        EXAMPLES::

            sage: t = TableauTuple([[[1,2,3],[4,5]],[[6,7]],[[8],[9]]])
            sage: t(1,0,0)
            6
            sage: t((1,0,0))
            6
            sage: t(3,3,3)
            Traceback (most recent call last):
            ...
            IndexError: the cell (3, 3, 3) is not contained in the tableau
        """
        if isinstance(cell[0], (int, Integer)):
            k, r, c = cell[0], cell[1], cell[2]
        else:
            k, r, c = cell[0]
        try:
            return self[k][r][c]
        except IndexError:
            raise IndexError("the cell (%s, %s, %s) is not contained in the tableau" % (k, r, c))

    def level(self):
        """
        Return the level of the tableau ``self``.

        This is just the number of components in the tableau tuple ``self``.

        EXAMPLES::

            sage: TableauTuple([[[7,8,9]],[],[[1,2,3],[4,5],[6]]]).level()
            3
        """
        return self._level

    def shape(self):
        r"""
        Return the :class:`PartitionTuple` which is the shape of the tableau
        tuple ``self``.

        EXAMPLES::

            sage: TableauTuple([[[7,8,9]],[],[[1,2,3],[4,5],[6]]]).shape()
            ([3], [], [3, 2, 1])
        """
        from sage.combinat.partition_tuple import PartitionTuples
        P = PartitionTuples()
        return P.element_class(P, [t.shape() for t in self])

    def size(self):
        """
        Return the size of the tableau tuple ``self``.

        This is just the number of boxes, or the size, of the underlying
        :class:`PartitionTuple`.

        EXAMPLES::

            sage: TableauTuple([[[7,8,9]],[],[[1,2,3],[4,5],[6]]]).size()
            9
        """
        return self.shape().size()

    def conjugate(self):
        r"""
        Return the conjugate of the tableau tuple ``self``.

        The conjugate tableau tuple `T'` is the :class:`TableauTuple`
        obtained from `T` by reversing the order of the components and
        conjugating each component -- that is, swapping the rows and
        columns of the all of :class:`Tableau` in `T` (see
        :meth:`sage.combinat.tableau.Tableau.conjugate`).

        EXAMPLES::

            sage: TableauTuple([[[1,2],[3,4]],[[5,6,7],[8]],[[9,10],[11],[12]]]).conjugate()
            ([[9, 11, 12], [10]], [[5, 8], [6], [7]], [[1, 3], [2, 4]])
        """
        conj = [t.conjugate() for t in reversed(self)]
        # attempt to return a tableau of the same type
        try:
            return self.parent()(conj)
        except Exception:
            try:
                return self.parent().element_class(self.parent(), conj)
            except Exception:
                return Tableau(conj)

    def pp(self):
        """
        Pretty printing for the tableau tuple ``self``.

        EXAMPLES::

            sage: TableauTuple([ [[1,2,3],[4,5]], [[1,2,3],[4,5]] ]).pp()
              1  2  3     1  2  3
              4  5        4  5
            sage: TableauTuple([ [[1,2],[3],[4]],[],[[6,7,8],[10,11],[12],[13]]]).pp()
              1  2     -     6  7  8
              3             10 11
              4             12
                            13
            sage: t = TableauTuple([ [[1,2,3],[4,5],[6],[9]], [[1,2,3],[4,5,8]], [[11,12,13],[14]] ])
            sage: t.pp()
              1  2  3     1  2  3    11 12 13
              4  5        4  5  8    14
              6
              9
            sage: TableauTuples.options(convention='french')
            sage: t.pp()
              9
              6
              4  5        4  5  8    14
              1  2  3     1  2  3    11 12 13
            sage: TableauTuples.options._reset()
        """
        print(self._repr_diagram())

    def to_word_by_row(self):
        """
        Return a word obtained from a row reading of the tableau tuple
        ``self``.

        EXAMPLES::

            sage: TableauTuple([[[1,2],[3,4]],[[5,6,7],[8]],[[9,10],[11],[12]]]).to_word_by_row()
            word: 12,11,9,10,8,5,6,7,3,4,1,2
        """
        w = []
        for t in self.components()[::-1]:
            for row in reversed(t):
                w += row
        return Word(w)

    # an alias -- should remove?
    to_word = to_word_by_row

    def to_word_by_column(self):
        """
        Return the word obtained from a column reading of the tableau tuple
        ``self``.

        EXAMPLES::

            sage: TableauTuple([[[1,2],[3,4]],[[5,6,7],[8]],[[9,10],[11],[12]]]).to_word_by_column()
            word: 12,11,9,10,8,5,6,7,3,1,4,2
        """
        w = []
        for t in self.conjugate():
            for row in t:
                w += row[::-1]
        return Word(w)

    def to_permutation(self):
        """
        Return a permutation with the entries in the tableau tuple ``self``.

        The permutation is obtained from ``self`` by reading the entries of the
        tableau tuple in order from left to right along the rows, and then
        top to bottom, in each component and then left to right along the
        components.

        EXAMPLES::

            sage: TableauTuple([[[1,2],[3,4]],[[5,6,7],[8]],[[9,10],[11],[12]]]).to_permutation()
            [12, 11, 9, 10, 8, 5, 6, 7, 3, 4, 1, 2]
        """
        return permutation.Permutation(self.to_word_by_row())

    def entries(self):
        """
        Return a sorted list of all entries of ``self``, in the order
        obtained by reading across the rows.

        EXAMPLES::

            sage: TableauTuple([[[1,2],[3,4]],[[5,6,7],[8]],[[9,10],[11],[12]]]).entries()
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            sage: TableauTuple([[[1,2],[3,4]],[[9,10],[11],[12]],[[5,6,7],[8]]]).entries()
            [1, 2, 3, 4, 9, 10, 11, 12, 5, 6, 7, 8]
        """
        return list(sum((s.entries() for s in self), ()))

    def entry(self, l, r, c):
        """
        Return the entry of the  cell ``(l, r, c)`` in ``self``.

        A cell is a tuple ``(l, r, c)`` of coordinates, where ``l`` is the
        component index, ``r`` is the row index, and ``c`` is the column index.

        EXAMPLES::

            sage: t = TableauTuple([[[1,2],[3,4]],[[5,6,7],[8]],[[9,10],[11],[12]]])
            sage: t.entry(1, 0, 0)
            5
            sage: t.entry(1, 1, 1)
            Traceback (most recent call last):
            ...
            IndexError: tuple index out of range
        """
        return self[l][r][c]

    def is_row_strict(self) -> bool:
        """
        Return ``True`` if the tableau ``self`` is row strict and ``False``
        otherwise.

        A tableau tuple is *row strict* if the entries in each row of each
        component are in increasing order, when read from left to right.

        EXAMPLES::

            sage: TableauTuple([[[5,7],[8]],[[1, 3], [2, 4]],[[6]]]).is_row_strict()
            True
            sage: TableauTuple([[[1, 2], [2, 4]],[[4,5,6],[7,8]]]).is_row_strict()
            True
            sage: TableauTuple([[[1]],[[2, 3], [2, 4]]]).is_row_strict()
            True
            sage: TableauTuple([[[1]],[[2, 2], [4,5]]]).is_row_strict()
            False
            sage: TableauTuple([[[1,2],[6,7]],[[4,8], [6, 9]],[]]).is_row_strict()
            True
        """
        return all(t.is_row_strict() for t in self)

    def first_row_descent(self):
        r"""
        Return the first cell of ``self`` that is not row standard.

        Cells are ordered left to right along the rows and then top to
        bottom. That is, the cell minimal `(k,r,c)` such that the entry in
        position `(k,r,c)` is bigger than the entry in position `(k,r,c+1)`.
        If there is no such cell then ``None`` is returned - in this
        case the tableau is row strict.

        OUTPUT:

        The cell corresponding to the first row descent or ``None``
        if the tableau is row strict.

        EXAMPLES::

            sage: TableauTuple([[[5,6,7],[1,2]],[[1,3,2],[4]]]).first_row_descent()
            (1, 0, 1)
            sage: TableauTuple([[[1,2,3],[4]],[[6,7,8],[1,2,3]],[[1,11]]]).first_row_descent() is None
            True
        """
        for k in range(len(self)):
            cell = self[k].first_row_descent()
            if cell is not None:
                return (k, cell[0], cell[1])
        return None

    def is_column_strict(self) -> bool:
        """
        Return ``True`` if the tableau ``self`` is column strict and ``False``
        otherwise.

        A tableau tuple is *column strict* if the entries in each column of
        each component are in increasing order, when read from top to bottom.

        EXAMPLES::

            sage: TableauTuple([[[5,7],[8]],[[1, 3], [2, 4]],[[6]]]).is_column_strict()
            True
            sage: TableauTuple([[[1, 2], [2, 4]],[[4,5,6],[7,8]]]).is_column_strict()
            True
            sage: TableauTuple([[[1]],[[2, 3], [2, 4]]]).is_column_strict()
            False
            sage: TableauTuple([[[1]],[[2, 2], [4,5]]]).is_column_strict()
            True
            sage: TableauTuple([[[1,2],[6,7]],[[4,8], [6, 9]],[]]).is_column_strict()
            True
        """
        return all(t.is_column_strict() for t in self)

    def first_column_descent(self):
        r"""
        Return the first cell of ``self`` is not column standard.

        Cells are ordered left to right along the rows and then top to
        bottom. That is, return the cell `(k,r,c)` with `(k,r,c)` minimal
        such that the entry in position `(k,r,c)` is bigger than the entry
        in position `(k,r,c+1)`. If there is no such cell then ``None``
        is returned - in this case the tableau is column strict.

        OUTPUT:

        The cell corresponding to the first column descent or ``None``
        if the tableau is column strict.

        EXAMPLES::

            sage: TableauTuple([[[3,5,6],[2,4,5]],[[1,4,5],[2,3]]]).first_column_descent()
            (0, 0, 0)
            sage: Tableau([[[1,2,3],[4]],[[5,6,7],[8,9]]]).first_column_descent() is None
            True
        """
        for k in range(len(self)):
            cell = self[k].first_column_descent()
            if cell is not None:
                return (k, cell[0], cell[1])
        return None

    def is_standard(self) -> bool:
        r"""
        Return ``True`` if the tableau ``self`` is a standard tableau and
        ``False`` otherwise.

        A tableau tuple is *standard* if it is row standard, column standard
        and the entries in the tableaux are `1, 2, \ldots, n`, where `n`
        is the :meth:`size` of the underlying partition tuple of ``self``.

        EXAMPLES::

            sage: TableauTuple([[[5,7],[8]],[[1, 3], [2, 4]],[[6]]]).is_standard()
            True
            sage: TableauTuple([[[1, 2], [2, 4]],[[4,5,6],[7,8]]]).is_standard()
            False
            sage: TableauTuple([[[1]],[[2, 3], [2, 4]]]).is_standard()
            False
            sage: TableauTuple([[[1]],[[2, 2], [4,5]]]).is_row_strict()
            False
            sage: TableauTuple([[[1,2],[6,7]],[[4,8], [6, 9]],[]]).is_standard()
            False
        """
        entries = sorted(self.entries())
        return entries == list(range(1, self.size() + 1)) and self.is_row_strict() and self.is_column_strict()

    def reduced_row_word(self):
        r"""
        Return the lexicographically minimal reduced expression for the
        permutation that maps the :meth:`initial_tableau` to ``self``.

        This reduced expression is a minimal length coset representative for the
        corresponding Young subgroup.  In one line notation, the permutation is
        obtained by concatenating the rows of the tableau from top to bottom in
        each component, and then left to right along the components.

        EXAMPLES::

            sage: StandardTableauTuple([[[1,2],[3]],[[4,5,6],[7,8],[9]]]).reduced_row_word()
            []
            sage: StandardTableauTuple([[[1,2],[3]],[[4,5,6],[7,9],[8]]]).reduced_row_word()
            [8]
            sage: StandardTableauTuple([[[1,2],[3]],[[4,5,7],[6,9],[8]]]).reduced_row_word()
            [6, 8]
            sage: StandardTableauTuple([[[1,2],[3]],[[4,5,8],[6,9],[7]]]).reduced_row_word()
            [6, 8, 7]
            sage: StandardTableauTuple([[[1,2],[3]],[[4,5,9],[6,8],[7]]]).reduced_row_word()
            [6, 7, 8, 7]
            sage: StandardTableauTuple([[[7,9],[8]],[[1,3,5],[2,6],[4]]]).reduced_row_word()
            [2, 3, 2, 1, 4, 3, 2, 5, 4, 3, 6, 5, 4, 3, 2, 7, 6, 5, 8, 7, 6, 5, 4]
        """
        from sage.combinat.permutation import Permutation
        return Permutation(list(self.entries())).inverse().reduced_word_lexmin()

    def reduced_column_word(self):
        r"""
        Return the lexicographically minimal reduced expression for the
        permutation that maps the :meth:`initial_column_tableau` to ``self``.

        This reduced expression is a minimal length coset representative for the
        corresponding Young subgroup.  In one line notation, the permutation is
        obtained by concatenating the rows of the tableau from top to bottom in
        each component, and then left to right along the components.

        EXAMPLES::

            sage: StandardTableauTuple([[[7,9],[8]],[[1,4,6],[2,5],[3]]]).reduced_column_word()
            []
            sage: StandardTableauTuple([[[7,9],[8]],[[1,3,6],[2,5],[4]]]).reduced_column_word()
            [3]
            sage: StandardTableauTuple([[[6,9],[8]],[[1,3,7],[2,5],[4]]]).reduced_column_word()
            [3, 6]
            sage: StandardTableauTuple([[[6,8],[9]],[[1,3,7],[2,5],[4]]]).reduced_column_word()
            [3, 6, 8]
            sage: StandardTableauTuple([[[5,8],[9]],[[1,3,7],[2,6],[4]]]).reduced_column_word()
            [3, 6, 5, 8]
        """
        from sage.combinat.permutation import Permutation
        return Permutation(list(self.conjugate().entries())).inverse().reduced_word_lexmin()

    def cells_containing(self, m):
        r"""
        Return the list of cells in which the letter ``m`` appears in the
        tableau ``self``.

        The list is ordered with cells appearing from left to right.

        EXAMPLES::

            sage: t = TableauTuple([[[4,5]],[[1,1,2,4],[2,4,4],[4]],[[1,3,4],[3,4]]])
            sage: t.cells_containing(4)
            [(0, 0, 0),
              (1, 2, 0),
              (1, 1, 1),
              (1, 1, 2),
              (1, 0, 3),
              (2, 1, 1),
              (2, 0, 2)]
            sage: t.cells_containing(6)
            []
        """
        return [(k, r, c) for k in range(len(self))
                for (r, c) in self[k].cells_containing(m)]

    def up(self, n=None):
        """
        An iterator for all the :class:`TableauTuple` that can be obtained
        from ``self`` by adding a cell with the label ``n``. If ``n`` is not
        specified then a cell with label ``n`` will be added to the tableau
        tuple, where ``n-1`` is the size of the tableau tuple before any cells
        are added.

        EXAMPLES::

            sage: list(TableauTuple([[[1,2]],[[3]]]).up())
            [([[1, 2, 4]], [[3]]),
              ([[1, 2], [4]], [[3]]),
              ([[1, 2]], [[3, 4]]),
              ([[1, 2]], [[3], [4]])]
        """
        if n is None:
            n = self.size()

        # Go through and add n+1 to the end of each of the rows
        # (We could call shape().addable_cells() but this seems more efficient)
        for k in range(len(self)):
            for row in range(len(self[k])):
                if row == 0 or self.shape()[k][row] < self.shape()[k][row - 1]:
                    new_t = self.to_list()  # a copy
                    new_t[k][row].append(n + 1)
                    yield StandardTableauTuple(new_t)
            # now add node to last row
            new_t = self.to_list()  # a copy
            new_t[k].append([n + 1])
            yield StandardTableauTuple(new_t)

    def row_stabilizer(self):
        """
        Return the :class:`PermutationGroup` corresponding to ``self``. That
        is, return subgroup of the symmetric group of degree :meth:`size`
        which is the row stabilizer of ``self``.

        EXAMPLES::

            sage: # needs sage.groups
            sage: t = TableauTuple([[[1,2,3],[4,5]],[[6,7]],[[8],[9]]])
            sage: rs = t.row_stabilizer()
            sage: rs.order()
            24
            sage: PermutationGroupElement([(1,3,2),(4,5)]) in rs
            True
            sage: PermutationGroupElement([(1,4)]) in rs
            False
            sage: rs.one().domain()
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        """
        # Ensure that the permutations involve all elements of the
        # tableau, by including the identity permutation on the set [1..n].
        n = max(self.entries())
        gens = [list(range(1, n + 1))]
        gens.extend((ti[j], ti[j + 1]) for t in self
                    for ti in t for j in range(len(ti) - 1))
        return PermutationGroup(gens)

    def column_stabilizer(self):
        """
        Return the :class:`PermutationGroup` corresponding to ``self``. That
        is, return subgroup of the symmetric group of degree :meth:`size`
        which is the column stabilizer of ``self``.

        EXAMPLES::

            sage: # needs sage.groups
            sage: t = TableauTuple([[[1,2,3],[4,5]],[[6,7]],[[8],[9]]])
            sage: cs = t.column_stabilizer()
            sage: cs.order()
            8
            sage: PermutationGroupElement([(1,3,2),(4,5)]) in cs
            False
            sage: PermutationGroupElement([(1,4)]) in cs
            True
        """

        return self.conjugate().row_stabilizer()

    def charge(self):
        r"""
        Return the charge of the reading word of ``self``.

        See :meth:`~sage.combinat.words.finite_word.FiniteWord_class.charge`
        for more information.

        EXAMPLES::

            sage: TableauTuple([[[4,5]],[[1,1,2,4],[2,4,4],[4]],[[1,3,4],[3,4]]]).charge()
            4
        """
        return self.to_word_by_row().charge()

    def cocharge(self):
        r"""
        Return the cocharge of the reading word of ``self``.

        See :meth:`~sage.combinat.words.finite_word.FiniteWord_class.cocharge`
        for more information.

        EXAMPLES::

            sage: TableauTuple([[[4,5]],[[1,1,2,4],[2,4,4],[4]],[[1,3,4],[3,4]]]).charge()
            4
        """
        return self.to_word_by_row().cocharge()

    def add_entry(self, cell, m):
        """
        Set the entry in ``cell`` equal to ``m``. If the cell does not exist
        then extend the tableau, otherwise just replace the entry.

        EXAMPLES::

            sage: s = StandardTableauTuple([ [[3,4,7],[6,8]], [[9,13],[12]], [[1,5],[2,11],[10]] ]); s.pp()
              3  4  7     9 13     1  5
              6  8       12        2 11
                                  10
            sage: t = s.add_entry( (0,0,3),14); t.pp(); t.category()
              3  4  7 14     9 13     1  5
              6  8          12        2 11
                                     10
            Category of elements of Standard tableau tuples
            sage: t = s.add_entry( (0,0,3),15); t.pp(); t.category()
              3  4  7 15     9 13     1  5
              6  8          12        2 11
                                     10
            Category of elements of Tableau tuples
            sage: t = s.add_entry( (1,1,1),14); t.pp(); t.category()
              3  4  7     9 13     1  5
              6  8       12 14     2 11
                                  10
            Category of elements of Standard tableau tuples
            sage: t = s.add_entry( (2,1,1),14); t.pp(); t.category()
              3  4  7     9 13     1  5
              6  8       12        2 14
                                  10
            Category of elements of Tableau tuples
            sage: t = s.add_entry( (2,1,2),14); t.pp(); t.category()
            Traceback (most recent call last):
            ...
            IndexError: (2, 1, 2) is not an addable cell of the tableau
        """
        k, r, c = cell
        tab = self.to_list()

        try:
            tab[k][r][c] = m
        except IndexError:
            if (k, r, c) in self.shape().addable_cells():
                # add (k,r,c) is an addable cell the following should work
                # so we do not need to trap anything
                if r == len(tab[k]):
                    tab[k].append([])

                tab[k][r].append(m)
            else:
                raise IndexError(f'{(k,r,c)} is not an addable cell of the tableau')

        # finally, try and return a tableau belonging to the same category
        try:
            return self.parent()(tab)
        except ValueError:
            try:
                return self.parent().element_class(self.parent(), tab)
            except ValueError:
                return TableauTuple(tab)

    def restrict(self, m=None):
        """
        Return the restriction of the standard tableau ``self`` to ``m``.

        The restriction is the subtableau of ``self`` whose entries are less
        than or equal to ``m``.

        By default, ``m`` is one less than the current size.

        EXAMPLES::

            sage: TableauTuple([[[5]],[[1,2],[3,4]]]).restrict()
            ([], [[1, 2], [3, 4]])
            sage: TableauTuple([[[5]],[[1,2],[3,4]]]).restrict(6)
            ([[5]], [[1, 2], [3, 4]])
            sage: TableauTuple([[[5]],[[1,2],[3,4]]]).restrict(5)
            ([[5]], [[1, 2], [3, 4]])
            sage: TableauTuple([[[5]],[[1,2],[3,4]]]).restrict(4)
            ([], [[1, 2], [3, 4]])
            sage: TableauTuple([[[5]],[[1,2],[3,4]]]).restrict(3)
            ([], [[1, 2], [3]])
            sage: TableauTuple([[[5]],[[1,2],[3,4]]]).restrict(2)
            ([], [[1, 2]])
            sage: TableauTuple([[[5]],[[1,2],[3,4]]]).restrict(1)
            ([], [[1]])
            sage: TableauTuple([[[5]],[[1,2],[3,4]]]).restrict(0)
            ([], [])

        Where possible the restricted tableau belongs to the same category as
        the original tableaux::

            sage: TableauTuple([[[5]],[[1,2],[3,4]]]).restrict(3).category()
            Category of elements of Tableau tuples
            sage: TableauTuple([[[5]],[[1,2],[3,4]]]).restrict(3).category()
            Category of elements of Tableau tuples
            sage: TableauTuples(level=2)([[[5]],[[1,2],[3,4]]]).restrict(3).category()
            Category of elements of Tableau tuples of level 2
        """
        if m is None:
            m = self.size() - 1
        # We are lucky in that currently restriction is defined for arbitrary
        # (level one) tableau and not just standard ones. If this ever changes
        # we will have to treat the cases where the components restrict to
        # empty lists of the form [[]] separately.
        tab = [t.restrict(m) for t in self]
        try:
            return self.parent()(tab)
        except ValueError:
            try:
                return self.parent().Element(tab)
            except ValueError:
                return TableauTuple(tab)

    def symmetric_group_action_on_entries(self, w):
        r"""
        Return the action of a permutation ``w`` on ``self``.

        Consider a standard tableau tuple
        `T = (t^{(1)}, t^{(2)}, \ldots t^{(l)})` of size `n`, then the
        action of `w \in S_n` is defined by permuting the entries of `T`
        (recall they are `1, 2, \ldots, n`). In particular, suppose the entry
        at cell `(k, i, j)` is `a`, then the entry becomes `w(a)`. In general,
        the resulting tableau tuple `wT` may *not* be standard.

        INPUT:

        - ``w`` -- a permutation

        EXAMPLES::

            sage: TableauTuple([[[1,2],[4]],[[3,5]]]).symmetric_group_action_on_entries( Permutation(((4,5))) )
            ([[1, 2], [5]], [[3, 4]])
            sage: TableauTuple([[[1,2],[4]],[[3,5]]]).symmetric_group_action_on_entries( Permutation(((1,2))) )
            ([[2, 1], [4]], [[3, 5]])
        """
        w = w + [i + 1 for i in range(len(w), self.size())]  # need to ensure that it belongs to Sym_size
        try:
            return self.parent()([[[w[entry - 1] for entry in row] for row in t] for t in self])
        except ValueError:
            return TableauTuples()([[[w[entry - 1] for entry in row] for row in t] for t in self])

    def content(self, k, multicharge):
        r"""
        Return the content ``k`` in ``self``.

        The content of `k` in a standard tableau. That is, if
        `k` appears in row `r` and column `c` of the tableau, then
        we return `c - r + a_k`, where the multicharge is
        `(a_1, a_2, \ldots, a_l)` and `l` is the level of the tableau.

        The multicharge determines the dominant weight

        .. MATH::

            \Lambda = \sum_{i=1}^l \Lambda_{a_i}

        of the affine special linear group. In the combinatorics, the
        multicharge simply offsets the contents in each component so that
        the cell `(k, r, c)` has content `a_k + c - r`.

        INPUT:

        - ``k`` -- integer in `\{1, 2, \ldots, n\}`
        - ``multicharge`` -- a sequence of integers of length `l`

        Here `l` is the :meth:`~TableauTuple.level` and `n` is the
        :meth:`~TableauTuple.size` of ``self``.

        EXAMPLES::

            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).content(3,[0,0])
            -1
            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).content(3,[0,1])
            0
            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).content(3,[0,2])
            1
            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).content(6,[0,2])
            Traceback (most recent call last):
            ...
            ValueError: 6 must be contained in the tableaux
        """
        for l, tableau in enumerate(self):
            for r, row in enumerate(tableau):
                try:
                    return multicharge[l] - r + row.index(k)
                except ValueError:
                    ValueError
        raise ValueError('%s must be contained in the tableaux' % k)

    def residue(self, k, e, multicharge):
        r"""
        Return the *residue* of the integer ``k`` in the tableau ``self``.

        The *residue* of `k` is `c - r + a_k` in `\ZZ / e\ZZ`, where `k`
        appears in row `r` and column `c` of the tableau and
        the multicharge is `(a_1, a_2, \ldots, a_l)`.

        The multicharge determines the dominant weight

        .. MATH::

            \sum_{i=1}^l \Lambda_{a_i}

        for the affine special linear group. In the combinatorics, it simply
        offsets the contents in each component so that the cell `(k, 0, 0)`
        has content `a_k`.

        INPUT:

        - ``k`` -- integer in `\{1, 2, \ldots, n\}`
        - ``e`` -- integer in `\{0, 2, 3, 4, 5, \ldots\}`
        - ``multicharge`` -- list of integers of length `l`

        Here `l` is the :meth:`~TableauTuple.level` and `n` is the
        :meth:`~TableauTuple.size` of ``self``.

        OUTPUT: the residue of ``k`` in a standard tableau. That is,

        EXAMPLES::

            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).residue(1, 3,[0,0])
            0
            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).residue(1, 3,[0,1])
            1
            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).residue(1, 3,[0,2])
            2
            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).residue(6, 3,[0,2])
            Traceback (most recent call last):
            ...
            ValueError: 6 must be contained in the tableaux
        """
        for l, tableau in enumerate(self):
            for r, row in enumerate(tableau):
                try:
                    return IntegerModRing(e)(multicharge[l] - r + row.index(k))
                except ValueError:
                    pass
        raise ValueError('%s must be contained in the tableaux' % k)


# -------------------------------------------------
# Row standard tableau tuple - element class
# -------------------------------------------------
class RowStandardTableauTuple(TableauTuple, metaclass=ClasscallMetaclass):
    r"""
    A class for row standard tableau tuples of shape a partition tuple.

    A row standard tableau tuple of size `n` is an ordered tuple of row
    standard tableaux (see :class:`RowStandardTableau`), with entries `1, 2,
    \ldots, n` such that, in each component, the entries are in increasing
    order along each row. If the tableau in component `k` has shape
    `\lambda^{(k)}` then `\lambda=(\lambda^{(1)},\ldots,\lambda^{(l)}` is a
    :class:`PartitionTuple`.

    .. NOTE::

        The tableaux appearing in a :class:`RowStandardTableauTuple` are row
        strict, but individually they are not standard tableaux because the
        entries in any single component of a :class:`RowStandardTableauTuple`
        will typically not be in bijection with `\{1, 2, \ldots, n\}`.

    INPUT:

    - ``t`` -- a tableau, a list of (standard) tableau or an equivalent list

    OUTPUT: a :class:`RowStandardTableauTuple` object constructed from ``t``

    .. NOTE::

        Sage uses the English convention for (tuples of) partitions and
        tableaux: the longer rows are displayed on top.  As with
        :class:`PartitionTuple`, in sage the cells, or nodes, of partition
        tuples are 0-based. For example, the (lexicographically) first cell in
        any non-empty partition tuple is `[0,0,0]`. Further, the coordinates
        ``[k,r,c]`` in a :class:`TableauTuple` refer to the component, row and
        column indices, respectively.

    EXAMPLES::

        sage: t = RowStandardTableauTuple([[[4,7],[3]],[[2,6,8],[1,5]],[[9]]]); t
        ([[4, 7], [3]], [[2, 6, 8], [1, 5]], [[9]])
        sage: t.pp()
          4  7     2  6  8     9
          3        1  5
        sage: t.shape()
        ([2, 1], [3, 2], [1])
        sage: t[0].pp()  # pretty printing
          4  7
          3
        sage: t.is_row_strict()
        True
        sage: t[0].is_standard()
        False
        sage: RowStandardTableauTuple([[],[],[]]) # An empty tableau tuple
        ([], [], [])
        sage: RowStandardTableauTuple([[[4,5],[6]],[[1,2,3]]]) in StandardTableauTuples()
        True
        sage: RowStandardTableauTuple([[[5,6],[4]],[[1,2,3]]]) in StandardTableauTuples()
        False

    When using code that will generate a lot of tableaux, it is slightly more
    efficient to construct a :class:`RowStandardTableauTuple` from the
    appropriate parent object::

        sage: RST = RowStandardTableauTuples()
        sage: RST([[[4,5],[7]],[[1,2,3],[6,8]],[[9]]])
        ([[4, 5], [7]], [[1, 2, 3], [6, 8]], [[9]])

    .. SEEALSO::

        - :class:`RowTableau`
        - :class:`RowTableaux`
        - :class:`TableauTuples`
        - :class:`TableauTuple`
        - :class:`StandardTableauTuples`
        - :class:`StandardTableauTuple`
        - :class:`RowStandardTableauTuples`

    TESTS::

        sage: RowStandardTableauTuple( [[3, 4, 5],[1, 2]] ).category()  # indirect doctest
        Category of elements of Row standard tableaux
        sage: RowStandardTableauTuple([[[3,4,5],[1,2]]]).category()  # indirect doctest
        Category of elements of Row standard tableaux
        sage: RowStandardTableauTuples()([[[3,4,5],[1,2]]]).category()  # indirect doctest
        Category of elements of Row standard tableaux

        sage: RowStandardTableauTuple([[[1,2,3]],[[1]]])
        Traceback (most recent call last):
        ...
        ValueError: entries must be in bijection with {1,2,...,n}

        sage: RowStandardTableauTuple([[],[[1,2,1]]])
        Traceback (most recent call last):
        ...
        ValueError: tableaux must be row strict

        sage: RowStandardTableauTuple([ [[1,2,4],[6]],[[0,1]],[[10]] ])
        Traceback (most recent call last):
        ...
        ValueError: entries must be in bijection with {1,2,...,n}

        sage: TestSuite(  RowStandardTableauTuple([[[3,4,6],[1]],[[2],[5]]]) ).run()
        sage: TestSuite(  RowStandardTableauTuple([[[3,4,6],[1]],[], [[2],[5]]]) ).run()
        sage: TestSuite(  RowStandardTableauTuple([[[3,4,6],[1]],[[7]], [[2],[5]]]) ).run()
    """
    @staticmethod
    def __classcall_private__(self, t):
        r"""
        This ensures that a :class:`RowStandardTableauTuple` is only constructed
        as an ``element_class()`` call of an appropriate parent.

        EXAMPLES::

            sage: t = RowStandardTableauTuple([[[3,4,6],[1]],[[2],[5]]])
            sage: t.parent()
            Row standard tableau tuples
            sage: t.category()
            Category of elements of Row standard tableau tuples
            sage: type(t)
            <class 'sage.combinat.tableau_tuple.RowStandardTableauTuples_all_with_category.element_class'>
            sage: RowStandardTableauTuples(level=2)(t).parent()
            Row standard tableau tuples of level 2
            sage: RowStandardTableauTuples(level=2, size=6)(t).parent()                 # needs sage.libs.flint
            Row standard tableau tuples of level 2 and size 6
        """
        if isinstance(t, (RowStandardTableau, RowStandardTableauTuple)):
            return t

        # The Tableau class is very general in that it allows the entries of a
        # tableau to be almost anything, including lists. For this reason we
        # first try and interpret t as a tuple of tableaux and if this fails we
        # then try to think of t as a tableau.
        try:
            t = [Tableau(s) for s in t]
        except (TypeError, ValueError):
            try:
                t = [RowStandardTableau(t)]
            except ValueError:
                pass

        if len(t) == 1:
            P = RowStandardTableaux_all()
            return P.element_class(P, t[0])
        P = RowStandardTableauTuples_all()
        return P.element_class(P, t)

    def __init__(self, parent, t, check=True):
        r"""
        Initialize a row standard tableau tuple.

        EXAMPLES::

            sage: t = RowStandardTableauTuples()([[[1,4],[2]],[[3]]])
            sage: s = TableauTuples(2)([[[1,4],[2]],[[3]]])
            sage: s == t
            True
            sage: s.parent()
            Tableau tuples of level 2
            sage: r = RowStandardTableauTuples(level=2)(t); r.parent()
            Row standard tableau tuples of level 2
            sage: isinstance(r, RowStandardTableauTuple)
            True
            sage: r in RowStandardTableauTuples()
            True
            sage: r in RowStandardTableauTuples(level=2)
            True
            sage: r in RowStandardTableauTuples(level=3)
            False
        """
        # Morally, a level 1 tableau should never end up here, however, in
        # practice it can because the RowStandardTableauTuples() iterator, for
        # example, generates RowStandardTableauTuples of level 1. These tableaux
        # should have RowStandardTableauTuples as their parent so we have to cope
        # with level 1 tableau after all.
        try:
            t = [Tableau(s) for s in t]
        except (TypeError, ValueError):
            try:
                t = [Tableau(t)]
            except ValueError:
                raise ValueError('not a valid row standard tableau tuple')

        super().__init__(parent, t)

        if check:
            # We still have to check that t is row standard.
            if not all(s.is_row_strict() for s in t):
                raise ValueError('tableaux must be row strict')

            # Finally, the more costly check that the entries are {1,2...n}
            entries = sorted(sum((s.entries() for s in t), ()))
            if not entries == list(range(1, len(entries) + 1)):
                raise ValueError('entries must be in bijection with {1,2,...,n}')

    def inverse(self, k):
        """
        Return the cell containing ``k`` in the tableau tuple ``self``.

        EXAMPLES::

            sage: RowStandardTableauTuple([[[3,4],[1,2]],[[5,6,7],[8]],[[9,10],[11],[12]]]).inverse(1)
            (0, 1, 0)
            sage: RowStandardTableauTuple([[[3,4],[1,2]],[[5,6,7],[8]],[[9,10],[11],[12]]]).inverse(2)
            (0, 1, 1)
            sage: RowStandardTableauTuple([[[3,4],[1,2]],[[5,6,7],[8]],[[9,10],[11],[12]]]).inverse(3)
            (0, 0, 0)
            sage: RowStandardTableauTuple([[[3,4],[1,2]],[[5,6,7],[8]],[[9,10],[11],[12]]]).inverse(4)
            (0, 0, 1)
            sage: StandardTableauTuple([[[1,2],[3,4]],[[5,6,7],[8]],[[9,10],[11],[12]]]).inverse(1)
            (0, 0, 0)
            sage: StandardTableauTuple([[[1,2],[3,4]],[[5,6,7],[8]],[[9,10],[11],[12]]]).inverse(2)
            (0, 0, 1)
            sage: StandardTableauTuple([[[1,2],[3,4]],[[5,6,7],[8]],[[9,10],[11],[12]]]).inverse(3)
            (0, 1, 0)
            sage: StandardTableauTuple([[[1,2],[3,4]],[[5,6,7],[8]],[[9,10],[11],[12]]]).inverse(12)
            (2, 2, 0)
        """
        for l in range(len(self)):
            for row in range(len(self[l])):
                try:
                    return (l, row, self[l][row].index(k))
                except ValueError:
                    pass
        raise ValueError('%s must be contained in the tableaux' % k)

    def residue_sequence(self, e, multicharge):
        r"""
        Return the :class:`sage.combinat.tableau_residues.ResidueSequence`
        of ``self``.

        INPUT:

        - ``e`` -- integer in `\{0, 2, 3, 4, 5, \ldots\}`
        - ``multicharge`` -- a sequence of integers of length equal
          to the level/length of ``self``

        OUTPUT:

        The :class:`residue sequence
        <sage.combinat.tableau_residues.ResidueSequence>` of the tableau.

        EXAMPLES::

            sage: RowStandardTableauTuple([[[5]],[[3,4],[1,2]]]).residue_sequence(3,[0,0])
            3-residue sequence (2,0,0,1,0) with multicharge (0,0)
            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).residue_sequence(3,[0,1])
            3-residue sequence (1,2,0,1,0) with multicharge (0,1)
            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).residue_sequence(3,[0,2])
            3-residue sequence (2,0,1,2,0) with multicharge (0,2)
        """
        res = [0] * self.size()
        for (k, r, c) in self.shape().cells():
            res[self[k][r][c] - 1] = multicharge[k] - r + c
        from sage.combinat.tableau_residues import ResidueSequence
        return ResidueSequence(e, multicharge, res, check=False)

    def degree(self, e, multicharge):
        r"""
        Return the Brundan-Kleshchev-Wang [BKW2011]_ degree of ``self``.

        The *degree* of a tableau is an integer that is defined recursively by
        successively stripping off the number `k`, for `k = n, n-1, \ldots, 1`,
        and at stage adding the count of the number of addable cell of the same
        residue minus the number of removable cells of them same residue as `k`
        and that are below `k` in the diagram.

        Note that even though this degree function was defined by
        Brundan-Kleshchev-Wang [BKW2011]_ the underlying combinatorics
        is much older, going back at least to Misra and Miwa.

        The degrees of the tableau `T` gives the degree of the homogeneous
        basis element of the graded Specht module which is indexed by `T`.

        INPUT:

        - ``e`` -- the *quantum characteristic* ``e``
        - ``multicharge`` -- (default: ``[0]``) the multicharge

        OUTPUT: the degree of the tableau ``self``, which is an integer

        EXAMPLES::

            sage: StandardTableauTuple([[[1]], [], []]).degree(0,(0,0,0))
            2
            sage: StandardTableauTuple([[],[[1]], []]).degree(0,(0,0,0))
            1
            sage: StandardTableauTuple([[], [], [[1]]]).degree(0,(0,0,0))
            0
            sage: StandardTableauTuple([[[1]],[[2]], []]).degree(0,(0,0,0))
            3
            sage: StandardTableauTuple([[[1]], [], [[2]]]).degree(0,(0,0,0))
            2
            sage: StandardTableauTuple([[],[[1]], [[2]]]).degree(0,(0,0,0))
            1
            sage: StandardTableauTuple([[[2]],[[1]], []]).degree(0,(0,0,0))
            1
            sage: StandardTableauTuple([[[2]], [], [[1]]]).degree(0,(0,0,0))
            0
            sage: StandardTableauTuple([[],[[2]], [[1]]]).degree(0,(0,0,0))
            -1
        """
        shape = self.shape()
        deg = shape._initial_degree(e, multicharge)
        res = shape.initial_tableau().residue_sequence(e, multicharge)
        for r in self.reduced_row_word():
            if res[r] == res[r + 1]:
                deg -= 2
            elif res[r] == res[r + 1] + 1 or res[r] == res[r + 1] - 1:
                deg += (e == 2 and 2 or 1)
            res = res.swap_residues(r, r + 1)
        return deg

    def codegree(self, e, multicharge):
        r"""
        Return the Brundan-Kleshchev-Wang [BKW2011]_ codegree of ``self``.

        The *codegree* of a tableau is an integer that is defined
        recursively by successively stripping off the number `k`, for
        `k = n, n-1, \ldots, 1` and at stage adding the number of addable
        cell of the same residue minus the number of removable cells of
        the same residue as `k` and which are above `k` in the diagram.

        The codegree of the tableau ``self`` gives the degree of  "dual"
        homogeneous basis element of the graded Specht module which is
        indexed by ``self``.

        INPUT:

        - ``e`` -- the *quantum characteristic*
        - ``multicharge`` -- the multicharge

        OUTPUT: the codegree of the tableau ``self``, which is an integer

        EXAMPLES::

            sage: StandardTableauTuple([[[1]], [], []]).codegree(0,(0,0,0))
            0
            sage: StandardTableauTuple([[],[[1]], []]).codegree(0,(0,0,0))
            1
            sage: StandardTableauTuple([[], [], [[1]]]).codegree(0,(0,0,0))
            2
            sage: StandardTableauTuple([[[1]],[[2]], []]).codegree(0,(0,0,0))
            -1
            sage: StandardTableauTuple([[[1]], [], [[2]]]).codegree(0,(0,0,0))
            0
            sage: StandardTableauTuple([[],[[1]], [[2]]]).codegree(0,(0,0,0))
            1
            sage: StandardTableauTuple([[[2]],[[1]], []]).codegree(0,(0,0,0))
            1
            sage: StandardTableauTuple([[[2]], [], [[1]]]).codegree(0,(0,0,0))
            2
            sage: StandardTableauTuple([[],[[2]], [[1]]]).codegree(0,(0,0,0))
            3
        """
        if not self:  # the trivial case
            return 0

        conj_shape = self.shape().conjugate()
        codeg = conj_shape._initial_degree(e, tuple(-r for r in multicharge))
        res = self.shape().initial_column_tableau().residue_sequence(e, multicharge)
        for r in self.reduced_column_word():
            if res[r] == res[r + 1]:
                codeg -= 2
            elif res[r] == res[r + 1] + 1 or res[r] == res[r + 1] - 1:
                codeg += (e == 2 and 2 or 1)
            res = res.swap_residues(r, r + 1)
        return codeg


# -------------------------------------------------
# Standard tableau tuple - element class
# -------------------------------------------------
class StandardTableauTuple(RowStandardTableauTuple):
    r"""
    A class to model a standard tableau of shape a partition tuple. This is
    a tuple of standard tableau with entries `1, 2, \ldots, n`, where `n`
    is the size of the underlying partition tuple, such that the entries
    increase along rows and down columns in each component of the tuple.

            sage: s = StandardTableauTuple([[1,2,3],[4,5]])
            sage: t = StandardTableauTuple([[1,2],[3,5],[4]])
            sage: s.dominates(t)
            True
            sage: t.dominates(s)
            False
            sage: StandardTableauTuple([[1,2,3],[4,5]]) in RowStandardTableauTuples()
            True

        The tableaux appearing in a :class:`StandardTableauTuple` are
        both row and column strict, but individually they are not standard
        tableaux because the entries in any single component of a
        :class:`StandardTableauTuple` will typically not be in bijection with
        `\{1, 2, \ldots, n\}`.

    INPUT:

    - ``t`` -- a tableau, a list of (standard) tableau or an equivalent list

    OUTPUT: a :class:`StandardTableauTuple` object constructed from ``t``

    .. NOTE::

        Sage uses the English convention for (tuples of) partitions and
        tableaux: the longer rows are displayed on top.  As with
        :class:`PartitionTuple`, in sage the cells, or nodes, of partition
        tuples are 0-based. For example, the (lexicographically) first cell in
        any non-empty partition tuple is `[0,0,0]`. Further, the coordinates
        ``[k,r,c]`` in a :class:`TableauTuple` refer to the component, row and
        column indices, respectively.

    EXAMPLES::

        sage: t = TableauTuple([ [[1,3,4],[7,9]], [[2,8,11],[6]], [[5,10]] ])
        sage: t
        ([[1, 3, 4], [7, 9]], [[2, 8, 11], [6]], [[5, 10]])
        sage: t[0][0][0]
        1
        sage: t[1][1][0]
        6
        sage: t[2][0][0]
        5
        sage: t[2][0][1]
        10

        sage: t = StandardTableauTuple([[[4,5],[7]],[[1,2,3],[6,8]],[[9]]]); t
        ([[4, 5], [7]], [[1, 2, 3], [6, 8]], [[9]])
        sage: t.pp()
          4  5     1  2  3     9
          7        6  8
        sage: t.shape()
        ([2, 1], [3, 2], [1])
        sage: t[0].pp()  # pretty printing
          4  5
          7
        sage: t.is_standard()
        True
        sage: t[0].is_standard()
        False
        sage: StandardTableauTuple([[],[],[]]) # An empty tableau tuple
        ([], [], [])

    When using code that will generate a lot of tableaux, it is slightly more
    efficient to construct a :class:`StandardTableauTuple` from the
    appropriate parent object::

        sage: STT = StandardTableauTuples()
        sage: STT([[[4,5],[7]],[[1,2,3],[6,8]],[[9]]])
        ([[4, 5], [7]], [[1, 2, 3], [6, 8]], [[9]])

    .. SEEALSO::

        - :class:`Tableau`
        - :class:`Tableaux`
        - :class:`TableauTuples`
        - :class:`TableauTuple`
        - :class:`StandardTableauTuples`

    TESTS::

        sage: StandardTableauTuple( [[1,2,3],[4,5]] ).category()  # indirect doctest
        Category of elements of Standard tableaux
        sage: StandardTableauTuple([[[1,2,3],[4,5]]]).category()  # indirect doctest
        Category of elements of Standard tableaux
        sage: StandardTableauTuples()([[[1,2,3],[4,5]]]).category()  # indirect doctest
        Category of elements of Standard tableaux

        sage: StandardTableauTuple([[[1,2,3]],[[1]]])
        Traceback (most recent call last):
        ...
        ValueError: entries must be in bijection with {1,2,...,n}

        sage: StandardTableauTuple([[],[[1,2,1]]])
        Traceback (most recent call last):
        ...
        ValueError: tableaux must be row strict

        sage: StandardTableauTuple([ [[1,2,4],[6]],[[0,1]],[[10]] ])
        Traceback (most recent call last):
        ...
        ValueError: entries must be in bijection with {1,2,...,n}

        sage: TestSuite(  StandardTableauTuple([[[1,3,4],[6]],[[2],[5]]]) ).run()
        sage: TestSuite(  StandardTableauTuple([[[1,3,4],[6]],[], [[2],[5]]]) ).run()
        sage: TestSuite(  StandardTableauTuple([[[1,3,4],[6]],[[7]], [[2],[5]]]) ).run()
    """
    @staticmethod
    def __classcall_private__(self, t):
        r"""
        This ensures that a :class:`StandardTableau` is only ever constructed
        as an ``element_class()`` call of an appropriate parent.

        EXAMPLES::

            sage: t = StandardTableauTuple([[[1,3,4],[6]],[[2],[5]]])
            sage: t.parent()
            Standard tableau tuples
            sage: t.category()
            Category of elements of Standard tableau tuples
            sage: type(t)
            <class 'sage.combinat.tableau_tuple.StandardTableauTuples_all_with_category.element_class'>
            sage: StandardTableauTuples(level=2)(t).parent()
            Standard tableau tuples of level 2
            sage: StandardTableauTuples(level=2, size=6)(t).parent()                    # needs sage.libs.flint
            Standard tableau tuples of level 2 and size 6
        """
        if isinstance(t, (StandardTableau, StandardTableauTuple)):
            return t

        # The Tableau class is very general in that it allows the entries of a
        # tableau to be almost anything, including lists. For this reason we
        # first try and interpret t as a tuple of tableaux and if this fails we
        # then try to think of t as a tableau.
        try:
            t = [StandardTableau(s) for s in t]
        except (TypeError, ValueError):
            try:
                t = [StandardTableau(t)]
            except ValueError:
                pass

        if len(t) == 1:
            return t[0]
        P = StandardTableauTuples_all()
        return P.element_class(P, t)

    def __init__(self, parent, t, check=True):
        r"""
        Initialize a standard tableau tuple.

        EXAMPLES::

            sage: t = StandardTableauTuples()([[[1,4],[2]],[[3]]])
            sage: s = TableauTuples(2)([[[1,4],[2]],[[3]]])
            sage: s == t
            True
            sage: s.parent()
            Tableau tuples of level 2
            sage: r = StandardTableauTuples(level=2)(t); r.parent()
            Standard tableau tuples of level 2
            sage: isinstance(r, StandardTableauTuple)
            True
            sage: r in StandardTableauTuples()
            True
            sage: r in StandardTableauTuples(level=2)
            True
            sage: r in StandardTableauTuples(level=3)
            False
        """
        # The check that ``t`` is valid tableau tuple is done by RowStandardTableauTuple
        super().__init__(parent, t, check=check)

        # As StandardTableauTuple inherits from RowStandardTableauTuple t must
        # be row strict and contain 1,2,...,n once each, so we only need to

        if check:
            # check that it is column strict
            if not all(s.is_column_strict() for s in self):
                raise ValueError('tableaux must be column strict')

    def dominates(self, t):
        """
        Return ``True`` if the tableau (tuple) ``self`` dominates the
        tableau ``t``. The two tableaux do not need to be of the same shape.

        EXAMPLES::

            sage: s = StandardTableauTuple([[1,2,3],[4,5]])
            sage: t = StandardTableauTuple([[1,2],[3,5],[4]])
            sage: s.dominates(t)
            True
            sage: t.dominates(s)
            False
        """
        return all(self.restrict(m).shape().dominates(t.restrict(m).shape())
                   for m in range(1, 1 + self.size()))

    def to_chain(self):
        """
        Return the chain of partitions corresponding to the standard
        tableau tuple ``self``.

        EXAMPLES::

            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).to_chain()
            [([], []),
              ([], [1]),
              ([], [2]),
              ([], [2, 1]),
              ([], [2, 2]),
              ([1], [2, 2])]
        """
        n = self.shape().size()
        if n == 0:
            return [self.shape()]
        return [self.restrict(k).shape() for k in range(n + 1)]

    def restrict(self, m=None):
        """
        Return the restriction of the standard tableau ``self`` to ``m``,
        which defaults to one less than the current :meth:`~TableauTuple.size`.

        EXAMPLES::

            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).restrict(6)
            ([[5]], [[1, 2], [3, 4]])
            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).restrict(5)
            ([[5]], [[1, 2], [3, 4]])
            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).restrict(4)
            ([], [[1, 2], [3, 4]])
            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).restrict(3)
            ([], [[1, 2], [3]])
            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).restrict(2)
            ([], [[1, 2]])
            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).restrict(1)
            ([], [[1]])
            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).restrict(0)
            ([], [])

        Where possible the restricted tableau belongs to the same category as
        the tableau ``self``::

            sage: TableauTuple([[[5]],[[1,2],[3,4]]]).restrict(3).category()
            Category of elements of Tableau tuples
            sage: StandardTableauTuple([[[5]],[[1,2],[3,4]]]).restrict(3).category()
            Category of elements of Standard tableau tuples
            sage: StandardTableauTuples([[1],[2,2]])([[[5]],[[1,2],[3,4]]]).restrict(3).category()
            Category of elements of Standard tableau tuples
            sage: StandardTableauTuples(level=2)([[[5]],[[1,2],[3,4]]]).restrict(3).category()
            Category of elements of Standard tableau tuples of level 2
        """
        if m is None:
            m = self.size() - 1
        # We are lucky in that currently restriction is defined for arbitrary
        # (level one) tableau and not just standard ones. If this ever changes
        # we will have to treat the cases where the components restrict to
        # empty lists of the form [[]] separately.
        tab = [t.restrict(m) for t in self]
        try:
            return self.parent()(tab)
        except ValueError:
            return StandardTableauTuple(tab)


# -------------------------------------------------
# Tableau tuples - parent classes
# -------------------------------------------------
class TableauTuples(UniqueRepresentation, Parent):
    """
    A factory class for the various classes of tableau tuples.

    INPUT:

    There are three optional arguments:

    - ``shape`` -- determines a :class:`PartitionTuple` which gives the shape
      of the :class:`TableauTuples`

    - ``level`` -- the level of the tableau tuples (positive integer)

    - ``size`` -- the size of the tableau tuples  (nonnegative integer)

    It is not necessary to use the keywords. If they are not specified then the
    first integer argument specifies the ``level`` and the second the ``size`` of the
    tableaux.

    OUTPUT: the corresponding class of tableau tuples

    The entries of a tableau can be any sage object. Because of this, no
    enumeration of the set of :class:`TableauTuples` is possible.

    EXAMPLES::

        sage: T3 = TableauTuples(3); T3
        Tableau tuples of level 3
        sage: [['a','b']] in TableauTuples()
        True
        sage: [['a','b']] in TableauTuples(level=3)
        False
        sage: t = TableauTuples(level=3)([[],[[1,1,1]],[]]); t
        ([], [[1, 1, 1]], [])
        sage: t in T3
        True
        sage: t in TableauTuples()
        True
        sage: t in TableauTuples(size=3)
        True
        sage: t in TableauTuples(size=4)
        False
        sage: t in StandardTableauTuples()
        False
        sage: t.parent()
        Tableau tuples of level 3
        sage: t.category()
        Category of elements of Tableau tuples of level 3

    .. SEEALSO::

       - :class:`Tableau`
       - :class:`StandardTableau`
       - :class:`StandardTableauTuples`

    TESTS::

        sage: TableauTuples(0)
        Traceback (most recent call last):
        ...
        ValueError: the level must be a positive integer

        sage: t = TableauTuples(3)([[],[],[[1,2],[3]]])
        sage: t.parent()
        Tableau tuples of level 3
        sage: TableauTuples(t)
        Traceback (most recent call last):
        ...
        ValueError: the level must be a positive integer
        sage: TableauTuples(3)([[1, 1]])
        Traceback (most recent call last):
        ...
        ValueError: [[1, 1]] is not an element of Tableau tuples of level 3

        sage: t0 = Tableau([[1]])
        sage: t1 = TableauTuples()([[1]])
        sage: t2 = TableauTuples()(t1)
        sage: t0 == t1 == t2
        True
        sage: t1 in TableauTuples()
        True
        sage: t1 in TableauTuples(1)
        True
        sage: t1 in TableauTuples(2)
        False

        sage: [[1]] in TableauTuples()
        True
        sage: [] in TableauTuples()
        True

        sage: TableauTuples(level=0)
        Traceback (most recent call last):
        ...
        ValueError: the level must be a positive integer

        sage: TestSuite( TableauTuples() ).run()
        sage: TestSuite( TableauTuples(level=1) ).run()
        sage: TestSuite( TableauTuples(level=2) ).run()
        sage: TestSuite( TableauTuples(level=6) ).run()
        sage: TestSuite( TableauTuples(size=0) ).run()
        sage: TestSuite( TableauTuples(size=1) ).run()
        sage: TestSuite( TableauTuples(size=2) ).run()
        sage: TestSuite( TableauTuples(size=10) ).run()
        sage: TestSuite( TableauTuples(level=1, size=0) ).run()
        sage: TestSuite( TableauTuples(level=1, size=1) ).run()
        sage: TestSuite( TableauTuples(level=1, size=10) ).run()
        sage: TestSuite( TableauTuples(level=2, size=0) ).run()
        sage: TestSuite( TableauTuples(level=2, size=1) ).run()
        sage: TestSuite( TableauTuples(level=2, size=10) ).run()
        sage: TestSuite( TableauTuples(level=6, size=0) ).run()
        sage: TestSuite( TableauTuples(level=6, size=1) ).run()
        sage: TestSuite( TableauTuples(level=6, size=10) ).run()

    Check that :issue:`14145` has been fixed::

        sage: 1 in TableauTuples()
        False
    """
    Element = TableauTuple
    level_one_parent_class = Tableaux_all  # used in element_constructor
    options = Tableaux.options

    @staticmethod
    def __classcall_private__(cls, level=None, size=None):
        r"""
        This is a factory class which returns the appropriate parent based on
        arguments.  See the documentation for :class:`TableauTuples` for more
        information.

        EXAMPLES::

            sage: TableauTuples()
            Tableau tuples
            sage: TableauTuples(3)
            Tableau tuples of level 3
            sage: TableauTuples(level=3)
            Tableau tuples of level 3
            sage: TableauTuples(size=3)
            Tableau tuples of size 3
            sage: TableauTuples(4,3)
            Tableau tuples of level 4 and size 3
            sage: TableauTuples(level=4,size=3)
            Tableau tuples of level 4 and size 3
            sage: TableauTuples(size=3,level=4)
            Tableau tuples of level 4 and size 3
        """
        # sanity testing
        if not (level is None or level in PositiveIntegers()):
            raise ValueError('the level must be a positive integer')

        if not (size is None or size in NN):
            raise ValueError('the size must be a nonnegative integer')

        # now that the inputs appear to make sense, return the appropriate class

        if level == 1:
            if size is not None:
                return Tableaux_size(size)
            else:
                return Tableaux_all()
        elif level is not None and size is not None:
            return TableauTuples_level_size(level=level, size=size)
        elif level is not None:
            return TableauTuples_level(level=level)
        elif size is not None:
            return TableauTuples_size(size=size)
        else:
            return TableauTuples_all()

    def _element_constructor_(self, t):
        r"""
        Construct an object from t as an element of ``self``, if possible.
        This is inherited by all :class:`TableauTuples`,
        :class:`StandardTableauTuples`, and :class:`StandardTableauTuples`
        classes.

        INPUT:

        - ``t`` -- data which can be interpreted as a tableau

        OUTPUT: the corresponding tableau object

        EXAMPLES::

            sage: T = TableauTuples(3)
            sage: T([[],[[1,2,1]],[]])   # indirect doctest
            ([], [[1, 2, 1]], [])
            sage: T([[],[[1,2,1]],[]]).parent() is T
            True
            sage: T( StandardTableauTuples(3)([[],[[1, 2, 3]],[]])).parent() is T
            True
            sage: T([[1,2]])    # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: [[1, 2]] is not an element of Tableau tuples of level 3
        """
        if t not in self:
            raise ValueError("%s is not an element of %s" % (t, self))

        # one way or another these two cases need to be treated separately
        if t == [] or t == [[]]:
            return self.level_one_parent_class().element_class(self.level_one_parent_class(), [])

        # Because Tableaux are considered to be TableauTuples we have to check to
        # see whether t is a Tableau or a TableauTuple in order to work out
        # which class t really belongs to.
        try:
            tab = [Tableau(s) for s in t]
        except (TypeError, ValueError):
            try:
                tab = [Tableau(t)]
            except ValueError:
                pass

        if tab in self:
            if len(tab) == 1:
                return self.level_one_parent_class().element_class(self.level_one_parent_class(), tab[0])
            else:
                return self.element_class(self, tab)

        raise ValueError('%s is not an element of %s' % (t, self))

    def __contains__(self, t):
        """
        Containment function of :class:`TableauTuples`.

        EXAMPLES::

            sage: T = TableauTuples()
            sage: [[1,2],[3,4]] in T
            True
            sage: [[1,2],[3]] in T
            True
            sage: [] in T
            True
            sage: [['a','b']] in T
            True
            sage: Tableau([['a']]) in T
            True

            sage: [1,2,3] in T
            False
            sage: [[1],[1,2]] in T
            False
            sage: ([[1,2],[4]],[[2,3],[1],[1]]) in T
            True

        Check that :issue:`14145` is fixed::

            sage: 1 in TableauTuples()
            False
        """
        if isinstance(t, (Tableau, TableauTuple)):
            return True
        elif isinstance(t, (tuple, list)):
            return all(s in Tableaux() for s in t) or t in Tableaux()
        else:
            return False

    # defaults for level, size and shape
    _level = None
    _size = None

    def level(self):
        """
        Return the ``level`` of a tableau tuple in  ``self``, or ``None`` if
        different tableau tuples in ``self`` can have different sizes. The
        ``level`` of a tableau tuple is just the level of the underlying
        :class:`PartitionTuple`.

        EXAMPLES::

            sage: TableauTuples().level() is None
            True
            sage: TableauTuples(7).level()
            7
        """
        return self._level

    def size(self):
        """
        Return the ``size`` of a tableau tuple in  ``self``, or ``None`` if
        different tableau tuples in ``self`` can have different sizes. The
        ``size`` of a tableau tuple is just the size of the underlying
        :class:`PartitionTuple`.

        EXAMPLES::

            sage: TableauTuples(size=14).size()
            14
        """
        return self._size

    def list(self):
        r"""
        If the set of tableau tuples ``self`` is finite then this function
        returns the list of these tableau tuples. If the class is infinite an
        error is returned.

        EXAMPLES::

            sage: StandardTableauTuples([[2,1],[2]]).list()
            [([[1, 2], [3]], [[4, 5]]),
             ([[1, 3], [2]], [[4, 5]]),
             ([[1, 2], [4]], [[3, 5]]),
             ([[1, 3], [4]], [[2, 5]]),
             ([[2, 3], [4]], [[1, 5]]),
             ([[1, 4], [2]], [[3, 5]]),
             ([[1, 4], [3]], [[2, 5]]),
             ([[2, 4], [3]], [[1, 5]]),
             ([[1, 2], [5]], [[3, 4]]),
             ([[1, 3], [5]], [[2, 4]]),
             ([[2, 3], [5]], [[1, 4]]),
             ([[1, 4], [5]], [[2, 3]]),
             ([[2, 4], [5]], [[1, 3]]),
             ([[3, 4], [5]], [[1, 2]]),
             ([[1, 5], [2]], [[3, 4]]),
             ([[1, 5], [3]], [[2, 4]]),
             ([[2, 5], [3]], [[1, 4]]),
             ([[1, 5], [4]], [[2, 3]]),
             ([[2, 5], [4]], [[1, 3]]),
             ([[3, 5], [4]], [[1, 2]])]
        """
        if self.is_finite():
            return list(self)
        raise NotImplementedError('this is an infinite set of tableaux')


class TableauTuples_all(TableauTuples):
    """
    The parent class of all :class:`TableauTuples`, with arbitrary ``level``
    and ``size``.
    """

    def __init__(self):
        r"""
        Initialize the class of all tableaux.

        EXAMPLES::

            sage: TableauTuples()
            Tableau tuples
        """
        super().__init__(category=Sets())
        self._level = None
        self._size = None

    def _repr_(self):
        """
        The string representation of a :class:`StandardTableauTuple`.

        EXAMPLES::

            sage: TableauTuples()    # indirect doctest
            Tableau tuples
        """
        return "Tableau tuples"

    def an_element(self):
        r"""
        Return a particular element of the class.

        EXAMPLES::

            sage: TableauTuples().an_element()
            ([[1]], [[2]], [[3]], [[4]], [[5]], [[6]], [[7]])
        """
        return self.element_class(self, [[[1]], [[2]], [[3]], [[4]],
                                         [[5]], [[6]], [[7]]])


class TableauTuples_level(TableauTuples):
    """
    Class of all :class:`TableauTuples` with a fixed ``level`` and arbitrary
    ``size``.
    """

    def __init__(self, level):
        r"""
        Initialize the class of tableaux of level ``level``.

        EXAMPLES::

            sage: TableauTuples(level=4)( [[[1,2],[4]],[],[],[[4,5,6],[7,8]]] )
            ([[1, 2], [4]], [], [], [[4, 5, 6], [7, 8]])
        """
        super().__init__(category=Sets())
        self._level = level

    def __contains__(self, t):
        """
        Containment function for :class:`TableauTuples` of a fixed ``level``.

        EXAMPLES::

            sage: T = TableauTuples(3)
            sage: [[[1,2,3]],[[1,2],[3,4]],[[2,4], [1]]] in T
            True
            sage: T([[[1,2,3]],[[1,2],[3,4]],[[2,4], [1]]])
            ([[1, 2, 3]], [[1, 2], [3, 4]], [[2, 4], [1]])
            sage: T(([[1,2,3]],[[1,2],[3,4]],[[2,4], [1]]))
            ([[1, 2, 3]], [[1, 2], [3, 4]], [[2, 4], [1]])
            sage: [[2,4],[1,3]] in T
            False
            sage: [[1],[2],[3]] in T
            False

        Check that :issue:`14145` is fixed::

            sage: 1 in TableauTuples(3)
            False
        """
        if isinstance(t, self.element_class):
            return self.level() == t.level()
        elif TableauTuples.__contains__(self, t) or isinstance(t, (list, tuple)):
            if all(s in Tableaux() for s in t):
                return len(t) == self.level()
            else:
                return self.level() == 1
        else:
            return False

    def _repr_(self):
        """
        The string representation of a :class:`StandardTableauTuple` of a
        fixed ``level``.

        EXAMPLES::

            sage: TableauTuples(4)    # indirect doctest
            Tableau tuples of level 4
        """
        return "Tableau tuples of level %s" % self.level()

    def an_element(self):
        r"""
        Return a particular element of the class.

        EXAMPLES::

            sage: TableauTuples(3).an_element()
            ([], [], [])
            sage: TableauTuples(5).an_element()
            ([], [], [], [], [])
            sage: T = TableauTuples(0)
            Traceback (most recent call last):
            ...
            ValueError: the level must be a positive integer
        """
        return self.element_class(self, [[] for _ in range(self.level())])


class TableauTuples_size(TableauTuples):
    """
    Class of all :class:`TableauTuples` with a arbitrary ``level`` and fixed
    ``size``.
    """

    def __init__(self, size):
        """
        Initialize the class of tableaux of size ``size``.

        EXAMPLES::

            sage: TableauTuples(size=6)
            Tableau tuples of size 6
        """
        super().__init__(category=Sets())
        self._size = size

    def __contains__(self, t):
        """
        Containment function for :class:`TableauTuples` of a fixed ``size``.

        EXAMPLES::

            sage: T = TableauTuples(size=3)
            sage: [[2,4], [1]] in T
            True
            sage: [[2,4],[1,3]] in T
            False
            sage: [[1,2,3]] in T
            True
            sage: [[1],[2],[3]] in T
            True
            sage: [[1],[2],[3],[4]] in T
            False

        Check that :issue:`14145` is fixed::

            sage: 1 in TableauTuples(size=3)
            False
        """
        if isinstance(t, self.element_class):
            return self.size() == t.size()
        elif TableauTuples.__contains__(self, t) or isinstance(t, (list, tuple)):
            if all(s in Tableaux() for s in t):
                return sum(sum(map(len, s)) for s in t) == self.size()
            else:
                return self.size() == sum(map(len, t))
        else:
            return False

    def _repr_(self):
        """
        The string representation of a :class:`StandardTableauTuple` of a
        fixed ``size``.

        EXAMPLES::

            sage: TableauTuples(size=4)    # indirect doctest
            Tableau tuples of size 4
        """
        return "Tableau tuples of size %s" % self.size()

    def an_element(self):
        r"""
        Return a particular element of the class.

        EXAMPLES::

            sage: TableauTuples(size=3).an_element()
            ([], [[1, 2, 3]], [])
            sage: TableauTuples(size=0).an_element()
            ([], [], [])
        """
        if self.size() == 0:
            return self.element_class(self, [[], [], []])
        else:
            return self.element_class(self, [[],
                                             [range(1, self.size() + 1)], []])


class TableauTuples_level_size(TableauTuples):
    """
    Class of all :class:`TableauTuples` with a fixed ``level`` and a fixed
    ``size``.
    """

    def __init__(self, level, size):
        r"""
        Initialize the class of tableaux of size ``size``.

        EXAMPLES::

            sage: TableauTuples(4,0)
            Tableau tuples of level 4 and size 0
            sage: TableauTuples(4,1)
            Tableau tuples of level 4 and size 1
            sage: TableauTuples(4,2)
            Tableau tuples of level 4 and size 2
            sage: TableauTuples(4,3)
            Tableau tuples of level 4 and size 3
        """
        super().__init__(category=Sets())
        self._level = level
        self._size = size

    def __contains__(self, t):
        """
        Containment function for :class:`TableauTuples` of a fixed ``level``
        and ``size``.

        EXAMPLES::

            sage: T = TableauTuples(3,3)
            sage: [[],[[2,4], [1]],[]] in T
            True
            sage: [[2,4],[1,3]] in T
            False

        Check that :issue:`14145` is fixed::

            sage: 1 in TableauTuples(3,3)
            False
        """
        if isinstance(t, self.element_class):
            return t.level() == self.level() and t.size() == self.size()
        elif TableauTuples.__contains__(self, t) or isinstance(t, (list, tuple)):
            if all(s in Tableaux() for s in t):
                return len(t) == self.level() and sum(sum(map(len, s)) for s in t) == self.size()
            else:
                return self.level() == 1 and self.size() == sum(map(len, t))
        else:
            return False

    def _repr_(self):
        """
        The string representation of the :class:`StandardTableauTuples` of
        given level and size.

        EXAMPLES::

            sage: TableauTuples(4,5)     # indirect doctest
            Tableau tuples of level 4 and size 5
            sage: TableauTuples(5,4)
            Tableau tuples of level 5 and size 4
            sage: TableauTuples(size=5,level=4)
            Tableau tuples of level 4 and size 5
        """
        return f"Tableau tuples of level {self.level()} and size {self.size()}"

    def an_element(self):
        r"""
        Return a particular element of the class.

        EXAMPLES::

            sage: TableauTuples(3,0).an_element()
            ([], [], [])
            sage: TableauTuples(3,1).an_element()
            ([[1]], [], [])
            sage: TableauTuples(3,2).an_element()
            ([[1, 2]], [], [])
        """
        if self.size() == 0:
            return self.element_class(self, [[]] * self.level())

        tab = [[list(range(1, self.size() + 1))]]
        tab.extend([] for _ in range(self.level() - 1))
        return self.element_class(self, tab)


# -------------------------------------------------
# Row standard tableau tuples - parent classes
# -------------------------------------------------
class RowStandardTableauTuples(TableauTuples):
    """
    A factory class for the various classes of tuples of row standard tableau.

    INPUT:

    There are three optional arguments:

    - ``level`` -- the :meth:`~TableauTuples.level` of the tuples of tableaux

    - ``size`` -- the :meth:`~TableauTuples.size` of the tuples of tableaux

    - ``shape`` -- list or a partition tuple specifying the :meth:`shape` of
      the row standard tableau tuples

    It is not necessary to use the keywords. If they are not used then the
    first integer argument specifies the :meth:`~TableauTuples.level` and
    the second the :meth:`~TableauTuples.size` of the tableau tuples.

    OUTPUT: the appropriate subclass of :class:`RowStandardTableauTuples`

    A tuple of row standard tableau is a tableau whose entries are positive
    integers which increase from left to right along the rows in each component.
    The entries do NOT need to increase from left to right along the components.

    .. NOTE::

        Sage uses the English convention for (tuples of) partitions and
        tableaux: the longer rows are displayed on top.  As with
        :class:`PartitionTuple`, in sage the cells, or nodes, of partition
        tuples are 0-based. For example, the (lexicographically) first cell
        in any non-empty partition tuple is `[0,0,0]`.

    EXAMPLES::

        sage: tabs = RowStandardTableauTuples([[2],[1,1]]); tabs
        Row standard tableau tuples of shape ([2], [1, 1])
        sage: tabs.cardinality()
        12
        sage: tabs[:]                                                                   # needs sage.graphs sage.rings.finite_rings
        [([[3, 4]], [[2], [1]]),
         ([[2, 4]], [[3], [1]]),
         ([[1, 4]], [[3], [2]]),
         ([[1, 2]], [[4], [3]]),
         ([[1, 3]], [[4], [2]]),
         ([[2, 3]], [[4], [1]]),
         ([[1, 4]], [[2], [3]]),
         ([[1, 3]], [[2], [4]]),
         ([[1, 2]], [[3], [4]]),
         ([[2, 3]], [[1], [4]]),
         ([[2, 4]], [[1], [3]]),
         ([[3, 4]], [[1], [2]])]

        sage: tabs = RowStandardTableauTuples(level=3); tabs
        Row standard tableau tuples of level 3
        sage: tabs[100]                                                                 # needs sage.libs.flint
        ([], [], [[2, 3], [1]])

        sage: RowStandardTableauTuples()[0]                                             # needs sage.libs.flint
        ([])

    TESTS::

        sage: # needs sage.libs.flint
        sage: TestSuite( RowStandardTableauTuples() ).run()
        sage: TestSuite( RowStandardTableauTuples(level=1) ).run()
        sage: TestSuite( RowStandardTableauTuples(level=4) ).run()
        sage: TestSuite( RowStandardTableauTuples(size=0) ).run(max_runs=50)  # recursion depth exceeded with default max_runs
        sage: TestSuite( RowStandardTableauTuples(size=6) ).run()
        sage: TestSuite( RowStandardTableauTuples(level=1, size=0) ).run()
        sage: TestSuite( RowStandardTableauTuples(level=1, size=0) ).run()
        sage: TestSuite( RowStandardTableauTuples(level=1, size=10) ).run()
        sage: TestSuite( RowStandardTableauTuples(level=4, size=0) ).run()
        sage: TestSuite( RowStandardTableauTuples(level=4, size=0) ).run()
        sage: TestSuite( RowStandardTableauTuples(level=4, size=10) ).run()     # long time
        sage: TestSuite( RowStandardTableauTuples(shape=[[1],[3,1],[],[2,1]]) ).run()

    .. SEEALSO::

        - :class:`TableauTuples`
        - :class:`Tableau`
        - :class:`RowStandardTableau`
        - :class:`RowStandardTableauTuples`
    """
    Element = RowStandardTableauTuple
    level_one_parent_class = RowStandardTableaux_all  # used in element_constructor

    @staticmethod
    def __classcall_private__(cls, *args, **kwargs):
        r"""
        This is a factory class which returns the appropriate parent based on
        arguments.  See the documentation for :class:`RowStandardTableauTuples`
        for more information.

        EXAMPLES::

            sage: RowStandardTableauTuples()
            Row standard tableau tuples
            sage: RowStandardTableauTuples(4)
            Row standard tableau tuples of level 4
            sage: RowStandardTableauTuples(4,3)                                         # needs sage.libs.flint
            Row standard tableau tuples of level 4 and size 3
            sage: RowStandardTableauTuples([ [2,1],[1],[1,1,1],[3,2] ])                 # needs sage.libs.flint
            Row standard tableau tuples of shape ([2, 1], [1], [1, 1, 1], [3, 2])

        TESTS::

            sage: RowStandardTableauTuples([ [2,1],[1],[1,1,1],[3,2,3] ])
            Traceback (most recent call last):
            ...
            ValueError: the shape must be a partition tuple

            sage: P = PartitionTuples()
            sage: pt = P([[1]]); pt
            ([1])
            sage: RowStandardTableauTuples(pt)                                          # needs sage.libs.flint
            Row standard tableaux of shape [1]
        """
        from sage.combinat.partition_tuple import PartitionTuple

        # first check the keyword arguments
        level = kwargs.get('level', None)
        shape = kwargs.get('shape', None)
        size = kwargs.get('size', None)

        for key in kwargs:
            if key not in ['level', 'shape', 'size']:
                raise ValueError('%s is not a valid argument for RowStandardTableauTuples' % key)

        # now process the positional arguments
        if args:
            # the first argument could be either the level or the shape
            if isinstance(args[0], (int, Integer)):
                if level is not None:
                    raise ValueError('the level was specified more than once')
                else:
                    level = args[0]
            else:
                if shape is not None:
                    raise ValueError('the shape was specified more than once')
                else:
                    shape = args[0]   # we check that it is a PartitionTuple below

        if len(args) == 2:  # both the level and size were specified
            if level is not None and size is not None:
                raise ValueError('the level or size was specified more than once')
            else:
                size = args[1]
        elif len(args) > 2:
            raise ValueError('too many arguments')

        # now check that the arguments are consistent
        if level is not None and (not isinstance(level, (int, Integer)) or level < 1):
            raise ValueError('the level must be a positive integer')

        if size is not None and (not isinstance(size, (int, Integer)) or size < 0):
            raise ValueError('the size must be a nonnegative integer')

        if shape is not None:
            try:
                shape = PartitionTuple(shape)
            except ValueError:
                raise ValueError('the shape must be a partition tuple')

            if level is None:
                level = shape.level()
            elif level != shape.level():
                raise ValueError('the shape and level must agree')
            if size is None:
                size = shape.size()
            elif size != shape.size():
                raise ValueError('the shape and size must agree')

        # now that the inputs appear to make sense, return the appropriate class
        if level is not None and level <= 1:
            from sage.combinat.partition_tuple import PartitionTuple
            if isinstance(shape, PartitionTuple):
                shape = shape[0]
            if shape is not None:
                return RowStandardTableaux_shape(shape)
            elif size is not None:
                return RowStandardTableaux_size(size)
            else:
                return RowStandardTableaux_all()
        elif shape is not None:
            return RowStandardTableauTuples_shape(shape)
        elif level is not None and size is not None:
            return RowStandardTableauTuples_level_size(level, size)
        elif level is not None:
            return RowStandardTableauTuples_level(level)
        elif size is not None:
            return RowStandardTableauTuples_size(size)
        else:
            return RowStandardTableauTuples_all()

    def __getitem__(self, r):
        r"""
        The default implementation of ``__getitem__`` for enumerated sets does
        not allow slices so we override it here.

        EXAMPLES::

            sage: RowStandardTableauTuples()[10:20]                                     # needs sage.libs.flint
            [([[2, 3], [1]]),
             ([[1, 2], [3]]),
             ([[1, 3], [2]]),
             ([[3], [2], [1]]),
             ([[2], [3], [1]]),
             ([[1], [3], [2]]),
             ([[1], [2], [3]]),
             ([[2], [1], [3]]),
             ([[3], [1], [2]]),
             ([[1, 2]], [])]

        .. TODO::

            Implement slices with step size different from `1` and make this
            a method for enumerate sets.
        """
        if isinstance(r, (int, Integer)):
            return self.unrank(r)
        elif isinstance(r, slice):
            start = 0 if r.start is None else r.start
            stop = r.stop
            if stop is None and not self.is_finite():
                raise ValueError('infinite set')
        else:
            raise ValueError('r must be an integer or a slice')
        count = 0
        tabs = []
        for t in self:
            if count == stop:
                break
            if count >= start:
                tabs.append(t)
            count += 1

        # this is to cope with empty slices endpoints like [:6] or [:}
        if count == stop or stop is None:
            return tabs
        raise IndexError('value out of range')

    def __contains__(self, t):
        """
        Containment function for :class:`RowStandardTableauTuples` of
        arbitrary ``level`` and ``size``.

        EXAMPLES::

            sage: T = RowStandardTableauTuples()
            sage: [[1,3],[2]] in T
            True
            sage: [] in T
            True
            sage: Tableau([[1]]) in T
            True
            sage: RowStandardTableauTuple([[1]]) in T
            True

            sage: [[1,2],[1]] in T
            False
            sage: [[1,1],[5]] in T
            False

        Check that :issue:`14145` is fixed::

            sage: 1 in RowStandardTableauTuples()
            False
        """
        if isinstance(t, (RowStandardTableau, RowStandardTableauTuple)):
            return True
        elif TableauTuples.__contains__(self, t) or isinstance(t, (list, tuple)):
            if all(s in Tableaux() for s in t):
                flatt = sorted(sum((list(row) for s in t for row in s), []))
                return (flatt == list(range(1, len(flatt) + 1))
                        and all(len(s) == 0 or all(row[i] < row[i + 1]
                                                   for row in s for i in range(len(row) - 1))
                                for s in t))
            else:
                return t in RowStandardTableaux()
        else:
            return False

    # set the default shape
    _shape = None

    def shape(self):
        """
        Return the shape of the set of :class:`RowStandardTableauTuples`, or
        ``None`` if it is not defined.

        EXAMPLES::

            sage: tabs=RowStandardTableauTuples(shape=[[5,2],[3,2],[],[1,1,1],[3]]); tabs
            Row standard tableau tuples of shape ([5, 2], [3, 2], [], [1, 1, 1], [3])
            sage: tabs.shape()
            ([5, 2], [3, 2], [], [1, 1, 1], [3])
            sage: RowStandardTableauTuples().shape() is None
            True
        """
        return self._shape


class RowStandardTableauTuples_all(RowStandardTableauTuples, DisjointUnionEnumeratedSets):
    """
    Default class of all :class:`RowStandardTableauTuples` with an arbitrary
    :meth:`~TableauTuples.level` and :meth:`~TableauTuples.size`.
    """

    def __init__(self):
        r"""
        Initialize the class of all row standard tableaux.

        .. WARNING::

            Input is not checked; please use :class:`RowStandardTableauTuples`
            to ensure the options are properly parsed.

        EXAMPLES::

            sage: RSTT = RowStandardTableauTuples()
            sage: TestSuite(RSTT).run()                                                 # needs sage.libs.flint
        """
        RowStandardTableauTuples.__init__(self)
        from sage.combinat.partition_tuple import PartitionTuples
        DisjointUnionEnumeratedSets.__init__(self,
            Family(PartitionTuples(), RowStandardTableauTuples_shape),
            facade=True, keepkey=False)

    def _repr_(self):
        """
        The string representation of the :class:`RowStandardTableauTuples` of
        arbitrary ``level`` and ``size``.

        EXAMPLES::

            sage: RowStandardTableauTuples()
            Row standard tableau tuples
        """
        return "Row standard tableau tuples"

    def an_element(self):
        r"""
        Return a particular element of the class.

        EXAMPLES::

            sage: RowStandardTableauTuples().an_element()
            ([[4, 5, 6, 7]], [[2, 3]], [[1]])
        """
        return self.element_class(self, reversed([[range(2**(i - 1), 2**i)]
                                                  for i in range(1, 4)]))


class RowStandardTableauTuples_level(RowStandardTableauTuples, DisjointUnionEnumeratedSets):
    """
    Class of all :class:`RowStandardTableauTuples` with a fixed ``level``
    and arbitrary ``size``.
    """

    def __init__(self, level):
        r"""
        Initialize the class of row standard tableaux of level
        ``level`` of arbitrary ``size``.

        .. WARNING::

            Input is not checked; please use :class:`RowStandardTableauTuples`
            to ensure the options are properly parsed.

        EXAMPLES::

            sage: RowStandardTableauTuples(3)
            Row standard tableau tuples of level 3
            sage: RowStandardTableauTuples(3)[:10]                                      # needs sage.libs.flint
            [([], [], []),
            ([[1]], [], []),
            ([], [[1]], []),
            ([], [], [[1]]),
            ([[1, 2]], [], []),
            ([[2], [1]], [], []),
            ([[1], [2]], [], []),
            ([[2]], [[1]], []),
            ([[1]], [[2]], []),
            ([[2]], [], [[1]])]
            sage: RowStandardTableauTuples(3).cardinality()
            +Infinity
        """
        RowStandardTableauTuples.__init__(self)
        from sage.combinat.partition_tuple import PartitionTuples_level
        DisjointUnionEnumeratedSets.__init__(self,
            Family(PartitionTuples_level(level), RowStandardTableauTuples_shape),
            facade=True, keepkey=False)
        self._level = level

    def _repr_(self):
        """
        The string representation of the :class:`RowStandardTableauTuples`
        of fixed ``level``.

        EXAMPLES::

            sage: RowStandardTableauTuples(3)    # indirect doctest
            Row standard tableau tuples of level 3
        """
        return 'Row standard tableau tuples of level %s' % self.level()

    def __contains__(self, t):
        """
        Containment function for :class:`RowStandardTableauTuples` of
        fixed ``level``.

        EXAMPLES::

            sage: T = RowStandardTableauTuples(3)
            sage: [[[2,3]],[[1]],[]] in T
            True
            sage: RowStandardTableauTuple([[2, 3], [1]]) in T
            False
            sage: [] in T
            False

        Check that :issue:`14145` is fixed::

            sage: 1 in RowStandardTableauTuples(3)
            False
        """
        if isinstance(t, RowStandardTableauTuple):
            return self.level() == t.level()
        elif RowStandardTableauTuples.__contains__(self, t):
            if all(s in Tableaux() for s in t):
                return len(t) == self.level()
            else:
                return self.level() == 1
        else:
            return False

    def an_element(self):
        r"""
        Return a particular element of the class.

        EXAMPLES::

            sage: RowStandardTableauTuples(2).an_element()
            ([[1]], [[2, 3]])
            sage: RowStandardTableauTuples(3).an_element()
            ([[1]], [[2, 3]], [[4, 5, 6, 7]])
        """
        return self.element_class(self, [[range(2**(i - 1), 2**i)]
                                         for i in range(1, self.level() + 1)])


class RowStandardTableauTuples_size(RowStandardTableauTuples, DisjointUnionEnumeratedSets):
    """
    Class of all :class:`RowStandardTableauTuples` with an arbitrary ``level``
    and a fixed ``size``.
    """

    def __init__(self, size):
        r"""
        Initialize the class of row standard tableaux of size ``size`` of
        arbitrary level.

        .. WARNING::

            Input is not checked; please use :class:`RowStandardTableauTuples`
            to ensure the options are properly parsed.

        EXAMPLES::

            sage: RowStandardTableauTuples(size=3) # indirect doctest
            Row standard tableau tuples of size 3
            sage: RowStandardTableauTuples(size=2)[:10]                                 # needs sage.libs.flint
            [([[1, 2]]),
            ([[2], [1]]),
            ([[1], [2]]),
            ([[1, 2]], []),
            ([[2], [1]], []),
            ([[1], [2]], []),
            ([[2]], [[1]]),
            ([[1]], [[2]]),
            ([], [[1, 2]]),
            ([], [[2], [1]])]
            sage: RowStandardTableauTuples(3).cardinality()
            +Infinity
        """
        RowStandardTableauTuples.__init__(self)
        from sage.combinat.partition_tuple import PartitionTuples_size
        DisjointUnionEnumeratedSets.__init__(self,
            Family(PartitionTuples_size(size), RowStandardTableauTuples_shape),
            facade=True, keepkey=False)
        self._size = size

    def _repr_(self):
        """
        The string representation of the :class:`RowStandardTableauTuples`
        of fixed ``size``.

        EXAMPLES::

            sage: RowStandardTableauTuples(size=3)
            Row standard tableau tuples of size 3
        """
        return "Row standard tableau tuples of size %s" % self.size()

    def __contains__(self, t):
        """
        Containment function for :class:`RowStandardTableauTuples` of fixed
        ``size``.

        EXAMPLES::

            sage: T = RowStandardTableauTuples(size=3)
            sage: ([[1,2]], [], [], [[3]]) in T
            True
            sage: [[[1,2]], [], [], [[5]]] in T
            False
            sage: Tableau([[1]]) in T
            False

            sage: 1 in RowStandardTableauTuples(size=3)
            False
        """
        if isinstance(t, self.element_class):
            return self.size() == t.size()
        elif t in RowStandardTableauTuples():
            if all(s in Tableaux() for s in t):
                return sum(sum(map(len, s)) for s in t) == self.size()
            else:
                return self.size() == sum(map(len, t))
        else:
            return False

    def an_element(self):
        r"""
        Return a particular element of the class.

        EXAMPLES::

            sage: RowStandardTableauTuples(size=2).an_element()
            ([[1]], [[2]], [], [])
            sage: RowStandardTableauTuples(size=4).an_element()
            ([[1]], [[2, 3, 4]], [], [])
        """
        if self.size() == 0:
            return self.element_class(self, [[], [], [], []])
        elif self.size() == 1:
            return self.element_class(self, [[[1]], [], [], []])
        return self.element_class(self, [[[1]], [range(2, self.size() + 1)],
                                         [], []])


class RowStandardTableauTuples_level_size(RowStandardTableauTuples, DisjointUnionEnumeratedSets):
    """
    Class of all :class:`RowStandardTableauTuples` with a fixed ``level``
    and a fixed ``size``.
    """

    def __init__(self, level, size):
        r"""
        Initialize the class of row standard tableaux of level ``level``
        and size ``size``.

        .. WARNING::

            Input is not checked; please use :class:`RowStandardTableauTuples`
            to ensure the options are properly parsed.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: RSTT43 = RowStandardTableauTuples(size=4, level=3); RSTT43
            Row standard tableau tuples of level 3 and size 4
            sage: RSTT43 is RowStandardTableauTuples(3,4)
            True
            sage: RowStandardTableauTuples(level=3, size=2)[:]
            [([[1, 2]], [], []),
            ([[2], [1]], [], []),
            ([[1], [2]], [], []),
            ([[2]], [[1]], []),
            ([[1]], [[2]], []),
            ([[2]], [], [[1]]),
            ([[1]], [], [[2]]),
            ([], [[1, 2]], []),
            ([], [[2], [1]], []),
            ([], [[1], [2]], []),
            ([], [[2]], [[1]]),
            ([], [[1]], [[2]]),
            ([], [], [[1, 2]]),
            ([], [], [[2], [1]]),
            ([], [], [[1], [2]])]
            sage: RowStandardTableauTuples(3,2).cardinality()
            15
        """
        RowStandardTableauTuples.__init__(self)
        from sage.combinat.partition_tuple import PartitionTuples_level_size
        DisjointUnionEnumeratedSets.__init__(self,
            Family(PartitionTuples_level_size(level, size),
                   RowStandardTableauTuples_shape),
            facade=True, keepkey=False)
        self._level = level
        self._size = size

    def _repr_(self):
        """
        The string representation of the :class:`RowStandardTableauTuples` of
        fixed ``level`` and size.

        EXAMPLES::

            sage: RowStandardTableauTuples(3, 4)                                        # needs sage.libs.flint
            Row standard tableau tuples of level 3 and size 4
        """
        return f"Row standard tableau tuples of level {self.level()} and size {self.size()}"

    def __contains__(self, t):
        """
        Containment function for :class:`RowStandardTableauTuples` of fixed
        ``level`` and size.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: tabs = RowStandardTableauTuples(level=4, size=4); tabs
            Row standard tableau tuples of level 4 and size 4
            sage: [[[2,4],[1]],[],[[3]],[]] in tabs
            True
            sage: tabs([[[1,2]],[],[[4],[3]],[]]) == RowStandardTableauTuple([[[1,2]],[],[[4],[3]],[]])
            True
            sage: RowStandardTableauTuple([[[2, 3]], [[1]]]) in tabs
            False

        Check that :issue:`14145` is fixed::

            sage: 1 in RowStandardTableauTuples(level=4, size=3)                        # needs sage.libs.flint
            False
        """
        if isinstance(t, self.element_class):
            return self.size() == t.size() and self.level() == t.level()
        elif t in RowStandardTableauTuples():
            if all(s in Tableaux() for s in t):
                return len(t) == self.level() and sum(sum(map(len, s)) for s in t) == self.size()
            else:
                return self.level() == 1 and self.size() == sum(map(len, t))
        else:
            return False

    def an_element(self):
        r"""
        Return a particular element of ``self``.

        EXAMPLES::

            sage: RowStandardTableauTuples(5, size=2).an_element()                      # needs sage.libs.flint
            ([], [], [], [], [[1], [2]])
            sage: RowStandardTableauTuples(2, size=4).an_element()                      # needs sage.libs.flint
            ([[1]], [[2, 3], [4]])
        """
        if self.size() == 0:
            return self.element_class(self, [[] for _ in range(self.level())])
        elif self.size() == 1:
            return self.element_class(self, sum([[[[1]]]], [[] for _ in range(self.level() - 1)]))
        elif self.size() == 2:
            return self.element_class(self, sum([[[[1], [2]]]], [[] for _ in range(self.level() - 1)]))
        return self.element_class(self, sum([[[[1]]],
            [[range(2, self.size()),
              [self.size()]]]], [[] for _ in range(self.level() - 2)]))


class RowStandardTableauTuples_shape(RowStandardTableauTuples):
    """
    Class of all :class:`RowStandardTableauTuples` of a fixed shape.
    """

    def __init__(self, shape):
        r"""
        Initialize the class of row standard tableaux of shape ``p``
        and no maximum entry.

        .. WARNING::

            Input is not checked; please use :class:`RowStandardTableauTuples`
            to ensure the options are properly parsed.

        EXAMPLES::

            sage: STT = RowStandardTableauTuples([[2,1],[2,1,1]])
            sage: STT
            Row standard tableau tuples of shape ([2, 1], [2, 1, 1])
            sage: STT.cardinality()
            1260
        """
        super().__init__(category=FiniteEnumeratedSets())
        from sage.combinat.partition_tuple import PartitionTuple
        self._shape = PartitionTuple(shape)
        self._level = len(shape)
        self._size = shape.size()

    def __contains__(self, t):
        """
        Containment function of :class:`RowStandardTableauTuples` of
        fixed shape.

        EXAMPLES::

            sage: STT = RowStandardTableauTuples([[2,1],[1]])
            sage: [[[13, 67]], [[14,67]]] in STT
            False
            sage: [[[1, 4],[3]], [[2]]] in STT
            True
            sage: ([[1, 4],[3]], [[2]]) in STT
            True

        Check that :issue:`14145` is fixed::

            sage: 1 in RowStandardTableauTuples([[2,1],[1]])
            False
        """
        if isinstance(t, self.element_class):
            return self.shape() == t.shape()
        elif t in RowStandardTableauTuples():
            if all(s in Tableaux() for s in t):
                return [[len(l) for l in s] for s in t] == self.shape()
            else:
                return list(self.shape()) == sum(map(len, t))
        else:
            return False

    def _repr_(self):
        """
        The string representation of the :class:`RowStandardTableauTuples` of
        fixed shape.

        EXAMPLES::

            sage: RowStandardTableauTuples([[2,1],[],[3,1,1,1]])
            Row standard tableau tuples of shape ([2, 1], [], [3, 1, 1, 1])
        """
        return 'Row standard tableau tuples of shape %s' % self.shape()

    def __iter__(self):
        r"""
        Iterate through the finite class of :class:`RowStandardTableauTuples`
        of a given :class:`PartitionTulpe` shape.

        The algorithm below is modelled on, but different than, the
        corresponding iterator for the row standard tableau of partition shape.
        In particular, the tableaux are generated in the reverse order here as
        that is easier (and more useful for applications to graded Specht
        modules).

        EXAMPLES::

            sage: RowStandardTableauTuples([[1],[1],[1]]).list()                        # needs sage.graphs sage.modules sage.rings.finite_rings
            [([[3]], [[2]], [[1]]),
             ([[2]], [[3]], [[1]]),
             ([[1]], [[3]], [[2]]),
             ([[1]], [[2]], [[3]]),
             ([[2]], [[1]], [[3]]),
             ([[3]], [[1]], [[2]])]
            sage: RowStandardTableauTuples([[2,1],[2]]).list()                          # needs sage.graphs sage.modules sage.rings.finite_rings
            [([[4, 5], [2]], [[1, 3]]),
             ([[4, 5], [3]], [[1, 2]]),
             ([[3, 5], [4]], [[1, 2]]),
             ([[3, 4], [5]], [[1, 2]]),
             ([[4, 5], [1]], [[2, 3]]),
             ([[3, 5], [1]], [[2, 4]]),
             ([[2, 5], [1]], [[3, 4]]),
             ([[1, 5], [2]], [[3, 4]]),
             ([[1, 4], [2]], [[3, 5]]),
             ([[1, 3], [2]], [[4, 5]]),
             ([[1, 2], [3]], [[4, 5]]),
             ([[2, 3], [1]], [[4, 5]]),
             ([[2, 4], [1]], [[3, 5]]),
             ([[3, 4], [1]], [[2, 5]]),
             ([[3, 4], [2]], [[1, 5]]),
             ([[2, 4], [3]], [[1, 5]]),
             ([[1, 4], [3]], [[2, 5]]),
             ([[1, 2], [4]], [[3, 5]]),
             ([[1, 3], [4]], [[2, 5]]),
             ([[2, 3], [4]], [[1, 5]]),
             ([[2, 3], [5]], [[1, 4]]),
             ([[1, 3], [5]], [[2, 4]]),
             ([[1, 2], [5]], [[3, 4]]),
             ([[1, 5], [3]], [[2, 4]]),
             ([[1, 5], [4]], [[2, 3]]),
             ([[1, 4], [5]], [[2, 3]]),
             ([[2, 4], [5]], [[1, 3]]),
             ([[2, 5], [4]], [[1, 3]]),
             ([[2, 5], [3]], [[1, 4]]),
             ([[3, 5], [2]], [[1, 4]])]

        TESTS::

            sage: def check(mu):                                                        # needs sage.graphs sage.modules sage.rings.finite_rings
            ....:     return (RowStandardTableauTuples(mu).cardinality()
            ....:             == len(RowStandardTableauTuples(mu).list()))
            sage: all(check(mu) for mu in PartitionTuples(4,4))                         # needs sage.graphs sage.modules sage.rings.finite_rings
            True
        """
        mu = self.shape()

        # Set up two lists clen and cclen which give the "end points" of
        # the components of mu and the rows of each component, respectively, so
        # that the numbers contained in component c of the initial tableau are
        #    tab[ clen[c]:clen[c+1] ]
        # and the numbers contained in row r of component c are
        #    tab[ clen[c]:clen[c+1] ][ cclen[c][r]: cclen[c][r+1] ]
        # where tab=[1,2,...,n] as above
        relations = []
        clen = [0] * (len(mu) + 1)
        cclen = [[0] * (len(mu[c]) + 1) for c in range(len(mu))]
        for c in range(len(mu)):
            for r in range(len(mu[c])):
                cclen[c][r + 1] = cclen[c][r] + mu[c][r]
                relations += [(clen[c]+cclen[c][r]+i+1, clen[c]+cclen[c][r]+i+2)
                              for i in range(mu[c][r]-1)]
            clen[c + 1] = clen[c] + cclen[c][-1]

        # To generate the row standard tableau tuples we are going to generate
        # them from linearisations of the poset from the rows of the tableau. We
        # will get them as "flattened" tableaux so we need to expand these one
        # line lists back into tableaux. This is done y the following functions.
        def tableau_from_list(tab):
            """
            Convert a list tab=[t_1,...,t_n] into the mu-tableau obtained by
            inserting t_1,..,t_n in order into the rows of mu, from left to right
            in each component and then left to right along the components.
            """
            return self.element_class(self,
                                      [[tab[clen[c]:clen[c+1]][cclen[c][r]:cclen[c][r+1]]
                                        for r in range(len(mu[c]))]
                                       for c in range(len(mu))],
                                      check=False)

        # now run through the linear extensions and return the corresponding tableau
        for lin in Poset((range(1, mu.size()+1), relations)).linear_extensions():
            linear_tab = list(permutation.Permutation(lin).inverse())
            yield tableau_from_list(linear_tab)

    def cardinality(self):
        r"""
        Return the number of row standard tableau tuples of with the same
        shape as the partition tuple ``self``.

        This is just the index of the corresponding Young subgroup in the
        full symmetric group.

        EXAMPLES::

            sage: RowStandardTableauTuples([[3,2,1],[]]).cardinality()
            60
            sage: RowStandardTableauTuples([[1],[1],[1]]).cardinality()
            6
            sage: RowStandardTableauTuples([[2,1],[1],[1]]).cardinality()
            60
        """
        mu = self.shape()
        return Integer(factorial(mu.size()) // prod(factorial(row) for nu in mu for row in nu))

    def an_element(self):
        r"""
        Return a particular element of ``self``.

        EXAMPLES::

            sage: RowStandardTableauTuples([[2],[2,1]]).an_element()                    # needs sage.graphs sage.modules
            ([[4, 5]], [[1, 3], [2]])
            sage: RowStandardTableauTuples([[10],[],[]]).an_element()                   # needs sage.graphs sage.modules
            ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [], [])
        """
        c = self.cardinality()
        return self[c > 3 and 4 or (c > 1 and -1 or 0)]


class RowStandardTableauTuples_residue(RowStandardTableauTuples):
    r"""
    Class of all row standard tableau tuples with a fixed residue sequence.

    Implicitly, this also specifies the quantum characteristic, multicharge
    and hence the level and size of the tableaux.

    .. NOTE::

        This class is not intended to be called directly, but rather,
        it is accessed through the row standard tableaux.

    EXAMPLES::

        sage: RowStandardTableau([[3,4,5],[1,2]]).residue_sequence(2).row_standard_tableaux()
        Row standard tableaux with 2-residue sequence (1,0,0,1,0) and multicharge (0)
        sage: RowStandardTableau([[3,4,5],[1,2]]).residue_sequence(3).row_standard_tableaux()
        Row standard tableaux with 3-residue sequence (2,0,0,1,2) and multicharge (0)
        sage: RowStandardTableauTuple([[[5,6],[7]],[[1,2,3],[4]]]).residue_sequence(2,(0,0)).row_standard_tableaux()
        Row standard tableaux with 2-residue sequence (0,1,0,1,0,1,1) and multicharge (0,0)
        sage: RowStandardTableauTuple([[[5,6],[7]],[[1,2,3],[4]]]).residue_sequence(3,(0,1)).row_standard_tableaux()
        Row standard tableaux with 3-residue sequence (1,2,0,0,0,1,2) and multicharge (0,1)
    """

    def __init__(self, residue):
        r"""
        Initialize ``self``.

        .. WARNING::

            Input is not checked; please use :class:`RowStandardTableauTuples`
            to ensure the options are properly parsed.

        EXAMPLES::

            sage: tabs = RowStandardTableau([[3,4,5],[1,2]]).residue_sequence(3).row_standard_tableaux()
            sage: TestSuite(tabs).run()
            sage: tabs = RowStandardTableauTuple([[[6],[7]],[[3,4,5],[1,2]]]).residue_sequence(2,(0,0)).row_standard_tableaux()
            sage: TestSuite(tabs).run()  # long time
        """
        super().__init__(category=FiniteEnumeratedSets())
        self._residue = residue
        self._quantum_characteristic = residue.quantum_characteristic()
        self._multicharge = residue.multicharge()
        self._level = residue.level()
        self._size = residue.size()
        self._base_ring = residue.base_ring()

    def _repr_(self):
        """
        Return the string representation of ``self``.

        EXAMPLES::

            sage: RowStandardTableauTuple([[[4,5],[3]],[[1,2]]]).residue_sequence(3,(0,1)).row_standard_tableaux()
            Row standard tableaux with 3-residue sequence (1,2,2,0,1) and multicharge (0,1)
            sage: StandardTableauTuple([[[1,2],[3]],[[4,5]]]).residue_sequence(3,(0,1)).row_standard_tableaux()
            Row standard tableaux with 3-residue sequence (0,1,2,1,2) and multicharge (0,1)
        """
        return 'Row standard tableaux with {}'.format(self._residue.__str__('and'))

    def __contains__(self, t):
        """
        Check containment of ``t`` in ``self``.

        EXAMPLES::

            sage: res = RowStandardTableauTuple([[[4,5],[3]],[[1,2]]]).residue_sequence(3,(0,1))
            sage: tabs = res.row_standard_tableaux(); tabs
            Row standard tableaux with 3-residue sequence (1,2,2,0,1) and multicharge (0,1)
            sage: [[[1,2],[3]],[[4,5]]] in tabs
            False
            sage: [[[4,5],[3]],[[1,2]]] in tabs
            True
            sage: [[[1,2],[4,5]],[[3]]] in tabs
            False
        """
        if not isinstance(t, self.element_class):
            try:
                t = RowStandardTableauTuple(t)
            except ValueError:
                return False

        return (t.residue_sequence(self._quantum_characteristic,
                                   self._multicharge) == self._residue)

    def __iter__(self):
        r"""
        Iterate through ``self``.

        We construct this sequence of tableaux recursively, as is easier (and
        more useful for applications to graded Specht modules).

        EXAMPLES::

            sage: R = RowStandardTableauTuple([[[4, 5], [3]],[[1,2]]]).residue_sequence(3, (0,1))
            sage: R.row_standard_tableaux()[:]                                          # needs sage.libs.flint
            [([[4, 5], [3]], [[1, 2]]),
             ([[4, 5], [2]], [[1, 3]]),
             ([[4], [3], [5]], [[1, 2]]),
             ([[4], [2], [5]], [[1, 3]]),
             ([], [[1, 3], [4, 5], [2]]),
             ([], [[1, 2], [4, 5], [3]]),
             ([], [[1, 3], [4], [2], [5]]),
             ([], [[1, 2], [4], [3], [5]])]
            sage: R = RowStandardTableauTuple([[[2,4],[1]],[[3]]]).residue_sequence(3,(0,1))
            sage: R.row_standard_tableaux()[:]                                          # needs sage.libs.flint
            [([[2, 4], [1], [3]], []),
             ([[2, 3], [1], [4]], []),
             ([[2, 4], [1]], [[3]]),
             ([[2, 3], [1]], [[4]]),
             ([[2], [1], [4]], [[3]]),
             ([[2], [1], [3]], [[4]]),
             ([], [[4], [2], [1], [3]]),
             ([], [[3], [2], [1], [4]])]
        """
        if self._size == 0:
            if self._level == 1:
                yield RowStandardTableau([])
            else:
                yield RowStandardTableauTuple([[] for _ in range(self._level)])  # the empty tableaux
            return

        # the only way that I know to generate these tableaux is to test all
        # possible shapes in the same block, which is cheap to test
        from sage.combinat.partition_tuple import PartitionTuples
        for mu in PartitionTuples(self._level, self._size):
            if mu.block(self._quantum_characteristic, self._multicharge) == self._residue.block():
                for t in RowStandardTableauTuples_residue_shape(self._residue, mu):
                    if self._level == 1:
                        yield t
                    else:
                        yield self.element_class(self, t, check=False)

    def quantum_characteristic(self):
        r"""
        Return the quantum characteristic of ``self``.

        EXAMPLES::

            sage: RowStandardTableau([[2,3],[1]]).residue_sequence(3,(0,1)).row_standard_tableaux().quantum_characteristic()
            3
            sage: StandardTableau([[1,2],[3]]).residue_sequence(3,(0,1)).row_standard_tableaux().quantum_characteristic()
            3
            sage: RowStandardTableauTuple([[[4]],[[2,3],[1]]]).residue_sequence(3,(0,1)).row_standard_tableaux().quantum_characteristic()
            3
            sage: StandardTableauTuple([[[4]],[[1,3],[2]]]).residue_sequence(3,(0,1)).row_standard_tableaux().quantum_characteristic()
            3
        """
        return self._quantum_characteristic

    def multicharge(self):
        r"""
        Return the multicharge of ``self``.

        EXAMPLES::

            sage: RowStandardTableau([[2,3],[1]]).residue_sequence(3,(0,1)).row_standard_tableaux().multicharge()
            (0, 1)
            sage: StandardTableau([[1,2],[3]]).residue_sequence(3,(0,1)).row_standard_tableaux().multicharge()
            (0, 1)
            sage: RowStandardTableauTuple([[[4]],[[2,3],[1]]]).residue_sequence(3,(0,1)).row_standard_tableaux().multicharge()
            (0, 1)
            sage: StandardTableauTuple([[[4]],[[1,3],[2]]]).residue_sequence(3,(0,1)).row_standard_tableaux().multicharge()
            (0, 1)
        """
        return self._multicharge

    def level(self):
        r"""
        Return the level of ``self``.

        EXAMPLES::

            sage: RowStandardTableau([[2,3],[1]]).residue_sequence(3,(0,1)).row_standard_tableaux().level()
            2
            sage: StandardTableau([[1,2],[3]]).residue_sequence(3,(0,1)).row_standard_tableaux().level()
            2
            sage: RowStandardTableauTuple([[[4]],[[2,3],[1]]]).residue_sequence(3,(0,1)).row_standard_tableaux().level()
            2
            sage: StandardTableauTuple([[[4]],[[1,3],[2]]]).residue_sequence(3,(0,1)).row_standard_tableaux().level()
            2
        """
        return self._level

    def size(self):
        r"""
        Return the size of ``self``.

        EXAMPLES::

            sage: RowStandardTableau([[2,3],[1]]).residue_sequence(3,(0,1)).row_standard_tableaux().size()
            3
            sage: StandardTableau([[1,2],[3]]).residue_sequence(3,(0,1)).row_standard_tableaux().size()
            3
            sage: RowStandardTableauTuple([[[4]],[[2,3],[1]]]).residue_sequence(3,(0,1)).row_standard_tableaux().size()
            4
            sage: StandardTableauTuple([[[4]],[[1,3],[2]]]).residue_sequence(3,(0,1)).row_standard_tableaux().size()
            4
        """
        return self._size

    def residue_sequence(self):
        r"""
        Return the residue sequence of ``self``.

        EXAMPLES::

            sage: RowStandardTableau([[2,3],[1]]).residue_sequence(3,(0,1)).row_standard_tableaux().residue_sequence()
            3-residue sequence (2,0,1) with multicharge (0,1)
            sage: StandardTableau([[1,2],[3]]).residue_sequence(3,(0,1)).row_standard_tableaux().residue_sequence()
            3-residue sequence (0,1,2) with multicharge (0,1)
            sage: RowStandardTableauTuple([[[4]],[[2,3],[1]]]).residue_sequence(3,(0,1)).row_standard_tableaux().residue_sequence()
            3-residue sequence (0,1,2,0) with multicharge (0,1)
            sage: StandardTableauTuple([[[4]],[[1,3],[2]]]).residue_sequence(3,(0,1)).row_standard_tableaux().residue_sequence()
            3-residue sequence (1,0,2,0) with multicharge (0,1)
        """
        return self._residue

    def an_element(self):
        r"""
        Return a particular element of ``self``.

        EXAMPLES::

            sage: RowStandardTableau([[2,3],[1]]).residue_sequence(3).row_standard_tableaux().an_element()
            [[2, 3], [1]]
            sage: StandardTableau([[1,3],[2]]).residue_sequence(3).row_standard_tableaux().an_element()
            [[1, 3], [2]]
            sage: RowStandardTableauTuple([[[4]],[[2,3],[1]]]).residue_sequence(3,(0,1)).row_standard_tableaux().an_element()                                   # needs sage.libs.flint
            sage: StandardTableauTuple([[[4]],[[1,3],[2]]]).residue_sequence(3,(0,1)).row_standard_tableaux().an_element()                                      # needs sage.libs.flint
            ([[4], [3], [1], [2]], [])
        """
        try:
            return self.unrank(0)
        except ValueError:
            return None


class RowStandardTableauTuples_residue_shape(RowStandardTableauTuples_residue):
    """
    All row standard tableau tuples with a fixed residue and shape.

    INPUT:

    - ``shape`` -- the shape of the partitions or partition tuples
    - ``residue`` -- the residue sequence of the label

    EXAMPLES::

        sage: res = RowStandardTableauTuple([[[3,6],[1]],[[5,7],[4],[2]]]).residue_sequence(3,(0,0))
        sage: tabs = res.row_standard_tableaux([[2,1],[2,1,1]]); tabs
        Row standard (2,1|2,1^2)-tableaux with 3-residue sequence (2,1,0,2,0,1,1) and multicharge (0,0)
        sage: tabs.shape()
        ([2, 1], [2, 1, 1])
        sage: tabs.level()
        2
        sage: tabs[:6]
        [([[5, 7], [4]], [[3, 6], [1], [2]]),
         ([[5, 7], [1]], [[3, 6], [4], [2]]),
         ([[3, 7], [4]], [[5, 6], [1], [2]]),
         ([[3, 7], [1]], [[5, 6], [4], [2]]),
         ([[5, 6], [4]], [[3, 7], [1], [2]]),
         ([[5, 6], [1]], [[3, 7], [4], [2]])]
    """

    def __init__(self, residue, shape):
        r"""
        Initialize ``self``.

        .. WARNING::

            Input is not checked; please use :class:`RowStandardTableauTuples`
            to ensure the options are properly parsed.

        TESTS::

            sage: res = RowStandardTableauTuple([[[1,3]],[[4,5],[2,6]]]).residue_sequence(3,(0,0))
            sage: tabs = res.row_standard_tableaux([[2],[2,2]])
            sage: TestSuite(tabs).run()
        """
        if residue.size() != shape.size():
            raise ValueError('the size of the shape and the length of the residue defence must coincide!')

        super().__init__(residue)
        self._shape = shape

        # The _standard_tableaux attribute below is used to generate the
        # tableaux in this class. The key observation is that any row standard
        # tableau is standard if we stretch it out to a tableau with one row in
        # each component
        multicharge = residue.multicharge()
        if shape.level() == 1:
            standard_shape = [[r] for r in shape]
            charge = [multicharge[0] - r for r in range(len(shape))]
        else:
            standard_shape = [[r] for mu in shape for r in mu]
            charge = [multicharge[c] - r for c in range(len(shape))
                      for r in range(len(shape[c]))]

        from sage.combinat.tableau_residues import ResidueSequence
        res = ResidueSequence(residue.quantum_characteristic(), charge, residue.residues())
        self._standard_tableaux = res.standard_tableaux(standard_shape)

        # to convert the tableaux in self._standard_tableaux to row standard
        # tableau we use the list _cumulative_lengths, which keeps track of the
        # cumulative lengths of each component
        if shape.level() == 1:
            self._cumulative_lengths = [0, len(shape)]
        else:
            self._cumulative_lengths = [0]*(shape.level()+1)
            for c in range(len(shape)):
                self._cumulative_lengths[c+1] = self._cumulative_lengths[c] + len(shape[c])

    def __contains__(self, t):
        """
        Check containment of ``t`` in ``self``.

        EXAMPLES::

            sage: tabs = RowStandardTableauTuple([[[1,3]],[[4],[2]]]).residue_sequence(3,(0,1)).row_standard_tableaux([[2],[1,1]])
            sage: [ [[1,2,3,4]], [[]] ] in tabs
            False
            sage: ([[1, 3]], [[4], [2]]) in tabs
            True
        """
        if not isinstance(t, self.element_class):
            try:
                t = RowStandardTableauTuple(t)
            except ValueError:
                return False
        return (t.shape() == self._shape
                and t.residue_sequence(self._quantum_characteristic,
                                       self._multicharge) == self._residue)

    def _repr_(self):
        """
        Return the string representation of ``self``.

        EXAMPLES::

            sage: RowStandardTableau([[1,3],[2,4]]).residue_sequence(3).row_standard_tableaux([2,2])
            Row standard (2^2)-tableaux with 3-residue sequence (0,2,1,0) and multicharge (0)
        """
        return 'Row standard ({})-tableaux with {}'.format(self._shape._repr_compact_high(),
                                                           self._residue.__str__('and'))

    def __iter__level_one(self):
        r"""
        Iterate through the row standard tableaux in ``self``.

        We construct this sequence of tableaux recursively, as it is easier
        (and more useful for applications to graded Specht modules).

        EXAMPLES::

            sage: RowStandardTableau([[2,4],[1,3]]).residue_sequence(3).row_standard_tableaux([2,2])[:] # indirect doctest
            [[[3, 4], [1, 2]], [[2, 4], [1, 3]]]
        """
        if self._size == 0:
            yield RowStandardTableau([])

        for t in self._standard_tableaux:
            yield RowStandardTableau([s[0] for s in t])

    def __iter__higher_levels(self):
        r"""
        Iterate through the row standard tableaux in ``self``.

        We construct this sequence of tableaux recursively, as it is easier
        (and more useful for applications to graded Specht modules).

        EXAMPLES::

            sage: RowStandardTableauTuple([[[2,4]],[[3,5],[1]]]).residue_sequence(3,[0,1]).row_standard_tableaux([[2],[2,1]])[:] # indirect doctest
            [([[2, 4]], [[3, 5], [1]]),
            ([[1, 4]], [[3, 5], [2]]),
            ([[2, 3]], [[4, 5], [1]]),
            ([[1, 3]], [[4, 5], [2]])]
        """
        if self._size == 0:
            yield self.element_class(self, [[] for _ in range(self._level)],
                                     check=False)  # the empty tableau
            return

        for t in self._standard_tableaux:
            yield self.element_class(self,
                [[t[r][0] for r in range(self._cumulative_lengths[c],
                                         self._cumulative_lengths[c + 1])]
                 for c in range(self._level)],
                check=False)

    @lazy_attribute
    def __iter__(self):
        r"""
        Iterate through the row standard tableaux in ``self``.

        We construct this sequence of tableaux recursively, as it is easier
        (and more useful for applications to graded Specht modules).

        EXAMPLES::

            sage: RowStandardTableau([[2,4],[1,3]]).residue_sequence(3).row_standard_tableaux([1,1,1,1])[:] # indirect doctest
            [[[3], [1], [4], [2]], [[2], [1], [4], [3]]]
            sage: RowStandardTableauTuple([[[2,4]],[[3,5],[1]]]).residue_sequence(3,[0,1]).row_standard_tableaux([[3],[1,1]])[:] # indirect doctest
            [([[2, 4, 5]], [[3], [1]]),
            ([[1, 4, 5]], [[3], [2]]),
            ([[2, 3, 5]], [[4], [1]]),
            ([[1, 3, 5]], [[4], [2]])]
        """
        if self._level == 1:
            return self.__iter__level_one
        else:
            return self.__iter__higher_levels


# -------------------------------------------------
# Standard tableau tuples - parent classes
# -------------------------------------------------
class StandardTableauTuples(RowStandardTableauTuples):
    """
    A factory class for the various classes of tuples of standard tableau.

    INPUT:

    There are three optional arguments:

    - ``level`` -- the :meth:`~TableauTuples.level` of the tuples of tableaux

    - ``size`` -- the :meth:`~TableauTuples.size` of the tuples of tableaux

    - ``shape`` -- list or a partition tuple specifying the :meth:`shape` of
      the standard tableau tuples

    It is not necessary to use the keywords. If they are not used then the first
    integer argument specifies the :meth:`~TableauTuples.level` and the second
    the :meth:`~TableauTuples.size` of the tableau tuples.

    OUTPUT: the appropriate subclass of :class:`StandardTableauTuples`

    A tuple of standard tableau is a tableau whose entries are positive
    integers which increase from left to right along the rows, and from top to
    bottom down the columns, in each component. The entries do NOT need to
    increase from left to right along the components.


    .. NOTE::

        Sage uses the English convention for (tuples of) partitions and
        tableaux: the longer rows are displayed on top.  As with
        :class:`PartitionTuple`, in sage the cells, or nodes, of partition
        tuples are 0-based. For example, the (lexicographically) first cell
        in any non-empty partition tuple is `[0,0,0]`.

    EXAMPLES::

        sage: tabs=StandardTableauTuples([[3],[2,2]]); tabs
        Standard tableau tuples of shape ([3], [2, 2])
        sage: tabs.cardinality()
        70
        sage: tabs[10:16]
        [([[1, 2, 3]], [[4, 6], [5, 7]]),
         ([[1, 2, 4]], [[3, 6], [5, 7]]),
         ([[1, 3, 4]], [[2, 6], [5, 7]]),
         ([[2, 3, 4]], [[1, 6], [5, 7]]),
         ([[1, 2, 5]], [[3, 6], [4, 7]]),
         ([[1, 3, 5]], [[2, 6], [4, 7]])]

        sage: tabs=StandardTableauTuples(level=3); tabs
        Standard tableau tuples of level 3
        sage: tabs[100]                                                                 # needs sage.libs.flint
        ([[1, 2], [3]], [], [[4]])

        sage: StandardTableauTuples()[0]                                                # needs sage.libs.flint
        ()

    TESTS::

        sage: # needs sage.libs.flint
        sage: TestSuite( StandardTableauTuples() ).run()
        sage: TestSuite( StandardTableauTuples(level=1) ).run()
        sage: TestSuite( StandardTableauTuples(level=4) ).run()
        sage: TestSuite( StandardTableauTuples(size=0) ).run(max_runs=50) # recursion depth exceeded with default max_runs
        sage: TestSuite( StandardTableauTuples(size=6) ).run()
        sage: TestSuite( StandardTableauTuples(level=1, size=0) ).run()
        sage: TestSuite( StandardTableauTuples(level=1, size=0) ).run()
        sage: TestSuite( StandardTableauTuples(level=1, size=10) ).run()
        sage: TestSuite( StandardTableauTuples(level=4, size=0) ).run()
        sage: TestSuite( StandardTableauTuples(level=4, size=0) ).run()

    .. SEEALSO::

        - :class:`TableauTuples`
        - :class:`Tableau`
        - :class:`StandardTableau`
        - :class:`StandardTableauTuples`
    """
    Element = StandardTableauTuple
    level_one_parent_class = StandardTableaux_all  # used in element_constructor

    @staticmethod
    def __classcall_private__(cls, *args, **kwargs):
        r"""
        This is a factory class which returns the appropriate parent based on
        arguments.

        See the documentation for :class:`StandardTableauTuples`
        for more information.

        EXAMPLES::

            sage: StandardTableauTuples()
            Standard tableau tuples
            sage: StandardTableauTuples(4)
            Standard tableau tuples of level 4
            sage: StandardTableauTuples(4,3)                                            # needs sage.libs.flint
            Standard tableau tuples of level 4 and size 3
            sage: StandardTableauTuples([ [2,1],[1],[1,1,1],[3,2] ])                    # needs sage.libs.flint
            Standard tableau tuples of shape ([2, 1], [1], [1, 1, 1], [3, 2])

        TESTS::

            sage: StandardTableauTuples([ [2,1],[1],[1,1,1],[3,2,3] ])                  # needs sage.libs.flint
            Traceback (most recent call last):
            ...
            ValueError: the shape must be a partition tuple

            sage: P = PartitionTuples()
            sage: pt = P([[1]]); pt
            ([1])
            sage: StandardTableauTuples(pt)                                             # needs sage.libs.flint
            Standard tableaux of shape [1]
        """
        from sage.combinat.partition_tuple import PartitionTuple

        # first check the keyword arguments
        level = kwargs.get('level', None)
        shape = kwargs.get('shape', None)
        size = kwargs.get('size', None)

        for key in kwargs:
            if key not in ['level', 'shape', 'size']:
                raise ValueError('%s is not a valid argument for StandardTableauTuples' % key)

        # now process the positional arguments
        if args:
            # the first argument could be either the level or the shape
            if isinstance(args[0], (int, Integer)):
                if level is not None:
                    raise ValueError('the level was specified more than once')
                else:
                    level = args[0]
            else:
                if shape is not None:
                    raise ValueError('the shape was specified more than once')
                else:
                    shape = args[0]   # we check that it is a PartitionTuple below

        if len(args) == 2:  # both the level and size were specified
            if level is not None and size is not None:
                raise ValueError('the level or size was specified more than once')
            else:
                size = args[1]
        elif len(args) > 2:
            raise ValueError('too man arguments!')

        # now check that the arguments are consistent
        if level is not None and (not isinstance(level, (int, Integer)) or level < 1):
            raise ValueError('the level must be a positive integer')

        if size is not None and (not isinstance(size, (int, Integer)) or size < 0):
            raise ValueError('the size must be a nonnegative integer')

        if shape is not None:
            try:
                shape = PartitionTuple(shape)
            except ValueError:
                raise ValueError('the shape must be a partition tuple')

            if level is None:
                level = shape.level()
            elif level != shape.level():
                raise ValueError('the shape and level must agree')
            if size is None:
                size = shape.size()
            elif size != shape.size():
                raise ValueError('the shape and size must agree')

        # now that the inputs appear to make sense, return the appropriate class
        if level is not None and level <= 1:
            if isinstance(shape, PartitionTuple):
                shape = shape[0]
            if shape is not None:
                return StandardTableaux_shape(shape)
            elif size is not None:
                return StandardTableaux_size(size)
            else:
                return StandardTableaux_all()
        elif shape is not None:
            return StandardTableauTuples_shape(shape)
        elif level is not None and size is not None:
            return StandardTableauTuples_level_size(level, size)
        elif level is not None:
            return StandardTableauTuples_level(level)
        elif size is not None:
            return StandardTableauTuples_size(size)
        else:
            return StandardTableauTuples_all()

    def __getitem__(self, r):
        r"""
        The default implementation of ``__getitem__`` for enumerated sets does
        not allow slices so we override it here.

        EXAMPLES::

            sage: StandardTableauTuples()[10:20]                                        # needs sage.libs.flint
            [([[1, 2], [3]]),
             ([[1], [2], [3]]),
             ([[1, 2]], []),
             ([[1], [2]], []),
             ([[1]], [[2]]),
             ([[2]], [[1]]),
             ([], [[1, 2]]),
             ([], [[1], [2]]),
             ([[1]], [], []),
             ([], [[1]], [])]

        .. TODO::

            Implement slices with step size different from `1` and make this
            a method for enumerate sets.
        """
        if isinstance(r, (int, Integer)):
            return self.unrank(r)
        elif isinstance(r, slice):
            start = 0 if r.start is None else r.start
            stop = r.stop
            if stop is None and not self.is_finite():
                raise ValueError('infinite set')
        else:
            raise ValueError('r must be an integer or a slice')
        count = 0
        tabs = []
        for t in self:
            if count == stop:
                break
            if count >= start:
                tabs.append(t)
            count += 1

        # this is to cope with empty slices endpoints like [:6] or [:}
        if count == stop or stop is None:
            return tabs
        raise IndexError('value out of range')

    def __contains__(self, t):
        """
        Containment function for :class:`StandardTableauTuples` of arbitrary
        ``level`` and ``size``.

        EXAMPLES::

            sage: T = StandardTableauTuples()
            sage: [[1,3],[2]] in T
            True
            sage: [] in T
            True
            sage: Tableau([[1]]) in T
            True
            sage: StandardTableauTuple([[1]]) in T
            True

            sage: [[1,2],[1]] in T
            False
            sage: [[1,1],[5]] in T
            False

        Check that :issue:`14145` is fixed::

            sage: 1 in StandardTableauTuples()
            False
        """
        if isinstance(t, (StandardTableau, StandardTableauTuple)):
            return True
        elif TableauTuples.__contains__(self, t) or isinstance(t, (list, tuple)):
            if all(s in Tableaux() for s in t):
                flatt = sorted(sum((list(row) for s in t for row in s), []))
                return flatt == list(range(1, len(flatt)+1)) and all(len(x) == 0 or
                  (all(row[i] < row[i+1] for row in x for i in range(len(row)-1))
                      and all(x[r][c] < x[r+1][c] for c in range(len(x[0]))
                              for r in range(len(x)-1) if len(x[r+1]) > c)) for x in t)
            else:
                return t in StandardTableaux()
        else:
            return False

    # set the default shape
    _shape = None

    def shape(self):
        """
        Return the shape of the set of :class:`StandardTableauTuples`, or
        ``None`` if it is not defined.

        EXAMPLES::

            sage: tabs=StandardTableauTuples(shape=[[5,2],[3,2],[],[1,1,1],[3]]); tabs
            Standard tableau tuples of shape ([5, 2], [3, 2], [], [1, 1, 1], [3])
            sage: tabs.shape()
            ([5, 2], [3, 2], [], [1, 1, 1], [3])
            sage: StandardTableauTuples().shape() is None
            True
        """
        return self._shape


class StandardTableauTuples_all(StandardTableauTuples, DisjointUnionEnumeratedSets):
    """
    Default class of all :class:`StandardTableauTuples` with an arbitrary
    :meth:`~TableauTuples.level` and :meth:`~TableauTuples.size`.
    """

    def __init__(self):
        r"""
        Initialize the class of all standard tableaux. Input is not
        checked; please use :class:`StandardTableauTuples` to ensure the
        options are properly parsed.

        EXAMPLES::

            sage: StandardTableauTuples()
            Standard tableau tuples
        """
        StandardTableauTuples.__init__(self)
        from sage.combinat.partition_tuple import PartitionTuples
        DisjointUnionEnumeratedSets.__init__(self,
                Family(PartitionTuples(), StandardTableauTuples_shape),
                facade=True, keepkey=False)

    def _repr_(self):
        """
        The string representation of the :class:`StandardTableauTuples` of
        arbitrary ``level`` and ``size``.

        EXAMPLES::

            sage: STT = StandardTableauTuples(); STT    # indirect doctest
            Standard tableau tuples
        """
        return "Standard tableau tuples"

    def __iter__(self):
        """
        Iterate through the infinite class of :class:`StandardTableauTuples`
        of arbitrary ``level`` and ``size``.

        Note that because these tableaux should have
        :class:`StandardTableauTuples` as their parent, any tuples of level 1
        will actually be a :class:`StandardTableauTuples` and NOT
        :class:`StandardTableaux`. As such they will have a restricted set
        of methods compared with usual :class:`StandardTableaux`. As they
        were constructed via this iterator this is presumably what is required
        so it should not cause any problems, especially as they are printed
        with brackets around them to alert the user that something is
        different.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: stt = StandardTableauTuples()
            sage: stt[0:8]
            [(),
             ([[1]]),
             ([], []),
             ([[1, 2]]),
             ([[1], [2]]),
             ([[1]], []),
             ([], [[1]]),
             ([], [], [])]
            sage: stt[5]
            ([[1]], [])
            sage: stt[50]
            ([], [[1, 3], [2]])
            sage: stt[47].parent() is stt
            True
        """
        from sage.combinat.partition_tuple import PartitionTuples
        for shape in PartitionTuples():
            # We use StandardTableauTuples(shape) to correctly deal with the
            # case when the shape is of level 1.
            for t in StandardTableauTuples(shape):
                yield self.element_class(self, t, check=False)


class StandardTableauTuples_level(StandardTableauTuples, DisjointUnionEnumeratedSets):
    """
    Class of all :class:`StandardTableauTuples` with a fixed ``level``
    and arbitrary ``size``.
    """

    def __init__(self, level):
        r"""
        Initialize the class of semistandard tableaux of level ``level`` of
        arbitrary ``size``.

        Input is not checked; please use
        :class:`StandardTableauTuples` to ensure the options are
        properly parsed.

        EXAMPLES::

            sage: StandardTableauTuples(3)
            Standard tableau tuples of level 3
        """
        StandardTableauTuples.__init__(self)
        from sage.combinat.partition_tuple import PartitionTuples_level
        DisjointUnionEnumeratedSets.__init__(self,
                Family(PartitionTuples_level(level), StandardTableauTuples_shape),
                facade=True, keepkey=False)
        self._level = level

    def _repr_(self):
        """
        The string representation of the :class:`StandardTableauTuples`
        of fixed ``level``.

        EXAMPLES::

            sage: StandardTableauTuples(3)    # indirect doctest
            Standard tableau tuples of level 3
        """
        return 'Standard tableau tuples of level %s' % self.level()

    def __contains__(self, t):
        """
        Containment function for :class:`StandardTableauTuples` of
        fixed ``level``.

        EXAMPLES::

            sage: T = StandardTableauTuples(3)
            sage: [[[1,2]],[[3]],[]] in T
            True
            sage: StandardTableauTuple([[1, 2], [3]]) in T
            False
            sage: [] in T
            False

        Check that :issue:`14145` is fixed::

            sage: 1 in StandardTableauTuples(3)
            False
        """
        if isinstance(t, StandardTableauTuple):
            return self.level() == t.level()
        elif StandardTableauTuples.__contains__(self, t):
            if all(s in Tableaux() for s in t):
                return len(t) == self.level()
            else:
                return self.level() == 1
        else:
            return False

    def __iter__(self):
        """
        Iterate through the infinite class of all
        :class:`StandardTableauTuples` of a fixed ``level``.

        EXAMPLES::

            sage: stt = StandardTableauTuples(3)
            sage: stt[0:8]                                                              # needs sage.libs.flint
            [([], [], []),
              ([[1]], [], []),
              ([], [[1]], []),
              ([], [], [[1]]),
              ([[1, 2]], [], []),
              ([[1], [2]], [], []),
              ([[1]], [[2]], []),
              ([[2]], [[1]], [])]
            sage: stt[50]                                                               # needs sage.libs.flint
            ([], [[1, 2, 3]], [])
            sage: stt[0].parent() is stt                                                # needs sage.libs.flint
            True
        """
        # Iterate through the PartitionTuples and then the tableaux
        # Note that the level is greater than one so we do not have to treat
        # StandardTableaux separately
        from sage.combinat.partition_tuple import PartitionTuples
        for shape in PartitionTuples(self.level()):
            for t in StandardTableauTuples_shape(shape):
                yield self.element_class(self, t, check=False)

    def an_element(self):
        r"""
        Return a particular element of the class.

        EXAMPLES::

            sage: StandardTableauTuples(size=2).an_element()
            ([[1]], [[2]], [], [])
            sage: StandardTableauTuples(size=4).an_element()
            ([[1]], [[2, 3, 4]], [], [])
        """
        return self.element_class(self, [[list(range(2**(i - 1), 2**i))]
                                         for i in range(1, self.level() + 1)])


class StandardTableauTuples_size(StandardTableauTuples, DisjointUnionEnumeratedSets):
    """
    Class of all :class:`StandardTableauTuples` with an arbitrary ``level``
    and a fixed ``size``.
    """

    def __init__(self, size):
        r"""
        Initialize the class of semistandard tableaux of size ``size`` of
        arbitrary level. Input is not checked; please use
        :class:`StandardTableauTuples` to ensure the options are properly
        parsed.

        EXAMPLES::

            sage: StandardTableauTuples(size=3)
            Standard tableau tuples of size 3
        """
        StandardTableauTuples.__init__(self)
        from sage.combinat.partition_tuple import PartitionTuples_size
        DisjointUnionEnumeratedSets.__init__(self,
                Family(PartitionTuples_size(size), StandardTableauTuples_shape),
                facade=True, keepkey=False)
        self._size = size

    def _repr_(self):
        """
        The string representation of the :class:`StandardTableauTuples`
        of fixed ``size``.

        EXAMPLES::

            sage: StandardTableauTuples(size=3)    # indirect doctest
            Standard tableau tuples of size 3
        """
        return "Standard tableau tuples of size %s" % self.size()

    def __contains__(self, t):
        """
        Containment function for :class:`StandardTableauTuples` of fixed
        ``size``.

        EXAMPLES::

            sage: T = StandardTableauTuples(size=3)
            sage: ([[1,2]], [], [], [[3]]) in T
            True
            sage: [[[1,2]], [], [], [[5]]] in T
            False
            sage: Tableau([[1]]) in T
            False

        Check that :issue:`14145` is fixed::

            sage: 1 in StandardTableauTuples(size=3)
            False
        """
        if isinstance(t, self.element_class):
            return self.size() == t.size()
        elif t in StandardTableauTuples():
            if all(s in Tableaux() for s in t):
                return sum(sum(map(len, s)) for s in t) == self.size()
            else:
                return self.size() == sum(map(len, t))
        else:
            return False

    def __iter__(self):
        """
        Iterate through the infinite class of all
        :class:`StandardTableauTuples` of a fixed ``size``.

        Note that because these tableaux should have
        :class:`StandardTableauTuples` as their parent, any tuples of level 1
        will actually be a :class:`StandardTableauTuples` and NOT
        :class:`StandardTableaux`. As such they will have a restricted set of
        methods compared with usual :class:`StandardTableaux`. As they
        were constructed via this iterator this is presumably what is required
        so it should not cause any problems, especially as they are printed
        with brackets around them to alert the user that something is
        different.

        EXAMPLES::

            sage: stt = StandardTableauTuples(size=3)
            sage: stt[0:8]                                                              # needs sage.libs.flint
            [([[1, 2, 3]]),
             ([[1, 3], [2]]),
             ([[1, 2], [3]]),
             ([[1], [2], [3]]),
             ([[1, 2, 3]], []),
             ([[1, 2], [3]], []),
             ([[1, 3], [2]], []),
             ([[1], [2], [3]], [])]
            sage: stt[50]                                                               # needs sage.libs.flint
            ([[3]], [[1]], [[2]])
            sage: stt[0].parent() is stt                                                # needs sage.libs.flint
            True
        """
        # Iterate through the PartitionTuples and then the tableaux
        from sage.combinat.partition_tuple import PartitionTuples
        for shape in PartitionTuples(size=self.size()):
            # We use StandardTableauTuples(shape) to correctly deal with the
            # case when the shape is of level 1.
            for t in StandardTableauTuples(shape):
                yield self.element_class(self, t, check=False)

    def an_element(self):
        r"""
        Return a particular element of the class.

        EXAMPLES::

            sage: StandardTableauTuples(size=2).an_element()
            ([[1]], [[2]], [], [])
            sage: StandardTableauTuples(size=4).an_element()
            ([[1]], [[2, 3, 4]], [], [])
        """
        if self.size() == 0:
            return self.element_class(self, [[], [], [], []])
        elif self.size() == 1:
            return self.element_class(self, [[[1]], [], [], []])
        return self.element_class(self, [[[1]],
                                         [list(range(2, self.size() + 1))],
                                         [], []])


class StandardTableauTuples_level_size(StandardTableauTuples, DisjointUnionEnumeratedSets):
    """
    Class of all :class:`StandardTableauTuples` with a fixed ``level`` and a
    fixed ``size``.
    """

    def __init__(self, level, size):
        r"""
        Initialize the class of semistandard tableaux of level ``level`` and
        size ``size``. Input is not checked; please use
        :class:`StandardTableauTuples` to ensure the options are properly
        parsed.

        EXAMPLES::

            sage: StandardTableauTuples(size=4, level=3)                                # needs sage.libs.flint
            Standard tableau tuples of level 3 and size 4
            sage: StandardTableauTuples(size=4, level=3) is StandardTableauTuples(3,4)  # needs sage.libs.flint
            True
        """
        StandardTableauTuples.__init__(self)
        from sage.combinat.partition_tuple import PartitionTuples_level_size
        DisjointUnionEnumeratedSets.__init__(self,
                Family(PartitionTuples_level_size(level, size), StandardTableauTuples_shape),
                facade=True, keepkey=False)
        self._level = level
        self._size = size

    def _repr_(self):
        """
        The string representation of the :class:`StandardTableauTuples` of
        fixed ``level`` and size.

        EXAMPLES::

            sage: StandardTableauTuples(3, 4)    # indirect doctest                     # needs sage.libs.flint
            Standard tableau tuples of level 3 and size 4
        """
        return f"Standard tableau tuples of level {self.level()} and size {self.size()}"

    def __contains__(self, t):
        """
        Containment function for :class:`StandardTableauTuples` of fixed
        ``level`` and size.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: tabs = StandardTableauTuples(level=4, size=3); tabs
            Standard tableau tuples of level 4 and size 3
            sage: [[[1,2]],[],[[3]],[]] in tabs
            True
            sage: tabs([[[1,2]],[],[[3]],[]]) == StandardTableauTuple([[[1,2]],[],[[3]],[]])
            True
            sage: StandardTableauTuple([[[1, 2]], [[3]]]) in tabs
            False
            sage: Tableau([[1]]) in tabs
            False

        Check that :issue:`14145` is fixed::

            sage: 1 in StandardTableauTuples(level=4, size=3)                           # needs sage.libs.flint
            False
        """
        if isinstance(t, self.element_class):
            return self.size() == t.size() and self.level() == t.level()
        elif t in StandardTableauTuples():
            if all(s in Tableaux() for s in t):
                return len(t) == self.level() and sum(sum(map(len, s)) for s in t) == self.size()
            else:
                return self.level() == 1 and self.size() == sum(map(len, t))
        else:
            return False

    def cardinality(self):
        """
        Return the number of elements in this set of tableaux.

        EXAMPLES::

            sage: StandardTableauTuples(3,2).cardinality()                              # needs sage.libs.flint
            12
            sage: StandardTableauTuples(4,6).cardinality()                              # needs sage.libs.flint
            31936
        """
        from sage.combinat.partition_tuple import PartitionTuples
        return sum(StandardTableauTuples_shape(shape).cardinality()
                   for shape in PartitionTuples(self.level(), self.size()))

    def __iter__(self):
        """
        Iterate through the finite class of all :class:`StandardTableauTuples`
        of a fixed ``level`` and size.

        Note that the level must be greater than 1 here so we can call
        :class:`StandardTableauTuples_shape` directly.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: stt = StandardTableauTuples(3, 3)
            sage: stt[0:8]
            [([[1, 2, 3]], [], []),
              ([[1, 2], [3]], [], []),
              ([[1, 3], [2]], [], []),
              ([[1], [2], [3]], [], []),
              ([[1, 2]], [[3]], []),
              ([[1, 3]], [[2]], []),
              ([[2, 3]], [[1]], []),
              ([[1], [2]], [[3]], [])]
            sage: stt[40]
            ([], [[2, 3]], [[1]])
            sage: stt[0].parent() is stt
            True
        """
        # Iterate through the PartitionTuples and then the tableaux
        from sage.combinat.partition_tuple import PartitionTuples
        for shape in PartitionTuples(level=self.level(), size=self.size()):
            for t in StandardTableauTuples_shape(shape):
                yield self.element_class(self, t, check=False)

    def an_element(self):
        r"""
        Return a particular element of the class.

        EXAMPLES::

            sage: StandardTableauTuples(5, size=2).an_element()                         # needs sage.libs.flint
            ([], [], [], [], [[1], [2]])
            sage: StandardTableauTuples(2, size=4).an_element()                         # needs sage.libs.flint
            ([[1]], [[2, 3], [4]])
        """
        if self.size() == 0:
            return self.element_class(self, [[] for _ in range(self.level())])
        elif self.size() == 1:
            return self.element_class(self, sum([[[[1]]]], [[] for _ in range(self.level() - 1)]))
        elif self.size() == 2:
            return self.element_class(self, sum([[[[1], [2]]]], [[] for _ in range(self.level() - 1)]))

        return self.element_class(self, sum([[[[1]]],
            [[list(range(2, self.size())),
              [self.size()]]]], [[] for _ in range(self.level() - 2)]))


class StandardTableauTuples_shape(StandardTableauTuples):
    """
    Class of all :class:`StandardTableauTuples` of a fixed shape.
    """

    def __init__(self, shape):
        r"""
        Initialize the class of semistandard tableaux of shape ``p`` and no
        maximum entry. Input is not checked; please use
        :class:`StandardTableauTuples` to ensure the options are properly
        parsed.

        EXAMPLES::

            sage: STT = StandardTableauTuples([[2,1],[2,1,1]]); STT
            Standard tableau tuples of shape ([2, 1], [2, 1, 1])
            sage: STT.cardinality()
            210
        """
        super().__init__(category=FiniteEnumeratedSets())
        from sage.combinat.partition_tuple import PartitionTuple
        self._shape = PartitionTuple(shape)
        self._level = len(shape)
        self._size = shape.size()

    def __contains__(self, t):
        """
        Containment function of :class:`StandardTableauTuples` of fixed shape.

        EXAMPLES::

            sage: STT = StandardTableauTuples([[2,1],[1]])
            sage: [[[13, 67]], [[14,67]]] in STT
            False
            sage: [[[1, 4],[3]], [[2]]] in STT
            True
            sage: ([[1, 4],[3]], [[2]]) in STT
            True

        Check that :issue:`14145` is fixed::

            sage: 1 in StandardTableauTuples([[2,1],[1]])
            False
        """
        if isinstance(t, self.element_class):
            return self.shape() == t.shape()
        if t in StandardTableauTuples():
            if all(s in Tableaux() for s in t):
                return [[len(l) for l in s] for s in t] == self.shape()
            else:
                return list(self.shape()) == sum(map(len, t))
        return False

    def _repr_(self):
        """
        The string representation of the :class:`StandardTableauTuples` of
        fixed shape.

        EXAMPLES::

            sage: StandardTableauTuples([[2,1],[],[3,1,1,1]])
            Standard tableau tuples of shape ([2, 1], [], [3, 1, 1, 1])
        """
        return 'Standard tableau tuples of shape %s' % self.shape()

    def __iter__(self):
        r"""
        Iterate through the finite class of :class:`StandardTableauTuples` of
        a given :class:`PartitionTuple` shape.

        The algorithm below is modelled on, but different than, the
        corresponding iterator for the standard tableau of partition shape. In
        particular, the tableaux are generated in the reverse order here as
        that is easier (and more useful for applications to graded Specht
        modules).

        EXAMPLES::

            sage: StandardTableauTuples([[1],[1],[1]]).list()
            [([[1]], [[2]], [[3]]),
             ([[2]], [[1]], [[3]]),
             ([[1]], [[3]], [[2]]),
             ([[2]], [[3]], [[1]]),
             ([[3]], [[1]], [[2]]),
             ([[3]], [[2]], [[1]])]
            sage: StandardTableauTuples([[2,1],[2]])[10:20]
            [([[2, 3], [5]], [[1, 4]]),
             ([[1, 4], [5]], [[2, 3]]),
             ([[2, 4], [5]], [[1, 3]]),
             ([[3, 4], [5]], [[1, 2]]),
             ([[1, 5], [2]], [[3, 4]]),
             ([[1, 5], [3]], [[2, 4]]),
             ([[2, 5], [3]], [[1, 4]]),
             ([[1, 5], [4]], [[2, 3]]),
             ([[2, 5], [4]], [[1, 3]]),
             ([[3, 5], [4]], [[1, 2]])]

        TESTS::

            sage: correct_number = lambda mu: StandardTableauTuples(mu).cardinality()==len(StandardTableauTuples(mu).list())
            sage: all(correct_number(mu) for mu in PartitionTuples(4,4))                # needs sage.libs.flint
            True
        """
        mu = self.shape()
        n = mu.size()

        # To generate the standard tableau tuples we are going to flatten them
        # into a list tab which is obtained by reading the tableau along rows.
        # The shape of mu gives a unique way of expanding this list into a
        # tableau which is done using the function tableau_from_list() below. We
        # start with the tableau containing the numbers 1,2,...,n entered in order
        # along the rows of each component and then left to right along the
        # components. This corresponds to the flat list tab=[1,2,...,n].
        tab = list(range(1, n + 1))

        # Set up two lists clen and cclen which give the "end points" of
        # the components of mu and the rows of each component, respectively, so
        # that the numbers contained in component c of the initial tableau are
        #    tab[ clen[c]:clen[c+1] ]
        # and the numbers contained in row r of component c are
        #    tab[ clen[c]:clen[c+1] ][ cclen[c][r]: cclen[c][r+1] ]
        # where tab=[1,2,...,n] as above
        clen = [0]*(len(mu)+1)
        cclen = [[0]*(len(mu[c])+1) for c in range(len(mu))]
        for c in range(len(mu)):
            for r in range(len(mu[c])):
                cclen[c][r+1] = cclen[c][r]+mu[c][r]
            clen[c+1] = clen[c] + cclen[c][-1]

        # now use clen and cclen to "inflate" tab into a tableau
        def tableau_from_list(tab):
            """
            Convert a list tab=[t_1,...,t_n] into the mu-tableau obtained by
            inserting t_1,..,t_n in order into the rows of mu, from left to right
            in each component and then left to right along the components.
            """
            return self.element_class(self, [[tab[clen[c]:clen[c+1]][cclen[c][r]:cclen[c][r+1]]
                                              for r in range(len(mu[c]))]
                                             for c in range(len(mu))],
                                      check=False)

        # We're now ready to start generating the tableaux. Here's the first one:
        initial_tableau = tableau_from_list(tab)
        yield initial_tableau

        # Number the columns of mu from left to right in each component starting
        # from the last component, then to the second last and so on. For example,
        # if \mu=[[2,1],[3]] then the column indices are [3 4 | 0 1 2]. Now
        # define cols to be the list with cols[r] the cols index of r in
        # the tableau tab, for 1\le i\le n. We initialise this for tab,
        # corresponding to the initial tableau.
        cols = [0]*(n+1)   # cols[m] is the column index of m in tab
        mins = [0]*n       # the kth position of tab is always larger than mins[k]
        offset = 0
        for t in initial_tableau[::-1]:
            for row in range(len(t)):
                for col in range(len(t[row])):
                    cols[t[row][col]] = col + offset
                    mins[t[row][col]-1] = row + col
            if t:
                offset += len(t[0])

        # To generate all of the tableaux we look for the first place where
        # cols[r]<cols[r-1]. Then swap r and s where s<r is maximal such that it
        # has a larger column index than r and is either in the same or an
        # earlier component.  (So, s=r-1 if r and r-1 are in the same
        # component.) We then insert 1,2,...,r-1 in order along the rows in the
        # positions that were occupied by 1,2,...,r and leave the numbers larger
        # than r where they were. The next function determines the integer s
        # that r swaps with.

        # define a list so the index i appears in component component[i]
        component = flatten([[i + 1] * mu[i].size() for i in range(len(mu))])

        def max_row_in_component(tab, r):
            """
            Return the largest integer less than r which has higher column index and
            is in the same or an earlier component, with the component index as
            high as possible.
            """
            # find the numbers less than r in same component as r-1
            c = component[tab.index(r)]
            while c > 0:
                comp = [m for m in tab[clen[c-1]:clen[c]] if m < r and cols[m] > cols[r]]
                if not comp:
                    c -= 1
                else:
                    return comp[-1]

        while True:    # loop until we drop! We'll break out of the loop when done
            r = 1      # find the smallest r with cols[r]<cols[r-1]
            while r < len(cols) and cols[r - 1] <= cols[r]:
                r += 1
            if r == len(cols):
                break    # we're at the last tableau so we're done!

            new_cols = list(cols)         # make copies of tab and cols
            new_tab = list(tab)
            s = max_row_in_component(tab, r)
            new_tab[tab.index(s)] = r     # move r to where s currently is
            changed = [-1] * r
            # The list changed records the indexes in new_tab
            # that are occupied by numbers less than or equal to r
            new_cols[r] = cols[s]
            # The new column indices in new_tab
            # the numbers in new_tab and new_cols which is slower.
            changed[-1] = tab.index(s)
            for t in range(1, r):
                i = 0  # find the leftmost index in tab where t can go
                while t <= mins[i] or (tab[i] > r or i in changed):
                    i += 1
                new_tab[i] = t
                new_cols[t] = cols[tab[i]]
                changed[t - 1] = i
            tab = new_tab
            cols = new_cols
            yield tableau_from_list(tab)

        # all done!

    def last(self):
        r"""
        Return the last standard tableau tuple in ``self``, with respect to
        the order that they are generated by the iterator.

        This is just the
        standard tableau tuple with the numbers `1,2, \ldots, n`, where `n`
        is :meth:`~TableauTuples.size`, entered in order down the columns form
        right to left along the components.

        EXAMPLES::

            sage: StandardTableauTuples([[2],[2,2]]).last().pp()
              5  6     1  3
                       2  4
        """
        return StandardTableauTuples(self.shape().conjugate()).first().conjugate()

    def cardinality(self):
        r"""
        Return the number of standard Young tableau tuples of with the same
        shape as the partition tuple ``self``.

        Let `\mu=(\mu^{(1)},\dots,\mu^{(l)})` be the ``shape`` of the
        tableaux in ``self`` and let `m_k=|\mu^{(k)}|`, for `1\le k\le l`.
        Multiplying by a (unique) coset representative of the Young subgroup
        `S_{m_1}\times\dots\times S_{m_l}` inside the symmetric group `S_n`, we
        can assume that `t` is standard and the numbers `1,2...,n` are entered
        in order from to right along the components of the tableau.  Therefore,
        there are

        .. MATH::

            \binom{n}{m_1,\dots,m_l}\prod_{k=1}^l |\text{Std}(\mu^{(k)})|

        standard tableau tuples of this shape, where `|\text{Std}(\mu^{(k)})|`
        is the number of standard tableau of shape `\mu^{(k)}`, for
        `1 \leq k \leq l`. This is given by the hook length formula.

        EXAMPLES::

            sage: StandardTableauTuples([[3,2,1],[]]).cardinality()
            16
            sage: StandardTableauTuples([[1],[1],[1]]).cardinality()
            6
            sage: StandardTableauTuples([[2,1],[1],[1]]).cardinality()
            40
            sage: StandardTableauTuples([[3,2,1],[3,2]]).cardinality()
            36960
        """
        mu = self.shape()
        return Integer(factorial(mu.size())
                       * prod(StandardTableaux(nu).cardinality() / factorial(nu.size()) for nu in mu))

    def an_element(self):
        r"""
        Return a particular element of the class.

        EXAMPLES::

            sage: StandardTableauTuples([[2],[2,1]]).an_element()
            ([[2, 4]], [[1, 3], [5]])
            sage: StandardTableauTuples([[10],[],[]]).an_element()
            ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [], [])
        """
        c = self.cardinality()
        return self[c > 3 and 4 or (c > 1 and -1 or 0)]

    def random_element(self):
        r"""
        Return a random standard tableau in ``self``.

        We do this by randomly selecting addable nodes to place
        `1, 2, \ldots, n`. Of course we could do this recursively, but it is
        more efficient to keep track of the (changing) list of addable nodes
        as we go.

        EXAMPLES::

            sage: StandardTableauTuples([[2],[2,1]]).random_element()  # random
            ([[1, 2]], [[3, 4], [5]])
        """
        tab = [[] for _ in range(self.level())]   # start with the empty tableau and add nodes
        mu = self.shape()
        cells = mu.cells()
        addables = [[i, 0, 0] for i in range(self.level()) if mu[i]]
        m = 0
        while m < mu.size():
            m += 1
            i = randint(0, len(addables) - 1)  # index for a random addable cell
            k, r, c = addables[i]  # the actual cell
            # remove the cell we just added from the list addable nodes
            addables.pop(i)
            # add m into the tableau
            if tab[k] == []:
                tab[k].append([])
            if len(tab[k]) == r:
                tab[k].append([])
            tab[k][r].append(m)
            # now update the list of addable cells - note they must also be in mu
            if (k, r, c + 1) in cells and (r == 0 or (r > 0 and len(tab[k][r - 1]) > c + 1)):
                addables.append([k, r, c + 1])
            if (k, r + 1, c) in cells and (c == 0 or (c > 0 and len(tab[k]) > r + 1 and len(tab[k][r + 1]) == c)):
                addables.append([k, r + 1, c])

        # Just to be safe we check that tab is standard and has shape mu by
        # using the class StandardTableauTuples(mu) to construct the tableau
        return self.element_class(self, tab)


class StandardTableaux_residue(StandardTableauTuples):
    r"""
    Class of all standard tableau tuples with a fixed residue sequence.

    Implicitly, this also specifies the quantum characteristic, multicharge
    and hence the level and size of the tableaux.

    .. NOTE::

        This class is not intended to be called directly, but rather,
        it is accessed through the standard tableaux.

    EXAMPLES::

        sage: StandardTableau([[1,2,3],[4,5]]).residue_sequence(2).standard_tableaux()
        Standard tableaux with 2-residue sequence (0,1,0,1,0) and multicharge (0)
        sage: StandardTableau([[1,2,3],[4,5]]).residue_sequence(3).standard_tableaux()
        Standard tableaux with 3-residue sequence (0,1,2,2,0) and multicharge (0)
        sage: StandardTableauTuple([[[5,6],[7]],[[1,2,3],[4]]]).residue_sequence(2,(0,0)).standard_tableaux()
        Standard tableaux with 2-residue sequence (0,1,0,1,0,1,1) and multicharge (0,0)
        sage: StandardTableauTuple([[[5,6],[7]],[[1,2,3],[4]]]).residue_sequence(3,(0,1)).standard_tableaux()
        Standard tableaux with 3-residue sequence (1,2,0,0,0,1,2) and multicharge (0,1)
    """

    def __init__(self, residue):
        r"""
        Initialize ``self``.

        .. NOTE::

            Input is not checked; please use :class:`StandardTableauTuples`
            to ensure the options are properly parsed.

        EXAMPLES::

            sage: T = StandardTableau([[1,2,3],[4,5]]).residue_sequence(3).standard_tableaux()
            sage: TestSuite(T).run()
            sage: T = StandardTableauTuple([[[6],[7]],[[1,2,3],[4,5]]]).residue_sequence(2,(0,0)).standard_tableaux()
            sage: TestSuite(T).run()
        """
        super().__init__(residue, category=FiniteEnumeratedSets())
        self._level = residue.level()
        self._multicharge = residue.multicharge()
        self._quantum_characteristic = residue.quantum_characteristic()
        self._residue = residue
        self._size = residue.size()

    def _repr_(self):
        """
        Return the string representation of ``self``.

        EXAMPLES::

            sage: StandardTableauTuple([[[1,2],[3]],[[4,5]]]).residue_sequence(3,(0,1)).standard_tableaux()
            Standard tableaux with 3-residue sequence (0,1,2,1,2) and multicharge (0,1)
        """
        return 'Standard tableaux with {}'.format(self._residue.__str__('and'))

    def __contains__(self, t):
        """
        Check containment of ``t`` in ``self``.

        EXAMPLES::

            sage: tabs = StandardTableauTuple([[[1,2],[3]],[[4,5]]]).residue_sequence(3,(0,1)).standard_tableaux()
            sage: tabs
            Standard tableaux with 3-residue sequence (0,1,2,1,2) and multicharge (0,1)
            sage: [[[1,2],[3]],[[4,5]]] in tabs
            True
            sage: [[[1,2],[3]],[[4,5]]] in tabs
            True
            sage: [[[4,5],[3]],[[1,2]]] in tabs
            False
            sage: [[[1,4,5],[3]],[[2]]] in tabs
            True
        """
        if not isinstance(t, self.element_class):
            try:
                t = StandardTableauTuple(t)
            except ValueError:
                return False

        return (t.residue_sequence(self._quantum_characteristic,
                                   self._multicharge) == self._residue)

    def __iter__(self):
        r"""
        Iterate through ``self``.

        We construct this sequence of tableaux recursively. is easier (and
        more useful for applications to graded Specht modules).

        EXAMPLES::

            sage: R = StandardTableauTuple([[[1,2],[5]],[[3,4]]]).residue_sequence(3, (0,1))
            sage: list(R.standard_tableaux())
            [([[1, 2, 4], [5]], [[3]]),
             ([[1, 2, 4]], [[3, 5]]),
             ([[1, 2, 5], [4]], [[3]]),
             ([[1, 2], [4]], [[3, 5]]),
             ([[1, 2, 5]], [[3, 4]]),
             ([[1, 2], [5]], [[3, 4]]),
             ([[1, 3, 4], [5]], [[2]]),
             ([[1, 3, 4]], [[2, 5]]),
             ([[1, 3, 5], [4]], [[2]]),
             ([[1, 3], [4]], [[2, 5]]),
             ([[1, 3, 5]], [[2, 4]]),
             ([[1, 3], [5]], [[2, 4]])]

            sage: R = StandardTableauTuple([[[1,4],[2]],[[3]]]).residue_sequence(3,(0,1))
            sage: list(R.standard_tableaux())
            [([[1, 3], [2], [4]], []),
             ([[1, 3], [2]], [[4]]),
             ([[1, 4], [2], [3]], []),
             ([[1], [2], [3]], [[4]]),
             ([[1, 4], [2]], [[3]]),
             ([[1], [2], [4]], [[3]])]
        """
        if self._size == 0:
            yield StandardTableauTuple([[] for _ in range(self._level)])  # the empty tableaux
            return

        for t in StandardTableaux_residue(self._residue.restrict(self._size - 1)):
            for cell in t.shape().addable_cells():
                if self._residue[self._size] == self._residue.parent().cell_residue(*cell):
                    # a cell of the right residue
                    if self._level == 1:
                        yield t.add_entry(cell, self._size)
                    else:
                        tab = _add_entry_fast(t, cell, self._size)
                        yield self.element_class(self, tab, check=False)


class StandardTableaux_residue_shape(StandardTableaux_residue):
    """
    All standard tableau tuples with a fixed residue and shape.

    INPUT:

    - ``shape`` -- the shape of the partitions or partition tuples
    - ``residue`` -- the residue sequence of the label

    EXAMPLES::

        sage: res = StandardTableauTuple([[[1,3],[6]],[[2,7],[4],[5]]]).residue_sequence(3,(0,0))
        sage: tabs = res.standard_tableaux([[2,1],[2,1,1]]); tabs
        Standard (2,1|2,1^2)-tableaux with 3-residue sequence (0,0,1,2,1,2,1) and multicharge (0,0)
        sage: tabs.shape()
        ([2, 1], [2, 1, 1])
        sage: tabs.level()
        2
        sage: tabs[:6]
        [([[2, 7], [6]], [[1, 3], [4], [5]]),
         ([[1, 7], [6]], [[2, 3], [4], [5]]),
         ([[2, 3], [6]], [[1, 7], [4], [5]]),
         ([[1, 3], [6]], [[2, 7], [4], [5]]),
         ([[2, 5], [6]], [[1, 3], [4], [7]]),
         ([[1, 5], [6]], [[2, 3], [4], [7]])]
    """

    def __init__(self, residue, shape):
        r"""
        Initialize ``self``.

        .. NOTE::

            Input is not checked; please use :class:`StandardTableauTuples`
            to ensure the options are properly parsed.

        TESTS::

            sage: res = StandardTableauTuple([[[1,3],[6]],[[2,7],[4],[5]]]).residue_sequence(3,(0,0))
            sage: tabs = res.standard_tableaux([[2,1],[2,1,1]])
            sage: TestSuite(tabs).run()
        """
        if residue.size() != shape.size():
            raise ValueError('the size of the shape and the length of the residue defence must coincide')

        StandardTableauTuples.__init__(self, category=FiniteEnumeratedSets())
        self._level = residue.level()
        self._multicharge = residue.multicharge()
        self._quantum_characteristic = residue.quantum_characteristic()
        self._residue = residue
        self._shape = shape
        self._size = residue.size()

    def __contains__(self, t):
        """
        Check containment of ``t`` in ``self``.

        EXAMPLES::

            sage: tabs=StandardTableauTuple([[[1,3]],[[2],[4]]]).residue_sequence(3,(0,1)).standard_tableaux([[2],[1,1]])
            sage: [ [[1,2,3,4]], [[]] ] in tabs
            False
            sage: ([[1, 2]], [[3], [4]]) in tabs
            True
        """
        if not isinstance(t, self.element_class):
            try:
                t = StandardTableauTuple(t)
            except ValueError:
                return False
        return (t.shape() == self._shape
                and t.residue_sequence(self._quantum_characteristic,
                                       self._multicharge) == self._residue)

    def _repr_(self):
        """
        Return the string representation of ``self``.

        EXAMPLES::

            sage: StandardTableau([[1,3],[2,4]]).residue_sequence(3).standard_tableaux([2,2])
            Standard (2^2)-tableaux with 3-residue sequence (0,2,1,0) and multicharge (0)
        """
        return 'Standard ({})-tableaux with {}'.format(self._shape._repr_compact_high(),
                                                       self._residue.__str__('and'))

    def __iter__(self):
        r"""
        Iterate through the row standard tableaux in ``self``.

        We construct this sequence of tableaux recursively, as it is easier
        (and more useful for applications to graded Specht modules).

        EXAMPLES::

            sage: StandardTableau([[1,3],[2,4]]).residue_sequence(3).standard_tableaux([2,2])[:]
            [[[1, 3], [2, 4]]]
        """
        if self._size == 0:
            yield StandardTableauTuple([[] for _ in range(self._level)])  # the empty tableaux
            return

        for cell in self._shape.removable_cells():
            if self._residue[self._size] == self._residue.parent().cell_residue(*cell):
                # a cell of the right residue
                for t in StandardTableaux_residue_shape(self._residue.restrict(self._size - 1),
                                                        self._shape.remove_cell(*cell)):
                    if self._level == 1:
                        yield t.add_entry(cell, self._size)
                    else:
                        tab = _add_entry_fast(t, cell, self._size)
                        yield self.element_class(self, tab, check=False)

    def an_element(self):
        r"""
        Return a particular element of ``self``.

        EXAMPLES::

            sage: T = StandardTableau([[1,3],[2]]).residue_sequence(3).standard_tableaux([2,1])
            sage: T.an_element()
            [[1, 3], [2]]
        """
        # the tableaux class may be empty so we trap a ValueError
        try:
            return self[0]
        except ValueError:
            return None


def _add_entry_fast(T, cell, m):
    """
    Helper function to set ``cell`` to ``m`` in ``T`` or add the
    cell to ``T`` with entry ``m``.

    INPUT:

    - ``T`` -- a tableau tuple
    - ``cell`` -- the cell
    - ``m`` -- the entry to add

    OUTPUT: list of lists of lists representing the tableau tuple

    .. WARNING::

        This function assumes that ``cell`` is either in ``T`` or
        and addable corner and does no checking of the input.

    TESTS::

        sage: from sage.combinat.tableau_tuple import _add_entry_fast
        sage: s = StandardTableauTuple([ [[3,4,7],[6,8]], [[9,13],[12]], [[1,5],[2,11],[10]] ]); s.pp()
          3  4  7     9 13     1  5
          6  8       12        2 11
                              10
        sage: t = _add_entry_fast(s, (0,0,3), 14)
        sage: TableauTuple(t).pp()
          3  4  7 14     9 13     1  5
          6  8          12        2 11
                                 10
        sage: t = _add_entry_fast(s, (1,1,1), 14)
        sage: TableauTuple(t).pp()
          3  4  7     9 13     1  5
          6  8       12 14     2 11
                              10
    """
    k, r, c = cell
    tab = T.to_list()

    try:
        tab[k][r][c] = m
    except IndexError:
        # k,r,c should otherwise be an addable cell
        # add (k,r,c) is an addable cell the following should work
        # so we do not need to trap anything
        if r == len(tab[k]):
            tab[k].append([])

        tab[k][r].append(m)
    return tab
