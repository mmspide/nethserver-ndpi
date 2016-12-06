===============
nethserver-ndpi
===============

This package install the following dependicies for nDPI:

- kernel module xt_ndpi
- kernel 3.10.0-514.el7.x86_64 from CentOS 7.3

The complete list of available DPI protocols can be obtained with the following command: ::

  db NethServer::Database::Ndpi keys
