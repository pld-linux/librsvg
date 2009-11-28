#
# Conditional build
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	libgsf		# build without libgsf (used for run-time decompression)
%bcond_without	libcroco	# build without CSS support through libcroco
%bcond_without	static_libs	# don't build static library
#
Summary:	A Raph's Library for Rendering SVG Data
Summary(pl.UTF-8):	Biblioteka Raph's SVG do renderowania danych SVG
Summary(pt_BR.UTF-8):	Biblioteca SVG
Summary(ru.UTF-8):	SVG библиотека
Summary(uk.UTF-8):	SVG бібліотека
Name:		librsvg
Version:	2.26.0
Release:	2
Epoch:		1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/librsvg/2.26/%{name}-%{version}.tar.bz2
# Source0-md5:	65dbd726a514fe8b797d26254b8efc1e
URL:		http://librsvg.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk+2-devel >= 2:2.12.8
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
%{?with_apidocs:BuildRequires:	gtk-doc-automake}
%{?with_libcroco:BuildRequires:	libcroco-devel >= 0.6.1}
%{?with_libgsf:BuildRequires:	libgsf-devel >= 1.14.4}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk+2
Requires:	glib2 >= 1:2.16.0
Requires:	gtk+2 >= 2:2.12.8
%{?with_libcroco:Requires:	libcroco >= 0.6.1}
%{?with_libgsf:Requires:	libgsf >= 1.14.4}
Requires:	libxml2 >= 1:2.6.31
Obsoletes:	browser-plugin-librsvg
Obsoletes:	librsvg0
Obsoletes:	mozilla-plugin-rsvg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# see gtk+2.spec for source of these ifdefs
%if "%{_lib}" != "lib"
%define         libext          %(lib="%{_lib}"; echo ${lib#lib})
%define         gtketcdir	/etc/gtk%{libext}-2.0
%define         pqext           -%{libext}
%else
%define         gtketcdir	/etc/gtk-2.0
%define         pqext           %{nil}
%endif

%description
An library to render SVG (scalable vector graphics), databased upon
libart.

%description -l pl.UTF-8
Biblioteka do renderowania SVG (skalowalnej grafiki wektorowej) oparta
na kodzie libart.

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
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 1:2.16.0
Requires:	gtk+2-devel >= 2:2.12.8
%{?with_libcroco:Requires:	libcroco-devel >= 0.6.1}
%{?with_libgsf:Requires:	libgsf-devel >= 1.14.4}
Requires:	libxml2-devel >= 1:2.6.31
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
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
This package contains static version of librsvg libraries.

%description static -l pl.UTF-8
Statyczna wersja bibliotek librsvg.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para o desenvolvimento de aplicações com
librsvg.

%package apidocs
Summary:	librsvg API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki librsvg
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
librsvg API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki librsvg.

%prep
%setup -q

%if !%{with apidocs}
echo 'CLEANFILES=' > gtk-doc.make
echo 'AC_DEFUN([GTK_DOC_CHECK],[])' >> acinclude.m4
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-mozilla-plugin \
	%{!?with_static_libs:--disable-static} \
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
%{_bindir}/gdk-pixbuf-query-loaders%{pqext} > %{gtketcdir}/gdk-pixbuf.loaders

%postun
/sbin/ldconfig
umask 022
if [ -x %{_bindir}/gdk-pixbuf-query-loaders%{pqext} ]; then
	%{_bindir}/gdk-pixbuf-query-loaders%{pqext} > %{gtketcdir}/gdk-pixbuf.loaders
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS NEWS
%attr(755,root,root) %{_bindir}/rsvg
%attr(755,root,root) %{_bindir}/rsvg-convert
%attr(755,root,root) %{_bindir}/rsvg-view
%attr(755,root,root) %{_libdir}/librsvg-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librsvg-2.so.2
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/engines/libsvg.so
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/loaders/svg_loader.so
%{_mandir}/man1/rsvg.1*
%{_pixmapsdir}/svg-viewer.svg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librsvg-2.so
%{_libdir}/librsvg-2.la
%{_pkgconfigdir}/librsvg-2.0.pc
%{_includedir}/librsvg-2

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/librsvg-2.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%endif
