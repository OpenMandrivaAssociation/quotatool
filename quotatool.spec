Summary:	Utility for setting filesystem quotas from the command line
Name:		quotatool
Version:	1.4.10
Release:	%mkrel 3
License:	GPL
Group:		System/Configuration/Other
URL:		http://quotatool.ekenberg.se/
Source0:	http://quotatool.ekenberg.se/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man8

%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README INSTALL AUTHORS
%{_bindir}/*
%{_mandir}/*/*

