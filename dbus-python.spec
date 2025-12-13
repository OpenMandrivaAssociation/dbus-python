%global __requires_exclude python-gi

Summary:	D-Bus Python Bindings
Name:		dbus-python
Version:	1.4.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://www.freedesktop.org/wiki/Software/DBusBindings
Source0:	http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.xz
Patch0:		linking.patch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(meson-python)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(python)
BuildRequires:	dbus-x11
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	make
BuildRequires:	autoconf-archive
BuildRequires:	patchelf

%description
D-Bus python bindings for use with python programs.

%package -n python-dbus
Summary:	D-Bus Python 3 Bindings
Group:		Development/Python
Provides:	dbus-python = %{EVRD}
%rename	python3-dbus
%rename	python-dbus

%description -n python-dbus
D-Bus python bindings for use with python 3 programs.

%package -n python-dbus-devel
Summary:	Development files for python-dbus
Group:		Development/Python
Requires:	python-dbus = %{EVRD}
BuildRequires:	pkgconfig(python)

%description -n python-dbus-devel
Header files for python-dbus and python3-dbus.

#build -p
#autoreconf -vfi

%install -a
mv %{buildroot}%{python_sitearch}/.dbus_python.mesonpy.libs/pkgconfig %{buildroot}%{_libdir}
sed -i 's\prefix=.*\prefix=/usr\g' %{buildroot}%{_libdir}/pkgconfig/dbus-python.pc
# For compatibility with where the header used to be in versions
# prior to 1.4.0 (updated 2025-12-13 after 6.0)
mkdir -p %{buildroot}%{_includedir}/dbus-1.0/dbus/
cd %{buildroot}%{_includedir}/dbus-1.0/dbus
ln -s ../../python%{pyver}/dbus-python/dbus-1.0/dbus/dbus-python.h .

#remove unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/dbus-python

%files -n python-dbus
%doc README NEWS doc/*.txt
%{python_sitearch}/_dbus_*
%{python_sitearch}/dbus/*
%{python_sitearch}/dbus_python-%{version}.dist-info

%files -n python-dbus-devel
%{_includedir}/python%{pyver}/dbus-python
%{_includedir}/dbus-1.0/dbus/*.h
%{_libdir}/pkgconfig/*.pc
