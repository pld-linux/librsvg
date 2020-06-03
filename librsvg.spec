#
# Conditional build
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	static_libs	# don't build static library
%bcond_without	vala		# Vala API (vala up to 0.38.x already contains librsvg-2.0.vapi)

%define		mver	2.48
%define		pver	6
Summary:	A Raph's Library for Rendering SVG Data
Summary(pl.UTF-8):	Biblioteka Raph's SVG do renderowania danych SVG
Summary(pt_BR.UTF-8):	Biblioteca SVG
Summary(ru.UTF-8):	SVG библиотека
Summary(uk.UTF-8):	SVG бібліотека
Name:		librsvg
Version:	%{mver}.%{pver}
Release:	1
Epoch:		1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/librsvg/%{mver}/%{name}-%{version}.tar.xz
# Source0-md5:	9e12b3560609cf66302f0b0d14a73f9f
Source1:	rsvg
Patch0:		x32.patch
Patch1:		%{name}-gtkdoc.patch
URL:		http://librsvg.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	cairo-devel >= 1.16.0
BuildRequires:	cairo-gobject-devel >= 1.16.0
BuildRequires:	cargo
BuildRequires:	docbook-dtd43-xml
BuildRequires:	fontconfig-devel
# pkgconfig(freetype) >= 20.0.14
BuildRequires:	freetype-devel >= 1:2.8
BuildRequires:	gdk-pixbuf2-devel >= 2.20
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gobject-introspection-devel >= 0.10.8
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.13}
%{?with_apidocs:BuildRequires:	gtk-doc-automake >= 1.13}
BuildRequires:	libcroco-devel >= 0.6.1
BuildRequires:	libtool >= 2:2.0
BuildRequires:	libxml2-devel >= 1:2.9.0
BuildRequires:	pango-devel >= 1:1.38.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rust >= 1.39
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 2:0.18}
BuildRequires:	xz
Requires(post,postun):	/sbin/ldconfig
Requires:	cairo-gobject >= 1.16.0
Requires:	freetype >= 1:2.8
Requires:	gdk-pixbuf2 >= 2.20
Requires:	glib2 >= 1:2.50.0
Requires:	libcroco >= 0.6.1
Requires:	libxml2 >= 1:2.9.0
Requires:	pango >= 1:1.38.0
Obsoletes:	browser-plugin-librsvg
Obsoletes:	librsvg-gtk+2
Obsoletes:	librsvg-gtk+3
Obsoletes:	librsvg0
Obsoletes:	mozilla-plugin-rsvg
# rust archs
ExclusiveArch:	%{x8664} %{ix86} aarch64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# see gdk-pixbuf2.spec for source of these ifdefs
%if "%{_lib}" != "lib"
%define         libext          %(lib="%{_lib}"; echo ${lib#lib})
%define         pqext           -%{libext}
%else
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
Requires:	cairo-gobject-devel >= 1.16.0
Requires:	freetype-devel >= 1:2.8
Requires:	gdk-pixbuf2-devel >= 2.20
Requires:	glib2-devel >= 1:2.50.0
Requires:	libcroco-devel >= 0.6.1
Requires:	libxml2-devel >= 1:2.9.0
Requires:	pango-devel >= 1:1.38.0
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
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description apidocs
librsvg API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki librsvg.

%package -n vala-librsvg
Summary:	Vala API for librsvg library
Summary(pl.UTF-8):	API języka Vala do biblioteki librsvg
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	vala >= 2:0.40

%description -n vala-librsvg
Vala API for librsvg library.

%description -n vala-librsvg -l pl.UTF-8
API języka Vala do biblioteki librsvg.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%if %{without apidocs}
echo 'CLEANFILES=' > gtk-doc.make
echo 'AC_DEFUN([GTK_DOC_CHECK],[])' >> acinclude.m4
%endif

%build
%{?with_apidocs:%{__gtkdocize}}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{__enable_disable apidocs gtk-doc} \
	--enable-introspection \
	--disable-silent-rules \
	%{__enable_disable static_libs static} \
	%{?with_vala:--enable-vala} \
	--with-html-dir=%{_gtkdocdir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/2.*.*/loaders/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/2.*.*/loaders/*.a
%endif
%{__rm} $RPM_BUILD_ROOT%{_libdir}/librsvg-2.la

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
%{_bindir}/gdk-pixbuf-query-loaders%{pqext} --update-cache || :

%postun
/sbin/ldconfig
umask 022
if [ -x %{_bindir}/gdk-pixbuf-query-loaders%{pqext} ]; then
	%{_bindir}/gdk-pixbuf-query-loaders%{pqext} --update-cache
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/rsvg
%attr(755,root,root) %{_bindir}/rsvg-convert
%attr(755,root,root) %{_libdir}/librsvg-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librsvg-2.so.2
%{_libdir}/girepository-1.0/Rsvg-2.0.typelib
%attr(755,root,root) %{_libdir}/gdk-pixbuf-2.0/2.*.*/loaders/libpixbufloader-svg.so
%{_datadir}/thumbnailers/librsvg.thumbnailer
%{_mandir}/man1/rsvg-convert.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librsvg-2.so
%{_includedir}/librsvg-2.0
%{_datadir}/gir-1.0/Rsvg-2.0.gir
%{_pkgconfigdir}/librsvg-2.0.pc

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

%if %{with vala}
%files -n vala-librsvg
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/librsvg-2.0.vapi
%endif
