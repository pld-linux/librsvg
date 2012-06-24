# Note that this is NOT a relocatable package

Summary:	Raph's SVG library
Summary(pl):	Biblioteka Raph's SVG
Summary(pt_BR):	Biblioteca SVG
Name:		librsvg
Version:	2.1.1
Release:	1
License:	LGPL
Vendor:		GNOME
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.1/%{name}-%{version}.tar.bz2
URL:		http://nautilus.eazel.com/
BuildRequires:	freetype-devel
BuildRequires:	gtk+2-devel >= 2.0.6
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel >= 2.4.23
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	librsvg0

%define		_prefix			/usr/X11R6

%description
An SVG library based upon libart.

%description -l pl
Biblioteka do obs�ugi grafiki wektorowej.

%description -l pt_BR
Biblioteca de Extens�o da Eazel.

%package devel
Summary:	Libraries and include files for developing with librsvg
Summary(pl):	Biblioteki i pliki nag��wkowe do developing'u z u�yciem librsvg
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para desenvolvimento com a librsvg
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	librsvg0-devel

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with librsvg.

%description devel -l pl
Bibliteki potrzebne do programowania, zawieraj�ce biblioteki i pliki
nag��wkowe, kt�re pomagaj� tworzenie oprogramowania z wykorzystaniem
librsvg.

%description devel -l pt_BR
Este pacote cont�m os arquivos necess�rios para desenvolver com base
na biblioteca librsvg.

%package static
Summary:	Static libraries and include files for developing with librsvg
Summary(es):	Archivos est�ticos necesarios para el desarrollo de aplicaciones con librsvg.
Summary(pl):	Statyczne biblioteki do developing'u z u�yciem librsvg
Summary(pt_BR):	Arquivos est�ticos necess�rios para o desenvolvimento de aplica��es com librsvg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package provides the necessary development static libraries to
allow you to develop with librsvg.

%description static -l pl
Bibliteki statyczne potrzebne do programowania, zawieraj�ce
biblioteki, kt�re wspomagaj� tworzenie oprogramowania z wykorzystaniem
librsvg.

%description static -l pt_BR
Bibliotecas est�ticas para o desenvolvimento de aplica��es com
librsvg.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/*.la
%{_libdir}/gtk-2.0
%{_datadir}/*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS NEWS
%attr(755,root,root) %{_libdir}/lib*.??
%{_pkgconfigdir}/*.pc
%{_includedir}/librsvg-2

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
