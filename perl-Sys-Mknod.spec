%define upstream_name	Sys-Mknod
%define upstream_version	0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Sys::Mknod - make special files
License:	GPL
Group:		Development/Perl
Url:		http://www.kernel.org/software/mon/
Source0:	http://search.cpan.org/CPAN/authors/id/S/SA/SAMV/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch
   
%description
Sys::Mknod - make special files

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
# I am sorry, we can't make test because because
# it try to run mknod, and we can't be root to
# build the package...
[ $UID -eq 0 ] || exit 0
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}
%{_mandir}/*/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 658881
- rebuild for updated spec-helper

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 408055
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.02-8mdv2009.0
+ Revision: 258424
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.02-7mdv2009.0
+ Revision: 246489
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.02-5mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-5mdv2008.0
+ Revision: 86923
- rebuild


* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 19:10:34 (54138)
- try to run test, if building as root...
- rebuild

* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 19:04:38 (54137)
Import perl-Sys-Mknod

* Sun Apr 30 2006 Olivier Thauvin <nanardon@mandriva.org> 0.02-3mdk
- rebuild

* Sat Feb 05 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.02-2mdk
- rebuild for new perl
- noarch

* Sun May 23 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.02-1mdk
- initial release

