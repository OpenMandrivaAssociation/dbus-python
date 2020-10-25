%global __requires_exclude python-gi

Summary:	D-Bus Python Bindings
Name:		dbus-python
Version:	1.2.16
Release:	5
License:	MIT
Group:		Development/Python
Url:		http://www.freedesktop.org/wiki/Software/DBusBindings
Source0:	http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:		linking.patch
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(python3)
BuildRequires:	dbus-x11

%description
D-Bus python bindings for use with python programs.

%package -n python-dbus
Summary:	D-Bus Python 3 Bindings
Group:		Development/Python
Requires:	dbus-x11
Provides:	dbus-python = %{EVRD}
%rename	python3-dbus
%rename	python-dbus

%description -n python-dbus
D-Bus python bindings for use with python 3 programs.

%package -n python-dbus-devel
Summary:	Development files for python-dbus and python2-dbus
Group:		Development/Python
Requires:	python-dbus = %{EVRD}
BuildRequires:	pkgconfig(python3)

%description -n python-dbus-devel
Header files for python-dbus and python3-dbus.

%prep
%autosetup -p1

%build
sed -i -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/g' configure*
autoreconf -fi
%configure --disable-api-docs
%make_build

%install
%make_install

#remove unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/dbus-python

%files -n python-dbus
%doc COPYING NEWS doc/*.txt
%doc README
%{py_puresitedir}/dbus*
%{py_platsitedir}/_dbus_*

%files -n python-dbus-devel
%{_includedir}/dbus-1.0/dbus/*.h
%{_libdir}/pkgconfig/*.pc
