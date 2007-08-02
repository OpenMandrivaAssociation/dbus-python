%define dbus_glib_version 0.70
%define dbus_version 0.93

%define _requires_exceptions pkgconfig\(.*\)

Summary: D-Bus Python Bindings 
Name: dbus-python
Version: 0.82.2
Release: %mkrel 1
URL: http://www.freedesktop.org/software/dbus
Source0: http://dbus.freedesktop.org/releases/%{name}-%{version}.tar.gz
Source1: http://dbus.freedesktop.org/releases/%{name}-%{version}.tar.gz.asc
License: AFL/GPL
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: dbus-devel >= %{dbus_version}
BuildRequires: dbus-glib-devel >= %{dbus_glib_version}
BuildRequires: python-devel
Requires: dbus >= %{dbus_version}


%description

D-Bus python bindings for use with python programs.   

%prep
%setup -q

%build

%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

#remove unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/dbus-python

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog NEWS doc/*.txt 
%doc README TODO 
%{py_platsitedir}/*dbus*
%{py_puresitedir}/*dbus*
%{_includedir}/dbus-1.0/dbus/*.h
%{_libdir}/pkgconfig/*.pc
