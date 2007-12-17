%define version	0.02
%define release	%mkrel 5
%define name 	perl-%realname
%define realname	Sys-Mknod

Summary:	Sys::Mknod - make special files
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Development/Perl
Source: 	http://search.cpan.org/CPAN/authors/id/S/SA/SAMV/%{realname}-%{version}.tar.bz2
URL: 		http://www.kernel.org/software/mon/
BuildRequires:	perl-devel
BuildArch:      noarch
   
%description
Sys::Mknod - make special files

%prep
%setup -q -n %{realname}-%{version}

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

%files
%defattr(-,root,root)
%{perl_vendorlib}
%{_mandir}/*/*
%doc Changes README

%clean
rm -rf $RPM_BUILD_ROOT


