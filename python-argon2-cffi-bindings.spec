%define module argon2-cffi-bindings
%define oname argon2_cffi_bindings
%bcond tests 1

Name:		python-argon2-cffi-bindings
Version:	25.1.0
Release:	1
Summary:	Low-level CFFI bindings for Argon2
URL:		https://pypi.org/project/argon2-cffi-bindings/
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/a/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python

BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-cython
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(libargon2)
BuildRequires:	python%{pyver}dist(cffi)
BuildRequires:	python%{pyver}dist(hypothesis)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif
Requires:	python%{pyver}dist(cffi) >= 2

%description
%{module} provides low-level CFFI bindings to the official
implementation of the Argon2 password hashing algorithm.

%prep -a
# Remove upstream's egg-info
rm -vrf src/%{oname}.egg-info

%build -p
#export CFLAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lpython%{pyver} -v"
%ifarch %arm aarch64 riscv64
	export ARGON2_CFFI_USE_SSE2=0
%else
	export ARGON2_CFFI_USE_SSE2=1
%endif
export ARGON2_CFFI_USE_SYSTEM=1

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
pytest -v
%endif

%files
%doc README.md
%license LICENSE
%{python_sitearch}/_%{oname}
%{python_sitearch}/%{oname}-%{version}.dist-info
