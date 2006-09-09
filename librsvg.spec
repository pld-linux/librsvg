#
# Conditional build
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	libgsf		# build without libgsf (used for run-time decompression)
%bcond_without	libcroco	# build without CSS support through libcroco
%bcond_without	gnomeprint	# build without gnome-print support in viewer
%bcond_without	gnomevfs	# build without gnome-vfs support
#
Summary:	A Raph's Library for Rendering SVG Data
Summary(pl):	Biblioteka Raph's SVG do renderowania danych SVG
Summary(pt_BR):	Biblioteca SVG
Summary(ru):	SVG ÂÉÂÌÉÏÔÅËÁ
Summary(uk):	SVG Â¦ÂÌ¦ÏÔÅËÁ
Name:		librsvg
Version:	2.16.0
Release:	1
Epoch:		1
License:	LGPL v2+
Vendor:		GNOME
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/librsvg/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	dc6385e62ed278732146bca5aab74568
URL:		http://librsvg.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.2.4
BuildRequires:	gtk+2-devel >= 2:2.10.2
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.7}
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.15.92}
%{?with_libcroco:BuildRequires:	libcroco-devel >= 0.6.1}
%{?with_gnomeprint:BuildRequires:	libgnomeprintui-devel >= 2.12.1}
%{?with_libgsf:BuildRequires:	libgsf-devel >= 1.14.1}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	popt-devel >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
Requires(post,postun):	gtk+2
Requires:	cairo >= 1.2.4
Requires:	gtk+2 >= 2:2.10.2
%{?with_libcroco:Requires:	libcroco >= 0.6.1}
%{?with_libgsf:Requires:	libgsf >= 1.14.1}
Requires:	libxml2 >= 1:2.6.26
Requires:	popt >= 1.5
Obsoletes:	browser-plugin-librsvg
Obsoletes:	librsvg0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An library to render SVG (scalable vector graphics), databased upon libart.

%description -l pl
Biblioteka do renderowania SVG (skalowalnej grafiki wektorowej) oparta
na kodzie libart.

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
%{?with_gnomevfs:Requires:	gnome-vfs2-devel >= 2.15.92}
Requires:	gtk+2-devel >= 2:2.10.2
Requires:	libart_lgpl-devel >= 2.3.17
%{?with_libcroco:Requires:	libcroco-devel >= 0.6.1}
%{?with_libgsf:Requires:	libgsf-devel >= 1.14.1}
Requires:	libxml2-devel >= 2.6.26
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

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_gnomevfs:--disable-gnome-vfs} \
	%{!?with_gnomeprint:--disable-gnome-print} \
	--disable-mozilla-plugin \
	%{?with_apidocs:--enable-gtk-doc} \
	%{!?with_libcroco:--without-croco} \
	%{!?with_libgsf:--without-svgz} \
	--with-html-dir=%{_gtkdocdir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/{engines,loaders}/*.{la,a}

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
