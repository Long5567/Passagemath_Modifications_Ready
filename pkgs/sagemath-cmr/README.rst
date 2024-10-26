==========================================================================
 passagemath: Combinatorial matrix recognition
==========================================================================

About SageMath
--------------

   "Creating a Viable Open Source Alternative to
    Magma, Maple, Mathematica, and MATLAB"

   Copyright (C) 2005-2024 The Sage Development Team

   https://www.sagemath.org

SageMath fully supports all major Linux distributions, recent versions of
macOS, and Windows (Windows Subsystem for Linux).

See https://doc.sagemath.org/html/en/installation/index.html
for general installation instructions.


About this pip-installable source distribution
----------------------------------------------

This pip-installable source distribution ``passagemath-cmr`` is a small
optional distribution for use with ``passagemath-standard``.

It provides a Cython interface to the CMR library (https://github.com/discopt/cmr),
providing recognition and decomposition algorithms for:

- Totally Unimodular Matrices
- Network Matrices
- Complement Totally Unimodular Matrices
- (Strongly) k-Modular and Unimodular Matrices
- Regular Matroids
- Graphic / Cographic / Planar Matrices
- Series-Parallel Matroids


Development
-----------

::

    $ git clone --origin passagemath https://github.com/passagemath/passagemath.git
    $ cd passagemath
    passagemath $ ./bootstrap
    passagemath $ ./.homebrew-build-env         # on macOS when homebrew is in use
    passagemath $ python3 -m venv cmr-venv
    passagemath $ source cmr-venv/bin/activate
    (cmr-venv) passagemath $ pip install -v -e pkgs/sagemath-cmr        \
                                            -e pkgs/sagemath-modules    \
                                            -e pkgs/sagemath-categories
