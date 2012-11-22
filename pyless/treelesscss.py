# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 treelesscss.g 2012-11-23 00:19:09

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=41
UNICODE_RANGE=63
STAR=40
EOF=-1
MEDIA_SYM=23
LBRACKET=39
INCLUDES=44
RPAREN=30
NAME=71
GREATER=36
ESCAPE=68
DIMENSION=104
STRINGESC=102
NL=105
COMMENT=99
D=76
E=77
F=78
G=79
A=73
B=74
RBRACE=25
C=75
L=84
M=85
NMCHAR=70
IMPORT_SYM=21
N=86
SUBSTRINGMATCH=48
O=87
H=80
I=81
J=82
K=83
NUMBER=51
U=93
T=92
W=95
V=94
Q=89
P=88
S=91
CDO=100
R=90
CDC=101
Y=97
PERCENTAGE=34
URL=72
X=96
Z=98
URI=22
PAGE_SYM=32
WS=103
DASHMATCH=45
EMS=53
N_PseudoFunction=16
N_RuleSet=7
NONASCII=66
N_MediaQuery=5
N_Selector=10
LBRACE=24
LPAREN=28
LENGTH=52
IMPORTANT_SYM=49
N_Function=12
TIME=58
KEYFRAMES_SYM=33
COMMA=26
N_StyleSheet=4
IDENT=27
PLUS=35
FREQ=59
RBRACKET=42
DOT=38
VPORTLEN=61
CHARSET_SYM=18
ANGLE=57
REMS=55
HASH=37
HEXCHAR=65
RESOLUTION=60
PREFIXMATCH=46
MINUS=64
N_Pseudo=15
SOLIDUS=50
SEMI=20
N_Empty=14
UNICODE=67
CHS=56
COLON=29
NMSTART=69
N_Declaration=11
FONTFACE_SYM=31
OPEQ=43
N_Term=17
EXS=54
M_KeyframeSelector=9
N_MediaExpr=6
N_Attrib=13
N_KeyframeBlock=8
SUFFIXMATCH=47
NTH=62
STRING=19

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "N_StyleSheet", "N_MediaQuery", "N_MediaExpr", "N_RuleSet", "N_KeyframeBlock", 
    "M_KeyframeSelector", "N_Selector", "N_Declaration", "N_Function", "N_Attrib", 
    "N_Empty", "N_Pseudo", "N_PseudoFunction", "N_Term", "CHARSET_SYM", 
    "STRING", "SEMI", "IMPORT_SYM", "URI", "MEDIA_SYM", "LBRACE", "RBRACE", 
    "COMMA", "IDENT", "LPAREN", "COLON", "RPAREN", "FONTFACE_SYM", "PAGE_SYM", 
    "KEYFRAMES_SYM", "PERCENTAGE", "PLUS", "GREATER", "HASH", "DOT", "LBRACKET", 
    "STAR", "FUNCTION", "RBRACKET", "OPEQ", "INCLUDES", "DASHMATCH", "PREFIXMATCH", 
    "SUFFIXMATCH", "SUBSTRINGMATCH", "IMPORTANT_SYM", "SOLIDUS", "NUMBER", 
    "LENGTH", "EMS", "EXS", "REMS", "CHS", "ANGLE", "TIME", "FREQ", "RESOLUTION", 
    "VPORTLEN", "NTH", "UNICODE_RANGE", "MINUS", "HEXCHAR", "NONASCII", 
    "UNICODE", "ESCAPE", "NMSTART", "NMCHAR", "NAME", "URL", "A", "B", "C", 
    "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", 
    "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "COMMENT", "CDO", "CDC", 
    "STRINGESC", "WS", "DIMENSION", "NL"
]




class treelesscss(TreeParser):
    grammarFileName = "treelesscss.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(treelesscss, self).__init__(input, state, *args, **kwargs)






                


        



    # $ANTLR start "styleSheet"
    # treelesscss.g:13:1: styleSheet : ^( N_StyleSheet ( charSet )? ( imports )* ( body )* ) ;
    def styleSheet(self, ):

        charSet1 = None

        imports2 = None


        try:
            try:
                # treelesscss.g:14:2: ( ^( N_StyleSheet ( charSet )? ( imports )* ( body )* ) )
                # treelesscss.g:14:4: ^( N_StyleSheet ( charSet )? ( imports )* ( body )* )
                pass 
                self.match(self.input, N_StyleSheet, self.FOLLOW_N_StyleSheet_in_styleSheet51)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # treelesscss.g:15:3: ( charSet )?
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == CHARSET_SYM) :
                        alt1 = 1
                    if alt1 == 1:
                        # treelesscss.g:15:4: charSet
                        pass 
                        self._state.following.append(self.FOLLOW_charSet_in_styleSheet56)
                        charSet1 = self.charSet()

                        self._state.following.pop()
                        #action start
                        self.output(charSet1); 
                        #action end



                    # treelesscss.g:16:3: ( imports )*
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == IMPORT_SYM) :
                            alt2 = 1


                        if alt2 == 1:
                            # treelesscss.g:16:4: imports
                            pass 
                            self._state.following.append(self.FOLLOW_imports_in_styleSheet66)
                            imports2 = self.imports()

                            self._state.following.pop()
                            #action start
                            self.output(imports2); 
                            #action end


                        else:
                            break #loop2
                    # treelesscss.g:17:3: ( body )*
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == N_RuleSet or LA3_0 == MEDIA_SYM) :
                            alt3 = 1


                        if alt3 == 1:
                            # treelesscss.g:17:3: body
                            pass 
                            self._state.following.append(self.FOLLOW_body_in_styleSheet75)
                            self.body()

                            self._state.following.pop()


                        else:
                            break #loop3

                    self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "styleSheet"


    # $ANTLR start "charSet"
    # treelesscss.g:24:1: charSet returns [gencode] : ^( CHARSET_SYM STRING ) ;
    def charSet(self, ):

        gencode = None

        STRING3 = None

        try:
            try:
                # treelesscss.g:25:4: ( ^( CHARSET_SYM STRING ) )
                # treelesscss.g:25:6: ^( CHARSET_SYM STRING )
                pass 
                self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet101)

                self.match(self.input, DOWN, None)
                STRING3=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet103)

                self.match(self.input, UP, None)
                #action start
                gencode =  '@charset {0}{1}'.format(STRING3.text, self.EOLSEMI) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "charSet"


    # $ANTLR start "imports"
    # treelesscss.g:33:1: imports returns [gencode] : ^( IMPORT_SYM importUrl ( media_query )* ) ;
    def imports(self, ):

        gencode = None

        importUrl4 = None

        media_query5 = None


          
        gencode =  '@import '
        mqs = []
        	
        try:
            try:
                # treelesscss.g:39:2: ( ^( IMPORT_SYM importUrl ( media_query )* ) )
                # treelesscss.g:39:4: ^( IMPORT_SYM importUrl ( media_query )* )
                pass 
                self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports141)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_importUrl_in_imports145)
                importUrl4 = self.importUrl()

                self._state.following.pop()
                #action start
                gencode += ((importUrl4 is not None) and [self.input.getTokenStream().toString(
                    self.input.getTreeAdaptor().getTokenStartIndex(importUrl4.start),
                    self.input.getTreeAdaptor().getTokenStopIndex(importUrl4.start)
                    )] or [None])[0] ; 
                #action end
                # treelesscss.g:41:3: ( media_query )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == N_MediaQuery) :
                        alt4 = 1


                    if alt4 == 1:
                        # treelesscss.g:41:5: media_query
                        pass 
                        self._state.following.append(self.FOLLOW_media_query_in_imports153)
                        media_query5 = self.media_query()

                        self._state.following.pop()
                        #action start
                        mqs.append(media_query5) ; 
                        #action end


                    else:
                        break #loop4

                self.match(self.input, UP, None)
                #action start
                   
                if len(mqs) > 0: gencode += ' ' + self.LISTCOMA.join(mqs);
                gencode += self.EOLSEMI ; 
                		
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "imports"

    class importUrl_return(TreeRuleReturnScope):
        def __init__(self):
            super(treelesscss.importUrl_return, self).__init__()





    # $ANTLR start "importUrl"
    # treelesscss.g:50:1: importUrl : ( STRING | URI );
    def importUrl(self, ):

        retval = self.importUrl_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:51:2: ( STRING | URI )
                # treelesscss.g:
                pass 
                if self.input.LA(1) == STRING or self.input.LA(1) == URI:
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "importUrl"


    # $ANTLR start "body"
    # treelesscss.g:59:1: body : ( ruleSet | media );
    def body(self, ):

        try:
            try:
                # treelesscss.g:60:2: ( ruleSet | media )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == N_RuleSet) :
                    alt5 = 1
                elif (LA5_0 == MEDIA_SYM) :
                    alt5 = 2
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # treelesscss.g:60:4: ruleSet
                    pass 
                    self._state.following.append(self.FOLLOW_ruleSet_in_body204)
                    self.ruleSet()

                    self._state.following.pop()


                elif alt5 == 2:
                    # treelesscss.g:61:4: media
                    pass 
                    self._state.following.append(self.FOLLOW_media_in_body211)
                    self.media()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "body"


    # $ANTLR start "media"
    # treelesscss.g:72:1: media : ^( MEDIA_SYM ( media_query )* ( body )* ) ;
    def media(self, ):

        media_query6 = None


          
        mqs = []
        	
        try:
            try:
                # treelesscss.g:77:2: ( ^( MEDIA_SYM ( media_query )* ( body )* ) )
                # treelesscss.g:77:4: ^( MEDIA_SYM ( media_query )* ( body )* )
                pass 
                self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media240)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # treelesscss.g:78:3: ( media_query )*
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == N_MediaQuery) :
                            alt6 = 1


                        if alt6 == 1:
                            # treelesscss.g:78:5: media_query
                            pass 
                            self._state.following.append(self.FOLLOW_media_query_in_media246)
                            media_query6 = self.media_query()

                            self._state.following.pop()
                            #action start
                            mqs.append(media_query6) ; 
                            #action end


                        else:
                            break #loop6
                    #action start
                       
                    mediahead = '@media';
                    if len(mqs) > 0: mediahead += ' ' + self.LISTCOMA.join(mqs);
                    mediahead += self.EOLLBRACKET;
                    self.output(mediahead);
                    self.indent_level += 1
                    		
                    #action end
                    # treelesscss.g:86:3: ( body )*
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if (LA7_0 == N_RuleSet or LA7_0 == MEDIA_SYM) :
                            alt7 = 1


                        if alt7 == 1:
                            # treelesscss.g:86:3: body
                            pass 
                            self._state.following.append(self.FOLLOW_body_in_media260)
                            self.body()

                            self._state.following.pop()


                        else:
                            break #loop7
                    #action start
                       
                    self.indent_level -= 1
                    self.output(self.EOLRBRACKET);
                    		
                    #action end

                    self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "media"


    # $ANTLR start "media_query"
    # treelesscss.g:98:1: media_query returns [gencode] : ^( N_MediaQuery ( media_stmt | media_expr )+ ) ;
    def media_query(self, ):

        gencode = None

        media_stmt7 = None

        media_expr8 = None


          
        mq = list()
        	
        try:
            try:
                # treelesscss.g:103:2: ( ^( N_MediaQuery ( media_stmt | media_expr )+ ) )
                # treelesscss.g:103:4: ^( N_MediaQuery ( media_stmt | media_expr )+ )
                pass 
                self.match(self.input, N_MediaQuery, self.FOLLOW_N_MediaQuery_in_media_query295)

                self.match(self.input, DOWN, None)
                # treelesscss.g:104:3: ( media_stmt | media_expr )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 3
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == IDENT) :
                        alt8 = 1
                    elif (LA8_0 == N_MediaExpr) :
                        alt8 = 2


                    if alt8 == 1:
                        # treelesscss.g:104:5: media_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_media_stmt_in_media_query301)
                        media_stmt7 = self.media_stmt()

                        self._state.following.pop()
                        #action start
                        mq.append(((media_stmt7 is not None) and [self.input.getTokenStream().toString(
                            self.input.getTreeAdaptor().getTokenStartIndex(media_stmt7.start),
                            self.input.getTreeAdaptor().getTokenStopIndex(media_stmt7.start)
                            )] or [None])[0]); 
                        #action end


                    elif alt8 == 2:
                        # treelesscss.g:105:5: media_expr
                        pass 
                        self._state.following.append(self.FOLLOW_media_expr_in_media_query309)
                        media_expr8 = self.media_expr()

                        self._state.following.pop()
                        #action start
                        mq.append(((media_expr8 is not None) and [self.input.getTokenStream().toString(
                            self.input.getTreeAdaptor().getTokenStartIndex(media_expr8.start),
                            self.input.getTreeAdaptor().getTokenStopIndex(media_expr8.start)
                            )] or [None])[0]); 
                        #action end


                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1

                self.match(self.input, UP, None)
                #action start
                gencode =  ' '.join(mq) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "media_query"

    class media_stmt_return(TreeRuleReturnScope):
        def __init__(self):
            super(treelesscss.media_stmt_return, self).__init__()





    # $ANTLR start "media_stmt"
    # treelesscss.g:111:1: media_stmt : IDENT ;
    def media_stmt(self, ):

        retval = self.media_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:112:2: ( IDENT )
                # treelesscss.g:112:4: IDENT
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_stmt335)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "media_stmt"

    class media_expr_return(TreeRuleReturnScope):
        def __init__(self):
            super(treelesscss.media_expr_return, self).__init__()





    # $ANTLR start "media_expr"
    # treelesscss.g:115:1: media_expr : ^( N_MediaExpr media_stmt ) ;
    def media_expr(self, ):

        retval = self.media_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:116:2: ( ^( N_MediaExpr media_stmt ) )
                # treelesscss.g:116:4: ^( N_MediaExpr media_stmt )
                pass 
                self.match(self.input, N_MediaExpr, self.FOLLOW_N_MediaExpr_in_media_expr347)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_media_stmt_in_media_expr349)
                self.media_stmt()

                self._state.following.pop()

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "media_expr"


    # $ANTLR start "ruleSet"
    # treelesscss.g:124:1: ruleSet : ^( N_RuleSet ( selector_list )+ declarationset ) ;
    def ruleSet(self, ):

        selector_list9 = None


          
        sellist = [];
        	
        try:
            try:
                # treelesscss.g:129:2: ( ^( N_RuleSet ( selector_list )+ declarationset ) )
                # treelesscss.g:129:4: ^( N_RuleSet ( selector_list )+ declarationset )
                pass 
                self.match(self.input, N_RuleSet, self.FOLLOW_N_RuleSet_in_ruleSet376)

                self.match(self.input, DOWN, None)
                # treelesscss.g:130:3: ( selector_list )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == N_Selector) :
                        alt9 = 1


                    if alt9 == 1:
                        # treelesscss.g:130:4: selector_list
                        pass 
                        self._state.following.append(self.FOLLOW_selector_list_in_ruleSet381)
                        selector_list9 = self.selector_list()

                        self._state.following.pop()
                        #action start
                        sellist.append(selector_list9); 
                        #action end


                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1
                #action start
                   
                self.output(self.LISTCOMA.join(sellist) + self.EOLLBRACKET);
                self.indent_level += 1;
                		
                #action end
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet394)
                self.declarationset()

                self._state.following.pop()
                #action start
                   
                self.indent_level -= 1
                self.output(self.EOLRBRACKET);
                		
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "ruleSet"


    # $ANTLR start "selector_list"
    # treelesscss.g:143:1: selector_list returns [gencode] : ^( N_Selector selector ) ;
    def selector_list(self, ):

        gencode = None

        selector10 = None


        try:
            try:
                # treelesscss.g:143:32: ( ^( N_Selector selector ) )
                # treelesscss.g:144:2: ^( N_Selector selector )
                pass 
                self.match(self.input, N_Selector, self.FOLLOW_N_Selector_in_selector_list417)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_selector_in_selector_list421)
                selector10 = self.selector()

                self._state.following.pop()
                #action start
                gencode =  selector10 
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "selector_list"


    # $ANTLR start "selector"
    # treelesscss.g:149:1: selector returns [gencode] : a= simpleSelector ( combinator b= simpleSelector )* ;
    def selector(self, ):

        gencode = None

        a = None

        b = None

        combinator11 = None


        try:
            try:
                # treelesscss.g:150:2: (a= simpleSelector ( combinator b= simpleSelector )* )
                # treelesscss.g:150:4: a= simpleSelector ( combinator b= simpleSelector )*
                pass 
                self._state.following.append(self.FOLLOW_simpleSelector_in_selector444)
                a = self.simpleSelector()

                self._state.following.pop()
                #action start
                gencode =  a 
                #action end
                # treelesscss.g:151:2: ( combinator b= simpleSelector )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == N_Pseudo or LA10_0 == IDENT or (PLUS <= LA10_0 <= HASH) or LA10_0 == STAR) :
                        alt10 = 1


                    if alt10 == 1:
                        # treelesscss.g:152:3: combinator b= simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector453)
                        combinator11 = self.combinator()

                        self._state.following.pop()
                        #action start
                        gencode += combinator11; 
                        #action end
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector461)
                        b = self.simpleSelector()

                        self._state.following.pop()
                        #action start
                                            
                        # This code decides if there will be whitespace between selectors or not
                        #TODO: Refactor this (to remove this 'strange construct')
                        if b[:1] == ':':
                        	gencode =  gencode.rstrip() + b
                        else:
                        	gencode += b;
                        		
                        #action end


                    else:
                        break #loop10




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "selector"


    # $ANTLR start "combinator"
    # treelesscss.g:164:1: combinator returns [gencode] : ( PLUS | GREATER | );
    def combinator(self, ):

        gencode = None

        PLUS12 = None
        GREATER13 = None

        try:
            try:
                # treelesscss.g:165:2: ( PLUS | GREATER | )
                alt11 = 3
                LA11 = self.input.LA(1)
                if LA11 == PLUS:
                    alt11 = 1
                elif LA11 == GREATER:
                    alt11 = 2
                elif LA11 == N_Pseudo or LA11 == IDENT or LA11 == HASH or LA11 == STAR:
                    alt11 = 3
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # treelesscss.g:165:4: PLUS
                    pass 
                    PLUS12=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator482)
                    #action start
                    gencode =  PLUS12.text 
                    #action end


                elif alt11 == 2:
                    # treelesscss.g:166:4: GREATER
                    pass 
                    GREATER13=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator491)
                    #action start
                    gencode =  GREATER13.text 
                    #action end


                elif alt11 == 3:
                    # treelesscss.g:167:5: 
                    pass 
                    #action start
                    gencode =  ' ' 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "combinator"


    # $ANTLR start "simpleSelector"
    # treelesscss.g:170:1: simpleSelector returns [gencode] : ( IDENT | STAR | HASH | pseudo );
    def simpleSelector(self, ):

        gencode = None

        IDENT14 = None
        STAR15 = None
        HASH16 = None
        pseudo17 = None


        try:
            try:
                # treelesscss.g:171:2: ( IDENT | STAR | HASH | pseudo )
                alt12 = 4
                LA12 = self.input.LA(1)
                if LA12 == IDENT:
                    alt12 = 1
                elif LA12 == STAR:
                    alt12 = 2
                elif LA12 == HASH:
                    alt12 = 3
                elif LA12 == N_Pseudo:
                    alt12 = 4
                else:
                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # treelesscss.g:171:4: IDENT
                    pass 
                    IDENT14=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_simpleSelector514)
                    #action start
                    gencode =  IDENT14.text 
                    #action end


                elif alt12 == 2:
                    # treelesscss.g:172:4: STAR
                    pass 
                    STAR15=self.match(self.input, STAR, self.FOLLOW_STAR_in_simpleSelector522)
                    #action start
                    gencode =  STAR15.text 
                    #action end


                elif alt12 == 3:
                    # treelesscss.g:173:4: HASH
                    pass 
                    HASH16=self.match(self.input, HASH, self.FOLLOW_HASH_in_simpleSelector530)
                    #action start
                    gencode =  HASH16.text 
                    #action end


                elif alt12 == 4:
                    # treelesscss.g:174:4: pseudo
                    pass 
                    self._state.following.append(self.FOLLOW_pseudo_in_simpleSelector538)
                    pseudo17 = self.pseudo()

                    self._state.following.pop()
                    #action start
                    gencode =  pseudo17 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "simpleSelector"


    # $ANTLR start "pseudo"
    # treelesscss.g:178:1: pseudo returns [gencode] : ^( N_Pseudo a= COLON (b= COLON )? IDENT ) ;
    def pseudo(self, ):

        gencode = None

        a = None
        b = None
        IDENT18 = None

        try:
            try:
                # treelesscss.g:179:2: ( ^( N_Pseudo a= COLON (b= COLON )? IDENT ) )
                # treelesscss.g:179:4: ^( N_Pseudo a= COLON (b= COLON )? IDENT )
                pass 
                self.match(self.input, N_Pseudo, self.FOLLOW_N_Pseudo_in_pseudo557)

                self.match(self.input, DOWN, None)
                a=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo561)
                # treelesscss.g:179:24: (b= COLON )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == COLON) :
                    alt13 = 1
                if alt13 == 1:
                    # treelesscss.g:179:24: b= COLON
                    pass 
                    b=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo565)



                IDENT18=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo568)

                self.match(self.input, UP, None)
                #action start
                gencode =  a.text + (b.text if b is not None else '') + IDENT18.text 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "pseudo"


    # $ANTLR start "declarationset"
    # treelesscss.g:188:1: declarationset : ( N_Empty | ( declaration )+ );
    def declarationset(self, ):

        try:
            try:
                # treelesscss.g:189:2: ( N_Empty | ( declaration )+ )
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == N_Empty) :
                    alt15 = 1
                elif (LA15_0 == N_Declaration) :
                    alt15 = 2
                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae

                if alt15 == 1:
                    # treelesscss.g:189:4: N_Empty
                    pass 
                    self.match(self.input, N_Empty, self.FOLLOW_N_Empty_in_declarationset589)


                elif alt15 == 2:
                    # treelesscss.g:190:4: ( declaration )+
                    pass 
                    # treelesscss.g:190:4: ( declaration )+
                    cnt14 = 0
                    while True: #loop14
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if (LA14_0 == N_Declaration) :
                            alt14 = 1


                        if alt14 == 1:
                            # treelesscss.g:190:4: declaration
                            pass 
                            self._state.following.append(self.FOLLOW_declaration_in_declarationset594)
                            self.declaration()

                            self._state.following.pop()


                        else:
                            if cnt14 >= 1:
                                break #loop14

                            eee = EarlyExitException(14, self.input)
                            raise eee

                        cnt14 += 1



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "declarationset"


    # $ANTLR start "declaration"
    # treelesscss.g:194:1: declaration : ^( N_Declaration property ( expr )? ( prio )? ) ;
    def declaration(self, ):

        property19 = None

        expr20 = None


        try:
            try:
                # treelesscss.g:195:2: ( ^( N_Declaration property ( expr )? ( prio )? ) )
                # treelesscss.g:195:4: ^( N_Declaration property ( expr )? ( prio )? )
                pass 
                self.match(self.input, N_Declaration, self.FOLLOW_N_Declaration_in_declaration608)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_property_in_declaration612)
                property19 = self.property()

                self._state.following.pop()
                #action start
                propout = property19 +  ":"; 
                #action end
                # treelesscss.g:197:3: ( expr )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == N_Term or LA16_0 == STRING or LA16_0 == URI or LA16_0 == IDENT or LA16_0 == UNICODE_RANGE) :
                    alt16 = 1
                if alt16 == 1:
                    # treelesscss.g:197:4: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_declaration619)
                    expr20 = self.expr()

                    self._state.following.pop()
                    #action start
                    propout += expr20
                    #action end



                # treelesscss.g:198:3: ( prio )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == IMPORTANT_SYM) :
                    alt17 = 1
                if alt17 == 1:
                    # treelesscss.g:198:4: prio
                    pass 
                    self._state.following.append(self.FOLLOW_prio_in_declaration629)
                    self.prio()

                    self._state.following.pop()
                    #action start
                    propout += ' !important'
                    #action end



                #action start
                   
                #TODO: Remove last semicolon in the declarationset (how?) ...
                self.output(propout + self.EOLSEMI);
                		
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "declaration"


    # $ANTLR start "property"
    # treelesscss.g:206:1: property returns [gencode] : IDENT ;
    def property(self, ):

        gencode = None

        IDENT21 = None

        try:
            try:
                # treelesscss.g:207:2: ( IDENT )
                # treelesscss.g:207:4: IDENT
                pass 
                IDENT21=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property656)
                #action start
                gencode =  IDENT21.text 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "property"


    # $ANTLR start "prio"
    # treelesscss.g:210:1: prio returns [gencode] : IMPORTANT_SYM ;
    def prio(self, ):

        gencode = None

        IMPORTANT_SYM22 = None

        try:
            try:
                # treelesscss.g:211:2: ( IMPORTANT_SYM )
                # treelesscss.g:211:4: IMPORTANT_SYM
                pass 
                IMPORTANT_SYM22=self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio675)
                #action start
                gencode =  IMPORTANT_SYM22.text 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "prio"


    # $ANTLR start "expr"
    # treelesscss.g:215:1: expr returns [gencode] : term ;
    def expr(self, ):

        gencode = None

        term23 = None


        try:
            try:
                # treelesscss.g:217:2: ( term )
                # treelesscss.g:217:4: term
                pass 
                self._state.following.append(self.FOLLOW_term_in_expr696)
                term23 = self.term()

                self._state.following.pop()
                #action start
                gencode =  term23 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "expr"


    # $ANTLR start "operator"
    # treelesscss.g:220:10: fragment operator returns [gencode] : ( SOLIDUS | COMMA | N_Empty );
    def operator(self, ):

        gencode = None

        SOLIDUS24 = None
        COMMA25 = None

        try:
            try:
                # treelesscss.g:221:2: ( SOLIDUS | COMMA | N_Empty )
                alt18 = 3
                LA18 = self.input.LA(1)
                if LA18 == SOLIDUS:
                    alt18 = 1
                elif LA18 == COMMA:
                    alt18 = 2
                elif LA18 == N_Empty:
                    alt18 = 3
                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae

                if alt18 == 1:
                    # treelesscss.g:221:4: SOLIDUS
                    pass 
                    SOLIDUS24=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator717)
                    #action start
                    gencode =  SOLIDUS24.text 
                    #action end


                elif alt18 == 2:
                    # treelesscss.g:222:4: COMMA
                    pass 
                    COMMA25=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator726)
                    #action start
                    gencode =  COMMA25.text 
                    #action end


                elif alt18 == 3:
                    # treelesscss.g:223:4: N_Empty
                    pass 
                    self.match(self.input, N_Empty, self.FOLLOW_N_Empty_in_operator735)
                    #action start
                    gencode =  '' 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "operator"


    # $ANTLR start "term"
    # treelesscss.g:226:1: term returns [gencode] : ( ^( N_Term unaryOperator termnum ) | ^( N_Term termnum ) | STRING | IDENT | URI | UNICODE_RANGE );
    def term(self, ):

        gencode = None

        STRING29 = None
        IDENT30 = None
        URI31 = None
        UNICODE_RANGE32 = None
        unaryOperator26 = None

        termnum27 = None

        termnum28 = None


        try:
            try:
                # treelesscss.g:227:2: ( ^( N_Term unaryOperator termnum ) | ^( N_Term termnum ) | STRING | IDENT | URI | UNICODE_RANGE )
                alt19 = 6
                LA19 = self.input.LA(1)
                if LA19 == N_Term:
                    LA19_1 = self.input.LA(2)

                    if (LA19_1 == 2) :
                        LA19_6 = self.input.LA(3)

                        if (LA19_6 == PLUS or LA19_6 == MINUS) :
                            alt19 = 1
                        elif (LA19_6 == PERCENTAGE or (NUMBER <= LA19_6 <= NTH)) :
                            alt19 = 2
                        else:
                            nvae = NoViableAltException("", 19, 6, self.input)

                            raise nvae

                    else:
                        nvae = NoViableAltException("", 19, 1, self.input)

                        raise nvae

                elif LA19 == STRING:
                    alt19 = 3
                elif LA19 == IDENT:
                    alt19 = 4
                elif LA19 == URI:
                    alt19 = 5
                elif LA19 == UNICODE_RANGE:
                    alt19 = 6
                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # treelesscss.g:227:4: ^( N_Term unaryOperator termnum )
                    pass 
                    self.match(self.input, N_Term, self.FOLLOW_N_Term_in_term754)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_unaryOperator_in_term756)
                    unaryOperator26 = self.unaryOperator()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_termnum_in_term758)
                    termnum27 = self.termnum()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    gencode =  unaryOperator26 + termnum27 
                    #action end


                elif alt19 == 2:
                    # treelesscss.g:228:4: ^( N_Term termnum )
                    pass 
                    self.match(self.input, N_Term, self.FOLLOW_N_Term_in_term768)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_termnum_in_term770)
                    termnum28 = self.termnum()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    gencode =  termnum28 
                    #action end


                elif alt19 == 3:
                    # treelesscss.g:229:4: STRING
                    pass 
                    STRING29=self.match(self.input, STRING, self.FOLLOW_STRING_in_term780)
                    #action start
                    gencode =  STRING29.text 
                    #action end


                elif alt19 == 4:
                    # treelesscss.g:230:4: IDENT
                    pass 
                    IDENT30=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term788)
                    #action start
                    gencode =  IDENT30.text 
                    #action end


                elif alt19 == 5:
                    # treelesscss.g:231:4: URI
                    pass 
                    URI31=self.match(self.input, URI, self.FOLLOW_URI_in_term797)
                    #action start
                    gencode =  URI31.text 
                    #action end


                elif alt19 == 6:
                    # treelesscss.g:233:4: UNICODE_RANGE
                    pass 
                    UNICODE_RANGE32=self.match(self.input, UNICODE_RANGE, self.FOLLOW_UNICODE_RANGE_in_term807)
                    #action start
                    gencode =  UNICODE_RANGE32.text 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "term"


    # $ANTLR start "termnum"
    # treelesscss.g:236:10: fragment termnum returns [gencode] : ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH );
    def termnum(self, ):

        gencode = None

        NUMBER33 = None
        PERCENTAGE34 = None
        LENGTH35 = None
        EMS36 = None
        EXS37 = None
        REMS38 = None
        CHS39 = None
        ANGLE40 = None
        TIME41 = None
        FREQ42 = None
        RESOLUTION43 = None
        VPORTLEN44 = None
        NTH45 = None

        try:
            try:
                # treelesscss.g:237:2: ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH )
                alt20 = 13
                LA20 = self.input.LA(1)
                if LA20 == NUMBER:
                    alt20 = 1
                elif LA20 == PERCENTAGE:
                    alt20 = 2
                elif LA20 == LENGTH:
                    alt20 = 3
                elif LA20 == EMS:
                    alt20 = 4
                elif LA20 == EXS:
                    alt20 = 5
                elif LA20 == REMS:
                    alt20 = 6
                elif LA20 == CHS:
                    alt20 = 7
                elif LA20 == ANGLE:
                    alt20 = 8
                elif LA20 == TIME:
                    alt20 = 9
                elif LA20 == FREQ:
                    alt20 = 10
                elif LA20 == RESOLUTION:
                    alt20 = 11
                elif LA20 == VPORTLEN:
                    alt20 = 12
                elif LA20 == NTH:
                    alt20 = 13
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # treelesscss.g:237:4: NUMBER
                    pass 
                    NUMBER33=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_termnum827)
                    #action start
                    gencode =  NUMBER33.text.strip() 
                    #action end


                elif alt20 == 2:
                    # treelesscss.g:238:4: PERCENTAGE
                    pass 
                    PERCENTAGE34=self.match(self.input, PERCENTAGE, self.FOLLOW_PERCENTAGE_in_termnum835)
                    #action start
                    gencode =  PERCENTAGE34.text.strip() 
                    #action end


                elif alt20 == 3:
                    # treelesscss.g:239:4: LENGTH
                    pass 
                    LENGTH35=self.match(self.input, LENGTH, self.FOLLOW_LENGTH_in_termnum843)
                    #action start
                    gencode =  LENGTH35.text.strip() 
                    #action end


                elif alt20 == 4:
                    # treelesscss.g:240:4: EMS
                    pass 
                    EMS36=self.match(self.input, EMS, self.FOLLOW_EMS_in_termnum851)
                    #action start
                    gencode =  EMS36.text.strip() 
                    #action end


                elif alt20 == 5:
                    # treelesscss.g:241:4: EXS
                    pass 
                    EXS37=self.match(self.input, EXS, self.FOLLOW_EXS_in_termnum860)
                    #action start
                    gencode =  EXS37.text.strip() 
                    #action end


                elif alt20 == 6:
                    # treelesscss.g:242:4: REMS
                    pass 
                    REMS38=self.match(self.input, REMS, self.FOLLOW_REMS_in_termnum869)
                    #action start
                    gencode =  REMS38.text.strip() 
                    #action end


                elif alt20 == 7:
                    # treelesscss.g:243:4: CHS
                    pass 
                    CHS39=self.match(self.input, CHS, self.FOLLOW_CHS_in_termnum878)
                    #action start
                    gencode =  CHS39.text.strip() 
                    #action end


                elif alt20 == 8:
                    # treelesscss.g:244:4: ANGLE
                    pass 
                    ANGLE40=self.match(self.input, ANGLE, self.FOLLOW_ANGLE_in_termnum887)
                    #action start
                    gencode =  ANGLE40.text.strip() 
                    #action end


                elif alt20 == 9:
                    # treelesscss.g:245:4: TIME
                    pass 
                    TIME41=self.match(self.input, TIME, self.FOLLOW_TIME_in_termnum896)
                    #action start
                    gencode =  TIME41.text.strip() 
                    #action end


                elif alt20 == 10:
                    # treelesscss.g:246:4: FREQ
                    pass 
                    FREQ42=self.match(self.input, FREQ, self.FOLLOW_FREQ_in_termnum905)
                    #action start
                    gencode =  FREQ42.text.strip() 
                    #action end


                elif alt20 == 11:
                    # treelesscss.g:247:4: RESOLUTION
                    pass 
                    RESOLUTION43=self.match(self.input, RESOLUTION, self.FOLLOW_RESOLUTION_in_termnum914)
                    #action start
                    gencode =  RESOLUTION43.text.strip() 
                    #action end


                elif alt20 == 12:
                    # treelesscss.g:248:4: VPORTLEN
                    pass 
                    VPORTLEN44=self.match(self.input, VPORTLEN, self.FOLLOW_VPORTLEN_in_termnum922)
                    #action start
                    gencode =  VPORTLEN44.text.strip() 
                    #action end


                elif alt20 == 13:
                    # treelesscss.g:249:4: NTH
                    pass 
                    NTH45=self.match(self.input, NTH, self.FOLLOW_NTH_in_termnum930)
                    #action start
                    gencode =  NTH45.text.strip() 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "termnum"


    # $ANTLR start "unaryOperator"
    # treelesscss.g:254:1: unaryOperator returns [gencode] : ( MINUS | PLUS );
    def unaryOperator(self, ):

        gencode = None

        MINUS46 = None
        PLUS47 = None

        try:
            try:
                # treelesscss.g:255:2: ( MINUS | PLUS )
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == MINUS) :
                    alt21 = 1
                elif (LA21_0 == PLUS) :
                    alt21 = 2
                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # treelesscss.g:255:4: MINUS
                    pass 
                    MINUS46=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_unaryOperator951)
                    #action start
                    gencode =  MINUS46.text 
                    #action end


                elif alt21 == 2:
                    # treelesscss.g:256:4: PLUS
                    pass 
                    PLUS47=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_unaryOperator959)
                    #action start
                    gencode =  PLUS47.text 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "unaryOperator"


    # Delegated rules


 

    FOLLOW_N_StyleSheet_in_styleSheet51 = frozenset([2])
    FOLLOW_charSet_in_styleSheet56 = frozenset([3, 7, 21, 23])
    FOLLOW_imports_in_styleSheet66 = frozenset([3, 7, 21, 23])
    FOLLOW_body_in_styleSheet75 = frozenset([3, 7, 23])
    FOLLOW_CHARSET_SYM_in_charSet101 = frozenset([2])
    FOLLOW_STRING_in_charSet103 = frozenset([3])
    FOLLOW_IMPORT_SYM_in_imports141 = frozenset([2])
    FOLLOW_importUrl_in_imports145 = frozenset([3, 5])
    FOLLOW_media_query_in_imports153 = frozenset([3, 5])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_ruleSet_in_body204 = frozenset([1])
    FOLLOW_media_in_body211 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media240 = frozenset([2])
    FOLLOW_media_query_in_media246 = frozenset([3, 5, 7, 23])
    FOLLOW_body_in_media260 = frozenset([3, 7, 23])
    FOLLOW_N_MediaQuery_in_media_query295 = frozenset([2])
    FOLLOW_media_stmt_in_media_query301 = frozenset([3, 6, 27])
    FOLLOW_media_expr_in_media_query309 = frozenset([3, 6, 27])
    FOLLOW_IDENT_in_media_stmt335 = frozenset([1])
    FOLLOW_N_MediaExpr_in_media_expr347 = frozenset([2])
    FOLLOW_media_stmt_in_media_expr349 = frozenset([3])
    FOLLOW_N_RuleSet_in_ruleSet376 = frozenset([2])
    FOLLOW_selector_list_in_ruleSet381 = frozenset([10, 11, 14])
    FOLLOW_declarationset_in_ruleSet394 = frozenset([3])
    FOLLOW_N_Selector_in_selector_list417 = frozenset([2])
    FOLLOW_selector_in_selector_list421 = frozenset([3])
    FOLLOW_simpleSelector_in_selector444 = frozenset([1, 15, 27, 35, 36, 37, 40])
    FOLLOW_combinator_in_selector453 = frozenset([15, 27, 35, 36, 37, 40])
    FOLLOW_simpleSelector_in_selector461 = frozenset([1, 15, 27, 35, 36, 37, 40])
    FOLLOW_PLUS_in_combinator482 = frozenset([1])
    FOLLOW_GREATER_in_combinator491 = frozenset([1])
    FOLLOW_IDENT_in_simpleSelector514 = frozenset([1])
    FOLLOW_STAR_in_simpleSelector522 = frozenset([1])
    FOLLOW_HASH_in_simpleSelector530 = frozenset([1])
    FOLLOW_pseudo_in_simpleSelector538 = frozenset([1])
    FOLLOW_N_Pseudo_in_pseudo557 = frozenset([2])
    FOLLOW_COLON_in_pseudo561 = frozenset([27, 29])
    FOLLOW_COLON_in_pseudo565 = frozenset([27])
    FOLLOW_IDENT_in_pseudo568 = frozenset([3])
    FOLLOW_N_Empty_in_declarationset589 = frozenset([1])
    FOLLOW_declaration_in_declarationset594 = frozenset([1, 11, 14])
    FOLLOW_N_Declaration_in_declaration608 = frozenset([2])
    FOLLOW_property_in_declaration612 = frozenset([3, 17, 19, 22, 27, 49, 63])
    FOLLOW_expr_in_declaration619 = frozenset([3, 49])
    FOLLOW_prio_in_declaration629 = frozenset([3])
    FOLLOW_IDENT_in_property656 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio675 = frozenset([1])
    FOLLOW_term_in_expr696 = frozenset([1])
    FOLLOW_SOLIDUS_in_operator717 = frozenset([1])
    FOLLOW_COMMA_in_operator726 = frozenset([1])
    FOLLOW_N_Empty_in_operator735 = frozenset([1])
    FOLLOW_N_Term_in_term754 = frozenset([2])
    FOLLOW_unaryOperator_in_term756 = frozenset([34, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62])
    FOLLOW_termnum_in_term758 = frozenset([3])
    FOLLOW_N_Term_in_term768 = frozenset([2])
    FOLLOW_termnum_in_term770 = frozenset([3])
    FOLLOW_STRING_in_term780 = frozenset([1])
    FOLLOW_IDENT_in_term788 = frozenset([1])
    FOLLOW_URI_in_term797 = frozenset([1])
    FOLLOW_UNICODE_RANGE_in_term807 = frozenset([1])
    FOLLOW_NUMBER_in_termnum827 = frozenset([1])
    FOLLOW_PERCENTAGE_in_termnum835 = frozenset([1])
    FOLLOW_LENGTH_in_termnum843 = frozenset([1])
    FOLLOW_EMS_in_termnum851 = frozenset([1])
    FOLLOW_EXS_in_termnum860 = frozenset([1])
    FOLLOW_REMS_in_termnum869 = frozenset([1])
    FOLLOW_CHS_in_termnum878 = frozenset([1])
    FOLLOW_ANGLE_in_termnum887 = frozenset([1])
    FOLLOW_TIME_in_termnum896 = frozenset([1])
    FOLLOW_FREQ_in_termnum905 = frozenset([1])
    FOLLOW_RESOLUTION_in_termnum914 = frozenset([1])
    FOLLOW_VPORTLEN_in_termnum922 = frozenset([1])
    FOLLOW_NTH_in_termnum930 = frozenset([1])
    FOLLOW_MINUS_in_unaryOperator951 = frozenset([1])
    FOLLOW_PLUS_in_unaryOperator959 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(treelesscss)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
