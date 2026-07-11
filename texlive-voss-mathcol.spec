%global tl_name voss-mathcol
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Typesetting mathematics in colour, in (La)TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/math/voss/mathCol
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/voss-mathcol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/voss-mathcol.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a short paper from the TeXnische Komodie, in German. Since the
body of the paper is dominated by clear LaTeX coding examples, most
LaTeX programmers will understand how to achieve the results shown in
the diagrams, even if they don't understand German.

