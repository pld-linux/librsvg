# Note that this is NOT a relocatable package

Summary:	Raph's SVG library
Summary(pl):	Biblioteka Raph's SVG
Name:		librsvg
Version:	1.0.1
Release:	1
License:	LGPL
Vendor:		GNOME
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/librsvg/%{name}-%{version}.tar.bz2
URL:		http://nautilus.eazel.com/
BuildRequires:	glib-devel >= 1.2.9
BuildRequires:	gtk+-devel >= 1.2.9
BuildRequires:	libxml-devel >= 1.8.10
BuildRequires:	gdk-pixbuf-devel >= 0.10.0
BuildRequires:	popt-devel >= 1.5
BuildRequires:	freetype-devel >= 2.0.1
BuildRequires:	libpng-devel
#BuildRequires:	arts-devel
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix		/usr/X11R6
%define _sysconfdir	/etc

%description
An SVG library based upon libart.

%description -l pl
Rozszerzona bibioteka eazel

%package devel
Summary:	Libraries and include files for developing with librsvg.
Summary(pl):	Biblioteki i pliki nag³ówkowe do developing'u z u¿yciem librsvg.
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%name = %{PACKAGE_VERSION}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with librsvg.

%description devel -l pl
Bibliteki potrzebne do programowania, zawieraj±ce biblioteki i pliki
nag³ówkowe, które pomagaj± tworzenie oprogramowania z wykorzystaniem 
librsvg.

%package static
Summary:	Static libraries and include files for developing with librsvg.
Summary(pl):	Statyczne biblioteki do developing'u z u¿yciem librsvg.
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%name = %{PACKAGE_VERSION}

%description static
This package provides the necessary development static libraries to allow you 
to develop with librsvg.

%description static -l pl
Bibliteki statyczne potrzebne do programowania, zawieraj±ce biblioteki, które 
wspomagaj± tworzenie oprogramowania z wykorzystaniem librsvg.

%prep
%setup -q

%build
%configure2_13

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf ChangeLog AUTHORS NEWS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/librsvg-config
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.sh
%{_includedir}/librsvg

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
