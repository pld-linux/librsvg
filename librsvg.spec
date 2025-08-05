#
# Conditional build
%bcond_without	apidocs		# gi-docgen based API documentation
%bcond_without	static_libs	# static library
%bcond_without	vala		# Vala API (vala up to 0.38.x already contains librsvg-2.0.vapi)

%define		crates_ver	2.60.0

Summary:	A Raph's Library for Rendering SVG Data
Summary(pl.UTF-8):	Biblioteka Raph's SVG do renderowania danych SVG
Summary(pt_BR.UTF-8):	Biblioteca SVG
Summary(ru.UTF-8):	SVG библиотека
Summary(uk.UTF-8):	SVG бібліотека
Name:		librsvg
Version:	2.60.0
Release:	2
Epoch:		1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/librsvg/2.60/%{name}-%{version}.tar.xz
# Source0-md5:	ba3320798fec656c58c849df030dd7d3
# cargo vendor-filterer --platform='*-unknown-linux-*' --tier=2 --features avif,pixbuf
Source1:	%{name}-crates-%{crates_ver}.tar.xz
# Source1-md5:	78edcd0935254159444a94c1d595b9c8
Source2:	rsvg
URL:		https://wiki.gnome.org/Projects/LibRsvg
BuildRequires:	cairo-devel >= 1.18.0
BuildRequires:	cairo-gobject-devel >= 1.18.0
BuildRequires:	cargo
BuildRequires:	cargo-c >= 0.9.19
BuildRequires:	dav1d-devel >= 1.3.0
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docutils
BuildRequires:	fontconfig-devel
# pkgconfig(freetype) >= 20.0.14
BuildRequires:	freetype-devel >= 1:2.8
# with fixed gdk_pixbuf_query_loaders in .pc file
BuildRequires:	gdk-pixbuf2-devel >= 2.42.12-2
%{?with_apidocs:BuildRequires:	gi-docgen >= 2021.1}
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gobject-introspection-devel >= 1.39.0
BuildRequires:	harfbuzz-devel >= 2.0.0
BuildRequires:	libxml2-devel >= 1:2.9.0
BuildRequires:	meson >= 1.3.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.50.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	rust >= 1.77.2
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 2:0.18}
BuildRequires:	xz
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gdk-pixbuf2
Requires:	cairo-gobject >= 1.18.0
Requires:	dav1d >= 1.3.0
Requires:	freetype >= 1:2.8
Requires:	gdk-pixbuf2 >= 2.20
Requires:	glib2 >= 1:2.50.0
Requires:	harfbuzz >= 2.0.0
Requires:	libxml2 >= 1:2.9.0
Requires:	pango >= 1:1.50.0
Obsoletes:	browser-plugin-librsvg < 1:2.15
Obsoletes:	librsvg-gtk+2 < 1:2.40
Obsoletes:	librsvg-gtk+3 < 1:2.46
Obsoletes:	librsvg0 < 2
Obsoletes:	mozilla-plugin-rsvg < 1:2.16.1
# rust archs
ExclusiveArch:	%{x8664} %{ix86} x32 aarch64 armv6hl armv7hl armv7hnl
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
Requires:	cairo-gobject-devel >= 1.18.0
Requires:	freetype-devel >= 1:2.8
Requires:	gdk-pixbuf2-devel >= 2.20
Requires:	glib2-devel >= 1:2.50.0
Requires:	libxml2-devel >= 1:2.9.0
Requires:	pango-devel >= 1:1.50.0
Obsoletes:	librsvg0-devel < 2

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
BuildArch:	noarch

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
BuildArch:	noarch

%description -n vala-librsvg
Vala API for librsvg library.

%description -n vala-librsvg -l pl.UTF-8
API języka Vala do biblioteki librsvg.

%prep
%setup -q -a1

%{__mv} librsvg-%{crates_ver}/* .

# use our offline registry
export CARGO_HOME="$(pwd)/.cargo"

mkdir -p "$CARGO_HOME"
cat >.cargo/config.toml <<EOF
[source.crates-io]
replace-with = 'vendored-sources'

[source.vendored-sources]
directory = '$PWD/vendor'
EOF

%build
export CARGO_HOME="$(pwd)/.cargo"
export PKG_CONFIG_ALLOW_CROSS=1
%meson \
	%{!?with_static_libs:--default-library=shared} \
	-Davif=enabled \
	-Ddocs=%{__enabled_disabled apidocs} \
	-Dintrospection=enabled \
	-Dpixbuf=enabled \
	-Dpixbuf-loader=enabled \
%ifarch x32
	-Dtriplet=x86_64-unknown-linux-gnux32 \
%endif
	-Dvala=%{__enabled_disabled vala}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

export CARGO_HOME="$(pwd)/.cargo"
export PKG_CONFIG_ALLOW_CROSS=1

%meson_install

cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/doc/Rsvg-2.0 $RPM_BUILD_ROOT%{_gidocdir}
%endif

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

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/rsvg
%attr(755,root,root) %{_bindir}/rsvg-convert
%attr(755,root,root) %{_libdir}/librsvg-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librsvg-2.so.2
%{_libdir}/girepository-1.0/Rsvg-2.0.typelib
%attr(755,root,root) %{_libdir}/gdk-pixbuf-2.0/2.*.*/loaders/libpixbufloader_svg.so
%{_datadir}/thumbnailers/librsvg.thumbnailer
%{?with_docs:%{_mandir}/man1/rsvg-convert.1*}

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
%{_gidocdir}/Rsvg-2.0
%endif

%if %{with vala}
%files -n vala-librsvg
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/librsvg-2.0.deps
%{_datadir}/vala/vapi/librsvg-2.0.vapi
%endif
