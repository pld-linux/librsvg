#
# Conditional build
# _without_gimp		- without gimp svg plugin
# _without_libgsf	- without libgsf (used for run-time decompression)
#
%ifarch ppc
%define	_without_gimp	1
%endif

Summary:	Raph's SVG library
Summary(pl):	Biblioteka Raph's SVG
Summary(pt_BR):	Biblioteca SVG
Summary(uk):	SVG Â¦ÂÌ¦ÏÔÅËÁ
Summary(uk):	SVG Â¦ÂÌ¦ÏÔÅËÁ
Name:		librsvg
Version:	2.3.1
Release:	2
License:	LGPL
Vendor:		GNOME
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	ef9317a3df6d99a44ddf75e4fbcaab4a
Patch0:		%{name}-link.patch
URL:		http://nautilus.eazel.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0.1
%{!?_without_gimp:BuildRequires: gimp-devel >= 1.3.17}
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libart_lgpl-devel >= 2.3.11
# TODO: libcroco-devel >= 0.1.0 (optional)
%{!?_without_libgsf:BuildRequires:	libgsf-devel >= 1.6.0}
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.5.1
BuildRequires:	popt-devel >= 1.5
Requires:	gtk+2 >= 2.2.0
Requires:	popt >= 1.5
Obsoletes:	librsvg0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if 0%{!?_without_gimp:1}
%define		gimpplugindir	%(gimptool-1.3 --gimpplugindir)/plug-ins
%endif

%description
An SVG library based upon libart.

%description -l pl
Biblioteka do obs³ugi grafiki wektorowej.

%description -l pt_BR
Biblioteca de Extensão da Eazel.

%description -l ru
âÉÂÌÉÏÔÅËÁ SVG, ÂÁÚÉÒÕÀÝÁÑÓÑ ÎÁ libart.

%description -l uk
â¦ÂÌ¦ÏÔÅËÁ SVG, ÂÁÚÏ×ÁÎÁ ÎÁ libart.

%package devel
Summary:	Include files for developing with librsvg
Summary(pl):	Pliki nag³ówkowe do tworzenia oprogramowania z u¿yciem librsvg
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento com a librsvg
Summary(ru):	âÉÂÌÉÏÔÅÞÎÙÅ ÌÉÎËÉ É ÆÁÊÌÙ ÚÁÇÏÌÏ×ËÏ× ÄÌÑ ÒÁÚÒÁÂÏÔËÉ Ó librsvg
Summary(uk):	â¦ÂÌ¦ÏÔÅÞÎ¦ Ì¦ÎËÉ ÔÁ ÆÁÊÌÉ ÚÁÇÏÌÏ×Ë¦× ÄÌÑ ÒÏÚÒÏÂËÉ Ú librsvg
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk+2-devel >= 2.2.0
Requires:	libart_lgpl-devel >= 2.3.11
%{!?_without_libgsf:Requires:	libgsf-devel >= 1.6.0}
Requires:	libxml2-devel >= 2.5.1
Obsoletes:	librsvg0-devel

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with librsvg.
 
%description devel -l pl
Pakiet zawiera pliki nag³ówkowe potrzebne do tworzenia oprogramowania
z wykorzystaniem librsvg.

%description devel -l pt_BR
Este pacote contém os arquivos necessários para desenvolver com base
na biblioteca librsvg.

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÎÅÏÂÈÏÄÉÍÙÅ ÆÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó
ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ librsvg.

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÎÅÏÂÈ¦ÄÎ¦ ÆÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ
librsvg.

%package static
Summary:	Static libraries for developing with librsvg
Summary(es):	Archivos estáticos necesarios para el desarrollo de aplicaciones con librsvg
Summary(pl):	Statyczne biblioteki librsvg
Summary(pt_BR):	Arquivos estáticos necessários para o desenvolvimento de aplicações com librsvg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static version of librsvg libraries.

%description static -l pl
Statyczna wersja bibliotek librsvg.

%description static -l pt_BR
Bibliotecas estáticas para o desenvolvimento de aplicações com
librsvg.

%package -n gimp-svg
Summary:	SVG plugin for Gimp
Summary:	Wtyczka SVG dla Gimpa
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}
Requires:	gimp >= 1.3

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
	%{?_without_gimp:--without-gimp} \
	%{?_without_libgsf:--without-svgz}

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
