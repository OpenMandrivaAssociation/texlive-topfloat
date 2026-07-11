%global tl_name topfloat
%global tl_revision 19084

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Move floats to the top of the page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/topfloat
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/topfloat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/topfloat.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Move floats to the top of the page

