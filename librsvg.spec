# TODO
# - mozilla_firefox bcond/subpackage
#
# Conditional build
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	libgsf		# build without libgsf (used for run-time decompression)
%bcond_without	libcroco	# build without CSS support through libcroco
%bcond_without	gnomeprint	# build without gnome-print support in viewer
%bcond_without	gnomevfs	# build without gnome-vfs support
%bcond_without	mozilla		# do not build mozilla plugin
#
Summary:	Raph's SVG library
Summary(pl):	Biblioteka Raph's SVG
Summary(pt_BR):	Biblioteca SVG
Summary(ru):	SVG ÂÉÂÌÉÏÔÅËÁ
Summary(uk):	SVG Â¦ÂÌ¦ÏÔÅËÁ
Name:		librsvg
Version:	2.14.3
Release:	1
Epoch:		1
License:	LGPL v2+
Vendor:		GNOME
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/librsvg/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	f926aa102ccc3ce99ddf257fcce8ebf4
URL:		http://librsvg.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.0.2
BuildRequires:	gtk+2-devel >= 2:2.8.6
%{?with_apidocs:BuildRequires:	gtk-doc >= 0.9}
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.10.0-2}
%{?with_libcroco:BuildRequires:	libcroco-devel >= 0.6.1}
%{?with_gnomeprint:BuildRequires:	libgnomeprintui-devel >= 2.12.1}
%{?with_libgsf:BuildRequires:	libgsf-devel >= 1.13.2}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.22
%{?with_mozilla:BuildRequires:	mozilla-devel}
BuildRequires:	popt-devel >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXft-devel
# CHECK ME! next two are propably not directly required here
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
%{!?with_gnomeprint:BuildConflicts:	libgnomeprintui-devel}
Requires(post,postun):	gtk+2
Requires:	cairo >= 1.0.2
Requires:	gtk+2 >= 2:2.8.6
%{?with_libcroco:Requires:	libcroco >= 0.6.1}
%{?with_libgsf:Requires:	libgsf >= 1.13.2}
Requires:	libxml2 >= 1:2.6.22
Requires:	popt >= 1.5
Obsoletes:	librsvg0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		mozilladir	%{_libdir}/mozilla

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
%{?with_gnomevfs:Requires:	gnome-vfs2-devel >= 2.10.0-2}
Requires:	gtk+2-devel >= 2:2.8.6
Requires:	libart_lgpl-devel >= 2.3.15
%{?with_libcroco:Requires:	libcroco-devel >= 0.6.0}
%{?with_libgsf:Requires:	libgsf-devel >= 1.13.2}
Requires:	libxml2-devel >= 2.6.22
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXft-devel
# CHECK ME! next two are propably not directly required here
Requires:	xorg-lib-libXinerama-devel
Requires:	xorg-lib-libXrandr-devel
Requires:	xorg-lib-libXrender-devel
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
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
This package contains static version of librsvg libraries.

%description static -l pl
Statyczna wersja bibliotek librsvg.

%description static -l pt_BR
Bibliotecas estáticas para o desenvolvimento de aplicações com
librsvg.

%package -n mozilla-plugin-rsvg
Summary:	Mozilla SVG plugin using librsvg
Summary(pl):	Wtyczka Mozilli do SVG wykorzystuj±ca librsvg
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	mozilla

%description -n mozilla-plugin-rsvg
This plugin allows Mozilla-family browsers to view Scalable Vector
Graphics content using librsvg.

%description -n mozilla-plugin-rsvg -l pl
Ta wtyczka pozwala na ogl±danie grafiki w formacie SVG (Scalable
Vector Graphics) w przegl±darkach z rodziny Mozilli.

%prep
%setup -q

%build
%{!?with_mozilla:export MOZILLA_CONFIG=no}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_libcroco:--without-croco} \
	%{!?with_libgsf:--without-svgz} \
	%{!?with_gnomevfs:--disable-gnome-vfs} \
	%{?with_apidocs:--enable-gtk-doc} \
	--with-html-dir=%{_gtkdocdir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/{engines,loaders}/*.{la,a}
rm -f $RPM_BUILD_ROOT%{mozilladir}/plugins/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
gdk-pixbuf-query-loaders > %{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders

%postun
/sbin/ldconfig
umask 022
gdk-pixbuf-query-loaders > %{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/engines/*.so
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/loaders/*.so
%{_mandir}/man1/rsvg.1*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/librsvg-2
%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%if %{with mozilla}
%files -n mozilla-plugin-rsvg
%defattr(644,root,root,755)
%attr(755,root,root) %{mozilladir}/plugins/*.so
%endif
