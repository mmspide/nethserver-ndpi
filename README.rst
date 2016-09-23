===============
nethserver-ndpi
===============

This package install the following dependicies for nDPI:

- kernel module xt_ndpi
- kernel-lt from Elrepo repository (required by xt_ndpi)

After the kernel-lt is installed:

- the kernel-lt package will be always set as default kernel
- the xt_npi module will be automatically loaded by Shorewall

The complete list of available DPI protocols can be obtained with the following command: ::

  db NethServer::Database::Ndpi keys
