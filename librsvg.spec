Summary:	Raph's SVG library
Summary(pl):	Biblioteka Raph's SVG
Summary(pt_BR):	Biblioteca SVG
Summary(uk):	SVG б╕бл╕отека
Summary(uk):	SVG б╕бл╕отека
Name:		librsvg
Version:	1.0.3
Release:	3
License:	LGPL
Vendor:		GNOME
Group:		Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/librsvg/%{name}-%{version}.tar.bz2
URL:		http://nautilus.eazel.com/
BuildRequires:	freetype-devel >= 2.0.1
BuildRequires:	gdk-pixbuf-devel >= 0.10.0
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.9
BuildRequires:	libpng-devel
BuildRequires:	libxml-devel >= 1.8.10
BuildRequires:	popt-devel >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	librsvg0

%define		_prefix			/usr/X11R6

%description
An SVG library based upon libart.

%description -l pl
Biblioteka do SVG bazuj╠ca na libart.

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
This package provides the necessary include files which allow you to
develop programs with librsvg.

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

%prep
%setup -q

%build
%configure2_13

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf ChangeLog AUTHORS NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/librsvg-config
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.sh
%{_includedir}/librsvg-1

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
