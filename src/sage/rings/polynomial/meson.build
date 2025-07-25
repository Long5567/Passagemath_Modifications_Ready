py.install_sources(
  '__init__.py',
  'all.py',
  'binary_form_reduce.py',
  'commutative_polynomial.pxd',
  'complex_roots.py',
  'convolution.py',
  'evaluation.pxd',
  'evaluation_flint.pxd',
  'evaluation_ntl.pxd',
  'flatten.py',
  'groebner_fan.py',
  'ideal.py',
  'infinite_polynomial_element.py',
  'infinite_polynomial_ring.py',
  'integer_valued_polynomials.py',
  'laurent_polynomial.pxd',
  'laurent_polynomial_ideal.py',
  'laurent_polynomial_mpair.pxd',
  'laurent_polynomial_ring.py',
  'laurent_polynomial_ring_base.py',
  'msolve.py',
  'multi_polynomial.pxd',
  'multi_polynomial_element.py',
  'multi_polynomial_ideal.py',
  'multi_polynomial_ideal_libsingular.pxd',
  'multi_polynomial_libsingular.pxd',
  'multi_polynomial_ring.py',
  'multi_polynomial_ring_base.pxd',
  'multi_polynomial_sequence.py',
  'omega.py',
  'ore_function_element.py',
  'ore_function_field.py',
  'ore_polynomial_element.pxd',
  'ore_polynomial_ring.py',
  'plural.pxd',
  'polydict.pxd',
  'polynomial_compiled.pxd',
  'polynomial_complex_arb.pxd',
  'polynomial_element.pxd',
  'polynomial_element_generic.py',
  'polynomial_fateman.py',
  'polynomial_gf2x.pxd',
  'polynomial_integer_dense_flint.pxd',
  'polynomial_integer_dense_ntl.pxd',
  'polynomial_modn_dense_ntl.pxd',
  'polynomial_quotient_ring.py',
  'polynomial_quotient_ring_element.py',
  'polynomial_rational_flint.pxd',
  'polynomial_ring.py',
  'polynomial_ring_constructor.py',
  'polynomial_ring_homomorphism.pxd',
  'polynomial_singular_interface.py',
  'polynomial_zmod_flint.pxd',
  'polynomial_zz_pex.pxd',
  'q_integer_valued_polynomials.py',
  'real_roots.pxd',
  'skew_polynomial_element.pxd',
  'skew_polynomial_finite_field.pxd',
  'skew_polynomial_finite_order.pxd',
  'skew_polynomial_ring.py',
  'symmetric_ideal.py',
  'symmetric_reduction.pxd',
  'term_order.py',
  'toy_buchberger.py',
  'toy_d_basis.py',
  'toy_variety.py',
  subdir: 'sage/rings/polynomial',
)

extension_data = {
  'commutative_polynomial' : files('commutative_polynomial.pyx'),
  'cyclotomic' : files('cyclotomic.pyx'),
  'evaluation_flint' : files('evaluation_flint.pyx'),
  'hilbert' : files('hilbert.pyx'),
  'laurent_polynomial' : files('laurent_polynomial.pyx'),
  'laurent_polynomial_mpair' : files('laurent_polynomial_mpair.pyx'),
  'multi_polynomial' : files('multi_polynomial.pyx'),
  'multi_polynomial_ring_base' : files('multi_polynomial_ring_base.pyx'),
  'ore_polynomial_element' : files('ore_polynomial_element.pyx'),
  'polydict' : files('polydict.pyx'),
  'polynomial_compiled' : files('polynomial_compiled.pyx'),
  'polynomial_complex_arb' : files('polynomial_complex_arb.pyx'),
  'polynomial_element' : files('polynomial_element.pyx'),
  'polynomial_number_field' : files('polynomial_number_field.pyx'),
  'polynomial_real_mpfr_dense' : files('polynomial_real_mpfr_dense.pyx'),
  'polynomial_ring_homomorphism' : files('polynomial_ring_homomorphism.pyx'),
  'real_roots' : files('real_roots.pyx'),
  'refine_root' : files('refine_root.pyx'),
  'skew_polynomial_element' : files('skew_polynomial_element.pyx'),
  'skew_polynomial_finite_field' : files('skew_polynomial_finite_field.pyx'),
  'skew_polynomial_finite_order' : files('skew_polynomial_finite_order.pyx'),
  'symmetric_reduction' : files('symmetric_reduction.pyx'),
}

foreach name, pyx : extension_data
  deps = [py_dep, cysignals, gmp, numpy]
  if name == 'evaluation_flint'
    deps += [flint, mpfi]
  elif name == 'polynomial_complex_arb'
    deps += [flint, mpfi]
  elif name == 'polynomial_real_mpfr_dense'
    deps += [mpfr]
  elif name == 'real_roots'
    deps += [flint, mpfi]
  elif name == 'hilbert'
    deps += [flint, mpfi]
  endif

  py.extension_module(
    name,
    sources: pyx,
    subdir: 'sage/rings/polynomial',
    install: true,
    include_directories: [
      inc_cpython,
      inc_ext,
      inc_flint,
      inc_ntl,
      inc_rings,
      inc_rings_finite,
    ],
    dependencies: deps,
  )
endforeach

extension_data_cpp = {
  'evaluation_ntl': files('evaluation_ntl.pyx'),
  'multi_polynomial_ideal_libsingular': files(
    'multi_polynomial_ideal_libsingular.pyx',
  ),
  'multi_polynomial_libsingular': files('multi_polynomial_libsingular.pyx'),
  'plural': files('plural.pyx'),
  'polynomial_gf2x': files('polynomial_gf2x.pyx'),
  'polynomial_integer_dense_flint': files('polynomial_integer_dense_flint.pyx'),
  'polynomial_integer_dense_ntl': files('polynomial_integer_dense_ntl.pyx'),
  'polynomial_modn_dense_ntl': files('polynomial_modn_dense_ntl.pyx'),
  'polynomial_rational_flint': files('polynomial_rational_flint.pyx'),
  'polynomial_zmod_flint': files('polynomial_zmod_flint.pyx'),
  'polynomial_zz_pex': files('polynomial_zz_pex.pyx'),
}

foreach name, pyx : extension_data_cpp
  deps = [py_dep, cysignals, gmp, numpy]
  if name == 'polynomial_rational_flint'
    deps += [
      cypari2,
      flint,
      mpfi,
      ntl,  # indirect dependency
    ]
  elif name == 'polynomial_zmod_flint'
    deps += [cypari2, flint]
  elif name == 'polynomial_integer_dense_flint'
    deps += [cypari2, flint, ntl]
  else
    deps += [cypari2, givaro, mpfi, mpfr, ntl, pari, singular]
  endif
  py.extension_module(
    name,
    sources: pyx,
    subdir: 'sage/rings/polynomial',
    install: true,
    override_options: ['cython_language=cpp'],
    include_directories: [
      inc_cpython,
      inc_ext,
      inc_flint,
      inc_ntl,
      inc_rings,
      inc_rings_finite,
    ],
    dependencies: deps,
  )

endforeach

install_subdir('padics', install_dir: sage_install_dir / 'rings/polynomial')
subdir('pbori')
subdir('weil')
