
# Conditional build
# _without_gimp		- without gimp svg plugin

%ifarch ppc
%define	_without_gimp	1
%endif

Summary:	Raph's SVG library
Summary(pl):	Biblioteka Raph's SVG
Summary(pt_BR):	Biblioteca SVG
Summary(uk):	SVG б╕бл╕отека
Summary(uk):	SVG б╕бл╕отека
Name:		librsvg
Version:	2.3.0
Release:	3
License:	LGPL
Vendor:		GNOME
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
# Source0-md5: 31139e949850f79fa44e089ef10543c2
Patch0:		%{name}-link.patch
URL:		http://nautilus.eazel.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0.1
%{!?_without_gimp:BuildRequires: gimp-devel >= 1.3.12}
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libart_lgpl-devel >= 2.3.11
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.5.1
BuildRequires:	popt-devel
Requires:	gtk+2 >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	librsvg0

%define		gimpplugindir	%(gimp-config --gimpplugindir)/plug-ins

%description
An SVG library based upon libart.

%description -l pl
Biblioteka do obsЁugi grafiki wektorowej.

%description -l pt_BR
Biblioteca de ExtensЦo da Eazel.

%description -l ru
Библиотека SVG, базирующаяся на libart.

%description -l uk
Б╕бл╕отека SVG, базована на libart.

%package devel
Summary:	Include files for developing with librsvg
Summary(pl):	Pliki nagЁСwkowe do tworzenia oprogramowania z u©yciem librsvg
Summary(pt_BR):	Bibliotecas e arquivos de inclusЦo para desenvolvimento com a librsvg
Summary(ru):	Библиотечные линки и файлы заголовков для разработки с librsvg
Summary(uk):	Б╕бл╕отечн╕ л╕нки та файли заголовк╕в для розробки з librsvg
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	librsvg0-devel

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with librsvg.
 
%description devel -l pl
Pakiet zawiera pliki nagЁСwkowe potrzebne do tworzenia oprogramowania
z wykorzystaniem librsvg.

%description devel -l pt_BR
Este pacote contИm os arquivos necessАrios para desenvolver com base
na biblioteca librsvg.

%description devel -l ru
Этот пакет содержит необходимые файлы для разработки программ с
использованием librsvg.

%description devel -l uk
Цей пакет м╕стить необх╕дн╕ файли для розробки програм з використанням
librsvg.

%package static
Summary:	Static libraries for developing with librsvg
Summary(es):	Archivos estАticos necesarios para el desarrollo de aplicaciones con librsvg
Summary(pl):	Statyczne biblioteki librsvg
Summary(pt_BR):	Arquivos estАticos necessАrios para o desenvolvimento de aplicaГУes com librsvg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static version of librsvg libraries.

%description static -l pl
Statyczna wersja bibliotek librsvg.

%description static -l pt_BR
Bibliotecas estАticas para o desenvolvimento de aplicaГУes com
librsvg.

%package -n gimp-svg
Summary:	SVG plugin for Gimp
Summary:	Wtyczka SVG dla Gimpa
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}
Requires:	gimp

%description -n gimp-svg
SVG plugin for Gimp.

%description -n gimp-svg -l pl
Wtyczka SVG dla Gimpa.

%prep
%setup -q
%patch -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
    %{?_without_gimp:--without-gimp}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	manonedir=%{_mandir}/man1

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/{engines,loaders}/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/engines/*.so
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/loaders/*.so
%{_mandir}/man1/rsvg.1*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS NEWS
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc
%{_includedir}/librsvg-2
%{_docdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%if %{?_without_gimp:0}%{!?_without_gimp:1}
%files -n gimp-svg
%defattr(644,root,root,755)
%attr(755,root,root) %{gimpplugindir}/svg
%endif
