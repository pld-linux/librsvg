# Note that this is NOT a relocatable package
%define name		librsvg
%define ver		1.0.1
%define RELEASE		0_cvs_0
%define rel		%{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}
%define prefix		/usr
%define sysconfdir	/etc

Name:		%name
Vendor:		GNOME
Distribution:	CVS
Summary:	Raph's SVG library
Summary(pl):	biblioteka Raph's SVG

Version: 	%ver
Release: 	%rel
Copyright: 	LGPL
Group:		System Environment/Libraries
Source: 	%{name}-%{ver}.tar.gz
URL: 		http://nautilus.eazel.com/
BuildRoot:	/var/tmp/%{name}-%{ver}-root
Docdir: 	%{prefix}/doc
Requires:	glib >= 1.2.9
Requires:	gtk+ >= 1.2.9
Requires:	libxml >= 1.8.10
Requires:	gdk-pixbuf >= 0.10.0
Requires:	popt >= 1.5
Requires:	freetype >= 2.0.1
Requires:	libpng

%description
Eazel Extension Library

%description -l pl
Rozszezona bibioteka eazel

%package devel
Summary:	Libraries and include files for developing with librsvg.
Group:		Development/Libraries
Requires:	%name = %{PACKAGE_VERSION}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with librsvg.

%description devel -l pl
Bibliteki potrzebne do programowania.

%changelog
* Tue Oct 10 2000 Robin Slomkowski <rslomkow@eazel.com>
- removed obsoletes from sub packages and added mozilla and trilobite
subpackages

* Wed Apr 26 2000 Ramiro Estrugo <ramiro@eazel.com>
- created this thing

%prep
%setup

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
CFLAGS="$RPM_OPT_FLAGS" ./configure $MYARCH_FLAGS --prefix=%{prefix} \
	--sysconfdir=%{sysconfdir}

make -k
make check

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
make -k prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT%{sysconfdir} install
for FILE in "$RPM_BUILD_ROOT/bin/*"; do
	file "$FILE" | grep -q not\ stripped && strip $FILE
done

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post
if ! grep %{prefix}/lib /etc/ld.so.conf > /dev/null ; then
	echo "%{prefix}/lib" >> /etc/ld.so.conf
fi
/sbin/ldconfig

%postun -p /sbin/ldconfig

%files

%defattr(0555, bin, bin)
%doc AUTHORS COPYING COPYING.LIB ChangeLog NEWS README
%{prefix}/lib/*.so*

%files devel

%defattr(0555, bin, bin)
%{prefix}/lib/*.la
%{prefix}/lib/*.sh
%{prefix}/bin/librsvg-config

%defattr(0444, bin, bin)
%{prefix}/include/librsvg/*.h
