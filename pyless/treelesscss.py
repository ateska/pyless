# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 treelesscss.g 2012-12-02 03:15:56

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

        self.dfa25 = self.DFA25(
            self, 25,
            eot = self.DFA25_eot,
            eof = self.DFA25_eof,
            min = self.DFA25_min,
            max = self.DFA25_max,
            accept = self.DFA25_accept,
            special = self.DFA25_special,
            transition = self.DFA25_transition
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

                        if (LA3_0 == N_RuleSet or LA3_0 == MEDIA_SYM or (FONTFACE_SYM <= LA3_0 <= KEYFRAMES_SYM)) :
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
                    self._state.following.append(self.FOLLOW_ruleSet_in_body204)
                    self.ruleSet()

                    self._state.following.pop()


                elif alt5 == 2:
                    # treelesscss.g:61:4: media
                    pass 
                    self._state.following.append(self.FOLLOW_media_in_body210)
                    self.media()

                    self._state.following.pop()


                elif alt5 == 3:
                    # treelesscss.g:62:4: page
                    pass 
                    self._state.following.append(self.FOLLOW_page_in_body217)
                    self.page()

                    self._state.following.pop()


                elif alt5 == 4:
                    # treelesscss.g:63:4: fontface
                    pass 
                    self._state.following.append(self.FOLLOW_fontface_in_body224)
                    self.fontface()

                    self._state.following.pop()


                elif alt5 == 5:
                    # treelesscss.g:64:4: keyframes
                    pass 
                    self._state.following.append(self.FOLLOW_keyframes_in_body230)
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


          
        mqs = []
        	
        try:
            try:
                # treelesscss.g:77:2: ( ^( MEDIA_SYM ( media_query )* ( body )* ) )
                # treelesscss.g:77:4: ^( MEDIA_SYM ( media_query )* ( body )* )
                pass 
                self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media255)

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
                            self._state.following.append(self.FOLLOW_media_query_in_media261)
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

                        if (LA7_0 == N_RuleSet or LA7_0 == MEDIA_SYM or (FONTFACE_SYM <= LA7_0 <= KEYFRAMES_SYM)) :
                            alt7 = 1


                        if alt7 == 1:
                            # treelesscss.g:86:3: body
                            pass 
                            self._state.following.append(self.FOLLOW_body_in_media275)
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
                self.match(self.input, N_MediaQuery, self.FOLLOW_N_MediaQuery_in_media_query310)

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
                        self._state.following.append(self.FOLLOW_media_stmt_in_media_query316)
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
                        self._state.following.append(self.FOLLOW_media_expr_in_media_query324)
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
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_stmt350)




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
                self.match(self.input, N_MediaExpr, self.FOLLOW_N_MediaExpr_in_media_expr362)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_media_stmt_in_media_expr364)
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


    # $ANTLR start "fontface"
    # treelesscss.g:125:1: fontface : ^( FONTFACE_SYM declarationset ) ;
    def fontface(self, ):

        try:
            try:
                # treelesscss.g:126:2: ( ^( FONTFACE_SYM declarationset ) )
                # treelesscss.g:126:4: ^( FONTFACE_SYM declarationset )
                pass 
                self.match(self.input, FONTFACE_SYM, self.FOLLOW_FONTFACE_SYM_in_fontface384)

                #action start
                   
                self.output('@fontface' + self.EOLLBRACKET);
                self.indent_level += 1;
                		
                #action end

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_declarationset_in_fontface392)
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
    # treelesscss.g:142:1: page : ^( PAGE_SYM ( pseudoPage )? declarationset ) ;
    def page(self, ):

        pseudoPage9 = None


        try:
            try:
                # treelesscss.g:143:2: ( ^( PAGE_SYM ( pseudoPage )? declarationset ) )
                # treelesscss.g:143:4: ^( PAGE_SYM ( pseudoPage )? declarationset )
                pass 
                self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page414)

                #action start
                out = '@page'
                #action end

                self.match(self.input, DOWN, None)
                # treelesscss.g:145:3: ( pseudoPage )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == IDENT) :
                    alt9 = 1
                if alt9 == 1:
                    # treelesscss.g:146:4: pseudoPage
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoPage_in_page427)
                    pseudoPage9 = self.pseudoPage()

                    self._state.following.pop()
                    #action start
                    out += ' ' + ((pseudoPage9 is not None) and [self.input.getTokenStream().toString(
                        self.input.getTreeAdaptor().getTokenStartIndex(pseudoPage9.start),
                        self.input.getTreeAdaptor().getTokenStopIndex(pseudoPage9.start)
                        )] or [None])[0]
                    #action end



                #action start
                   
                self.output(out + self.EOLLBRACKET);
                self.indent_level += 1;
                		
                #action end
                self._state.following.append(self.FOLLOW_declarationset_in_page445)
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
    # treelesscss.g:161:1: pseudoPage : IDENT ;
    def pseudoPage(self, ):

        retval = self.pseudoPage_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:162:2: ( IDENT )
                # treelesscss.g:162:4: IDENT
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage463)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "pseudoPage"


    # $ANTLR start "keyframes"
    # treelesscss.g:169:1: keyframes : ^( KEYFRAMES_SYM IDENT ( keyframes_block )* ) ;
    def keyframes(self, ):

        IDENT10 = None

        try:
            try:
                # treelesscss.g:170:2: ( ^( KEYFRAMES_SYM IDENT ( keyframes_block )* ) )
                # treelesscss.g:170:4: ^( KEYFRAMES_SYM IDENT ( keyframes_block )* )
                pass 
                self.match(self.input, KEYFRAMES_SYM, self.FOLLOW_KEYFRAMES_SYM_in_keyframes479)

                self.match(self.input, DOWN, None)
                IDENT10=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_keyframes481)
                #action start
                   
                self.output('@keyframes ' + IDENT10.text + self.EOLLBRACKET);
                self.indent_level += 1;
                		
                #action end
                # treelesscss.g:175:3: ( keyframes_block )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == N_KeyframeBlock) :
                        alt10 = 1


                    if alt10 == 1:
                        # treelesscss.g:175:3: keyframes_block
                        pass 
                        self._state.following.append(self.FOLLOW_keyframes_block_in_keyframes489)
                        self.keyframes_block()

                        self._state.following.pop()


                    else:
                        break #loop10
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
    # treelesscss.g:183:1: keyframes_block : ^( N_KeyframeBlock ( keyframe_selector )+ declarationset ) ;
    def keyframes_block(self, ):

        keyframe_selector11 = None


        try:
            try:
                # treelesscss.g:184:2: ( ^( N_KeyframeBlock ( keyframe_selector )+ declarationset ) )
                # treelesscss.g:184:4: ^( N_KeyframeBlock ( keyframe_selector )+ declarationset )
                pass 
                self.match(self.input, N_KeyframeBlock, self.FOLLOW_N_KeyframeBlock_in_keyframes_block509)

                #action start
                ks = []; 
                #action end

                self.match(self.input, DOWN, None)
                # treelesscss.g:186:3: ( keyframe_selector )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == M_KeyframeSelector) :
                        alt11 = 1


                    if alt11 == 1:
                        # treelesscss.g:187:4: keyframe_selector
                        pass 
                        self._state.following.append(self.FOLLOW_keyframe_selector_in_keyframes_block522)
                        keyframe_selector11 = self.keyframe_selector()

                        self._state.following.pop()
                        #action start
                        ks.append(keyframe_selector11); 
                        #action end


                    else:
                        if cnt11 >= 1:
                            break #loop11

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1
                #action start
                   
                self.output(' '.join(ks) + self.EOLLBRACKET);
                self.indent_level += 1;
                		
                #action end
                self._state.following.append(self.FOLLOW_declarationset_in_keyframes_block541)
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
    # treelesscss.g:203:1: keyframe_selector returns [gencode] : ^( M_KeyframeSelector ( IDENT | PERCENTAGE ) ) ;
    def keyframe_selector(self, ):

        gencode = None

        IDENT12 = None
        PERCENTAGE13 = None

        try:
            try:
                # treelesscss.g:204:2: ( ^( M_KeyframeSelector ( IDENT | PERCENTAGE ) ) )
                # treelesscss.g:204:4: ^( M_KeyframeSelector ( IDENT | PERCENTAGE ) )
                pass 
                self.match(self.input, M_KeyframeSelector, self.FOLLOW_M_KeyframeSelector_in_keyframe_selector565)

                self.match(self.input, DOWN, None)
                # treelesscss.g:204:25: ( IDENT | PERCENTAGE )
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == IDENT) :
                    alt12 = 1
                elif (LA12_0 == PERCENTAGE) :
                    alt12 = 2
                else:
                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # treelesscss.g:205:5: IDENT
                    pass 
                    IDENT12=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_keyframe_selector574)
                    #action start
                    gencode =  IDENT12.text 
                    #action end


                elif alt12 == 2:
                    # treelesscss.g:206:5: PERCENTAGE
                    pass 
                    PERCENTAGE13=self.match(self.input, PERCENTAGE, self.FOLLOW_PERCENTAGE_in_keyframe_selector583)
                    #action start
                    gencode =  PERCENTAGE13.text 
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
    # treelesscss.g:215:1: ruleSet : ^( N_RuleSet ( selector_list )+ declarationset ) ;
    def ruleSet(self, ):

        selector_list14 = None


          
        sellist = [];
        	
        try:
            try:
                # treelesscss.g:220:2: ( ^( N_RuleSet ( selector_list )+ declarationset ) )
                # treelesscss.g:220:4: ^( N_RuleSet ( selector_list )+ declarationset )
                pass 
                self.match(self.input, N_RuleSet, self.FOLLOW_N_RuleSet_in_ruleSet617)

                self.match(self.input, DOWN, None)
                # treelesscss.g:221:3: ( selector_list )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == N_Selector) :
                        alt13 = 1


                    if alt13 == 1:
                        # treelesscss.g:221:4: selector_list
                        pass 
                        self._state.following.append(self.FOLLOW_selector_list_in_ruleSet622)
                        selector_list14 = self.selector_list()

                        self._state.following.pop()
                        #action start
                        sellist.append(selector_list14); 
                        #action end


                    else:
                        if cnt13 >= 1:
                            break #loop13

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1
                #action start
                   
                self.output(self.LISTCOMA.join(sellist) + self.EOLLBRACKET);
                self.indent_level += 1;
                		
                #action end
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet635)
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
    # treelesscss.g:234:1: selector_list returns [gencode] : ^( N_Selector selector ) ;
    def selector_list(self, ):

        gencode = None

        selector15 = None


        try:
            try:
                # treelesscss.g:234:32: ( ^( N_Selector selector ) )
                # treelesscss.g:235:2: ^( N_Selector selector )
                pass 
                self.match(self.input, N_Selector, self.FOLLOW_N_Selector_in_selector_list658)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_selector_in_selector_list662)
                selector15 = self.selector()

                self._state.following.pop()
                #action start
                gencode =  selector15 
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
    # treelesscss.g:240:1: selector returns [gencode] : a= simpleSelector ( combinator b= simpleSelector )* ;
    def selector(self, ):

        gencode = None

        a = None

        b = None

        combinator16 = None


        try:
            try:
                # treelesscss.g:241:2: (a= simpleSelector ( combinator b= simpleSelector )* )
                # treelesscss.g:241:4: a= simpleSelector ( combinator b= simpleSelector )*
                pass 
                self._state.following.append(self.FOLLOW_simpleSelector_in_selector685)
                a = self.simpleSelector()

                self._state.following.pop()
                #action start
                gencode =  a 
                #action end
                # treelesscss.g:242:2: ( combinator b= simpleSelector )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == N_Attrib or LA14_0 == N_Pseudo or LA14_0 == IDENT or (PLUS <= LA14_0 <= HASH) or LA14_0 == STAR) :
                        alt14 = 1


                    if alt14 == 1:
                        # treelesscss.g:243:3: combinator b= simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector694)
                        combinator16 = self.combinator()

                        self._state.following.pop()
                        #action start
                        gencode += combinator16; 
                        #action end
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector702)
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
                        break #loop14




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "selector"


    # $ANTLR start "combinator"
    # treelesscss.g:255:1: combinator returns [gencode] : ( PLUS | GREATER | );
    def combinator(self, ):

        gencode = None

        PLUS17 = None
        GREATER18 = None

        try:
            try:
                # treelesscss.g:256:2: ( PLUS | GREATER | )
                alt15 = 3
                LA15 = self.input.LA(1)
                if LA15 == PLUS:
                    alt15 = 1
                elif LA15 == GREATER:
                    alt15 = 2
                elif LA15 == N_Attrib or LA15 == N_Pseudo or LA15 == IDENT or LA15 == HASH or LA15 == STAR:
                    alt15 = 3
                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae

                if alt15 == 1:
                    # treelesscss.g:256:4: PLUS
                    pass 
                    PLUS17=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator723)
                    #action start
                    gencode =  PLUS17.text 
                    #action end


                elif alt15 == 2:
                    # treelesscss.g:257:4: GREATER
                    pass 
                    GREATER18=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator732)
                    #action start
                    gencode =  GREATER18.text 
                    #action end


                elif alt15 == 3:
                    # treelesscss.g:258:5: 
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
    # treelesscss.g:261:1: simpleSelector returns [gencode] : ( IDENT | STAR | HASH | pseudo | attrib );
    def simpleSelector(self, ):

        gencode = None

        IDENT19 = None
        STAR20 = None
        HASH21 = None
        pseudo22 = None

        attrib23 = None


        try:
            try:
                # treelesscss.g:262:2: ( IDENT | STAR | HASH | pseudo | attrib )
                alt16 = 5
                LA16 = self.input.LA(1)
                if LA16 == IDENT:
                    alt16 = 1
                elif LA16 == STAR:
                    alt16 = 2
                elif LA16 == HASH:
                    alt16 = 3
                elif LA16 == N_Pseudo:
                    alt16 = 4
                elif LA16 == N_Attrib:
                    alt16 = 5
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # treelesscss.g:262:4: IDENT
                    pass 
                    IDENT19=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_simpleSelector755)
                    #action start
                    gencode =  IDENT19.text 
                    #action end


                elif alt16 == 2:
                    # treelesscss.g:263:4: STAR
                    pass 
                    STAR20=self.match(self.input, STAR, self.FOLLOW_STAR_in_simpleSelector763)
                    #action start
                    gencode =  STAR20.text 
                    #action end


                elif alt16 == 3:
                    # treelesscss.g:264:4: HASH
                    pass 
                    HASH21=self.match(self.input, HASH, self.FOLLOW_HASH_in_simpleSelector771)
                    #action start
                    gencode =  HASH21.text 
                    #action end


                elif alt16 == 4:
                    # treelesscss.g:265:4: pseudo
                    pass 
                    self._state.following.append(self.FOLLOW_pseudo_in_simpleSelector779)
                    pseudo22 = self.pseudo()

                    self._state.following.pop()
                    #action start
                    gencode =  pseudo22 
                    #action end


                elif alt16 == 5:
                    # treelesscss.g:266:4: attrib
                    pass 
                    self._state.following.append(self.FOLLOW_attrib_in_simpleSelector786)
                    attrib23 = self.attrib()

                    self._state.following.pop()
                    #action start
                    gencode =  attrib23 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "simpleSelector"


    # $ANTLR start "pseudo"
    # treelesscss.g:269:1: pseudo returns [gencode] : ^( N_Pseudo a= COLON (b= COLON )? IDENT ) ;
    def pseudo(self, ):

        gencode = None

        a = None
        b = None
        IDENT24 = None

        try:
            try:
                # treelesscss.g:270:2: ( ^( N_Pseudo a= COLON (b= COLON )? IDENT ) )
                # treelesscss.g:270:4: ^( N_Pseudo a= COLON (b= COLON )? IDENT )
                pass 
                self.match(self.input, N_Pseudo, self.FOLLOW_N_Pseudo_in_pseudo804)

                self.match(self.input, DOWN, None)
                a=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo808)
                # treelesscss.g:270:24: (b= COLON )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == COLON) :
                    alt17 = 1
                if alt17 == 1:
                    # treelesscss.g:270:24: b= COLON
                    pass 
                    b=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo812)



                IDENT24=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo815)

                self.match(self.input, UP, None)
                #action start
                gencode =  a.text + (b.text if b is not None else '') + IDENT24.text 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "pseudo"


    # $ANTLR start "attrib"
    # treelesscss.g:276:1: attrib returns [gencode] : ^( N_Attrib attribBody ) ;
    def attrib(self, ):

        gencode = None

        attribBody25 = None


        try:
            try:
                # treelesscss.g:277:2: ( ^( N_Attrib attribBody ) )
                # treelesscss.g:277:4: ^( N_Attrib attribBody )
                pass 
                self.match(self.input, N_Attrib, self.FOLLOW_N_Attrib_in_attrib838)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attribBody_in_attrib840)
                attribBody25 = self.attribBody()

                self._state.following.pop()

                self.match(self.input, UP, None)
                #action start
                gencode =  '[' + attribBody25 + ']'  
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "attrib"


    # $ANTLR start "attribBody"
    # treelesscss.g:281:1: attribBody returns [gencode] : ( IDENT | ^( attribOper IDENT term ) );
    def attribBody(self, ):

        gencode = None

        IDENT26 = None
        IDENT27 = None
        attribOper28 = None

        term29 = None


        try:
            try:
                # treelesscss.g:282:2: ( IDENT | ^( attribOper IDENT term ) )
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == IDENT) :
                    alt18 = 1
                elif ((OPEQ <= LA18_0 <= SUBSTRINGMATCH)) :
                    alt18 = 2
                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae

                if alt18 == 1:
                    # treelesscss.g:282:4: IDENT
                    pass 
                    IDENT26=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody862)
                    #action start
                    gencode =  IDENT26.text 
                    #action end


                elif alt18 == 2:
                    # treelesscss.g:283:4: ^( attribOper IDENT term )
                    pass 
                    self._state.following.append(self.FOLLOW_attribOper_in_attribBody871)
                    attribOper28 = self.attribOper()

                    self._state.following.pop()

                    self.match(self.input, DOWN, None)
                    IDENT27=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody873)
                    self._state.following.append(self.FOLLOW_term_in_attribBody875)
                    term29 = self.term()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    gencode =  IDENT27.text + ((attribOper28 is not None) and [self.input.getTokenStream().toString(
                        self.input.getTreeAdaptor().getTokenStartIndex(attribOper28.start),
                        self.input.getTreeAdaptor().getTokenStopIndex(attribOper28.start)
                        )] or [None])[0] + term29 
                    #action end



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
    # treelesscss.g:287:10: fragment attribOper : ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH );
    def attribOper(self, ):

        retval = self.attribOper_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:288:2: ( OPEQ | INCLUDES | DASHMATCH | PREFIXMATCH | SUFFIXMATCH | SUBSTRINGMATCH )
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
    # treelesscss.g:299:1: declarationset : ( N_Empty | ( declaration )+ );
    def declarationset(self, ):

        try:
            try:
                # treelesscss.g:300:2: ( N_Empty | ( declaration )+ )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == N_Empty) :
                    alt20 = 1
                elif (LA20_0 == N_Declaration) :
                    alt20 = 2
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # treelesscss.g:300:4: N_Empty
                    pass 
                    self.match(self.input, N_Empty, self.FOLLOW_N_Empty_in_declarationset934)


                elif alt20 == 2:
                    # treelesscss.g:301:4: ( declaration )+
                    pass 
                    # treelesscss.g:301:4: ( declaration )+
                    cnt19 = 0
                    while True: #loop19
                        alt19 = 2
                        LA19_0 = self.input.LA(1)

                        if (LA19_0 == N_Declaration) :
                            alt19 = 1


                        if alt19 == 1:
                            # treelesscss.g:301:4: declaration
                            pass 
                            self._state.following.append(self.FOLLOW_declaration_in_declarationset939)
                            self.declaration()

                            self._state.following.pop()


                        else:
                            if cnt19 >= 1:
                                break #loop19

                            eee = EarlyExitException(19, self.input)
                            raise eee

                        cnt19 += 1



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "declarationset"


    # $ANTLR start "declaration"
    # treelesscss.g:305:1: declaration : ^( N_Declaration property ( expr )? ( prio )? ) ;
    def declaration(self, ):

        property30 = None

        expr31 = None


        try:
            try:
                # treelesscss.g:306:2: ( ^( N_Declaration property ( expr )? ( prio )? ) )
                # treelesscss.g:306:4: ^( N_Declaration property ( expr )? ( prio )? )
                pass 
                self.match(self.input, N_Declaration, self.FOLLOW_N_Declaration_in_declaration953)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_property_in_declaration957)
                property30 = self.property()

                self._state.following.pop()
                #action start
                propout = ((property30 is not None) and [self.input.getTokenStream().toString(
                    self.input.getTreeAdaptor().getTokenStartIndex(property30.start),
                    self.input.getTreeAdaptor().getTokenStopIndex(property30.start)
                    )] or [None])[0] +  ":"; 
                #action end
                # treelesscss.g:308:3: ( expr )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == N_Space or LA21_0 == N_Term or LA21_0 == STRING or LA21_0 == URI or (COMMA <= LA21_0 <= IDENT) or LA21_0 == HASH or LA21_0 == SOLIDUS or LA21_0 == UNICODE_RANGE) :
                    alt21 = 1
                if alt21 == 1:
                    # treelesscss.g:308:4: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_declaration964)
                    expr31 = self.expr()

                    self._state.following.pop()
                    #action start
                    propout += expr31
                    #action end



                # treelesscss.g:309:3: ( prio )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == IMPORTANT_SYM) :
                    alt22 = 1
                if alt22 == 1:
                    # treelesscss.g:309:4: prio
                    pass 
                    self._state.following.append(self.FOLLOW_prio_in_declaration974)
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
    # treelesscss.g:317:1: property : IDENT ;
    def property(self, ):

        retval = self.property_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:318:2: ( IDENT )
                # treelesscss.g:318:4: IDENT
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property997)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "property"


    # $ANTLR start "prio"
    # treelesscss.g:321:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        try:
            try:
                # treelesscss.g:322:2: ( IMPORTANT_SYM )
                # treelesscss.g:322:4: IMPORTANT_SYM
                pass 
                self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1008)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "prio"


    # $ANTLR start "expr"
    # treelesscss.g:326:1: expr returns [gencode] : ( ^( operator a= expr b= expr ) | term );
    def expr(self, ):

        gencode = None

        a = None

        b = None

        operator32 = None

        term33 = None


        try:
            try:
                # treelesscss.g:327:2: ( ^( operator a= expr b= expr ) | term )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == N_Space or LA23_0 == COMMA or LA23_0 == SOLIDUS) :
                    alt23 = 1
                elif (LA23_0 == N_Term or LA23_0 == STRING or LA23_0 == URI or LA23_0 == IDENT or LA23_0 == HASH or LA23_0 == UNICODE_RANGE) :
                    alt23 = 2
                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # treelesscss.g:327:4: ^( operator a= expr b= expr )
                    pass 
                    self._state.following.append(self.FOLLOW_operator_in_expr1026)
                    operator32 = self.operator()

                    self._state.following.pop()

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr1032)
                    a = self.expr()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_expr_in_expr1036)
                    b = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    gencode =  a + operator32 + b 
                    #action end


                elif alt23 == 2:
                    # treelesscss.g:330:4: term
                    pass 
                    self._state.following.append(self.FOLLOW_term_in_expr1049)
                    term33 = self.term()

                    self._state.following.pop()
                    #action start
                    gencode =  term33 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "expr"


    # $ANTLR start "operator"
    # treelesscss.g:333:10: fragment operator returns [gencode] : ( SOLIDUS | COMMA | N_Space );
    def operator(self, ):

        gencode = None

        SOLIDUS34 = None
        COMMA35 = None

        try:
            try:
                # treelesscss.g:334:2: ( SOLIDUS | COMMA | N_Space )
                alt24 = 3
                LA24 = self.input.LA(1)
                if LA24 == SOLIDUS:
                    alt24 = 1
                elif LA24 == COMMA:
                    alt24 = 2
                elif LA24 == N_Space:
                    alt24 = 3
                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # treelesscss.g:334:4: SOLIDUS
                    pass 
                    SOLIDUS34=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator1070)
                    #action start
                    gencode =  SOLIDUS34.text 
                    #action end


                elif alt24 == 2:
                    # treelesscss.g:335:4: COMMA
                    pass 
                    COMMA35=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator1079)
                    #action start
                    gencode =  COMMA35.text 
                    #action end


                elif alt24 == 3:
                    # treelesscss.g:336:4: N_Space
                    pass 
                    self.match(self.input, N_Space, self.FOLLOW_N_Space_in_operator1088)
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
    # treelesscss.g:339:1: term returns [gencode] : ( ^( N_Term unaryOperator termnum ) | ^( N_Term termnum ) | STRING | IDENT | URI | hexColor | UNICODE_RANGE );
    def term(self, ):

        gencode = None

        STRING39 = None
        IDENT40 = None
        URI41 = None
        UNICODE_RANGE43 = None
        unaryOperator36 = None

        termnum37 = None

        termnum38 = None

        hexColor42 = None


        try:
            try:
                # treelesscss.g:340:2: ( ^( N_Term unaryOperator termnum ) | ^( N_Term termnum ) | STRING | IDENT | URI | hexColor | UNICODE_RANGE )
                alt25 = 7
                alt25 = self.dfa25.predict(self.input)
                if alt25 == 1:
                    # treelesscss.g:340:4: ^( N_Term unaryOperator termnum )
                    pass 
                    self.match(self.input, N_Term, self.FOLLOW_N_Term_in_term1107)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_unaryOperator_in_term1109)
                    unaryOperator36 = self.unaryOperator()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_termnum_in_term1111)
                    termnum37 = self.termnum()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    gencode =  ((unaryOperator36 is not None) and [self.input.getTokenStream().toString(
                        self.input.getTreeAdaptor().getTokenStartIndex(unaryOperator36.start),
                        self.input.getTreeAdaptor().getTokenStopIndex(unaryOperator36.start)
                        )] or [None])[0] + termnum37 
                    #action end


                elif alt25 == 2:
                    # treelesscss.g:341:4: ^( N_Term termnum )
                    pass 
                    self.match(self.input, N_Term, self.FOLLOW_N_Term_in_term1121)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_termnum_in_term1123)
                    termnum38 = self.termnum()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    gencode =  termnum38 
                    #action end


                elif alt25 == 3:
                    # treelesscss.g:342:4: STRING
                    pass 
                    STRING39=self.match(self.input, STRING, self.FOLLOW_STRING_in_term1133)
                    #action start
                    gencode =  STRING39.text 
                    #action end


                elif alt25 == 4:
                    # treelesscss.g:343:4: IDENT
                    pass 
                    IDENT40=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term1141)
                    #action start
                    gencode =  IDENT40.text 
                    #action end


                elif alt25 == 5:
                    # treelesscss.g:344:4: URI
                    pass 
                    URI41=self.match(self.input, URI, self.FOLLOW_URI_in_term1150)
                    #action start
                    gencode =  URI41.text 
                    #action end


                elif alt25 == 6:
                    # treelesscss.g:345:4: hexColor
                    pass 
                    self._state.following.append(self.FOLLOW_hexColor_in_term1159)
                    hexColor42 = self.hexColor()

                    self._state.following.pop()
                    #action start
                    gencode =  ((hexColor42 is not None) and [self.input.getTokenStream().toString(
                        self.input.getTreeAdaptor().getTokenStartIndex(hexColor42.start),
                        self.input.getTreeAdaptor().getTokenStopIndex(hexColor42.start)
                        )] or [None])[0] 
                    #action end


                elif alt25 == 7:
                    # treelesscss.g:346:4: UNICODE_RANGE
                    pass 
                    UNICODE_RANGE43=self.match(self.input, UNICODE_RANGE, self.FOLLOW_UNICODE_RANGE_in_term1167)
                    #action start
                    gencode =  UNICODE_RANGE43.text 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "term"


    # $ANTLR start "termnum"
    # treelesscss.g:349:10: fragment termnum returns [gencode] : ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH | function );
    def termnum(self, ):

        gencode = None

        NUMBER44 = None
        PERCENTAGE45 = None
        LENGTH46 = None
        EMS47 = None
        EXS48 = None
        REMS49 = None
        CHS50 = None
        ANGLE51 = None
        TIME52 = None
        FREQ53 = None
        RESOLUTION54 = None
        VPORTLEN55 = None
        NTH56 = None
        function57 = None


        try:
            try:
                # treelesscss.g:350:2: ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | REMS | CHS | ANGLE | TIME | FREQ | RESOLUTION | VPORTLEN | NTH | function )
                alt26 = 14
                LA26 = self.input.LA(1)
                if LA26 == NUMBER:
                    alt26 = 1
                elif LA26 == PERCENTAGE:
                    alt26 = 2
                elif LA26 == LENGTH:
                    alt26 = 3
                elif LA26 == EMS:
                    alt26 = 4
                elif LA26 == EXS:
                    alt26 = 5
                elif LA26 == REMS:
                    alt26 = 6
                elif LA26 == CHS:
                    alt26 = 7
                elif LA26 == ANGLE:
                    alt26 = 8
                elif LA26 == TIME:
                    alt26 = 9
                elif LA26 == FREQ:
                    alt26 = 10
                elif LA26 == RESOLUTION:
                    alt26 = 11
                elif LA26 == VPORTLEN:
                    alt26 = 12
                elif LA26 == NTH:
                    alt26 = 13
                elif LA26 == N_Function:
                    alt26 = 14
                else:
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae

                if alt26 == 1:
                    # treelesscss.g:350:4: NUMBER
                    pass 
                    NUMBER44=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_termnum1187)
                    #action start
                    gencode =  NUMBER44.text.strip() 
                    #action end


                elif alt26 == 2:
                    # treelesscss.g:351:4: PERCENTAGE
                    pass 
                    PERCENTAGE45=self.match(self.input, PERCENTAGE, self.FOLLOW_PERCENTAGE_in_termnum1195)
                    #action start
                    gencode =  PERCENTAGE45.text.strip() 
                    #action end


                elif alt26 == 3:
                    # treelesscss.g:352:4: LENGTH
                    pass 
                    LENGTH46=self.match(self.input, LENGTH, self.FOLLOW_LENGTH_in_termnum1203)
                    #action start
                    gencode =  LENGTH46.text.strip() 
                    #action end


                elif alt26 == 4:
                    # treelesscss.g:353:4: EMS
                    pass 
                    EMS47=self.match(self.input, EMS, self.FOLLOW_EMS_in_termnum1211)
                    #action start
                    gencode =  EMS47.text.strip() 
                    #action end


                elif alt26 == 5:
                    # treelesscss.g:354:4: EXS
                    pass 
                    EXS48=self.match(self.input, EXS, self.FOLLOW_EXS_in_termnum1220)
                    #action start
                    gencode =  EXS48.text.strip() 
                    #action end


                elif alt26 == 6:
                    # treelesscss.g:355:4: REMS
                    pass 
                    REMS49=self.match(self.input, REMS, self.FOLLOW_REMS_in_termnum1229)
                    #action start
                    gencode =  REMS49.text.strip() 
                    #action end


                elif alt26 == 7:
                    # treelesscss.g:356:4: CHS
                    pass 
                    CHS50=self.match(self.input, CHS, self.FOLLOW_CHS_in_termnum1238)
                    #action start
                    gencode =  CHS50.text.strip() 
                    #action end


                elif alt26 == 8:
                    # treelesscss.g:357:4: ANGLE
                    pass 
                    ANGLE51=self.match(self.input, ANGLE, self.FOLLOW_ANGLE_in_termnum1247)
                    #action start
                    gencode =  ANGLE51.text.strip() 
                    #action end


                elif alt26 == 9:
                    # treelesscss.g:358:4: TIME
                    pass 
                    TIME52=self.match(self.input, TIME, self.FOLLOW_TIME_in_termnum1256)
                    #action start
                    gencode =  TIME52.text.strip() 
                    #action end


                elif alt26 == 10:
                    # treelesscss.g:359:4: FREQ
                    pass 
                    FREQ53=self.match(self.input, FREQ, self.FOLLOW_FREQ_in_termnum1265)
                    #action start
                    gencode =  FREQ53.text.strip() 
                    #action end


                elif alt26 == 11:
                    # treelesscss.g:360:4: RESOLUTION
                    pass 
                    RESOLUTION54=self.match(self.input, RESOLUTION, self.FOLLOW_RESOLUTION_in_termnum1274)
                    #action start
                    gencode =  RESOLUTION54.text.strip() 
                    #action end


                elif alt26 == 12:
                    # treelesscss.g:361:4: VPORTLEN
                    pass 
                    VPORTLEN55=self.match(self.input, VPORTLEN, self.FOLLOW_VPORTLEN_in_termnum1282)
                    #action start
                    gencode =  VPORTLEN55.text.strip() 
                    #action end


                elif alt26 == 13:
                    # treelesscss.g:362:4: NTH
                    pass 
                    NTH56=self.match(self.input, NTH, self.FOLLOW_NTH_in_termnum1290)
                    #action start
                    gencode =  NTH56.text.strip() 
                    #action end


                elif alt26 == 14:
                    # treelesscss.g:363:4: function
                    pass 
                    self._state.following.append(self.FOLLOW_function_in_termnum1299)
                    function57 = self.function()

                    self._state.following.pop()
                    #action start
                    gencode =  function57 
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
    # treelesscss.g:367:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        retval = self.unaryOperator_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:368:2: ( MINUS | PLUS )
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
    # treelesscss.g:373:1: function returns [gencode] : ^( N_Function fnct_name fnct_args ) ;
    def function(self, ):

        gencode = None

        fnct_name58 = None

        fnct_args59 = None


        try:
            try:
                # treelesscss.g:374:2: ( ^( N_Function fnct_name fnct_args ) )
                # treelesscss.g:374:4: ^( N_Function fnct_name fnct_args )
                pass 
                self.match(self.input, N_Function, self.FOLLOW_N_Function_in_function1337)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_fnct_name_in_function1339)
                fnct_name58 = self.fnct_name()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_fnct_args_in_function1341)
                fnct_args59 = self.fnct_args()

                self._state.following.pop()

                self.match(self.input, UP, None)
                #action start
                gencode =  fnct_name58 + fnct_args59 + ')' 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "function"


    # $ANTLR start "fnct_name"
    # treelesscss.g:378:1: fnct_name returns [gencode] : ^( FUNCTION ( IDENT | COLON | DOT )* ) ;
    def fnct_name(self, ):

        gencode = None

        IDENT60 = None
        COLON61 = None
        DOT62 = None
        FUNCTION63 = None

        try:
            try:
                # treelesscss.g:379:2: ( ^( FUNCTION ( IDENT | COLON | DOT )* ) )
                # treelesscss.g:379:4: ^( FUNCTION ( IDENT | COLON | DOT )* )
                pass 
                FUNCTION63=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name1363)

                #action start
                prefix = []; 
                #action end

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # treelesscss.g:381:3: ( IDENT | COLON | DOT )*
                    while True: #loop27
                        alt27 = 4
                        LA27 = self.input.LA(1)
                        if LA27 == IDENT:
                            alt27 = 1
                        elif LA27 == COLON:
                            alt27 = 2
                        elif LA27 == DOT:
                            alt27 = 3

                        if alt27 == 1:
                            # treelesscss.g:381:5: IDENT
                            pass 
                            IDENT60=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name1375)
                            #action start
                            prefix.append(IDENT60.text); 
                            #action end


                        elif alt27 == 2:
                            # treelesscss.g:382:5: COLON
                            pass 
                            COLON61=self.match(self.input, COLON, self.FOLLOW_COLON_in_fnct_name1384)
                            #action start
                            prefix.append(COLON61.text); 
                            #action end


                        elif alt27 == 3:
                            # treelesscss.g:383:5: DOT
                            pass 
                            DOT62=self.match(self.input, DOT, self.FOLLOW_DOT_in_fnct_name1393)
                            #action start
                            prefix.append(DOT62.text); 
                            #action end


                        else:
                            break #loop27

                    self.match(self.input, UP, None)

                #action start
                gencode =  ''.join(prefix) + FUNCTION63.text 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return gencode

    # $ANTLR end "fnct_name"


    # $ANTLR start "fnct_args"
    # treelesscss.g:388:10: fragment fnct_args returns [gencode] : ( ^( COMMA a= fnct_args b= fnct_args ) | ^( OPEQ IDENT expr ) | term );
    def fnct_args(self, ):

        gencode = None

        COMMA64 = None
        IDENT65 = None
        OPEQ66 = None
        a = None

        b = None

        expr67 = None

        term68 = None


        try:
            try:
                # treelesscss.g:389:2: ( ^( COMMA a= fnct_args b= fnct_args ) | ^( OPEQ IDENT expr ) | term )
                alt28 = 3
                LA28 = self.input.LA(1)
                if LA28 == COMMA:
                    alt28 = 1
                elif LA28 == OPEQ:
                    alt28 = 2
                elif LA28 == N_Term or LA28 == STRING or LA28 == URI or LA28 == IDENT or LA28 == HASH or LA28 == UNICODE_RANGE:
                    alt28 = 3
                else:
                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae

                if alt28 == 1:
                    # treelesscss.g:389:4: ^( COMMA a= fnct_args b= fnct_args )
                    pass 
                    COMMA64=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args1425)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_fnct_args_in_fnct_args1429)
                    a = self.fnct_args()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_fnct_args_in_fnct_args1433)
                    b = self.fnct_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    gencode =  a + COMMA64.text + b  
                    #action end


                elif alt28 == 2:
                    # treelesscss.g:392:4: ^( OPEQ IDENT expr )
                    pass 
                    OPEQ66=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_args1446)

                    self.match(self.input, DOWN, None)
                    IDENT65=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_args1448)
                    self._state.following.append(self.FOLLOW_expr_in_fnct_args1450)
                    expr67 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)
                    #action start
                    gencode =  IDENT65.text + OPEQ66.text + expr67  
                    #action end


                elif alt28 == 3:
                    # treelesscss.g:394:4: term
                    pass 
                    self._state.following.append(self.FOLLOW_term_in_fnct_args1461)
                    term68 = self.term()

                    self._state.following.pop()
                    #action start
                    gencode =  term68  
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
                self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor1478)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "hexColor"


    # Delegated rules


    # lookup tables for DFA #25

    DFA25_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA25_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA25_min = DFA.unpack(
        u"\1\22\1\2\5\uffff\1\14\2\uffff"
        )

    DFA25_max = DFA.unpack(
        u"\1\100\1\2\5\uffff\1\101\2\uffff"
        )

    DFA25_accept = DFA.unpack(
        u"\2\uffff\1\3\1\4\1\5\1\6\1\7\1\uffff\1\1\1\2"
        )

    DFA25_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA25_transition = [
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

    # class definition for DFA #25

    class DFA25(DFA):
        pass


 

    FOLLOW_N_StyleSheet_in_styleSheet51 = frozenset([2])
    FOLLOW_charSet_in_styleSheet56 = frozenset([3, 7, 22, 24, 32, 33, 34])
    FOLLOW_imports_in_styleSheet66 = frozenset([3, 7, 22, 24, 32, 33, 34])
    FOLLOW_body_in_styleSheet75 = frozenset([3, 7, 24, 32, 33, 34])
    FOLLOW_CHARSET_SYM_in_charSet101 = frozenset([2])
    FOLLOW_STRING_in_charSet103 = frozenset([3])
    FOLLOW_IMPORT_SYM_in_imports141 = frozenset([2])
    FOLLOW_importUrl_in_imports145 = frozenset([3, 5])
    FOLLOW_media_query_in_imports153 = frozenset([3, 5])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_ruleSet_in_body204 = frozenset([1])
    FOLLOW_media_in_body210 = frozenset([1])
    FOLLOW_page_in_body217 = frozenset([1])
    FOLLOW_fontface_in_body224 = frozenset([1])
    FOLLOW_keyframes_in_body230 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media255 = frozenset([2])
    FOLLOW_media_query_in_media261 = frozenset([3, 5, 7, 24, 32, 33, 34])
    FOLLOW_body_in_media275 = frozenset([3, 7, 24, 32, 33, 34])
    FOLLOW_N_MediaQuery_in_media_query310 = frozenset([2])
    FOLLOW_media_stmt_in_media_query316 = frozenset([3, 6, 28])
    FOLLOW_media_expr_in_media_query324 = frozenset([3, 6, 28])
    FOLLOW_IDENT_in_media_stmt350 = frozenset([1])
    FOLLOW_N_MediaExpr_in_media_expr362 = frozenset([2])
    FOLLOW_media_stmt_in_media_expr364 = frozenset([3])
    FOLLOW_FONTFACE_SYM_in_fontface384 = frozenset([2])
    FOLLOW_declarationset_in_fontface392 = frozenset([3])
    FOLLOW_PAGE_SYM_in_page414 = frozenset([2])
    FOLLOW_pseudoPage_in_page427 = frozenset([11, 14])
    FOLLOW_declarationset_in_page445 = frozenset([3])
    FOLLOW_IDENT_in_pseudoPage463 = frozenset([1])
    FOLLOW_KEYFRAMES_SYM_in_keyframes479 = frozenset([2])
    FOLLOW_IDENT_in_keyframes481 = frozenset([3, 8])
    FOLLOW_keyframes_block_in_keyframes489 = frozenset([3, 8])
    FOLLOW_N_KeyframeBlock_in_keyframes_block509 = frozenset([2])
    FOLLOW_keyframe_selector_in_keyframes_block522 = frozenset([9, 11, 14])
    FOLLOW_declarationset_in_keyframes_block541 = frozenset([3])
    FOLLOW_M_KeyframeSelector_in_keyframe_selector565 = frozenset([2])
    FOLLOW_IDENT_in_keyframe_selector574 = frozenset([3])
    FOLLOW_PERCENTAGE_in_keyframe_selector583 = frozenset([3])
    FOLLOW_N_RuleSet_in_ruleSet617 = frozenset([2])
    FOLLOW_selector_list_in_ruleSet622 = frozenset([10, 11, 14])
    FOLLOW_declarationset_in_ruleSet635 = frozenset([3])
    FOLLOW_N_Selector_in_selector_list658 = frozenset([2])
    FOLLOW_selector_in_selector_list662 = frozenset([3])
    FOLLOW_simpleSelector_in_selector685 = frozenset([1, 13, 16, 28, 36, 37, 38, 41])
    FOLLOW_combinator_in_selector694 = frozenset([13, 16, 28, 36, 37, 38, 41])
    FOLLOW_simpleSelector_in_selector702 = frozenset([1, 13, 16, 28, 36, 37, 38, 41])
    FOLLOW_PLUS_in_combinator723 = frozenset([1])
    FOLLOW_GREATER_in_combinator732 = frozenset([1])
    FOLLOW_IDENT_in_simpleSelector755 = frozenset([1])
    FOLLOW_STAR_in_simpleSelector763 = frozenset([1])
    FOLLOW_HASH_in_simpleSelector771 = frozenset([1])
    FOLLOW_pseudo_in_simpleSelector779 = frozenset([1])
    FOLLOW_attrib_in_simpleSelector786 = frozenset([1])
    FOLLOW_N_Pseudo_in_pseudo804 = frozenset([2])
    FOLLOW_COLON_in_pseudo808 = frozenset([28, 30])
    FOLLOW_COLON_in_pseudo812 = frozenset([28])
    FOLLOW_IDENT_in_pseudo815 = frozenset([3])
    FOLLOW_N_Attrib_in_attrib838 = frozenset([2])
    FOLLOW_attribBody_in_attrib840 = frozenset([3])
    FOLLOW_IDENT_in_attribBody862 = frozenset([1])
    FOLLOW_attribOper_in_attribBody871 = frozenset([2])
    FOLLOW_IDENT_in_attribBody873 = frozenset([18, 20, 23, 28, 38, 64])
    FOLLOW_term_in_attribBody875 = frozenset([3])
    FOLLOW_set_in_attribOper0 = frozenset([1])
    FOLLOW_N_Empty_in_declarationset934 = frozenset([1])
    FOLLOW_declaration_in_declarationset939 = frozenset([1, 11, 14])
    FOLLOW_N_Declaration_in_declaration953 = frozenset([2])
    FOLLOW_property_in_declaration957 = frozenset([3, 15, 18, 20, 23, 27, 28, 38, 50, 51, 64])
    FOLLOW_expr_in_declaration964 = frozenset([3, 50])
    FOLLOW_prio_in_declaration974 = frozenset([3])
    FOLLOW_IDENT_in_property997 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1008 = frozenset([1])
    FOLLOW_operator_in_expr1026 = frozenset([2])
    FOLLOW_expr_in_expr1032 = frozenset([15, 18, 20, 23, 27, 28, 38, 51, 64])
    FOLLOW_expr_in_expr1036 = frozenset([3])
    FOLLOW_term_in_expr1049 = frozenset([1])
    FOLLOW_SOLIDUS_in_operator1070 = frozenset([1])
    FOLLOW_COMMA_in_operator1079 = frozenset([1])
    FOLLOW_N_Space_in_operator1088 = frozenset([1])
    FOLLOW_N_Term_in_term1107 = frozenset([2])
    FOLLOW_unaryOperator_in_term1109 = frozenset([12, 35, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])
    FOLLOW_termnum_in_term1111 = frozenset([3])
    FOLLOW_N_Term_in_term1121 = frozenset([2])
    FOLLOW_termnum_in_term1123 = frozenset([3])
    FOLLOW_STRING_in_term1133 = frozenset([1])
    FOLLOW_IDENT_in_term1141 = frozenset([1])
    FOLLOW_URI_in_term1150 = frozenset([1])
    FOLLOW_hexColor_in_term1159 = frozenset([1])
    FOLLOW_UNICODE_RANGE_in_term1167 = frozenset([1])
    FOLLOW_NUMBER_in_termnum1187 = frozenset([1])
    FOLLOW_PERCENTAGE_in_termnum1195 = frozenset([1])
    FOLLOW_LENGTH_in_termnum1203 = frozenset([1])
    FOLLOW_EMS_in_termnum1211 = frozenset([1])
    FOLLOW_EXS_in_termnum1220 = frozenset([1])
    FOLLOW_REMS_in_termnum1229 = frozenset([1])
    FOLLOW_CHS_in_termnum1238 = frozenset([1])
    FOLLOW_ANGLE_in_termnum1247 = frozenset([1])
    FOLLOW_TIME_in_termnum1256 = frozenset([1])
    FOLLOW_FREQ_in_termnum1265 = frozenset([1])
    FOLLOW_RESOLUTION_in_termnum1274 = frozenset([1])
    FOLLOW_VPORTLEN_in_termnum1282 = frozenset([1])
    FOLLOW_NTH_in_termnum1290 = frozenset([1])
    FOLLOW_function_in_termnum1299 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_N_Function_in_function1337 = frozenset([2])
    FOLLOW_fnct_name_in_function1339 = frozenset([18, 20, 23, 27, 28, 38, 44, 64])
    FOLLOW_fnct_args_in_function1341 = frozenset([3])
    FOLLOW_FUNCTION_in_fnct_name1363 = frozenset([2])
    FOLLOW_IDENT_in_fnct_name1375 = frozenset([3, 28, 30, 39])
    FOLLOW_COLON_in_fnct_name1384 = frozenset([3, 28, 30, 39])
    FOLLOW_DOT_in_fnct_name1393 = frozenset([3, 28, 30, 39])
    FOLLOW_COMMA_in_fnct_args1425 = frozenset([2])
    FOLLOW_fnct_args_in_fnct_args1429 = frozenset([18, 20, 23, 27, 28, 38, 44, 64])
    FOLLOW_fnct_args_in_fnct_args1433 = frozenset([3])
    FOLLOW_OPEQ_in_fnct_args1446 = frozenset([2])
    FOLLOW_IDENT_in_fnct_args1448 = frozenset([15, 18, 20, 23, 27, 28, 38, 51, 64])
    FOLLOW_expr_in_fnct_args1450 = frozenset([3])
    FOLLOW_term_in_fnct_args1461 = frozenset([1])
    FOLLOW_HASH_in_hexColor1478 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(treelesscss)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
