%define upstream_name	Sys-Mknod
%define upstream_version	0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Sys::Mknod - make special files
License: 	GPL
Group: 		Development/Perl
Url: 		http://www.kernel.org/software/mon/
Source0:	http://search.cpan.org/CPAN/authors/id/S/SA/SAMV/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:  noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}
   
%description
Sys::Mknod - make special files

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
# I am sorry, we can't make test because because
# it try to run mknod, and we can't be root to
# build the package...
[ $UID -eq 0 ] || exit 0
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{perl_vendorlib}
%{_mandir}/*/*
%doc Changes README
