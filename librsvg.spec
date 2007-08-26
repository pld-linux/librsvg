#
# Conditional build
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	libgsf		# build without libgsf (used for run-time decompression)
%bcond_without	libcroco	# build without CSS support through libcroco
%bcond_without	gnomeprint	# build without gnome-print support in viewer
%bcond_without	gnomevfs	# build without gnome-vfs support
%bcond_without	gnome		# disable gnomeprint and gnomevfs
#
%if %{without gnome}
%undefine	with_gnomeprint
%undefine	with_gnomevfs
%endif
Summary:	A Raph's Library for Rendering SVG Data
Summary(pl.UTF-8):	Biblioteka Raph's SVG do renderowania danych SVG
Summary(pt_BR.UTF-8):	Biblioteca SVG
Summary(ru.UTF-8):	SVG библиотека
Summary(uk.UTF-8):	SVG бібліотека
Name:		librsvg
Version:	2.18.1
Release:	1
Epoch:		1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/librsvg/2.18/%{name}-%{version}.tar.bz2
# Source0-md5:	ab250b52cffb436e76f763e72f58e03d
URL:		http://librsvg.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.2.4
BuildRequires:	glib2-devel >= 1:2.12.13
BuildRequires:	gtk+2-devel >= 2:2.10.14
BuildRequires:	gtk-doc-automake
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.18.0}
%{?with_libcroco:BuildRequires:	libcroco-devel >= 0.6.1}
%{?with_gnomeprint:BuildRequires:	libgnomeprintui-devel >= 2.18.0}
%{?with_libgsf:BuildRequires:	libgsf-devel >= 1.14.4}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
Requires(post,postun):	gtk+2
Requires:	cairo >= 1.2.4
Requires:	glib2 >= 1:2.12.13
Requires:	gtk+2 >= 2:2.10.14
%{?with_libcroco:Requires:	libcroco >= 0.6.1}
%{?with_libgsf:Requires:	libgsf >= 1.14.4}
Requires:	libxml2 >= 1:2.6.28
Obsoletes:	browser-plugin-librsvg
Obsoletes:	mozilla-plugin-rsvg
Obsoletes:	librsvg0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An library to render SVG (scalable vector graphics), databased upon libart.

%description -l pl.UTF-8
Biblioteka do renderowania SVG (skalowalnej grafiki wektorowej) oparta
na kodzie libart.

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
Requires:	glib2 >= 1:2.12.13
%{?with_gnomevfs:Requires:	gnome-vfs2-devel >= 2.18.0}
Requires:	gtk+2-devel >= 2:2.10.14
Requires:	libart_lgpl-devel >= 2.3.17
%{?with_libcroco:Requires:	libcroco-devel >= 0.6.1}
%{?with_libgsf:Requires:	libgsf-devel >= 1.14.4}
Requires:	libxml2-devel >= 2.6.28
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
%attr(755,root,root) %{_bindir}/rsvg*
%attr(755,root,root) %{_libdir}/librsvg-2.so.*.*.*
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/engines/*.so
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/loaders/*.so
%{_mandir}/man1/rsvg.1*
%{_pixmapsdir}/svg-viewer.svg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librsvg-2.so
%{_libdir}/librsvg-2.la
%{_pkgconfigdir}/librsvg-2.0.pc
%{_includedir}/librsvg-2
%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/librsvg-2.a
