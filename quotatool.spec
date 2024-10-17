Summary:	Utility for setting filesystem quotas from the command line
Name:		quotatool
Version:	1.4.12
Release:	2
License:	GPL
Group:		System/Configuration/Other
URL:		https://quotatool.ekenberg.se/
Source0:	http://quotatool.ekenberg.se/%{name}-%{version}.tar.gz

%description
Quotatool is a utility to set filesystem quotas from the commandline. Most
quota-utilities are interactive, requiring manual intervention from the user.
Quotatool on the other hand is not, making it suitable for use in scripts and
other non-interactive situations.

%prep

%setup -q

%build
%configure
%make

%install

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man8

%makeinstall

%files
%doc COPYING README INSTALL AUTHORS
%{_bindir}/*
%{_mandir}/*/*



%changelog
* Fri Feb 24 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.4.12-1
+ Revision: 780121
- version update 1.4.12

* Tue Sep 29 2009 Frederik Himpe <fhimpe@mandriva.org> 1.4.11-1mdv2010.0
+ Revision: 451055
- update to new version 1.4.11

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.4.10-5mdv2010.0
+ Revision: 433046
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.4.10-4mdv2009.0
+ Revision: 260006
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.4.10-3mdv2009.0
+ Revision: 247808
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Sep 25 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.10-1mdv2008.1
+ Revision: 92741
- import quotatool

