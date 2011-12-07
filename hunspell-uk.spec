Name: hunspell-uk
Summary: Ukrainian hunspell dictionaries
Version: 1.6.0
Release: 1.1%{?dist}
Source: http://downloads.sourceforge.net/ispell-uk/myspell-uk_UA-%{version}.zip
Group: Applications/Text
URL: http://sourceforge.net/projects/ispell-uk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Ukrainian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-uk-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p uk_UA.dic uk_UA.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_uk_UA.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.6.0-1.1
- Rebuilt for RHEL 6

* Tue Aug 18 2009 Caolan McNamara <caolanm@redhat.com> - 1.6.0-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Caolan McNamara <caolanm@redhat.com> - 1.5.7-1
- latest version

* Tue Sep 30 2008 Caolan McNamara <caolanm@redhat.com> - 1.5.5-1
- latest version

* Tue Sep 16 2008 Caolan McNamara <caolanm@redhat.com> - 1.5.0-2
- fixup extra Source lines

* Mon Sep 15 2008 Caolan McNamara <caolanm@redhat.com> - 1.5.0-1
- initial version
