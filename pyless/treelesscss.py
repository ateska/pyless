# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 treelesscss.g 2012-12-02 12:53:37

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=42
UNICODE_RANGE=64
STAR=41
EOF=-1
MEDIA_SYM=24
LBRACKET=40
INCLUDES=45
RPAREN=31
NAME=72
GREATER=37
ESCAPE=69
DIMENSION=105
STRINGESC=103
NL=106
COMMENT=100
D=77
E=78
F=79
G=80
A=74
B=75
RBRACE=26
C=76
L=85
M=86
NMCHAR=71
IMPORT_SYM=22
N=87
SUBSTRINGMATCH=49
O=88
H=81
I=82
J=83
K=84
NUMBER=52
U=94
T=93
W=96
V=95
Q=90
P=89
S=92
CDO=101
R=91
CDC=102
Y=98
PERCENTAGE=35
URL=73
X=97
Z=99
URI=23
PAGE_SYM=33
WS=104
DASHMATCH=46
EMS=54
N_PseudoFunction=17
N_RuleSet=7
NONASCII=67
N_MediaQuery=5
N_Selector=10
LBRACE=25
LPAREN=29
LENGTH=53
IMPORTANT_SYM=50
N_Function=12
TIME=59
KEYFRAMES_SYM=34
COMMA=27
N_StyleSheet=4
IDENT=28
PLUS=36
FREQ=60
RBRACKET=43
DOT=39
VPORTLEN=62
CHARSET_SYM=19
ANGLE=58
REMS=56
HASH=38
HEXCHAR=66
RESOLUTION=61
PREFIXMATCH=47
MINUS=65
N_Pseudo=16
SOLIDUS=51
SEMI=21
N_Empty=14
UNICODE=68
CHS=57
COLON=30
NMSTART=70
N_Declaration=11
OPEQ=44
FONTFACE_SYM=32
N_Term=18
EXS=55
N_Space=15
M_KeyframeSelector=9
N_MediaExpr=6
N_Attrib=13
N_KeyframeBlock=8
SUFFIXMATCH=48
NTH=63
STRING=20

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "N_StyleSheet", "N_MediaQuery", "N_MediaExpr", "N_RuleSet", "N_KeyframeBlock", 
    "M_KeyframeSelector", "N_Selector", "N_Declaration", "N_Function", "N_Attrib", 
    "N_Empty", "N_Space", "N_Pseudo", "N_PseudoFunction", "N_Term", "CHARSET_SYM", 
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

        self.dfa26 = self.DFA26(
            self, 26,
            eot = self.DFA26_eot,
            eof = self.DFA26_eof,
            min = self.DFA26_min,
            max = self.DFA26_max,
            accept = self.DFA26_accept,
            special = self.DFA26_special,
            transition = self.DFA26_transition
            )






                


        



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
                        # treelesscss.g:16:5: charSet
                        pass 
                        self._state.following.append(self.FOLLOW_charSet_in_styleSheet61)
                        charSet1 = self.charSet()

                        self._state.following.pop()
                        #action start
                        self.output(charSet1); 
                        #action end



                    # treelesscss.g:18:3: ( imports )*
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == IMPORT_SYM) :
                            alt2 = 1


                        if alt2 == 1:
                            # treelesscss.g:19:5: imports
                            pass 
                            self._state.following.append(self.FOLLOW_imports_in_styleSheet79)
                            imports2 = self.imports()

                            self._state.following.pop()
                            #action start
                            self.output(imports2); 
                            #action end


                        else:
                            break #loop2
                    # treelesscss.g:21:3: ( body )*
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == N_RuleSet or LA3_0 == MEDIA_SYM or (FONTFACE_SYM <= LA3_0 <= KEYFRAMES_SYM)) :
                            alt3 = 1


                        if alt3 == 1:
                            # treelesscss.g:21:3: body
                            pass 
                            self._state.following.append(self.FOLLOW_body_in_styleSheet91)
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
    # treelesscss.g:27:1: charSet returns [gencode] : ^( CHARSET_SYM STRING ) ;
    def charSet(self, ):

        gencode = None

        STRING3 = None

        try:
            try:
                # treelesscss.g:28:4: ( ^( CHARSET_SYM STRING ) )
                # treelesscss.g:28:6: ^( CHARSET_SYM STRING )
                pass 
                self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet115)

                self.match(self.input, DOWN, None)
                STRING3=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet117)

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
    # treelesscss.g:35:1: imports returns [gencode] : ^( IMPORT_SYM importUrl ( media_query )* ) ;
    def imports(self, ):

        gencode = None

        importUrl4 = None

        media_query5 = None


        try:
            try:
                # treelesscss.g:36:2: ( ^( IMPORT_SYM importUrl ( media_query )* ) )
                # treelesscss.g:36:4: ^( IMPORT_SYM importUrl ( media_query )* )
                pass 
                self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports144)

                #action start
                                   
                gencode =  '@import '
                mqs = list(); 
                				
                #action end

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_importUrl_in_imports152)
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
                        # treelesscss.g:42:5: media_query
                        pass 
                        self._state.following.append(self.FOLLOW_media_query_in_imports164)
                        media_query5 = self.media_query()

                        self._state.following.pop()
                        #action start
                        mqs.append(media_query5) ; 
                        #action end


                    else:
                        break #loop4
                #action start
                     
                if len(mqs) > 0: gencode += ' ' + self.LISTCOMA.join(mqs);
                gencode += self.EOLSEMI ; 
                				
                #action end

                self.match(self.input, UP, None)




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
    # treelesscss.g:59:1: body : ( ruleSet | media | page | fontface | keyframes );
    def body(self, ):

        try:
            try:
                # treelesscss.g:60:2: ( ruleSet | media | page | fontface | keyframes )
                alt5 = 5
                LA5 = self.input.LA(1)
                if LA5 == N_RuleSet:
                    alt5 = 1
                elif LA5 == MEDIA_SYM:
                    alt5 = 2
                elif LA5 == PAGE_SYM:
                    alt5 = 3
                elif LA5 == FONTFACE_SYM:
                    alt5 = 4
                elif LA5 == KEYFRAMES_SYM:
                    alt5 = 5
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # treelesscss.g:60:4: ruleSet
                    pass 
                    self._state.following.append(self.FOLLOW_ruleSet_in_body210)
                    self.ruleSet()

                    self._state.following.pop()


                elif alt5 == 2:
                    # treelesscss.g:61:4: media
                    pass 
                    self._state.following.append(self.FOLLOW_media_in_body216)
                    self.media()

                    self._state.following.pop()


                elif alt5 == 3:
                    # treelesscss.g:62:4: page
                    pass 
                    self._state.following.append(self.FOLLOW_page_in_body223)
                    self.page()

                    self._state.following.pop()


                elif alt5 == 4:
                    # treelesscss.g:63:4: fontface
                    pass 
                    self._state.following.append(self.FOLLOW_fontface_in_body230)
                    self.fontface()

                    self._state.following.pop()


                elif alt5 == 5:
                    # treelesscss.g:64:4: keyframes
                    pass 
                    self._state.following.append(self.FOLLOW_keyframes_in_body236)
                    self.keyframes()

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


        try:
            try:
                # treelesscss.g:73:2: ( ^( MEDIA_SYM ( media_query )* ( body )* ) )
                # treelesscss.g:73:4: ^( MEDIA_SYM ( media_query )* ( body )* )
                pass 
                self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media254)

                #action start
                mqs = list(); 
                #action end

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # treelesscss.g:74:3: ( media_query )*
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == N_MediaQuery) :
                            alt6 = 1


                        if alt6 == 1:
                            # treelesscss.g:75:5: media_query
                            pass 
                            self._state.following.append(self.FOLLOW_media_query_in_media267)
                            media_query6 = self.media_query()

                            self._state.following.pop()
                            #action start
                            mqs.append(media_query6); 
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
                    # treelesscss.g:84:3: ( body )*
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if (LA7_0 == N_RuleSet or LA7_0 == MEDIA_SYM or (FONTFACE_SYM <= LA7_0 <= KEYFRAMES_SYM)) :
                            alt7 = 1


                        if alt7 == 1:
                            # treelesscss.g:84:3: body
                            pass 
                            self._state.following.append(self.FOLLOW_body_in_media286)
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
    # treelesscss.g:95:1: media_query returns [gencode] : ^( N_MediaQuery ( media_stmt | media_expr )+ ) ;
    def media_query(self, ):

        gencode = None

        media_stmt7 = None

        media_expr8 = None


        try:
            try:
                # treelesscss.g:96:2: ( ^( N_MediaQuery ( media_stmt | media_expr )+ ) )
                # treelesscss.g:96:4: ^( N_MediaQuery ( media_stmt | media_expr )+ )
                pass 
                self.match(self.input, N_MediaQuery, self.FOLLOW_N_MediaQuery_in_media_query314)

                #action start
                mq = list(); 
                #action end

                self.match(self.input, DOWN, None)
                # treelesscss.g:97:3: ( media_stmt | media_expr )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 3
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == IDENT) :
                        alt8 = 1
                    elif (LA8_0 == N_MediaExpr) :
                        alt8 = 2


                    if alt8 == 1:
                        # treelesscss.g:98:5: media_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_media_stmt_in_media_query326)
                        media_stmt7 = self.media_stmt()

                        self._state.following.pop()
                        #action start
                        mq.append(((media_stmt7 is not None) and [self.input.getTokenStream().toString(
                            self.input.getTreeAdaptor().getTokenStartIndex(media_stmt7.start),
                            self.input.getTreeAdaptor().getTokenStopIndex(media_stmt7.start)
                            )] or [None])[0]); 
                        #action end


                    elif alt8 == 2:
                        # treelesscss.g:99:5: media_expr
                        pass 
                        self._state.following.append(self.FOLLOW_media_expr_in_media_query334)
                        media_expr8 = self.media_expr()

                        self._state.following.pop()
                        #action start
                        mq.append(media_expr8); 
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
    # treelesscss.g:104:1: media_stmt : IDENT ;
    def media_stmt(self, ):

        retval = self.media_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:105:2: ( IDENT )
                # treelesscss.g:105:4: IDENT
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_stmt360)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "media_stmt"


    # $ANTLR start "media_expr"
    # treelesscss.g:108:1: media_expr returns [gencode] : ^( N_MediaExpr media_stmt ( expr )? ) ;
    def media_expr(self, ):

        gencode = None

        media_stmt9 = None

        expr10 = None


        try:
            try:
                # treelesscss.g:109:2: ( ^( N_MediaExpr media_stmt ( expr )? ) )
                # treelesscss.g:109:4: ^( N_MediaExpr media_stmt ( expr )? )
                pass 
                self.match(self.input, N_MediaExpr, self.FOLLOW_N_MediaExpr_in_media_expr376)

                #action start
                gencode =  '(' 
                #action end

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_media_stmt_in_media_expr383)
                media_stmt9 = self.media_stmt()

                self._state.following.pop()
                #action start
                gencode += ((media_stmt9 is not None) and [self.input.getTokenStream().toString(
                    self.input.getTreeAdaptor().getTokenStartIndex(media_stmt9.start),
                    self.input.getTreeAdaptor().getTokenStopIndex(media_stmt9.start)
                    )] or [None])[0]; 
                #action end
                # treelesscss.g:111:3: ( expr )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == N_Space or LA9_0 == N_Term or LA9_0 == STRING or LA9_0 == URI or (COMMA <= LA9_0 <= IDENT) or LA9_0 == HASH or LA9_0 == SOLIDUS or LA9_0 == UNICODE_RANGE) :
                    alt9 = 1
                if alt9 == 1:
                    # treelesscss.g:112:5: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_media_expr396)
                    expr10 = self.expr()

                    self._state.following.pop()
                    #action start
                    gencode += ':' + expr10; 
                    #action end




                self.match(self.input, UP, None)
                #action start
                gencode += ')'; 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "media_expr"


    # $ANTLR start "fontface"
    # treelesscss.g:121:1: fontface : ^( FONTFACE_SYM declarationset ) ;
    def fontface(self, ):

        try:
            try:
                # treelesscss.g:122:2: ( ^( FONTFACE_SYM declarationset ) )
                # treelesscss.g:122:4: ^( FONTFACE_SYM declarationset )
                pass 
                self.match(self.input, FONTFACE_SYM, self.FOLLOW_FONTFACE_SYM_in_fontface428)

                #action start
                     
                self.output('@fontface' + self.EOLLBRACKET);
                self.indent_level += 1;
                				
                #action end

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_declarationset_in_fontface438)
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

    # $ANTLR end "fontface"


    # $ANTLR start "page"
    # treelesscss.g:137:1: page : ^( PAGE_SYM ( pseudoPage )? declarationset ) ;
    def page(self, ):

        pseudoPage11 = None


        try:
            try:
                # treelesscss.g:138:2: ( ^( PAGE_SYM ( pseudoPage )? declarationset ) )
                # treelesscss.g:138:4: ^( PAGE_SYM ( pseudoPage )? declarationset )
                pass 
                self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page460)

                #action start
                out = '@page'; 
                #action end

                self.match(self.input, DOWN, None)
                # treelesscss.g:139:3: ( pseudoPage )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == IDENT) :
                    alt10 = 1
                if alt10 == 1:
                    # treelesscss.g:140:5: pseudoPage
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoPage_in_page474)
                    pseudoPage11 = self.pseudoPage()

                    self._state.following.pop()
                    #action start
                    out += ' ' + ((pseudoPage11 is not None) and [self.input.getTokenStream().toString(
                        self.input.getTreeAdaptor().getTokenStartIndex(pseudoPage11.start),
                        self.input.getTreeAdaptor().getTokenStopIndex(pseudoPage11.start)
                        )] or [None])[0]; 
                    #action end



                #action start
                     
                self.output(out + self.EOLLBRACKET);
                self.indent_level += 1;
                				
                #action end
                self._state.following.append(self.FOLLOW_declarationset_in_page491)
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

    # $ANTLR end "page"

    class pseudoPage_return(TreeRuleReturnScope):
        def __init__(self):
            super(treelesscss.pseudoPage_return, self).__init__()





    # $ANTLR start "pseudoPage"
    # treelesscss.g:153:1: pseudoPage : IDENT ;
    def pseudoPage(self, ):

        retval = self.pseudoPage_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:154:2: ( IDENT )
                # treelesscss.g:154:4: IDENT
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage509)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "pseudoPage"


    # $ANTLR start "keyframes"
    # treelesscss.g:161:1: keyframes : ^( KEYFRAMES_SYM IDENT ( keyframes_block )* ) ;
    def keyframes(self, ):

        IDENT12 = None

        try:
            try:
                # treelesscss.g:162:2: ( ^( KEYFRAMES_SYM IDENT ( keyframes_block )* ) )
                # treelesscss.g:162:4: ^( KEYFRAMES_SYM IDENT ( keyframes_block )* )
                pass 
                self.match(self.input, KEYFRAMES_SYM, self.FOLLOW_KEYFRAMES_SYM_in_keyframes525)

                self.match(self.input, DOWN, None)
                IDENT12=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_keyframes527)
                #action start
                     
                self.output('@keyframes ' + IDENT12.text + self.EOLLBRACKET);
                self.indent_level += 1;
                				
                #action end
                # treelesscss.g:167:3: ( keyframes_block )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == N_KeyframeBlock) :
                        alt11 = 1


                    if alt11 == 1:
                        # treelesscss.g:167:3: keyframes_block
                        pass 
                        self._state.following.append(self.FOLLOW_keyframes_block_in_keyframes537)
                        self.keyframes_block()

                        self._state.following.pop()


                    else:
                        break #loop11
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

    # $ANTLR end "keyframes"


    # $ANTLR start "keyframes_block"
    # treelesscss.g:174:1: keyframes_block : ^( N_KeyframeBlock ( keyframe_selector )+ declarationset ) ;
    def keyframes_block(self, ):

        keyframe_selector13 = None


        try:
            try:
                # treelesscss.g:175:2: ( ^( N_KeyframeBlock ( keyframe_selector )+ declarationset ) )
                # treelesscss.g:175:4: ^( N_KeyframeBlock ( keyframe_selector )+ declarationset )
                pass 
                self.match(self.input, N_KeyframeBlock, self.FOLLOW_N_KeyframeBlock_in_keyframes_block557)

                #action start
                ks = list(); 
                #action end

                self.match(self.input, DOWN, None)
                # treelesscss.g:176:3: ( keyframe_selector )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == M_KeyframeSelector) :
                        alt12 = 1


                    if alt12 == 1:
                        # treelesscss.g:176:5: keyframe_selector
                        pass 
                        self._state.following.append(self.FOLLOW_keyframe_selector_in_keyframes_block566)
                        keyframe_selector13 = self.keyframe_selector()

                        self._state.following.pop()
                        #action start
                        ks.append(keyframe_selector13); 
                        #action end


                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1
                #action start
                     
                self.output(' '.join(ks) + self.EOLLBRACKET);
                self.indent_level += 1;
                				
                #action end
                self._state.following.append(self.FOLLOW_declarationset_in_keyframes_block589)
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

    # $ANTLR end "keyframes_block"


    # $ANTLR start "keyframe_selector"
    # treelesscss.g:190:1: keyframe_selector returns [gencode] : ^( M_KeyframeSelector ( IDENT | PERCENTAGE ) ) ;
    def keyframe_selector(self, ):

        gencode = None

        IDENT14 = None
        PERCENTAGE15 = None

        try:
            try:
                # treelesscss.g:191:2: ( ^( M_KeyframeSelector ( IDENT | PERCENTAGE ) ) )
                # treelesscss.g:191:4: ^( M_KeyframeSelector ( IDENT | PERCENTAGE ) )
                pass 
                self.match(self.input, M_KeyframeSelector, self.FOLLOW_M_KeyframeSelector_in_keyframe_selector612)

                self.match(self.input, DOWN, None)
                # treelesscss.g:192:3: ( IDENT | PERCENTAGE )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == IDENT) :
                    alt13 = 1
                elif (LA13_0 == PERCENTAGE) :
                    alt13 = 2
                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # treelesscss.g:192:5: IDENT
                    pass 
                    IDENT14=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_keyframe_selector618)
                    #action start
                    gencode =  IDENT14.text 
                    #action end


                elif alt13 == 2:
                    # treelesscss.g:193:5: PERCENTAGE
                    pass 
                    PERCENTAGE15=self.match(self.input, PERCENTAGE, self.FOLLOW_PERCENTAGE_in_keyframe_selector627)
                    #action start
                    gencode =  PERCENTAGE15.text 
                    #action end




                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "keyframe_selector"


    # $ANTLR start "ruleSet"
    # treelesscss.g:201:1: ruleSet : ^( N_RuleSet ( selector_list )+ declarationset ) ;
    def ruleSet(self, ):

        selector_list16 = None


        try:
            try:
                # treelesscss.g:202:2: ( ^( N_RuleSet ( selector_list )+ declarationset ) )
                # treelesscss.g:202:4: ^( N_RuleSet ( selector_list )+ declarationset )
                pass 
                self.match(self.input, N_RuleSet, self.FOLLOW_N_RuleSet_in_ruleSet651)

                #action start
                sellist = list(); 
                #action end

                self.match(self.input, DOWN, None)
                # treelesscss.g:203:3: ( selector_list )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == N_Selector) :
                        alt14 = 1


                    if alt14 == 1:
                        # treelesscss.g:204:4: selector_list
                        pass 
                        self._state.following.append(self.FOLLOW_selector_list_in_ruleSet663)
                        selector_list16 = self.selector_list()

                        self._state.following.pop()
                        #action start
                        sellist.append(selector_list16); 
                        #action end


                    else:
                        if cnt14 >= 1:
                            break #loop14

                        eee = EarlyExitException(14, self.input)
                        raise eee

                    cnt14 += 1
                #action start
                     
                self.output(self.LISTCOMA.join(sellist) + self.EOLLBRACKET);
                self.indent_level += 1;
                				
                #action end
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet681)
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
    # treelesscss.g:217:1: selector_list returns [gencode] : ^( N_Selector selector ) ;
    def selector_list(self, ):

        gencode = None

        selector17 = None


        try:
            try:
                # treelesscss.g:217:32: ( ^( N_Selector selector ) )
                # treelesscss.g:218:2: ^( N_Selector selector )
                pass 
                self.match(self.input, N_Selector, self.FOLLOW_N_Selector_in_selector_list703)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_selector_in_selector_list707)
                selector17 = self.selector()

                self._state.following.pop()
                #action start
                gencode =  selector17 
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
    # treelesscss.g:222:1: selector returns [gencode] : a= simpleSelector ( combinator b= simpleSelector )* ;
    def selector(self, ):

        gencode = None

        a = None

        b = None

        combinator18 = None


        try:
            try:
                # treelesscss.g:223:2: (a= simpleSelector ( combinator b= simpleSelector )* )
                # treelesscss.g:223:4: a= simpleSelector ( combinator b= simpleSelector )*
                pass 
                self._state.following.append(self.FOLLOW_simpleSelector_in_selector727)
                a = self.simpleSelector()

                self._state.following.pop()
                #action start
                gencode =  a 
                #action end
                # treelesscss.g:224:2: ( combinator b= simpleSelector )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == N_Attrib or LA15_0 == N_Pseudo or LA15_0 == IDENT or (PLUS <= LA15_0 <= HASH) or LA15_0 == STAR) :
                        alt15 = 1


                    if alt15 == 1:
                        # treelesscss.g:225:3: combinator b= simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector736)
                        combinator18 = self.combinator()

                        self._state.following.pop()
                        #action start
                        gencode += combinator18; 
                        #action end
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector744)
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
                        break #loop15




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "selector"


    # $ANTLR start "combinator"
    # treelesscss.g:238:1: combinator returns [gencode] : ( PLUS | GREATER | );
    def combinator(self, ):

        gencode = None

        PLUS19 = None
        GREATER20 = None

        try:
            try:
                # treelesscss.g:239:2: ( PLUS | GREATER | )
                alt16 = 3
                LA16 = self.input.LA(1)
                if LA16 == PLUS:
                    alt16 = 1
                elif LA16 == GREATER:
                    alt16 = 2
                elif LA16 == N_Attrib or LA16 == N_Pseudo or LA16 == IDENT or LA16 == HASH or LA16 == STAR:
                    alt16 = 3
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # treelesscss.g:239:4: PLUS
                    pass 
                    PLUS19=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator769)
                    #action start
                    gencode =  PLUS19.text 
                    #action end


                elif alt16 == 2:
                    # treelesscss.g:240:4: GREATER
                    pass 
                    GREATER20=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator778)
                    #action start
                    gencode =  GREATER20.text 
                    #action end


                elif alt16 == 3:
                    # treelesscss.g:241:6: 
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
    # treelesscss.g:244:1: simpleSelector returns [gencode] : ( IDENT | STAR | HASH | pseudo | attrib );
    def simpleSelector(self, ):

        gencode = None

        IDENT21 = None
        STAR22 = None
        HASH23 = None
        pseudo24 = None

        attrib25 = None


        try:
            try:
                # treelesscss.g:245:2: ( IDENT | STAR | HASH | pseudo | attrib )
                alt17 = 5
                LA17 = self.input.LA(1)
                if LA17 == IDENT:
                    alt17 = 1
                elif LA17 == STAR:
                    alt17 = 2
                elif LA17 == HASH:
                    alt17 = 3
                elif LA17 == N_Pseudo:
                    alt17 = 4
                elif LA17 == N_Attrib:
                    alt17 = 5
                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae

                if alt17 == 1:
                    # treelesscss.g:245:4: IDENT
                    pass 
                    IDENT21=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_simpleSelector803)
                    #action start
                    gencode =  IDENT21.text 
                    #action end


                elif alt17 == 2:
                    # treelesscss.g:246:4: STAR
                    pass 
                    STAR22=self.match(self.input, STAR, self.FOLLOW_STAR_in_simpleSelector812)
                    #action start
                    gencode =  STAR22.text 
                    #action end


                elif alt17 == 3:
                    # treelesscss.g:247:4: HASH
                    pass 
                    HASH23=self.match(self.input, HASH, self.FOLLOW_HASH_in_simpleSelector821)
                    #action start
                    gencode =  HASH23.text 
                    #action end


                elif alt17 == 4:
                    # treelesscss.g:248:4: pseudo
                    pass 
                    self._state.following.append(self.FOLLOW_pseudo_in_simpleSelector830)
                    pseudo24 = self.pseudo()

                    self._state.following.pop()
                    #action start
                    gencode =  pseudo24 
                    #action end


                elif alt17 == 5:
                    # treelesscss.g:249:4: attrib
                    pass 
                    self._state.following.append(self.FOLLOW_attrib_in_simpleSelector838)
                    attrib25 = self.attrib()

                    self._state.following.pop()
                    #action start
                    gencode =  attrib25 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "simpleSelector"


    # $ANTLR start "pseudo"
    # treelesscss.g:252:1: pseudo returns [gencode] : ^( N_Pseudo a= COLON (b= COLON )? IDENT ) ;
    def pseudo(self, ):

        gencode = None

        a = None
        b = None
        IDENT26 = None

        try:
            try:
                # treelesscss.g:253:2: ( ^( N_Pseudo a= COLON (b= COLON )? IDENT ) )
                # treelesscss.g:253:4: ^( N_Pseudo a= COLON (b= COLON )? IDENT )
                pass 
                self.match(self.input, N_Pseudo, self.FOLLOW_N_Pseudo_in_pseudo857)

                self.match(self.input, DOWN, None)
                a=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo863)
                #action start
                gencode =  a.text 
                #action end
                # treelesscss.g:255:3: (b= COLON )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == COLON) :
                    alt18 = 1
                if alt18 == 1:
                    # treelesscss.g:256:5: b= COLON
                    pass 
                    b=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo878)
                    #action start
                    gencode += b.text; 
                    #action end



                IDENT26=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo890)
                #action start
                gencode += IDENT26.text; 
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "pseudo"


    # $ANTLR start "attrib"
    # treelesscss.g:264:1: attrib returns [gencode] : ^( N_Attrib attribBody ) ;
    def attrib(self, ):

        gencode = None

        attribBody27 = None


        try:
            try:
                # treelesscss.g:265:2: ( ^( N_Attrib attribBody ) )
                # treelesscss.g:265:4: ^( N_Attrib attribBody )
                pass 
                self.match(self.input, N_Attrib, self.FOLLOW_N_Attrib_in_attrib914)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attribBody_in_attrib918)
                attribBody27 = self.attribBody()

                self._state.following.pop()
                #action start
                gencode =  '[' + attribBody27 + ']'  
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "attrib"


    # $ANTLR start "attribBody"
    # treelesscss.g:269:1: attribBody returns [gencode] : ( IDENT | ^( attribOper IDENT term ) );
    def attribBody(self, ):

        gencode = None

        IDENT28 = None
        IDENT29 = None
        attribOper30 = None

        term31 = None


        try:
            try:
                # treelesscss.g:270:2: ( IDENT | ^( attribOper IDENT term ) )
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == IDENT) :
                    alt19 = 1
                elif ((OPEQ <= LA19_0 <= SUBSTRINGMATCH)) :
                    alt19 = 2
                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # treelesscss.g:270:4: IDENT
                    pass 
                    IDENT28=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody936)
                    #action start
                    gencode =  IDENT28.text 
                    #action end


                elif alt19 == 2:
                    # treelesscss.g:271:4: ^( attribOper IDENT term )
                    pass 
                    self._state.following.append(self.FOLLOW_attribOper_in_attribBody946)
                    attribOper30 = self.attribOper()

                    self._state.following.pop()

                    self.match(self.input, DOWN, None)
                    IDENT29=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody950)
                    self._state.following.append(self.FOLLOW_term_in_attribBody954)
                    term31 = self.term()

                    self._state.following.pop()
                    #action start
                    gencode =  IDENT29.text + ((attribOper30 is not None) and [self.input.getTokenStream().toString(
                        self.input.getTreeAdaptor().getTokenStartIndex(attribOper30.start),
                        self.input.getTreeAdaptor().getTokenStopIndex(attribOper30.start)
                        )] or [None])[0] + term31 
                    #action end

                    self.match(self.input, UP, None)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "attribBody"

    class attribOper_return(TreeRuleReturnScope):
        def __init__(self):
            super(treelesscss.attribOper_return, self).__init__()





    # $ANTLR start "attribOper"
    # treelesscss.g:276:10: fragment attribOper : ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH );
    def attribOper(self, ):

        retval = self.attribOper_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:277:2: ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH )
                # treelesscss.g:
                pass 
                if (OPEQ <= self.input.LA(1) <= SUBSTRINGMATCH):
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

    # $ANTLR end "attribOper"


    # $ANTLR start "declarationset"
    # treelesscss.g:288:1: declarationset : ( N_Empty | ( declaration )+ );
    def declarationset(self, ):

        try:
            try:
                # treelesscss.g:289:2: ( N_Empty | ( declaration )+ )
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == N_Empty) :
                    alt21 = 1
                elif (LA21_0 == N_Declaration) :
                    alt21 = 2
                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # treelesscss.g:289:4: N_Empty
                    pass 
                    self.match(self.input, N_Empty, self.FOLLOW_N_Empty_in_declarationset1011)


                elif alt21 == 2:
                    # treelesscss.g:290:4: ( declaration )+
                    pass 
                    # treelesscss.g:290:4: ( declaration )+
                    cnt20 = 0
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == N_Declaration) :
                            alt20 = 1


                        if alt20 == 1:
                            # treelesscss.g:290:4: declaration
                            pass 
                            self._state.following.append(self.FOLLOW_declaration_in_declarationset1016)
                            self.declaration()

                            self._state.following.pop()


                        else:
                            if cnt20 >= 1:
                                break #loop20

                            eee = EarlyExitException(20, self.input)
                            raise eee

                        cnt20 += 1



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "declarationset"


    # $ANTLR start "declaration"
    # treelesscss.g:294:1: declaration : ^( N_Declaration property ( expr )? ( prio )? ) ;
    def declaration(self, ):

        property32 = None

        expr33 = None


        try:
            try:
                # treelesscss.g:295:2: ( ^( N_Declaration property ( expr )? ( prio )? ) )
                # treelesscss.g:295:4: ^( N_Declaration property ( expr )? ( prio )? )
                pass 
                self.match(self.input, N_Declaration, self.FOLLOW_N_Declaration_in_declaration1030)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_property_in_declaration1034)
                property32 = self.property()

                self._state.following.pop()
                #action start
                propout = ((property32 is not None) and [self.input.getTokenStream().toString(
                    self.input.getTreeAdaptor().getTokenStartIndex(property32.start),
                    self.input.getTreeAdaptor().getTokenStopIndex(property32.start)
                    )] or [None])[0] +  ":"; 
                #action end
                # treelesscss.g:297:3: ( expr )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == N_Space or LA22_0 == N_Term or LA22_0 == STRING or LA22_0 == URI or (COMMA <= LA22_0 <= IDENT) or LA22_0 == HASH or LA22_0 == SOLIDUS or LA22_0 == UNICODE_RANGE) :
                    alt22 = 1
                if alt22 == 1:
                    # treelesscss.g:298:5: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_declaration1047)
                    expr33 = self.expr()

                    self._state.following.pop()
                    #action start
                    propout += expr33
                    #action end



                # treelesscss.g:300:3: ( prio )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == IMPORTANT_SYM) :
                    alt23 = 1
                if alt23 == 1:
                    # treelesscss.g:301:5: prio
                    pass 
                    self._state.following.append(self.FOLLOW_prio_in_declaration1065)
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

    class property_return(TreeRuleReturnScope):
        def __init__(self):
            super(treelesscss.property_return, self).__init__()





    # $ANTLR start "property"
    # treelesscss.g:309:1: property : IDENT ;
    def property(self, ):

        retval = self.property_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:310:2: ( IDENT )
                # treelesscss.g:310:4: IDENT
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property1091)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "property"


    # $ANTLR start "prio"
    # treelesscss.g:313:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        try:
            try:
                # treelesscss.g:314:2: ( IMPORTANT_SYM )
                # treelesscss.g:314:4: IMPORTANT_SYM
                pass 
                self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1102)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "prio"


    # $ANTLR start "expr"
    # treelesscss.g:318:1: expr returns [gencode] : ( ^( operator a= expr b= expr ) | term );
    def expr(self, ):

        gencode = None

        a = None

        b = None

        operator34 = None

        term35 = None


        try:
            try:
                # treelesscss.g:319:2: ( ^( operator a= expr b= expr ) | term )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == N_Space or LA24_0 == COMMA or LA24_0 == SOLIDUS) :
                    alt24 = 1
                elif (LA24_0 == N_Term or LA24_0 == STRING or LA24_0 == URI or LA24_0 == IDENT or LA24_0 == HASH or LA24_0 == UNICODE_RANGE) :
                    alt24 = 2
                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # treelesscss.g:319:4: ^( operator a= expr b= expr )
                    pass 
                    self._state.following.append(self.FOLLOW_operator_in_expr1120)
                    operator34 = self.operator()

                    self._state.following.pop()

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr1126)
                    a = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr1132)
                    b = self.expr()

                    self._state.following.pop()
                    #action start
                    gencode =  a + operator34 + b 
                    #action end

                    self.match(self.input, UP, None)


                elif alt24 == 2:
                    # treelesscss.g:323:4: term
                    pass 
                    self._state.following.append(self.FOLLOW_term_in_expr1144)
                    term35 = self.term()

                    self._state.following.pop()
                    #action start
                    gencode =  term35 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "expr"


    # $ANTLR start "operator"
    # treelesscss.g:326:10: fragment operator returns [gencode] : ( SOLIDUS | COMMA | N_Space );
    def operator(self, ):

        gencode = None

        SOLIDUS36 = None
        COMMA37 = None

        try:
            try:
                # treelesscss.g:327:2: ( SOLIDUS | COMMA | N_Space )
                alt25 = 3
                LA25 = self.input.LA(1)
                if LA25 == SOLIDUS:
                    alt25 = 1
                elif LA25 == COMMA:
                    alt25 = 2
                elif LA25 == N_Space:
                    alt25 = 3
                else:
                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # treelesscss.g:327:4: SOLIDUS
                    pass 
                    SOLIDUS36=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator1165)
                    #action start
                    gencode =  SOLIDUS36.text 
                    #action end


                elif alt25 == 2:
                    # treelesscss.g:328:4: COMMA
                    pass 
                    COMMA37=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator1174)
                    #action start
                    gencode =  COMMA37.text 
                    #action end


                elif alt25 == 3:
                    # treelesscss.g:329:4: N_Space
                    pass 
                    self.match(self.input, N_Space, self.FOLLOW_N_Space_in_operator1183)
                    #action start
                    gencode =  ' ' 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "operator"


    # $ANTLR start "term"
    # treelesscss.g:332:1: term returns [gencode] : ( ^( N_Term unaryOperator termnum ) | ^( N_Term termnum ) | STRING | IDENT | URI | hexColor | UNICODE_RANGE );
    def term(self, ):

        gencode = None

        STRING41 = None
        IDENT42 = None
        URI43 = None
        UNICODE_RANGE45 = None
        unaryOperator38 = None

        termnum39 = None

        termnum40 = None

        hexColor44 = None


        try:
            try:
                # treelesscss.g:333:2: ( ^( N_Term unaryOperator termnum ) | ^( N_Term termnum ) | STRING | IDENT | URI | hexColor | UNICODE_RANGE )
                alt26 = 7
                alt26 = self.dfa26.predict(self.input)
                if alt26 == 1:
                    # treelesscss.g:333:4: ^( N_Term unaryOperator termnum )
                    pass 
                    self.match(self.input, N_Term, self.FOLLOW_N_Term_in_term1202)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_unaryOperator_in_term1206)
                    unaryOperator38 = self.unaryOperator()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_termnum_in_term1210)
                    termnum39 = self.termnum()

                    self._state.following.pop()
                    #action start
                    gencode =  ((unaryOperator38 is not None) and [self.input.getTokenStream().toString(
                        self.input.getTreeAdaptor().getTokenStartIndex(unaryOperator38.start),
                        self.input.getTreeAdaptor().getTokenStopIndex(unaryOperator38.start)
                        )] or [None])[0] + termnum39 
                    #action end

                    self.match(self.input, UP, None)


                elif alt26 == 2:
                    # treelesscss.g:337:4: ^( N_Term termnum )
                    pass 
                    self.match(self.input, N_Term, self.FOLLOW_N_Term_in_term1224)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_termnum_in_term1228)
                    termnum40 = self.termnum()

                    self._state.following.pop()
                    #action start
                    gencode =  termnum40 
                    #action end

                    self.match(self.input, UP, None)


                elif alt26 == 3:
                    # treelesscss.g:340:4: STRING
                    pass 
                    STRING41=self.match(self.input, STRING, self.FOLLOW_STRING_in_term1242)
                    #action start
                    gencode =  STRING41.text 
                    #action end


                elif alt26 == 4:
                    # treelesscss.g:341:4: IDENT
                    pass 
                    IDENT42=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term1250)
                    #action start
                    gencode =  IDENT42.text 
                    #action end


                elif alt26 == 5:
                    # treelesscss.g:342:4: URI
                    pass 
                    URI43=self.match(self.input, URI, self.FOLLOW_URI_in_term1259)
                    #action start
                    gencode =  URI43.text 
                    #action end


                elif alt26 == 6:
                    # treelesscss.g:343:4: hexColor
                    pass 
                    self._state.following.append(self.FOLLOW_hexColor_in_term1268)
                    hexColor44 = self.hexColor()

                    self._state.following.pop()
                    #action start
                    gencode =  ((hexColor44 is not None) and [self.input.getTokenStream().toString(
                        self.input.getTreeAdaptor().getTokenStartIndex(hexColor44.start),
                        self.input.getTreeAdaptor().getTokenStopIndex(hexColor44.start)
                        )] or [None])[0] 
                    #action end


                elif alt26 == 7:
                    # treelesscss.g:344:4: UNICODE_RANGE
                    pass 
                    UNICODE_RANGE45=self.match(self.input, UNICODE_RANGE, self.FOLLOW_UNICODE_RANGE_in_term1276)
                    #action start
                    gencode =  UNICODE_RANGE45.text 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "term"


    # $ANTLR start "termnum"
    # treelesscss.g:347:10: fragment termnum returns [gencode] : ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH | function );
    def termnum(self, ):

        gencode = None

        NUMBER46 = None
        PERCENTAGE47 = None
        LENGTH48 = None
        EMS49 = None
        EXS50 = None
        REMS51 = None
        CHS52 = None
        ANGLE53 = None
        TIME54 = None
        FREQ55 = None
        RESOLUTION56 = None
        VPORTLEN57 = None
        NTH58 = None
        function59 = None


        try:
            try:
                # treelesscss.g:348:2: ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH | function )
                alt27 = 14
                LA27 = self.input.LA(1)
                if LA27 == NUMBER:
                    alt27 = 1
                elif LA27 == PERCENTAGE:
                    alt27 = 2
                elif LA27 == LENGTH:
                    alt27 = 3
                elif LA27 == EMS:
                    alt27 = 4
                elif LA27 == EXS:
                    alt27 = 5
                elif LA27 == REMS:
                    alt27 = 6
                elif LA27 == CHS:
                    alt27 = 7
                elif LA27 == ANGLE:
                    alt27 = 8
                elif LA27 == TIME:
                    alt27 = 9
                elif LA27 == FREQ:
                    alt27 = 10
                elif LA27 == RESOLUTION:
                    alt27 = 11
                elif LA27 == VPORTLEN:
                    alt27 = 12
                elif LA27 == NTH:
                    alt27 = 13
                elif LA27 == N_Function:
                    alt27 = 14
                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae

                if alt27 == 1:
                    # treelesscss.g:348:4: NUMBER
                    pass 
                    NUMBER46=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_termnum1296)
                    #action start
                    gencode =  NUMBER46.text.strip() 
                    #action end


                elif alt27 == 2:
                    # treelesscss.g:349:4: PERCENTAGE
                    pass 
                    PERCENTAGE47=self.match(self.input, PERCENTAGE, self.FOLLOW_PERCENTAGE_in_termnum1304)
                    #action start
                    gencode =  PERCENTAGE47.text.strip() 
                    #action end


                elif alt27 == 3:
                    # treelesscss.g:350:4: LENGTH
                    pass 
                    LENGTH48=self.match(self.input, LENGTH, self.FOLLOW_LENGTH_in_termnum1312)
                    #action start
                    gencode =  LENGTH48.text.strip() 
                    #action end


                elif alt27 == 4:
                    # treelesscss.g:351:4: EMS
                    pass 
                    EMS49=self.match(self.input, EMS, self.FOLLOW_EMS_in_termnum1320)
                    #action start
                    gencode =  EMS49.text.strip() 
                    #action end


                elif alt27 == 5:
                    # treelesscss.g:352:4: EXS
                    pass 
                    EXS50=self.match(self.input, EXS, self.FOLLOW_EXS_in_termnum1329)
                    #action start
                    gencode =  EXS50.text.strip() 
                    #action end


                elif alt27 == 6:
                    # treelesscss.g:353:4: REMS
                    pass 
                    REMS51=self.match(self.input, REMS, self.FOLLOW_REMS_in_termnum1338)
                    #action start
                    gencode =  REMS51.text.strip() 
                    #action end


                elif alt27 == 7:
                    # treelesscss.g:354:4: CHS
                    pass 
                    CHS52=self.match(self.input, CHS, self.FOLLOW_CHS_in_termnum1347)
                    #action start
                    gencode =  CHS52.text.strip() 
                    #action end


                elif alt27 == 8:
                    # treelesscss.g:355:4: ANGLE
                    pass 
                    ANGLE53=self.match(self.input, ANGLE, self.FOLLOW_ANGLE_in_termnum1356)
                    #action start
                    gencode =  ANGLE53.text.strip() 
                    #action end


                elif alt27 == 9:
                    # treelesscss.g:356:4: TIME
                    pass 
                    TIME54=self.match(self.input, TIME, self.FOLLOW_TIME_in_termnum1365)
                    #action start
                    gencode =  TIME54.text.strip() 
                    #action end


                elif alt27 == 10:
                    # treelesscss.g:357:4: FREQ
                    pass 
                    FREQ55=self.match(self.input, FREQ, self.FOLLOW_FREQ_in_termnum1374)
                    #action start
                    gencode =  FREQ55.text.strip() 
                    #action end


                elif alt27 == 11:
                    # treelesscss.g:358:4: RESOLUTION
                    pass 
                    RESOLUTION56=self.match(self.input, RESOLUTION, self.FOLLOW_RESOLUTION_in_termnum1383)
                    #action start
                    gencode =  RESOLUTION56.text.strip() 
                    #action end


                elif alt27 == 12:
                    # treelesscss.g:359:4: VPORTLEN
                    pass 
                    VPORTLEN57=self.match(self.input, VPORTLEN, self.FOLLOW_VPORTLEN_in_termnum1391)
                    #action start
                    gencode =  VPORTLEN57.text.strip() 
                    #action end


                elif alt27 == 13:
                    # treelesscss.g:360:4: NTH
                    pass 
                    NTH58=self.match(self.input, NTH, self.FOLLOW_NTH_in_termnum1399)
                    #action start
                    gencode =  NTH58.text.strip() 
                    #action end


                elif alt27 == 14:
                    # treelesscss.g:361:4: function
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_termnum1408)
                    function59 = self.function()

                    self._state.following.pop()
                    #action start
                    gencode =  function59 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "termnum"

    class unaryOperator_return(TreeRuleReturnScope):
        def __init__(self):
            super(treelesscss.unaryOperator_return, self).__init__()





    # $ANTLR start "unaryOperator"
    # treelesscss.g:365:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        retval = self.unaryOperator_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:366:2: ( MINUS | PLUS )
                # treelesscss.g:
                pass 
                if self.input.LA(1) == PLUS or self.input.LA(1) == MINUS:
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

    # $ANTLR end "unaryOperator"


    # $ANTLR start "function"
    # treelesscss.g:371:1: function returns [gencode] : ^( N_Function fnct_name fnct_args ) ;
    def function(self, ):

        gencode = None

        fnct_name60 = None

        fnct_args61 = None


        try:
            try:
                # treelesscss.g:372:2: ( ^( N_Function fnct_name fnct_args ) )
                # treelesscss.g:372:4: ^( N_Function fnct_name fnct_args )
                pass 
                self.match(self.input, N_Function, self.FOLLOW_N_Function_in_function1446)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_fnct_name_in_function1450)
                fnct_name60 = self.fnct_name()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_fnct_args_in_function1454)
                fnct_args61 = self.fnct_args()

                self._state.following.pop()
                #action start
                gencode =  fnct_name60 + fnct_args61 + ')' 
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "function"


    # $ANTLR start "fnct_name"
    # treelesscss.g:377:1: fnct_name returns [gencode] : ^( FUNCTION ( IDENT | COLON | DOT )* ) ;
    def fnct_name(self, ):

        gencode = None

        IDENT62 = None
        COLON63 = None
        DOT64 = None
        FUNCTION65 = None

        try:
            try:
                # treelesscss.g:378:2: ( ^( FUNCTION ( IDENT | COLON | DOT )* ) )
                # treelesscss.g:378:4: ^( FUNCTION ( IDENT | COLON | DOT )* )
                pass 
                FUNCTION65=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name1473)

                #action start
                prefix = list(); 
                #action end

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # treelesscss.g:379:3: ( IDENT | COLON | DOT )*
                    while True: #loop28
                        alt28 = 4
                        LA28 = self.input.LA(1)
                        if LA28 == IDENT:
                            alt28 = 1
                        elif LA28 == COLON:
                            alt28 = 2
                        elif LA28 == DOT:
                            alt28 = 3

                        if alt28 == 1:
                            # treelesscss.g:379:5: IDENT
                            pass 
                            IDENT62=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name1482)
                            #action start
                            prefix.append(IDENT62.text); 
                            #action end


                        elif alt28 == 2:
                            # treelesscss.g:380:5: COLON
                            pass 
                            COLON63=self.match(self.input, COLON, self.FOLLOW_COLON_in_fnct_name1491)
                            #action start
                            prefix.append(COLON63.text); 
                            #action end


                        elif alt28 == 3:
                            # treelesscss.g:381:5: DOT
                            pass 
                            DOT64=self.match(self.input, DOT, self.FOLLOW_DOT_in_fnct_name1500)
                            #action start
                            prefix.append(DOT64.text); 
                            #action end


                        else:
                            break #loop28

                    self.match(self.input, UP, None)

                #action start
                gencode =  ''.join(prefix) + FUNCTION65.text 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "fnct_name"


    # $ANTLR start "fnct_args"
    # treelesscss.g:386:10: fragment fnct_args returns [gencode] : ( ^( COMMA a= fnct_args b= fnct_args ) | ^( OPEQ IDENT expr ) | term );
    def fnct_args(self, ):

        gencode = None

        COMMA66 = None
        IDENT67 = None
        OPEQ68 = None
        a = None

        b = None

        expr69 = None

        term70 = None


        try:
            try:
                # treelesscss.g:387:2: ( ^( COMMA a= fnct_args b= fnct_args ) | ^( OPEQ IDENT expr ) | term )
                alt29 = 3
                LA29 = self.input.LA(1)
                if LA29 == COMMA:
                    alt29 = 1
                elif LA29 == OPEQ:
                    alt29 = 2
                elif LA29 == N_Term or LA29 == STRING or LA29 == URI or LA29 == IDENT or LA29 == HASH or LA29 == UNICODE_RANGE:
                    alt29 = 3
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # treelesscss.g:387:4: ^( COMMA a= fnct_args b= fnct_args )
                    pass 
                    COMMA66=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args1534)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_fnct_args_in_fnct_args1540)
                    a = self.fnct_args()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_fnct_args_in_fnct_args1546)
                    b = self.fnct_args()

                    self._state.following.pop()
                    #action start
                    gencode =  a + COMMA66.text + b  
                    #action end

                    self.match(self.input, UP, None)


                elif alt29 == 2:
                    # treelesscss.g:391:4: ^( OPEQ IDENT expr )
                    pass 
                    OPEQ68=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_args1557)

                    self.match(self.input, DOWN, None)
                    IDENT67=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_args1561)
                    self._state.following.append(self.FOLLOW_expr_in_fnct_args1565)
                    expr69 = self.expr()

                    self._state.following.pop()
                    #action start
                    gencode =  IDENT67.text + OPEQ68.text + expr69  
                    #action end

                    self.match(self.input, UP, None)


                elif alt29 == 3:
                    # treelesscss.g:395:4: term
                    pass 
                    self._state.following.append(self.FOLLOW_term_in_fnct_args1577)
                    term70 = self.term()

                    self._state.following.pop()
                    #action start
                    gencode =  term70  
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "fnct_args"

    class hexColor_return(TreeRuleReturnScope):
        def __init__(self):
            super(treelesscss.hexColor_return, self).__init__()





    # $ANTLR start "hexColor"
    # treelesscss.g:399:1: hexColor : HASH ;
    def hexColor(self, ):

        retval = self.hexColor_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:400:2: ( HASH )
                # treelesscss.g:400:4: HASH
                pass 
                self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor1594)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "hexColor"


    # Delegated rules


    # lookup tables for DFA #26

    DFA26_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA26_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA26_min = DFA.unpack(
        u"\1\22\1\2\5\uffff\1\14\2\uffff"
        )

    DFA26_max = DFA.unpack(
        u"\1\100\1\2\5\uffff\1\101\2\uffff"
        )

    DFA26_accept = DFA.unpack(
        u"\2\uffff\1\3\1\4\1\5\1\6\1\7\1\uffff\1\1\1\2"
        )

    DFA26_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA26_transition = [
        DFA.unpack(u"\1\1\1\uffff\1\2\2\uffff\1\4\4\uffff\1\3\11\uffff\1"
        u"\5\31\uffff\1\6"),
        DFA.unpack(u"\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\11\26\uffff\1\11\1\10\17\uffff\14\11\1\uffff\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #26

    class DFA26(DFA):
        pass


 

    FOLLOW_N_StyleSheet_in_styleSheet51 = frozenset([2])
    FOLLOW_charSet_in_styleSheet61 = frozenset([3, 7, 22, 24, 32, 33, 34])
    FOLLOW_imports_in_styleSheet79 = frozenset([3, 7, 22, 24, 32, 33, 34])
    FOLLOW_body_in_styleSheet91 = frozenset([3, 7, 24, 32, 33, 34])
    FOLLOW_CHARSET_SYM_in_charSet115 = frozenset([2])
    FOLLOW_STRING_in_charSet117 = frozenset([3])
    FOLLOW_IMPORT_SYM_in_imports144 = frozenset([2])
    FOLLOW_importUrl_in_imports152 = frozenset([3, 5])
    FOLLOW_media_query_in_imports164 = frozenset([3, 5])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_ruleSet_in_body210 = frozenset([1])
    FOLLOW_media_in_body216 = frozenset([1])
    FOLLOW_page_in_body223 = frozenset([1])
    FOLLOW_fontface_in_body230 = frozenset([1])
    FOLLOW_keyframes_in_body236 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media254 = frozenset([2])
    FOLLOW_media_query_in_media267 = frozenset([3, 5, 7, 24, 32, 33, 34])
    FOLLOW_body_in_media286 = frozenset([3, 7, 24, 32, 33, 34])
    FOLLOW_N_MediaQuery_in_media_query314 = frozenset([2])
    FOLLOW_media_stmt_in_media_query326 = frozenset([3, 6, 28])
    FOLLOW_media_expr_in_media_query334 = frozenset([3, 6, 28])
    FOLLOW_IDENT_in_media_stmt360 = frozenset([1])
    FOLLOW_N_MediaExpr_in_media_expr376 = frozenset([2])
    FOLLOW_media_stmt_in_media_expr383 = frozenset([3, 15, 18, 20, 23, 27, 28, 38, 51, 64])
    FOLLOW_expr_in_media_expr396 = frozenset([3])
    FOLLOW_FONTFACE_SYM_in_fontface428 = frozenset([2])
    FOLLOW_declarationset_in_fontface438 = frozenset([3])
    FOLLOW_PAGE_SYM_in_page460 = frozenset([2])
    FOLLOW_pseudoPage_in_page474 = frozenset([11, 14])
    FOLLOW_declarationset_in_page491 = frozenset([3])
    FOLLOW_IDENT_in_pseudoPage509 = frozenset([1])
    FOLLOW_KEYFRAMES_SYM_in_keyframes525 = frozenset([2])
    FOLLOW_IDENT_in_keyframes527 = frozenset([3, 8])
    FOLLOW_keyframes_block_in_keyframes537 = frozenset([3, 8])
    FOLLOW_N_KeyframeBlock_in_keyframes_block557 = frozenset([2])
    FOLLOW_keyframe_selector_in_keyframes_block566 = frozenset([9, 11, 14])
    FOLLOW_declarationset_in_keyframes_block589 = frozenset([3])
    FOLLOW_M_KeyframeSelector_in_keyframe_selector612 = frozenset([2])
    FOLLOW_IDENT_in_keyframe_selector618 = frozenset([3])
    FOLLOW_PERCENTAGE_in_keyframe_selector627 = frozenset([3])
    FOLLOW_N_RuleSet_in_ruleSet651 = frozenset([2])
    FOLLOW_selector_list_in_ruleSet663 = frozenset([10, 11, 14])
    FOLLOW_declarationset_in_ruleSet681 = frozenset([3])
    FOLLOW_N_Selector_in_selector_list703 = frozenset([2])
    FOLLOW_selector_in_selector_list707 = frozenset([3])
    FOLLOW_simpleSelector_in_selector727 = frozenset([1, 13, 16, 28, 36, 37, 38, 41])
    FOLLOW_combinator_in_selector736 = frozenset([13, 16, 28, 36, 37, 38, 41])
    FOLLOW_simpleSelector_in_selector744 = frozenset([1, 13, 16, 28, 36, 37, 38, 41])
    FOLLOW_PLUS_in_combinator769 = frozenset([1])
    FOLLOW_GREATER_in_combinator778 = frozenset([1])
    FOLLOW_IDENT_in_simpleSelector803 = frozenset([1])
    FOLLOW_STAR_in_simpleSelector812 = frozenset([1])
    FOLLOW_HASH_in_simpleSelector821 = frozenset([1])
    FOLLOW_pseudo_in_simpleSelector830 = frozenset([1])
    FOLLOW_attrib_in_simpleSelector838 = frozenset([1])
    FOLLOW_N_Pseudo_in_pseudo857 = frozenset([2])
    FOLLOW_COLON_in_pseudo863 = frozenset([28, 30])
    FOLLOW_COLON_in_pseudo878 = frozenset([28])
    FOLLOW_IDENT_in_pseudo890 = frozenset([3])
    FOLLOW_N_Attrib_in_attrib914 = frozenset([2])
    FOLLOW_attribBody_in_attrib918 = frozenset([3])
    FOLLOW_IDENT_in_attribBody936 = frozenset([1])
    FOLLOW_attribOper_in_attribBody946 = frozenset([2])
    FOLLOW_IDENT_in_attribBody950 = frozenset([15, 18, 20, 23, 27, 28, 38, 51, 64])
    FOLLOW_term_in_attribBody954 = frozenset([3])
    FOLLOW_set_in_attribOper0 = frozenset([1])
    FOLLOW_N_Empty_in_declarationset1011 = frozenset([1])
    FOLLOW_declaration_in_declarationset1016 = frozenset([1, 11, 14])
    FOLLOW_N_Declaration_in_declaration1030 = frozenset([2])
    FOLLOW_property_in_declaration1034 = frozenset([3, 15, 18, 20, 23, 27, 28, 38, 50, 51, 64])
    FOLLOW_expr_in_declaration1047 = frozenset([3, 50])
    FOLLOW_prio_in_declaration1065 = frozenset([3])
    FOLLOW_IDENT_in_property1091 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1102 = frozenset([1])
    FOLLOW_operator_in_expr1120 = frozenset([2])
    FOLLOW_expr_in_expr1126 = frozenset([15, 18, 20, 23, 27, 28, 38, 51, 64])
    FOLLOW_expr_in_expr1132 = frozenset([3])
    FOLLOW_term_in_expr1144 = frozenset([1])
    FOLLOW_SOLIDUS_in_operator1165 = frozenset([1])
    FOLLOW_COMMA_in_operator1174 = frozenset([1])
    FOLLOW_N_Space_in_operator1183 = frozenset([1])
    FOLLOW_N_Term_in_term1202 = frozenset([2])
    FOLLOW_unaryOperator_in_term1206 = frozenset([12, 35, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_termnum_in_term1210 = frozenset([3])
    FOLLOW_N_Term_in_term1224 = frozenset([2])
    FOLLOW_termnum_in_term1228 = frozenset([3])
    FOLLOW_STRING_in_term1242 = frozenset([1])
    FOLLOW_IDENT_in_term1250 = frozenset([1])
    FOLLOW_URI_in_term1259 = frozenset([1])
    FOLLOW_hexColor_in_term1268 = frozenset([1])
    FOLLOW_UNICODE_RANGE_in_term1276 = frozenset([1])
    FOLLOW_NUMBER_in_termnum1296 = frozenset([1])
    FOLLOW_PERCENTAGE_in_termnum1304 = frozenset([1])
    FOLLOW_LENGTH_in_termnum1312 = frozenset([1])
    FOLLOW_EMS_in_termnum1320 = frozenset([1])
    FOLLOW_EXS_in_termnum1329 = frozenset([1])
    FOLLOW_REMS_in_termnum1338 = frozenset([1])
    FOLLOW_CHS_in_termnum1347 = frozenset([1])
    FOLLOW_ANGLE_in_termnum1356 = frozenset([1])
    FOLLOW_TIME_in_termnum1365 = frozenset([1])
    FOLLOW_FREQ_in_termnum1374 = frozenset([1])
    FOLLOW_RESOLUTION_in_termnum1383 = frozenset([1])
    FOLLOW_VPORTLEN_in_termnum1391 = frozenset([1])
    FOLLOW_NTH_in_termnum1399 = frozenset([1])
    FOLLOW_function_in_termnum1408 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_N_Function_in_function1446 = frozenset([2])
    FOLLOW_fnct_name_in_function1450 = frozenset([15, 18, 20, 23, 27, 28, 38, 44, 51, 64])
    FOLLOW_fnct_args_in_function1454 = frozenset([3])
    FOLLOW_FUNCTION_in_fnct_name1473 = frozenset([2])
    FOLLOW_IDENT_in_fnct_name1482 = frozenset([3, 28, 30, 39])
    FOLLOW_COLON_in_fnct_name1491 = frozenset([3, 28, 30, 39])
    FOLLOW_DOT_in_fnct_name1500 = frozenset([3, 28, 30, 39])
    FOLLOW_COMMA_in_fnct_args1534 = frozenset([2])
    FOLLOW_fnct_args_in_fnct_args1540 = frozenset([15, 18, 20, 23, 27, 28, 38, 44, 51, 64])
    FOLLOW_fnct_args_in_fnct_args1546 = frozenset([3])
    FOLLOW_OPEQ_in_fnct_args1557 = frozenset([2])
    FOLLOW_IDENT_in_fnct_args1561 = frozenset([15, 18, 20, 23, 27, 28, 38, 51, 64])
    FOLLOW_expr_in_fnct_args1565 = frozenset([3])
    FOLLOW_term_in_fnct_args1577 = frozenset([1])
    FOLLOW_HASH_in_hexColor1594 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(treelesscss)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
