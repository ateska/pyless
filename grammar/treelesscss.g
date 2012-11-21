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
	: ^( N_StyleSheet
		(charSet { self.output($charSet.gencode); } )?
		(imports { self.output($imports.gencode); } )*
		body*	// Body is 'direct' output function
	)
	;

// -----------------
// Character set.   Picks up the user specified character set, should it be present.
//
charSet returns [gencode]
  	: ^(CHARSET_SYM STRING)
  		{ $gencode = '@charset {0}{1}'.format($STRING.text, self.EOLSEMI); }
    	;


// ---------
// Import.  Location of an external style sheet to include in the ruleset.
//
imports returns [gencode]
	@init
	{
		$gencode = '@import ';
		mqs = []
	}
	: ^(IMPORT_SYM
		importUrl { $gencode += $importUrl.text ; }
		( media_query { mqs.append($media_query.gencode) ; } ) *
	)
		{
			if len(mqs) > 0: $gencode += ' ' + self.LISTCOMA.join(mqs);
			$gencode += self.EOLSEMI ; 
		}
    		
	;

importUrl
	: STRING
	| URI
	;


// ---------
// Body
//
body
	: media
//	: ruleSet
//	| media
//	| page
//	| fontface
//	| keyframes
	;


// ---------
// Media.   Introduce a set of rules that are to be used if the consumer indicates
//          it belongs to the signified medium.
//
media
	@init
	{
		mqs = []
	}
	: ^(MEDIA_SYM
		( media_query { mqs.append($media_query.gencode) ; } ) *
		{
			mediahead = '@media';
			if len(mqs) > 0: mediahead += ' ' + self.LISTCOMA.join(mqs);
			mediahead += self.EOLLBRACKET;
			self.output(mediahead);
			self.indent_level += 1
		}
		body*
	)
	{
		self.indent_level -= 1
		self.output(self.EOLRBRACKET);
	}
	;


// ---------    
// Media queries
//
media_query returns [gencode]
	@init
	{
		mq = list()
	}
	: ^(N_MediaQuery
		( media_stmt { mq.append($media_stmt.text); }
		| media_expr { mq.append($media_expr.text); }
		)+ 
	)
		{ $gencode = ' '.join(mq); }
	;

media_stmt
	: IDENT
	;

media_expr
	: ^(N_MediaExpr media_stmt )
	//TODO: : ^(N_MediaExpr media_stmt expr? )
	;
