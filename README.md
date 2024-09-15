# mps-buildtools
Scripts for building with CMake projects


CMake can be used to build C++ (and other language) software
projects on multiple platforms. The mps-buildtools scripts
allow a developer to set up a CMake project that has the
following instructions for the end user:

- unpack the tarball
- cd to the project directory created by unpacking the tarball
- ./configure
- make all
- make install

A main feature of mps-buildtools is to allow these instructions
to work on Windows and MacOS as well as Linux or other Unix
platforms.



# thello

 This is a simple "Hello, world" C++ project that uses mps-buildtools
 in conjunction with CMake.

# tlib

 This subproject creates a library that is used by
 the tlib-test and tlib-test-source examples.

# tlib-test

 This example shows how to link to a library (tlib) and
 also how to install program assets, in this case
 a simple help file.

# tlib-test-source

 This is the same as tlib-test, but the library is compiled
 from source instead of being linked, an approach that is
 necessary when cross-compiling or compiling for Android or
 IOS.



