# TODO: Fix tests (django twisted) ?
# TODO: Move tests to separate package
#
# Conditional build:
%bcond_with	tests	# perform "make test"

%define		module	PyAMF
Summary:	Action Message Format (AMF) support for Python
Summary(pl.UTF-8):	Wsparcie dla Action Message Format (AMF)
Name:		python-%{module}
Version:	0.8.0
Release:	1
License:	MIT
Group:		Development/Languages/Python
# http://pypi.python.org/packages/source/P/PyAMF/PyAMF-0.6.1.tar.gz
Source0:	https://pypi.python.org/packages/a0/06/43976c0e3951b9bf7ba0d7d614a8e3e024eb5a1c6acecc9073b81c94fb52/%{module}-%{version}.tar.gz
# Source0-md5:	51e810531a663b55e686286edb23e82a
URL:		http://www.pyamf.org/index.html
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyAMF provides Action Message Format (AMF) support for Python that is
compatible with the Adobe Flash Player. It includes integration with
Python web frameworks like Django, Pylons, Twisted, SQLAlchemy, web2py
and more.

%description -l pl.UTF-8
PyAMF dostarcza wsparcie Action Message Format (AMF) dla Pythona
kompatybilne z Adobe Flash Player. Integruje się z Pythonowymi
framworkami www jak Django, Pylons, Twisted, SQLAlchemy, web2py i
inne.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%dir %{py_sitedir}/cpyamf
%attr(755,root,root) %{py_sitedir}/cpyamf/*.so
%{py_sitedir}/cpyamf/__init__.*
%{py_sitedir}/pyamf
%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}-%{version}-*.egg-info
%endif
