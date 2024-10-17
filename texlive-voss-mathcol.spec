Name:		texlive-voss-mathcol
Version:	32954
Release:	2
Summary:	Typesetting mathematics in colour, in (La)TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/math/voss/mathCol
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/voss-mathcol.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/voss-mathcol.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a short paper from the TeXnische Komodie, in German.
Since the body of the paper is dominated by clear LaTeX coding
examples, most LaTeX programmers will understand how to achieve
the results shown in the diagrams, even if they don't
understand German.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/voss-mathcol/Changes
%doc %{_texmfdistdir}/doc/latex/voss-mathcol/mathCol.bib
%doc %{_texmfdistdir}/doc/latex/voss-mathcol/mathCol.ltx
%doc %{_texmfdistdir}/doc/latex/voss-mathcol/mathCol.pdf
%doc %{_texmfdistdir}/doc/latex/voss-mathcol/mathCol.tex
%doc %{_texmfdistdir}/doc/latex/voss-mathcol/run.doc

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
