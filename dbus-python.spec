Summary: D-Bus Python Bindings
Name: dbus-python
Version: 1.0.0
Release: 2
License: MIT
Group: Development/Python
URL: http://www.freedesktop.org/wiki/Software/DBusBindings
Source0: http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1: http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz.asc

BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
BuildRequires: python-devel

%description
D-Bus python bindings for use with python programs.

%package -n python-dbus
Summary: D-Bus Python Bindings
Group: Development/Python
Obsoletes: %{name} < %{version}-%{release}
Provides: %{name} = %{version}-%{release}
Requires: dbus

%description -n python-dbus
D-Bus python bindings for use with python programs.

%package -n python-dbus-devel
Summary: The pkgconfig for %{name}
Group: Development/GNOME and GTK+
Requires: python-dbus = %{version}

%description -n python-dbus-devel
The pkgconfig for %{name}.

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x --disable-api-docs
%make

%install
rm -rf %{buildroot} 
%makeinstall_std

#remove unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/dbus-python

%files -n python-dbus
%doc COPYING NEWS doc/*.txt
%doc README TODO
%{py_puresitedir}/dbus*
%{py_platsitedir}/_dbus_*
%{_includedir}/dbus-1.0/dbus/*.h

%files -n python-dbus-devel
%{_libdir}/pkgconfig/*.pc
