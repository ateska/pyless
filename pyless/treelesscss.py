# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 treelesscss.g 2012-11-22 00:22:14

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=40
UNICODE_RANGE=62
STAR=39
EOF=-1
MEDIA_SYM=22
INCLUDES=43
LBRACKET=38
RPAREN=29
NAME=70
GREATER=35
ESCAPE=67
DIMENSION=103
STRINGESC=101
NL=104
COMMENT=98
D=75
E=76
F=77
G=78
A=72
B=73
RBRACE=24
C=74
L=83
M=84
NMCHAR=69
IMPORT_SYM=20
N=85
SUBSTRINGMATCH=47
O=86
H=79
I=80
J=81
K=82
NUMBER=50
U=92
T=91
W=94
V=93
Q=88
P=87
S=90
CDO=99
R=89
CDC=100
Y=96
PERCENTAGE=33
URL=71
X=95
Z=97
URI=21
PAGE_SYM=31
WS=102
DASHMATCH=44
EMS=52
N_PseudoFunction=16
N_RuleSet=7
NONASCII=65
N_MediaQuery=5
N_Selector=10
LBRACE=23
LPAREN=27
LENGTH=51
IMPORTANT_SYM=48
N_Function=12
TIME=57
KEYFRAMES_SYM=32
COMMA=25
N_StyleSheet=4
IDENT=26
PLUS=34
FREQ=58
RBRACKET=41
DOT=37
VPORTLEN=60
CHARSET_SYM=17
ANGLE=56
REMS=54
HASH=36
HEXCHAR=64
RESOLUTION=59
PREFIXMATCH=45
MINUS=63
N_Pseudo=15
SOLIDUS=49
N_Empty=14
SEMI=19
UNICODE=66
CHS=55
COLON=28
NMSTART=68
N_Declaration=11
FONTFACE_SYM=30
OPEQ=42
EXS=53
M_KeyframeSelector=9
N_MediaExpr=6
N_Attrib=13
N_KeyframeBlock=8
SUFFIXMATCH=46
NTH=61
STRING=18

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "N_StyleSheet", "N_MediaQuery", "N_MediaExpr", "N_RuleSet", "N_KeyframeBlock", 
    "M_KeyframeSelector", "N_Selector", "N_Declaration", "N_Function", "N_Attrib", 
    "N_Empty", "N_Pseudo", "N_PseudoFunction", "CHARSET_SYM", "STRING", 
    "SEMI", "IMPORT_SYM", "URI", "MEDIA_SYM", "LBRACE", "RBRACE", "COMMA", 
    "IDENT", "LPAREN", "COLON", "RPAREN", "FONTFACE_SYM", "PAGE_SYM", "KEYFRAMES_SYM", 
    "PERCENTAGE", "PLUS", "GREATER", "HASH", "DOT", "LBRACKET", "STAR", 
    "FUNCTION", "RBRACKET", "OPEQ", "INCLUDES", "DASHMATCH", "PREFIXMATCH", 
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

                        if (LA3_0 == MEDIA_SYM) :
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
    # treelesscss.g:59:1: body : media ;
    def body(self, ):

        try:
            try:
                # treelesscss.g:60:2: ( media )
                # treelesscss.g:60:4: media
                pass 
                self._state.following.append(self.FOLLOW_media_in_body204)
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
    # treelesscss.g:73:1: media : ^( MEDIA_SYM ( media_query )* ( body )* ) ;
    def media(self, ):

        media_query6 = None


          
        mqs = []
        	
        try:
            try:
                # treelesscss.g:78:2: ( ^( MEDIA_SYM ( media_query )* ( body )* ) )
                # treelesscss.g:78:4: ^( MEDIA_SYM ( media_query )* ( body )* )
                pass 
                self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media233)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # treelesscss.g:79:3: ( media_query )*
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == N_MediaQuery) :
                            alt5 = 1


                        if alt5 == 1:
                            # treelesscss.g:79:5: media_query
                            pass 
                            self._state.following.append(self.FOLLOW_media_query_in_media239)
                            media_query6 = self.media_query()

                            self._state.following.pop()
                            #action start
                            mqs.append(media_query6) ; 
                            #action end


                        else:
                            break #loop5
                    #action start
                       
                    mediahead = '@media';
                    if len(mqs) > 0: mediahead += ' ' + self.LISTCOMA.join(mqs);
                    mediahead += self.EOLLBRACKET;
                    self.output(mediahead);
                    self.indent_level += 1
                    		
                    #action end
                    # treelesscss.g:87:3: ( body )*
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == MEDIA_SYM) :
                            alt6 = 1


                        if alt6 == 1:
                            # treelesscss.g:87:3: body
                            pass 
                            self._state.following.append(self.FOLLOW_body_in_media253)
                            self.body()

                            self._state.following.pop()


                        else:
                            break #loop6

                    self.match(self.input, UP, None)

                #action start
                  
                self.indent_level -= 1
                self.output(self.EOLRBRACKET);
                	
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "media"


    # $ANTLR start "media_query"
    # treelesscss.g:99:1: media_query returns [gencode] : ^( N_MediaQuery ( media_stmt | media_expr )+ ) ;
    def media_query(self, ):

        gencode = None

        media_stmt7 = None

        media_expr8 = None


          
        mq = list()
        	
        try:
            try:
                # treelesscss.g:104:2: ( ^( N_MediaQuery ( media_stmt | media_expr )+ ) )
                # treelesscss.g:104:4: ^( N_MediaQuery ( media_stmt | media_expr )+ )
                pass 
                self.match(self.input, N_MediaQuery, self.FOLLOW_N_MediaQuery_in_media_query287)

                self.match(self.input, DOWN, None)
                # treelesscss.g:105:3: ( media_stmt | media_expr )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 3
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == IDENT) :
                        alt7 = 1
                    elif (LA7_0 == N_MediaExpr) :
                        alt7 = 2


                    if alt7 == 1:
                        # treelesscss.g:105:5: media_stmt
                        pass 
                        self._state.following.append(self.FOLLOW_media_stmt_in_media_query293)
                        media_stmt7 = self.media_stmt()

                        self._state.following.pop()
                        #action start
                        mq.append(((media_stmt7 is not None) and [self.input.getTokenStream().toString(
                            self.input.getTreeAdaptor().getTokenStartIndex(media_stmt7.start),
                            self.input.getTreeAdaptor().getTokenStopIndex(media_stmt7.start)
                            )] or [None])[0]); 
                        #action end


                    elif alt7 == 2:
                        # treelesscss.g:106:5: media_expr
                        pass 
                        self._state.following.append(self.FOLLOW_media_expr_in_media_query301)
                        media_expr8 = self.media_expr()

                        self._state.following.pop()
                        #action start
                        mq.append(((media_expr8 is not None) and [self.input.getTokenStream().toString(
                            self.input.getTreeAdaptor().getTokenStartIndex(media_expr8.start),
                            self.input.getTreeAdaptor().getTokenStopIndex(media_expr8.start)
                            )] or [None])[0]); 
                        #action end


                    else:
                        if cnt7 >= 1:
                            break #loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1

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
    # treelesscss.g:112:1: media_stmt : IDENT ;
    def media_stmt(self, ):

        retval = self.media_stmt_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:113:2: ( IDENT )
                # treelesscss.g:113:4: IDENT
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_stmt327)




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
    # treelesscss.g:116:1: media_expr : ^( N_MediaExpr media_stmt ) ;
    def media_expr(self, ):

        retval = self.media_expr_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:117:2: ( ^( N_MediaExpr media_stmt ) )
                # treelesscss.g:117:4: ^( N_MediaExpr media_stmt )
                pass 
                self.match(self.input, N_MediaExpr, self.FOLLOW_N_MediaExpr_in_media_expr339)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_media_stmt_in_media_expr341)
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


    # Delegated rules


 

    FOLLOW_N_StyleSheet_in_styleSheet51 = frozenset([2])
    FOLLOW_charSet_in_styleSheet56 = frozenset([3, 20, 22])
    FOLLOW_imports_in_styleSheet66 = frozenset([3, 20, 22])
    FOLLOW_body_in_styleSheet75 = frozenset([3, 22])
    FOLLOW_CHARSET_SYM_in_charSet101 = frozenset([2])
    FOLLOW_STRING_in_charSet103 = frozenset([3])
    FOLLOW_IMPORT_SYM_in_imports141 = frozenset([2])
    FOLLOW_importUrl_in_imports145 = frozenset([3, 5])
    FOLLOW_media_query_in_imports153 = frozenset([3, 5])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_media_in_body204 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media233 = frozenset([2])
    FOLLOW_media_query_in_media239 = frozenset([3, 5, 22])
    FOLLOW_body_in_media253 = frozenset([3, 22])
    FOLLOW_N_MediaQuery_in_media_query287 = frozenset([2])
    FOLLOW_media_stmt_in_media_query293 = frozenset([3, 6, 26])
    FOLLOW_media_expr_in_media_query301 = frozenset([3, 6, 26])
    FOLLOW_IDENT_in_media_stmt327 = frozenset([1])
    FOLLOW_N_MediaExpr_in_media_expr339 = frozenset([2])
    FOLLOW_media_stmt_in_media_expr341 = frozenset([3])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(treelesscss)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
