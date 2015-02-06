%define		_class		Science
%define		_subclass	Chemistry
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.1.2
Release:	2
Summary:	Manipulate chemical objects: atoms, molecules, etc
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Science_Chemistry/
Source0:	http://download.pear.php.net/package/Science_Chemistry-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
General classes to represent Atoms, Molecules and Macromolecules. Also
parsing code for PDB, CML and XYZ file formats. Examples of parsing
and conversion to/from chemical structure formats.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

# nuke useless files
rm -f %{buildroot}%{_datadir}/pear/data/%{upstream_name}/*

%clean



%files
%doc %{upstream_name}-%{version}
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-3mdv2012.0
+ Revision: 742267
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2
+ Revision: 679571
- mass rebuild

* Wed Dec 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1mdv2011.0
+ Revision: 625914
- fix build
- 1.1.1

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-11mdv2011.0
+ Revision: 613765
- the mass rebuild of 2010.1 packages

* Tue Nov 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-10mdv2010.1
+ Revision: 467074
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-9mdv2010.0
+ Revision: 441562
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-8mdv2009.0
+ Revision: 237059
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.1.0-7mdv2008.1
+ Revision: 140730
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-7mdv2007.0
+ Revision: 82547
- Import php-pear-Science_Chemistry

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-1mdk
- initial Mandriva package (PLD import)


