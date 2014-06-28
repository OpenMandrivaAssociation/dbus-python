%define _disable_ld_no_undefined 1

Summary:	D-Bus Python Bindings
Name:		dbus-python
Version:	1.2.0
Release:	7
License:	MIT
Group:		Development/Python
Url:		http://www.freedesktop.org/wiki/Software/DBusBindings
Source0:	http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python3)

%description
D-Bus python bindings for use with python programs.

%package -n python2-dbus
Summary:	D-Bus Python Bindings
Group:		Development/Python
Requires:	dbus
%rename python-dbus

%description -n python2-dbus
D-Bus python 2 bindings for use with python programs.

%package -n python-dbus
Summary:	D-Bus Python 3 Bindings
Group:		Development/Python
Requires:	dbus
%rename python3-dbus

%description -n python-dbus
D-Bus python bindings for use with python 3 programs.

%package -n python-dbus-devel
Summary:	Development files for python-dbus and python2-dbus
Group:		Development/Python
Requires:	python2-dbus = %{EVRD}
Requires:	python-dbus = %{EVRD}

%description -n python-dbus-devel
Header files for python-dbus and python3-dbus.

%prep
%setup -q -c -a 0
mv %{name}-%{version} python2
cp -r python2 python3

%build
pushd python2
sed -i -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/g' configure*
autoreconf -fi
%configure2_5x --disable-api-docs PYTHON=%{_bindir}/python2
%make
popd

pushd python3
sed -i -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/g' configure*
autoreconf -fi
%configure2_5x --disable-api-docs
%make
popd

%install
pushd python2
%makeinstall_std
popd

pushd python3
%makeinstall_std
popd

#remove unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/dbus-python

%files -n python2-dbus
%doc python2/COPYING python2/NEWS python2/doc/*.txt
%doc python2/README
%{py2_puresitedir}/dbus*
%{py2_platsitedir}/_dbus_*

%files -n python-dbus
%doc python3/COPYING python3/NEWS python3/doc/*.txt
%doc python3/README
%{py_puresitedir}/dbus*
%{py_platsitedir}/_dbus_*

%files -n python-dbus-devel
%{_includedir}/dbus-1.0/dbus/*.h
%{_libdir}/pkgconfig/*.pc

