#!/usr/bin/perl 
 
use strict;
use CGI;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
 
my $cgi = CGI->new();
 
print $cgi->header;
print <<END_HTML;

<!DOCTYPE html
	PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	 "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US" xml:lang="en-US">
<head>
<title>Homework 2 Page</title>
<link rel="stylesheet" type="text/css" href="360.css" />
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
</head>
<body>
<div id="content"><h1>Sequence Database</h1><form method="post" action="/~nickster/cgi/database.cgi" enctype="multipart/form-data">
Enter the name of your sequence: <br /><input type="text" name="seqname"  size="50" /><p />Enter your sequence here: <br />
<textarea name="sequence"  rows="10" cols="50"></textarea>
<p /><input type="submit" name="add" value="Add Sequence" title="Add a sequence to the database" /><p />
<hr /><form method="post" action="/~nickster/cgi/database.cgi" enctype="multipart/form-data">
Enter the sequence to search (leave the fields you want blank empty)<br />Name of sequence: <br />
<input type="text" name="searchname"  size="50" /><p />Sequence characters: <br /><textarea name="searchseq"  rows="2" columnts="50">
</textarea><p />Enter your email address to send you the results: <br /><input type="text" name="email"  size="20" /><p />
<input type="submit" name="search" value="Search" title="Search for a sequence in the database" /></form><hr />
<form method="post" action="/~nickster/cgi/database.cgi" enctype="multipart/form-data">
Press this button if you want to reset the database<br />
<input type="submit" name="reset" value="Reset" title="Remove all sequences from the database." /></form><hr />
</div>
</body>
</html>

END_HTML
