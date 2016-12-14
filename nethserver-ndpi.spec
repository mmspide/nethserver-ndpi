Name: nethserver-ndpi
Version: 1.1.0
Release: 1%{?dist}
Summary: Conifigure ndpi kernel modules
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}
License: GPL

BuildRequires: nethserver-devtools

Requires: kmod-xt_ndpi

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
* Wed Dec 14 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1
- DPI: porting to kernel 3.10.0-514.el7.x86_64 - NethServer/dev#5170

* Wed Sep 28 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- nDPI support: deep packet inspection - NethServer/dev#5102

