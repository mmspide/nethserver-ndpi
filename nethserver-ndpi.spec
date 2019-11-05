Name: nethserver-ndpi
Version: 1.3.3
Release: 1%{?dist}
Summary: Conifigure ndpi kernel modules
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}
License: GPL

BuildRequires: nethserver-devtools

Requires: kmod-xt_ndpi > 2.3.0
Requires: conntrack-tools

%description
Install and configure an nDPI kernel modules

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update

%doc COPYING

%changelog
* Tue Nov 05 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.3.3-1
- NDPI: try to avoid kernel panic - Bug NethServer/dev#5901

* Mon Oct 28 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.3.2-1
- Shorewall stopped after ndpi update - Bug NethServer/dev#5890

* Wed Oct 16 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.3.1-1
- shorewall stopped with ndpi and old 7.5 kernel - Bug NethServer/dev#5868

* Tue Oct 01 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.3.0-1
- nDPI: update to 2.8.0 for kernel-3.10.0-1062 - NethServer/dev#5841

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

