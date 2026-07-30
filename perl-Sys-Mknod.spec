%define upstream_name	Sys-Mknod
%define upstream_version 0.02
Name:		perl-%{upstream_name}
Version:	0.02
Release:	1

Summary:	Sys::Mknod - make special files
License:	GPL
Group:		Development/Perl
Url:		https://www.kernel.org/software/mon/
Source0:	https://cpan.metacpan.org/authors/id/S/SA/SAMV/Sys-Mknod-0.02.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch
   
%description
Sys::Mknod - make special files

%prep
%setup -q -n %{upstream_name}-%{version}

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


