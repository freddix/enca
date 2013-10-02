Summary:	Extremely Naive Charset Analyser
Name:		enca
Version:	1.15
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.cihar.com/enca/%{name}-%{version}.tar.bz2
# Source0-md5:	fef132969d26e649719eae08297a4a52
Patch0:		%{name}-libdir.patch
URL:		http://freshmeat.net/projects/enca/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	iconv
BuildRequires:	recode-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enca is an Extremely Naive Charset Analyser. It detects character set
and encoding of text files and can also convert them to other
encodings using either a built-in converter or external libraries and
tools like libiconv, librecode, or cstocs.

%package libs
Summary:	Shared Enca library
Group:		Libraries

%description libs
This package contains shared Enca library other programs can
make use of.

%package devel
Summary:	Header files for ENCA library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for ENCA library.

%package apidocs
Summary:	ENCA library API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
ENCA library API documentation.


%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/enconv.1
echo '.so enca.1' > $RPM_BUILD_ROOT%{_mandir}/man1/enconv.1

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libexecdir}/enca
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc README.devel
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libenca

