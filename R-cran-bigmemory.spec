%define		fversion	%(echo %{version} |tr r -)
%define		modulename	bigmemory
Summary:	Massive matrices creation, access and manipulation
Name:		R-cran-%{modulename}
Version:	4.2.3
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	57bab87f26f20868727a90ecd88c9b9e
BuildRequires:	R >= 2.8.1
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Create, store, access, and manipulate massive matrices. Matrices are
allocated to shared memory and may use memory-mapped files. Packages
biganalytics, bigtabulate, synchronicity, and bigalgebra provide advanced
functionality.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

#%post
#(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
# R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)

#%postun
#if [ -f %{_libdir}/R/bin/Rcmd ];then
#	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
#	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)
#fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
