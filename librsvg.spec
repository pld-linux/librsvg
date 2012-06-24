#
# Conditional build
%bcond_without	libgsf		# build without libgsf (used for run-time decompression)
%bcond_without	libcroco	# build without CSS support through libcroco
#
Summary:	Raph's SVG library
Summary(pl):	Biblioteka Raph's SVG
Summary(pt_BR):	Biblioteca SVG
Summary(ru):	SVG ����������
Summary(uk):	SVG ¦�̦�����
Name:		librsvg
Version:	2.7.1
Release:	1
Epoch:		1
License:	LGPL
Vendor:		GNOME
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	bfdb8ef48923fcfbb38cf7dd2ec848f8
Patch1:		%{name}-ac.patch
URL:		http://librsvg.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	gtk-doc >= 0.9
BuildRequires:	libart_lgpl-devel >= 2.3.15
%{?with_libcroco:BuildRequires:	libcroco-devel >= 0.5.0}
%{?with_libgsf:BuildRequires:	libgsf-devel >= 1.6.0}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.5.10
BuildRequires:	mozilla-embedded-devel
BuildRequires:	popt-devel >= 1.5
BuildRequires:	xcursor-devel
BuildRequires:	xft-devel
BuildRequires:	xrender-devel
PreReq:		mozilla-embedded
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk+2
Requires:	gtk+2 >= 2:2.4.0
Requires:	libart_lgpl >= 2.3.15
%{?with_libcroco:Requires:	libcroco >= 0.5.0}
%{?with_libgsf:Requires:	libgsf >= 1.6.0}
Requires:	libxml2 >= 2.5.10
Requires:	popt >= 1.5
Obsoletes:	librsvg0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		mozilladir	%{_libdir}/mozilla

%description
An SVG library based upon libart.

%description -l pl
Biblioteka do obs�ugi grafiki wektorowej.

%description -l pt_BR
Biblioteca de Extens�o da Eazel.

%description -l ru
���������� SVG, ������������ �� libart.

%description -l uk
��̦����� SVG, �������� �� libart.

%package devel
Summary:	Include files for developing with librsvg
Summary(pl):	Pliki nag��wkowe do tworzenia oprogramowania z u�yciem librsvg
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para desenvolvimento com a librsvg
Summary(ru):	������������ ����� � ����� ���������� ��� ���������� � librsvg
Summary(uk):	��̦����Φ ̦��� �� ����� �������˦� ��� �������� � librsvg
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk+2-devel >= 2:2.4.0
Requires:	libart_lgpl-devel >= 2.3.15
%{?with_libcroco:Requires:	libcroco-devel >= 0.5.0}
%{?with_libgsf:Requires:	libgsf-devel >= 1.6.0}
Requires:	libxml2-devel >= 2.5.10
Obsoletes:	librsvg0-devel

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with librsvg.

%description devel -l pl
Pakiet zawiera pliki nag��wkowe potrzebne do tworzenia oprogramowania
z wykorzystaniem librsvg.

%description devel -l pt_BR
Este pacote cont�m os arquivos necess�rios para desenvolver com base
na biblioteca librsvg.

%description devel -l ru
���� ����� �������� ����������� ����� ��� ���������� �������� �
�������������� librsvg.

%description devel -l uk
��� ����� ͦ����� ����Ȧ�Φ ����� ��� �������� ������� � �������������
librsvg.

%package static
Summary:	Static libraries for developing with librsvg
Summary(es):	Archivos est�ticos necesarios para el desarrollo de aplicaciones con librsvg
Summary(pl):	Statyczne biblioteki librsvg
Summary(pt_BR):	Arquivos est�ticos necess�rios para o desenvolvimento de aplica��es com librsvg
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
This package contains static version of librsvg libraries.

%description static -l pl
Statyczna wersja bibliotek librsvg.

%description static -l pt_BR
Bibliotecas est�ticas para o desenvolvimento de aplica��es com
librsvg.

%package -n	mozilla-plugin-rsvg
Summary:	Mozilla SVG plugin using librsvg
Summary(pl):	Wtyczka Mozilli do SVG wykorzystuj�ca librsvg
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	mozilla-embedded

%description -n mozilla-plugin-rsvg
This plugin allows Mozilla-family browsers to view Scalable Vector
Graphics content using librsvg.

%description -n mozilla-plugin-rsvg -l pl
Ta wtyczka pozwala na ogl�danie grafiki w formacie SVG (Scalable
Vector Graphics) w przegl�darkach z rodziny Mozilli.

%prep
%setup -q
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_libcroco:--without-croco} \
	%{!?with_libgsf:--without-svgz} \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}/%{name}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/{engines,loaders}/*.{la,a}
rm -f $RPM_BUILD_ROOT%{mozilladir}/plugins/*.{la,a}

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

%files -n mozilla-plugin-rsvg
%defattr(644,root,root,755)
%attr(755,root,root) %{mozilladir}/plugins/*.so
