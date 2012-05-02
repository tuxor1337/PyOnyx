PyOnyx
======

Python API for the onyx/* libraries provided with the imx508 toolchain for Onyx Boox devices (e.g. M92)

We are creating the SIP files for SIP 4.12.2. The source code is provided with the respective source tarball in the repository's root directory. The necessary Python 2.7.3 and PyQt 4.8.5 builds (fully compatible with the Qt version from the Onyx toolchain) are available from the onyx_pyqt.zip file.

Please refer to http://www.mobileread.com/forums/showthread.php?t=177011 for further information and support.

Requirements
------------

Make sure, you have Python 2.7.3, PyQt 4.8.5 and SIP 4.12.2 somewhere in your $PATH and in your $LD_LIBRARY_PATH.

Building PyOnyx has only been tested with the versions provided with this repository so far.

Build and install PyOnyx
------------------------

mkdir compiling
python ../configure.py
make
make install

At the moment, it's not possible to set any build parameters.