Name:		texlive-easyfloats
Version:	57204
Release:	2
Summary:	An easier interface to insert figures, tables and other objects in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/easyfloats
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easyfloats.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easyfloats.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easyfloats.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
In standard LaTeX inserting objects like figures or tables
requires too much knowledge for beginners and too much typing
effort and hardcoding for people like me. This package aims to
make insertion of figures and tables easier for both beginners
and experts. Despite the term floats in it's name it also
allows to disable floating of such objects.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/easyfloats
%{_texmfdistdir}/tex/latex/easyfloats
%doc %{_texmfdistdir}/doc/latex/easyfloats

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
