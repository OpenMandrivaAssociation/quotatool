Summary:	Utility for setting filesystem quotas from the command line
Name:		quotatool
Version:	1.4.12
Release:	1
License:	GPL
Group:		System/Configuration/Other
URL:		http://quotatool.ekenberg.se/
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

