# TODO
# - check what browsers can be supported by browser plugin
#
# Conditional build
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	libgsf		# build without libgsf (used for run-time decompression)
%bcond_without	libcroco	# build without CSS support through libcroco
%bcond_without	gnomeprint	# build without gnome-print support in viewer
%bcond_without	gnomevfs	# build without gnome-vfs support
%bcond_without	mozilla		# do not build mozilla plugin
#
Summary:	A Raph's Library for Rendering SVG Data
Summary(pl):	Biblioteka Raph's SVG do renderowania danych SVG
Summary(pt_BR):	Biblioteca SVG
Summary(ru):	SVG ÂÉÂÌÉÏÔÅËÁ
Summary(uk):	SVG Â¦ÂÌ¦ÏÔÅËÁ
Name:		librsvg
Version:	2.14.4
Release:	1
Epoch:		1
License:	LGPL v2+
Vendor:		GNOME
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/librsvg/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	945617bb094975d7353a3852302297c1
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
%{?with_mozilla:BuildRequires:	rpmbuild(macros) >= 1.236}
BuildRequires:	popt-devel >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
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

%define		_plugindir	%{_libdir}/browser-plugins

# list of supported browsers, in free form text
%define		browsers	mozilla, mozilla-firefox, netscape, seamonkey

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
%{?with_gnomevfs:Requires:	gnome-vfs2-devel >= 2.10.0-2}
Requires:	gtk+2-devel >= 2:2.8.6
Requires:	libart_lgpl-devel >= 2.3.15
%{?with_libcroco:Requires:	libcroco-devel >= 0.6.0}
%{?with_libgsf:Requires:	libgsf-devel >= 1.13.2}
Requires:	libxml2-devel >= 2.6.22
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

%package -n browser-plugin-%{name}
Summary:	SVG browse plugin using librsvg
Summary(pl):	Wtyczka SVG do przegl±darski WWW wykorzystuj±ca librsvg
Group:		X11/Applications/Multimedia
Requires:	browser-plugins(%{_target_base_arch})
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	mozilla-plugin-rsvg
Obsoletes:	mozilla-plugin-rsvg

%description -n browser-plugin-%{name}
This plugin allows Mozilla-family browsers to view Scalable Vector
Graphics content using librsvg.

Supported browsers: %{browsers}.

%description -n browser-plugin-%{name} -l pl
Ta wtyczka pozwala na ogl±danie grafiki w formacie SVG (Scalable
Vector Graphics) w przegl±darkach z rodziny Mozilli.

Obs³ugiwane przegl±darki: %{browsers}.

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
	plugindir=%{_plugindir} \
	pkgconfigdir=%{_pkgconfigdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/{engines,loaders}/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_plugindir}/*.{la,a}

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

%triggerin -n browser-plugin-%{name} -- mozilla
%nsplugin_install -d %{_libdir}/mozilla/plugins libmozsvgdec.so

%triggerun -n browser-plugin-%{name} -- mozilla
%nsplugin_uninstall -d %{_libdir}/mozilla/plugins libmozsvgdec.so

%triggerin -n browser-plugin-%{name} -- mozilla-firefox
%nsplugin_install -d %{_libdir}/mozilla-firefox/plugins libmozsvgdec.so

%triggerun -n browser-plugin-%{name} -- mozilla-forefox
%nsplugin_uninstall -d %{_libdir}/mozilla-firefox/plugins libmozsvgdec.so

%triggerin -n browser-plugin-%{name} -- netscape-common
%nsplugin_install -d %{_libdir}/netscape/plugins libmozsvgdec.so

%triggerun -n browser-plugin-%{name} -- netscape-common
%nsplugin_uninstall -d %{_libdir}/netscape/plugins libmozsvgdec.so

%triggerin -n browser-plugin-%{name} -- seamonkey
%nsplugin_install -d %{_libdir}/seamonkey/plugins libmozsvgdec.so

%triggerun -n browser-plugin-%{name} -- seamonkey
%nsplugin_uninstall -d %{_libdir}/seamonkey/plugins libmozsvgdec.so

# as rpm removes the old obsoleted package files after the triggers
# are ran, add another trigger to make the links there.
%triggerpostun -n browser-plugin-%{name} -- mozilla-plugin-rsvg
%nsplugin_install -f -d %{_libdir}/mozilla/plugins libmozsvgdec.so

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
%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/*.so
%endif
