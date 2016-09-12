===============
nethserver-ndpi
===============

This package install the following dependicies for nDPI:

- kernel module xt_ndpi
- kernel-lt from Elrepo repository (required by xt_ndpi)

Also after the kernel-lt is installed, the package will set it
as default kernel for the next reboot.

The xt_npi module is automatically loaded at boot.
