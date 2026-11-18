%define name smeserver-ipset
%define version 1.0
%define release 4
Summary: This is what smeserver-ipset does.
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Source: %{name}-%{version}.tar.gz
License: GNU GPL version 2
Group: SMEserver/addon
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
BuildArchitectures: noarch
BuildRequires: smeserver-devtools
Requires: smeserver-release >= 26:10.0
Requires: ipset
AutoReqProv: no

%description
A Bash shell script which uses ipset and iptables to ban a large number of IP addresses published in IP blacklists. ipset uses a hashtable to store/fetch IP addresses and thus the IP lookup is a lot (!) faster than thousands of sequentially parsed iptables ban rules.

%changelog
* Tue Nov 17 2026 Jean-Philippe Pialasse <jpp@koozali.org> 1.0-4.sme
- fix typo and load modules

* Sun Jun 28 2026 Jean-Philippe Pialasse <jpp@koozali.org> 1.0-3.sme
- add ipset requirement, reorder event, release requirement
- expand masq template

* Fri Jun 26 2026 Jean-Philippe Pialasse <jpp@koozali.org> 1.0-1.sme
- initial release for SME 11 [SME: 13628]
  thanks to Stefano Zamboni for that work


%prep

%setup -q

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
> %{name}-%{version}-filelist
#echo "%doc COPYING"  >> %{name}-%{version}-filelist
#--dir <dir> 'attr(755,user,grp)' \
#--file <file> 'attr(755,root,root)' \

%clean
cd ..
rm -rf %{name}-%{version}

%pre

%preun

%post

%postun
#uninstall
%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
