Summary:	X Virtual Keyboard library
Summary(pl.UTF-8):	Biblioteka wirtualnej klawiatury dla X
Name:		libfakekey
Version:	0.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://projects.o-hand.com/matchbox/sources/libfakekey/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	83dbde4d77e8baf0176fe4291d8a2303
Patch0:		%{name}-build.patch
URL:		http://projects.o-hand.com/matchbox/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Virtual Keyboard library.

%description -l pl.UTF-8
Biblioteka wirtualnej klawiatury dla X.

%package devel
Summary:	Header files for libfakekey library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libfakekey
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXtst-devel

%description devel
Header files for libfakekey library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libfakekey.

%package static
Summary:	Static libfakekey library
Summary(pl.UTF-8):	Statyczna biblioteka libfakekey
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libfakekey library.

%description static -l pl.UTF-8
Statyczna biblioteka libfakekey.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libfakekey.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfakekey.so.[0-9]

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfakekey.so
%{_libdir}/libfakekey.la
%{_includedir}/fakekey
%{_pkgconfigdir}/libfakekey.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libfakekey.a
