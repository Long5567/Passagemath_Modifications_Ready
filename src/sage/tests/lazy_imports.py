# sage_setup: distribution = sagemath-repl
# sage.doctest: needs sage.all
r"""
TESTS:

Check that all non deprecated lazy imports resolve correctly. We avoid libgiac
on purpose because it does print stuff, see :issue:`31655`.::

    sage: from sage.misc.lazy_import import LazyImport
    sage: G = globals()
    sage: for name, obj in sorted(G.items()):
    ....:     if name in ('libgiac', 'FriCAS', 'Gfan', 'Macaulay2', 'four_ti_2',
    ....:                 'fricas', 'fricas_console', 'frobby', 'gfan', 'macaulay2',
    ....:                 'macaulay2_console', 'qepcad', 'qepcad_console',
    ....:                 'qepcad_formula', 'qepcad_version'):
    ....:          continue
    ....:     if type(obj) is LazyImport and obj._get_deprecation_issue() == 0:
    ....:         try:
    ....:             _ = obj._get_object()
    ....:         except Exception as e:
    ....:             print('{} does not resolve: {}'.format(name, e))

Check that all deprecated lazy imports resolve correctly::

    sage: import warnings
    sage: for name, obj in sorted(G.items()):
    ....:     if type(obj) is LazyImport and obj._get_deprecation_issue() != 0:
    ....:         with warnings.catch_warnings(record=True) as w:
    ....:             _ = obj._get_object()
    ....:             assert w[0].category == DeprecationWarning
"""
