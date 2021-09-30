%global __requires_exclude python-gi

Summary:	D-Bus Python Bindings
Name:		dbus-python
Version:	1.2.18
Release:	2
License:	MIT
Group:		Development/Python
Url:		http://www.freedesktop.org/wiki/Software/DBusBindings
Source0:	http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:		linking.patch
Patch1:		0001-Move-python-modules-to-architecture-specific-directo.patch
BuildRequires:	python3dist(setuptools)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(python)
BuildRequires:	dbus-x11

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

%prep
%autosetup -p1

%build
autoreconf -vfi
%py_build

%install
%py_install

mkdir -p %{buildroot}%{_libdir}/pkgconfig/
install -p -m 0644 build/temp.linux-*-%{python_version}/dbus-python.pc %{buildroot}%{_libdir}/pkgconfig/
sed -i 's\prefix=.*\prefix=/usr\g' %{buildroot}%{_libdir}/pkgconfig/dbus-python.pc
mkdir -p %{buildroot}%{_includedir}/dbus-1.0/dbus/
install -p -m 0444 include/dbus/dbus-python.h %{buildroot}%{_includedir}/dbus-1.0/dbus/

#remove unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/dbus-python

%files -n python-dbus
%doc README NEWS doc/*.txt
%{python_sitearch}/_dbus_*
%{python_sitearch}/dbus/*
%{python_sitearch}/dbus_python-%{version}-py*.*.egg-info/
%{python_sitearch}/dbus_python-%{version}-py*.*.egg-info/PKG-INFO

%files -n python-dbus-devel
%{_includedir}/dbus-1.0/dbus/*.h
%{_libdir}/pkgconfig/*.pc
