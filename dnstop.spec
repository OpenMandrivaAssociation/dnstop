%define	name	dnstop
%define version 20060424
%define release %mkrel 1

Summary:	This displays various tables of DNS traffic on your network
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD
Group:		Monitoring
URL:		http://dnstop.measurement-factory.com/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	libpcap-devel >= 0.7
BuildRequires:	ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
dnstop is a libpcap application (ala tcpdump) that displays
various tables of DNS traffic on your network, including tables
of source and destination IP addresses, query types, top level
domains and second level domains. 

%prep

%setup -q -n %{name}-%{version}

%build
%make CFLAGS="%{optflags}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man8
install -m755 dnstop %{buildroot}%{_sbindir}/
install -m644 dnstop.8 %{buildroot}%{_mandir}/man8/
						
%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE
%attr(0755,root,root) %{_sbindir}/dnstop
%attr(0644,root,root) %{_mandir}/man8/dnstop.8*


