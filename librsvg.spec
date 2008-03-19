# Conditional build
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	libgsf		# build without libgsf (used for run-time decompression)
%bcond_without	libcroco	# build without CSS support through libcroco
%bcond_without	gnomeprint	# build without gnome-print support in viewer
%bcond_without	gnomevfs	# build without gnome-vfs support
%bcond_without	mozilla		# do not build mozilla plugin
#
Summary:	A Raph's Library for Rendering SVG Data
Summary(pl.UTF-8):	Biblioteka Raph's SVG
Summary(pt_BR.UTF-8):	Biblioteca SVG
Summary(ru.UTF-8):	SVG библиотека
Summary(uk.UTF-8):	SVG бібліотека
Name:		librsvg
Version:	2.14.3
Release:	4
Epoch:		1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/librsvg/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	f926aa102ccc3ce99ddf257fcce8ebf4
URL:		http://librsvg.sourceforge.net/
Patch0:		%{name}-xulrunner.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.0.2
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.10.0-2}
BuildRequires:	gtk+2-devel >= 2:2.8.6
%{?with_apidocs:BuildRequires:	gtk-doc >= 0.9}
%{?with_libcroco:BuildRequires:	libcroco-devel >= 0.6.1}
%{?with_gnomeprint:BuildRequires:	libgnomeprintui-devel >= 2.12.1}
%{?with_libgsf:BuildRequires:	libgsf-devel >= 1.13.2}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.22
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.5
BuildRequires:	rpm-pythonprov
%{?with_mozilla:BuildRequires:	rpmbuild(macros) >= 1.357}
%{?with_mozilla:BuildRequires:	xulrunner-devel}
BuildRequires:	xcursor-devel
BuildRequires:	xft-devel
BuildRequires:	xrender-devel
%{!?with_gnomeprint:BuildConflicts:	libgnomeprintui-devel}
Requires(post,postun):	gtk+2
Requires:	cairo >= 1.0.2
Requires:	gtk+2 >= 2:2.8.20-3.2
%{?with_libcroco:Requires:	libcroco >= 0.6.1}
%{?with_libgsf:Requires:	libgsf >= 1.13.2}
Requires:	libxml2 >= 1:2.6.22
Requires:	popt >= 1.5
Obsoletes:	librsvg0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if "%{_lib}" != "lib"
%define		libext		%(lib="%{_lib}"; echo ${lib#lib})
%define		_gtkconfdir	/etc/gtk%{libext}-2.0
%define		pqext		-%{libext}
%else
%define		_gtkconfdir	/etc/gtk-2.0
%define		pqext		%{nil}
%endif


%description
An library to render SVG (scalable vector graphics), databased upon
libart.

%description -l pl.UTF-8
Biblioteka do obsługi grafiki wektorowej.

%description -l pt_BR.UTF-8
Biblioteca de Extensão da Eazel.

%description -l ru.UTF-8
Библиотека SVG, базирующаяся на libart.

%description -l uk.UTF-8
Бібліотека SVG, базована на libart.

%package devel
Summary:	Include files for developing with librsvg
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia oprogramowania z użyciem librsvg
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolvimento com a librsvg
Summary(ru.UTF-8):	Библиотечные линки и файлы заголовков для разработки с librsvg
Summary(uk.UTF-8):	Бібліотечні лінки та файли заголовків для розробки з librsvg
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

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe potrzebne do tworzenia oprogramowania
z wykorzystaniem librsvg.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos necessários para desenvolver com base
na biblioteca librsvg.

%description devel -l ru.UTF-8
Этот пакет содержит необходимые файлы для разработки программ с
использованием librsvg.

%description devel -l uk.UTF-8
Цей пакет містить необхідні файли для розробки програм з використанням
librsvg.

%package static
Summary:	Static libraries for developing with librsvg
Summary(es.UTF-8):	Archivos estáticos necesarios para el desarrollo de aplicaciones con librsvg
Summary(pl.UTF-8):	Statyczne biblioteki librsvg
Summary(pt_BR.UTF-8):	Arquivos estáticos necessários para o desenvolvimento de aplicações com librsvg
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
This package contains static version of librsvg libraries.

%description static -l pl.UTF-8
Statyczna wersja bibliotek librsvg.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para o desenvolvimento de aplicações com
librsvg.

%package -n browser-plugin-%{name}
Summary:	SVG browse plugin using librsvg
Summary(pl.UTF-8):	Wtyczka SVG do przeglądarski WWW wykorzystująca librsvg
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Provides:	mozilla-plugin-rsvg
Obsoletes:	mozilla-plugin-rsvg

%description -n browser-plugin-%{name}
This plugin allows Mozilla-family browsers to view Scalable Vector
Graphics content using librsvg.

%description -n browser-plugin-%{name} -l pl.UTF-8
Ta wtyczka pozwala na oglądanie grafiki w formacie SVG (Scalable
Vector Graphics) w przeglądarkach z rodziny Mozilli.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-mozilla-plugin \
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
	plugindir=%{_browserpluginsdir} \
	pkgconfigdir=%{_pkgconfigdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/{engines,loaders}/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_browserpluginsdir}/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
gdk-pixbuf-query-loaders%{pqext} > %{_gtkconfdir}/gdk-pixbuf.loaders

%postun
/sbin/ldconfig
umask 022
gdk-pixbuf-query-loaders%{pqext} > %{_gtkconfdir}/gdk-pixbuf.loaders

%post -n browser-plugin-%{name}
%update_browser_plugins

%postun -n browser-plugin-%{name}
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

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
%if %{with apidocs}
%{_gtkdocdir}/%{name}
%endif

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%if %{with mozilla}
%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_browserpluginsdir}/*.so
%endif
