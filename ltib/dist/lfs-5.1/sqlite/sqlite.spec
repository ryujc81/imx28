%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : SQLite database engine
Name            : sqlite
Version         : 3.6.12
Release         : 1
License         : Public Domain
Vendor          : SQLite Consortium
Packager        : ProFUSION embedded systems <contact@profusion.mobi>
Group           : System Environment/Libraries
URL             : http://www.sqlite.org/2017
Source          : %{name}-amalgamation-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
SQLite is a software library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine.

%Prep
%setup

%Build
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build}
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*.la" | xargs rm -f

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*

