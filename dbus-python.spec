%define dbus_glib_version 0.74
%define dbus_version 1.1.2

%define _requires_exceptions pkgconfig\(.*\)

Summary:		D-Bus Python Bindings
Name:			dbus-python
Version:		1.1.1
Release:		1
URL:			http://www.freedesktop.org/wiki/Software/DBusBindings
Source0:		http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
#Patch0:			dbus-python-0.83.2-fix-linkage.patch
License:		MIT
Group:			Development/Python
BuildRequires:	dbus-devel >= %{dbus_version}
BuildRequires:	dbus-glib-devel >= %{dbus_glib_version}
BuildRequires:	python-devel

%description
D-Bus python bindings for use with python programs.

%package -n python-dbus
Summary:		D-Bus Python Bindings
Group:			Development/Python
Obsoletes:		%{name} < %{version}-%{release}
Provides:		%{name} = %{version}-%{release}
Requires:		dbus >= %{dbus_version}

%description -n python-dbus
D-Bus python bindings for use with python programs.

%prep
%setup -q
#patch0 -p0 -b .link

%build
%configure2_5x --disable-api-docs
%make

%install
%makeinstall_std

#remove unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/dbus-python

%files -n python-dbus
%doc COPYING NEWS doc/*.txt
%doc README
%{py_puresitedir}/dbus*
%{py_platsitedir}/_dbus_*
%{_includedir}/dbus-1.0/dbus/*.h
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu May 26 2011 Götz Waschk <waschk@mandriva.org> 0.84.0-1mdv2011.0
+ Revision: 679160
- update to new version 0.84.0

* Sat Apr 09 2011 Funda Wang <fwang@mandriva.org> 0.83.2-2
+ Revision: 652085
- re-enable patch0

* Fri Dec 03 2010 Götz Waschk <waschk@mandriva.org> 0.83.2-1mdv2011.0
+ Revision: 606072
- new version
- disable generation of API docs

* Sat Oct 30 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.83.1-2mdv2011.0
+ Revision: 590654
- rebuild for new python 2.7

* Fri Feb 19 2010 Frederic Crozat <fcrozat@mandriva.com> 0.83.1-1mdv2011.0
+ Revision: 508014
- Release 0.83.0
- Remove patch0 (merged upstream)

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.83.0-5mdv2010.0
+ Revision: 413339
- rebuild

* Mon Jan 26 2009 Funda Wang <fwang@mandriva.org> 0.83.0-4mdv2009.1
+ Revision: 333692
- add patch from https://bugs.freedesktop.org/show_bug.cgi?id=17551
- fix linkage

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 0.83.0-3mdv2009.1
+ Revision: 318619
- rebuild for python 2.6
- correct source locations

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 0.83.0-2mdv2009.1
+ Revision: 318618
- rebuild for new python

  + Götz Waschk <waschk@mandriva.org>
    - fix URL

* Thu Jul 24 2008 Frederic Crozat <fcrozat@mandriva.com> 0.83.0-1mdv2009.0
+ Revision: 245078
- Release 0.83.0

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.82.4-3mdv2009.0
+ Revision: 220575
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.82.4-2mdv2008.1
+ Revision: 148503
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- do not package big ChangeLog

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 11 2007 Frederic Crozat <fcrozat@mandriva.com> 0.82.4-1mdv2008.1
+ Revision: 117363
- Release 0.82.4

* Mon Oct 22 2007 Jérôme Soyer <saispo@mandriva.org> 0.82.3-1mdv2008.1
+ Revision: 101074
- New release 0.82.3

* Tue Aug 21 2007 David Walluck <walluck@mandriva.org> 0.82.2-2mdv2008.0
+ Revision: 68140
- change package name to python-dbus

* Thu Aug 02 2007 Frederic Crozat <fcrozat@mandriva.com> 0.82.2-1mdv2008.0
+ Revision: 58015
- Release 0.82.2

* Thu Jul 12 2007 Frederic Crozat <fcrozat@mandriva.com> 0.82.1-1mdv2008.0
+ Revision: 51501
- Release 0.82.1

* Fri Jun 15 2007 Funda Wang <fwang@mandriva.org> 0.81.1-1mdv2008.0
+ Revision: 39842
- New version

* Wed May 23 2007 Frederic Crozat <fcrozat@mandriva.com> 0.81.0-2mdv2008.0
+ Revision: 30112
- disable autorequire on pkgconfig .pc file, it forces dbus-devel dependency

* Wed May 09 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.81.0-1mdv2008.0
+ Revision: 25629
- New version


* Thu Feb 15 2007 Frederic Crozat <fcrozat@mandriva.com> 0.80.2-1mdv2007.0
+ Revision: 121294
-Release 0.80.2

  + Nicolas Lécureuil <neoclust@mandriva.org>

* Thu Jan 25 2007 Frederic Crozat <fcrozat@mandriva.com> 0.80.1-1mdv2007.1
+ Revision: 113404
-Fix x86-64 build
-Release 0.80.1

* Thu Dec 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.71-5mdv2007.1
+ Revision: 97022
- fix dependencies, as pyrex is now python-pyrex

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 0.71-4mdv2007.1
+ Revision: 88194
- Import dbus-python

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 0.71-4mdv2007.1
- update file list

* Thu Aug 24 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.71-3mdv2007.0
- fix group

* Sat Aug 05 2006 Götz Waschk <waschk@mandriva.org> 0.71-2mdv2007.0
- fix buildrequires

* Tue Aug 01 2006 Frederic Crozat <fcrozat@mandriva.com> 0.71-1mdv2007.0
- Initial mandriva package (based on fedora)

