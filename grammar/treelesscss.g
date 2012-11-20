tree grammar treelesscss;

options {
    tokenVocab=lesscss;
    ASTLabelType=CommonTree;
    language=Python;
}

// -------------
// Main rule.
//
//
styleSheet
	: ^( N_StyleSheet charSet? imports* )
	//^(N_StyleSheet charSet? imports* bodylist?)
	;

// -----------------
// Character set.   Picks up the user specified character set, should it be present.
//
charSet
  	: ^(CHARSET_SYM STRING)
  		{ self.TP_charSet($STRING); }
    	;


// ---------
// Import.  Location of an external style sheet to include in the ruleset.
//
imports
	: ^(IMPORT_SYM importUrl )
	//: ^(IMPORT_SYM importUrl  media_query_list? )
    		{ self.TP_imports($importUrl.text); }
	;

importUrl
	: STRING
	| URI
	;


/*
// ---------    
// Media queries
//
media_query_list
	: ^(N_MediaQuery media_query+)
	;

media_query
	: ( media_stmt | media_expr )+
	;

media_stmt
	: IDENT
	;

media_expr
	: ^(N_MediaExpr media_stmt )
	//TODO: : ^(N_MediaExpr media_stmt expr? )
	;
*/