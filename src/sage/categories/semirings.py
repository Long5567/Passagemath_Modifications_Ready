# sage_setup: distribution = sagemath-categories
r"""
Semirings
"""
# ****************************************************************************
#  Copyright (C) 2010 Nicolas Borie <nicolas.borie@math.u-psud.fr>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#                  https://www.gnu.org/licenses/
# *****************************************************************************

from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.magmas_and_additive_magmas import MagmasAndAdditiveMagmas


class Semirings(CategoryWithAxiom):
    """
    The category of semirings.

    A semiring `(S, +, *)` is similar to a ring, but without the
    requirement that each element must have an additive inverse. In
    other words, it is a combination of a commutative additive monoid
    `(S, +)` and a multiplicative monoid `(S, *)`, where `*` distributes
    over `+`.

    .. SEEALSO::

        :wikipedia:`Semiring`

    EXAMPLES::

        sage: Semirings()
        Category of semirings
        sage: Semirings().super_categories()
        [Category of associative additive commutative additive
         associative additive unital distributive magmas and additive magmas,
         Category of monoids]

        sage: sorted(Semirings().axioms())
        ['AdditiveAssociative', 'AdditiveCommutative', 'AdditiveUnital',
         'Associative', 'Distributive', 'Unital']

        sage: Semirings() is (CommutativeAdditiveMonoids() & Monoids()).Distributive()
        True

        sage: Semirings().AdditiveInverse()
        Category of rings


    TESTS::

        sage: TestSuite(Semirings()).run()
        sage: Semirings().example()
        An example of a semiring: the ternary-logic semiring
    """
    _base_category_class_and_axiom = (MagmasAndAdditiveMagmas.Distributive.AdditiveAssociative.AdditiveCommutative.AdditiveUnital.Associative, "Unital")

    def __lean_init__(self):
        r"""
        Return the category as Lean mathlib input for a typeclass.

        EXAMPLES::

            sage: from sage.categories.semirings import Semirings
            sage: C = Semirings(); C
            Category of semirings
            sage: C.__lean_init__()
            'semiring'
        """
        # defined in algebra.ring.basic
        return 'semiring'
