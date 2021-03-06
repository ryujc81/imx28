%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : GStreamer Plugins Good
Name            : gst-plugins-good
Version         : 0.10.30
Release         : 1
License         : LGPL
Vendor          : Freescale
Packager        : Dexter Ji
Group           : Applications/System
Source          : %{name}0.10_%{version}.orig.tar.bz2
Patch1          : %{name}-0.10.5-relink.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup
%patch1 -p1

%Build
./configure --prefix=%{_prefix} --host=$CFGHOST \
	    --build=%{_build} --without-check \
	    --disable-speex \
	    --disable-shout2test --disable-shout2 \
	    --disable-dv1394 --disable-libpng \
	    --disable-libdv --disable-libcaca \
	    --disable-ladspa --disable-jpeg \
	    --disable-flac \
	    --disable-esd --disable-esdtest \
	    --disable-cairo --disable-aalib \
	    --disable-aalibtest --disable-x \
	    --disable-xvideo --disable-hal NM=nm
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
