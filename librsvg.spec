# Note that this is NOT a relocatable package

Summary:	Raph's SVG library
Summary(pl):	Biblioteka Raph's SVG
Summary(pt_BR):	Biblioteca SVG
Name:		librsvg
Version:	1.0.3
Release:	2
License:	LGPL
Vendor:		GNOME
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
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
Rozszerzona bibioteka eazel.

%description -l pt_BR
Biblioteca de Extens„o da Eazel.

%package devel
Summary:	Libraries and include files for developing with librsvg
Summary(pl):	Biblioteki i pliki nag≥Ûwkowe do developing'u z uøyciem librsvg
Summary(pt_BR):	Bibliotecas e arquivos de inclus„o para desenvolvimento com a librsvg
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Obsoletes:	librsvg0-devel

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with librsvg.

%description devel -l pl
Bibliteki potrzebne do programowania, zawieraj±ce biblioteki i pliki
nag≥Ûwkowe, ktÛre pomagaj± tworzenie oprogramowania z wykorzystaniem
librsvg.

%description devel -l pt_BR
Este pacote contÈm os arquivos necess·rios para desenvolver com base
na biblioteca librsvg.

%package static
Summary:	Static libraries and include files for developing with librsvg
Summary(es):	Archivos est·ticos necesarios para el desarrollo de aplicaciones con librsvg.
Summary(pl):	Statyczne biblioteki do developing'u z uøyciem librsvg
Summary(pt_BR):	Arquivos est·ticos necess·rios para o desenvolvimento de aplicaÁıes com librsvg
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
This package provides the necessary development static libraries to
allow you to develop with librsvg.

%description static -l pl
Bibliteki statyczne potrzebne do programowania, zawieraj±ce
biblioteki, ktÛre wspomagaj± tworzenie oprogramowania z wykorzystaniem
librsvg.

%description static -l pt_BR
Bibliotecas est·ticas para o desenvolvimento de aplicaÁıes com
librsvg.

%prep
%setup -q

%build
%configure2_13

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf ChangeLog AUTHORS NEWS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

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
