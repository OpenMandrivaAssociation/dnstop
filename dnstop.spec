Summary:	This displays various tables of DNS traffic on your network
Name:		dnstop
Version:	20090128
Release:	%mkrel 2
License:	BSD
Group:		Monitoring
URL:		http://dnstop.measurement-factory.com/
Source0:	http://dns.measurement-factory.com/tools/dnstop/src/%{name}-%{version}.tar.gz
BuildRequires:	libpcap-devel >= 0.7
BuildRequires:	ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
dnstop is a libpcap application (ala tcpdump) that displays
various tables of DNS traffic on your network, including tables
of source and destination IP addresses, query types, top level
domains and second level domains. 

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make CFLAGS="%{optflags} -DUSE_IPV6=1 -DUSE_PPP=0"

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
%doc CHANGES LICENSE
%attr(0755,root,root) %{_sbindir}/dnstop
%attr(0644,root,root) %{_mandir}/man8/dnstop.8*
