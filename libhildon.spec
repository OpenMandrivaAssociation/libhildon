%define	major 0
%define libname	%mklibname hildon %{major}
%define develname %mklibname -d hildon

Summary:	Hildon libraries
Name:		libhildon
Version:	2.0.6
Release:	%mkrel 5
Group:		System/Libraries
License:	LGPLv2+
URL:		http://live.gnome.org/Hildon
Source0:	http://repository.maemo.org/pool/diablo/free/libh/libhildon/libhildon_%{version}-1.tar.gz
Patch0:		libhildon-2.0.6-poname.diff
BuildRequires:	esound-devel
BuildRequires:	gtk2-devel
BuildRequires:	libGConf2-devel
BuildRequires:	libx11-devel
BuildRequires:	png-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot  

%description
Hildon is the widget library for maemo. It contains widgets appropriate for
internet tablet applications.

%package -n	%{libname}
Summary:	Hildon libraries development files
Group:		System/Libraries

%description -n	%{libname}
Hildon is the widget library for maemo. It contains widgets appropriate for
internet tablet applications.

%package -n	%{develname}
Summary:	Hildon libraries development files
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	hildon-devel = %{version}-%{release}

%description -n	%{develname}
Hildon is the widget library for maemo. It contains widgets appropriate for
internet tablet applications.

This package contains all necessary include files, libraries, configuration
files and development tools needed to compile and link applications using the
hildon library.

%prep

%setup -q -n libhildon-%{version}
%patch0 -p0

%build
rm -f configure
libtoolize --copy --force; aclocal -I m4; autoheader; automake --add-missing --copy --gnu; autoconf
export LIBS="-lX11"

%configure2_5x \
    --without-maemo-gtk

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname} -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README COPYING
%{_libdir}/libhildon-1.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/hildon-1
%{_libdir}/*.*a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

