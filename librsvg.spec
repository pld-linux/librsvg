# Note that this is NOT a relocatable package

Summary:	Raph's SVG library
Summary(pl):	biblioteka Raph's SVG
Name:		librsvg
Version:	1.0.1
Release:	1
License:	LGPL
Vendor:		GNOME
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/librsvg/%{name}-%{version}.tar.bz2
URL:		http://nautilus.eazel.com/
BuildRequires:	glib-devel >= 1.2.9
BuildRequires:	gtk+-devel >= 1.2.9
BuildRequires:	libxml-devel >= 1.8.10
BuildRequires:	gdk-pixbuf-devel >= 0.10.0
BuildRequires:	popt-devel >= 1.5
BuildRequires:	freetype-devel >= 2.0.1
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix		/usr
%define _sysconfdir	/etc

%description
Eazel Extension Library

%description -l pl
Rozszezona bibioteka eazel

%package devel
Summary:	Libraries and include files for developing with librsvg.
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%name = %{PACKAGE_VERSION}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with librsvg.

%description devel -l pl
Bibliteki potrzebne do programowania.

%prep
%setup -q

%build
%ifarch alpha
	MYARCH_FLAGS="--host=alpha-redhat-linux"
%endif

LC_ALL=""
LINGUAS=""
LANG=""
export LC_ALL LINGUAS LANG

## Warning!  Make sure there are no spaces or tabs after the \ 
## continuation character, or else the rpm demons will eat you.
CFLAGS="$RPM_OPT_FLAGS" ./configure $MYARCH_FLAGS --prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir}

make -k
make check

%install
rm -rf $RPM_BUILD_ROOT
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
%{__make} -k prefix=$RPM_BUILD_ROOT%{_prefix} sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir} install
for FILE in "$RPM_BUILD_ROOT/bin/*"; do
	file "$FILE" | grep -q not\ stripped && strip $FILE
done

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post
if ! grep %{_prefix}/lib /etc/ld.so.conf > /dev/null ; then
	echo "%{_prefix}/lib" >> /etc/ld.so.conf
fi
/sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)

%defattr(0555, bin, bin)
%doc AUTHORS COPYING COPYING.LIB ChangeLog NEWS README
%{_libdir}/*.so*

%files devel
%defattr(644,root,root,755)

%defattr(0555, bin, bin)
%{_libdir}/*.la
%{_libdir}/*.sh
%attr(755,root,root) %{_bindir}/librsvg-config

%defattr(0444, bin, bin)
%{_includedir}/librsvg/*.h
