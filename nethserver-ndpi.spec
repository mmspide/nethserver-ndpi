Name: nethserver-ndpi
Version: 1.2.0
Release: 1%{?dist}
Summary: Conifigure ndpi kernel modules
Source: %{name}-%{version}.tar.gz
Source1: https://github.com/NethServer/xt_ndpi-kmod/releases/download/nDPI-2.8_3.10.0-957.el7/xt_ndpi.ko
URL: %{url_prefix}/%{name}
License: GPL

BuildRequires: nethserver-devtools

# Disable debuginfo creation
%define debug_package %{nil}

Requires: kmod-xt_ndpi > 2.7.0
Requires: conntrack-tools

%description
Install and configure an nDPI kernel modules

%prep
%setup

%build
%{makedocs}
perl createlinks
mkdir -p root/lib/modules/3.10.0-957.el7.x86_64/extra/xt_ndpi
cp -p %{SOURCE1} root/lib/modules/3.10.0-957.el7.x86_64/extra/xt_ndpi/

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update

%doc COPYING

%post
echo "Installing NethServer nDPI kernel module. This may take some time ..."
echo "/lib/modules/3.10.0-957.el7.x86_64/extra/xt_ndpi/xt_ndpi.ko" | /sbin/weak-modules --add-modules
echo "Done."

%postun
echo "Removing NethServer nDPI kernel module. This may take some time ..."
echo "/lib/modules/3.10.0-957.el7.x86_64/extra/xt_ndpi/xt_ndpi.ko" | /sbin/weak-modules --remove-modules
echo "Done."


%changelog
* Wed Dec 05 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- Firewall: update to nDPI-netfilter-2.2 and nDPI-2.4  - NethServer/dev#5645

* Thu May 17 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.2-1
- nDPI: support CentOS 7.5 - NethServer/dev#5482

* Fri Nov 24 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.1-1
- shorewall: some netfilter helpers not loaded - Bug NethServer/dev#5385

* Wed Dec 14 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1
- DPI: porting to kernel 3.10.0-514.el7.x86_64 - NethServer/dev#5170

* Wed Sep 28 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- nDPI support: deep packet inspection - NethServer/dev#5102

