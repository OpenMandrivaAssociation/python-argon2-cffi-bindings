%define module argon2-cffi-bindings
%define uname argon2_cffi_bindings

Name:		python-argon2-cffi-bindings
Version:	21.2.0
Release:	1
Summary:	Low-level CFFI bindings for Argon2
URL:		https://pypi.org/project/argon2-cffi-bindings/
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/a/%{module}/%{module}-%{version}.tar.gz
BuildSystem:	python

BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-cython
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(libargon2)
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
BuildRequires:	python-cffi
BuildRequires:	python-hypothesis
BuildRequires:	python-pip
BuildRequires:	python-pytest

Requires:	python-cffi >= 1.0.1

%description
%{module} provides low-level CFFI bindings to the official
implementation of the Argon2 password hashing algorithm.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
#export CFLAGS="%{optflags}"
export LDFLAGS="%{optflags} -v"
%ifarch %arm aarch64 riscv64
	export ARGON2_CFFI_USE_SSE2=0
%else
	export ARGON2_CFFI_USE_SSE2=1
%endif
export ARGON2_CFFI_USE_SYSTEM=1
%py_build

%install
%py3_install


%files
%{python_sitearch}/_%{uname}
%{python_sitearch}/%{uname}-%{version}*-info
%doc README.md CHANGELOG.md
%license LICENSE