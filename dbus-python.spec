%define dbus_glib_version 0.74
%define dbus_version 1.1.2

%define _requires_exceptions pkgconfig\(.*\)

Summary: D-Bus Python Bindings
Name: dbus-python
Version: 0.83.2
Release: %mkrel 1
URL: http://www.freedesktop.org/wiki/Software/DBusBindings
Source0: http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1: http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz.asc
Patch0: dbus-python-0.83.0-fix-linkage.patch
License: MIT
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: dbus-devel >= %{dbus_version}
BuildRequires: dbus-glib-devel >= %{dbus_glib_version}
BuildRequires: python-devel

%description
D-Bus python bindings for use with python programs.

%package -n python-dbus
Summary: D-Bus Python Bindings
Group: Development/Python
Obsoletes: %{name} < %{version}-%{release}
Provides: %{name} = %{version}-%{release}
Requires: dbus >= %{dbus_version}

%description -n python-dbus
D-Bus python bindings for use with python programs.

%prep
%setup -q
# not sure it is really needed
#patch0 -p0

%build
%configure2_5x --disable-api-docs
%make

%install
rm -rf %{buildroot}

%makeinstall_std

#remove unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/dbus-python

%clean
rm -rf %{buildroot}

%files -n python-dbus
%defattr(-,root,root)
%doc COPYING NEWS doc/*.txt
%doc README TODO
%{py_puresitedir}/dbus*
%{py_platsitedir}/_dbus_*
%{_includedir}/dbus-1.0/dbus/*.h
%{_libdir}/pkgconfig/*.pc
