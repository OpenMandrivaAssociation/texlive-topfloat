# revision 19084
# category Package
# catalog-ctan /macros/latex/contrib/topfloat
# catalog-date 2007-01-17 10:01:14 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-topfloat
Version:	20070117
Release:	1
Summary:	Move floats to the top of the page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/topfloat
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/topfloat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/topfloat.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
