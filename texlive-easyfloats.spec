%global tl_name easyfloats
%global tl_revision 72699

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.0
Release:	%{tl_revision}.1
Summary:	An easier interface to insert figures, tables and other objects in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/easyfloats
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/easyfloats.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/easyfloats.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/easyfloats.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(caption)
Requires:	texlive(environ)
Requires:	texlive(etoolbox)
Requires:	texlive(float)
Requires:	texlive(pgf)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
In standard LaTeX inserting objects like figures or tables requires too
much knowledge for beginners and too much typing effort and hardcoding
for people like me. This package aims to make insertion of figures and
tables easier for both beginners and experts. Despite the term "floats"
in its name, it also allows to disable floating of such objects.

