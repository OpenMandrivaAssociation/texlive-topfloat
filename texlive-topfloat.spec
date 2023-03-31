Name:		texlive-topfloat
Version:	19084
Release:	2
Summary:	Move floats to the top of the page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/topfloat
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/topfloat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/topfloat.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive topfloat package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/topfloat/topfloat.sty
%doc %{_texmfdistdir}/doc/latex/topfloat/topfloat.pdf
%doc %{_texmfdistdir}/doc/latex/topfloat/topfloat.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
