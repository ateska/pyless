# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 treelesscss.g 2012-11-20 23:20:42

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
    # treelesscss.g:13:1: styleSheet : ^( N_StyleSheet ( charSet )? ( imports )* ) ;
    def styleSheet(self, ):

        try:
            try:
                # treelesscss.g:14:2: ( ^( N_StyleSheet ( charSet )? ( imports )* ) )
                # treelesscss.g:14:4: ^( N_StyleSheet ( charSet )? ( imports )* )
                pass 
                self.match(self.input, N_StyleSheet, self.FOLLOW_N_StyleSheet_in_styleSheet51)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # treelesscss.g:14:20: ( charSet )?
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == CHARSET_SYM) :
                        alt1 = 1
                    if alt1 == 1:
                        # treelesscss.g:14:20: charSet
                        pass 
                        self._state.following.append(self.FOLLOW_charSet_in_styleSheet53)
                        self.charSet()

                        self._state.following.pop()



                    # treelesscss.g:14:29: ( imports )*
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == IMPORT_SYM) :
                            alt2 = 1


                        if alt2 == 1:
                            # treelesscss.g:14:29: imports
                            pass 
                            self._state.following.append(self.FOLLOW_imports_in_styleSheet56)
                            self.imports()

                            self._state.following.pop()


                        else:
                            break #loop2

                    self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "styleSheet"


    # $ANTLR start "charSet"
    # treelesscss.g:21:1: charSet : ^( CHARSET_SYM STRING ) ;
    def charSet(self, ):

        STRING1 = None

        try:
            try:
                # treelesscss.g:22:4: ( ^( CHARSET_SYM STRING ) )
                # treelesscss.g:22:6: ^( CHARSET_SYM STRING )
                pass 
                self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet78)

                self.match(self.input, DOWN, None)
                STRING1=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet80)

                self.match(self.input, UP, None)
                #action start
                self.TP_charSet(STRING1); 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "charSet"


    # $ANTLR start "imports"
    # treelesscss.g:30:1: imports : ^( IMPORT_SYM importUrl ) ;
    def imports(self, ):

        importUrl2 = None


        try:
            try:
                # treelesscss.g:31:2: ( ^( IMPORT_SYM importUrl ) )
                # treelesscss.g:31:4: ^( IMPORT_SYM importUrl )
                pass 
                self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports107)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_importUrl_in_imports109)
                importUrl2 = self.importUrl()

                self._state.following.pop()

                self.match(self.input, UP, None)
                #action start
                self.TP_imports(((importUrl2 is not None) and [self.input.getTokenStream().toString(
                    self.input.getTreeAdaptor().getTokenStartIndex(importUrl2.start),
                    self.input.getTreeAdaptor().getTokenStopIndex(importUrl2.start)
                    )] or [None])[0]); 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "imports"

    class importUrl_return(TreeRuleReturnScope):
        def __init__(self):
            super(treelesscss.importUrl_return, self).__init__()





    # $ANTLR start "importUrl"
    # treelesscss.g:36:1: importUrl : ( STRING | URI );
    def importUrl(self, ):

        retval = self.importUrl_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # treelesscss.g:37:2: ( STRING | URI )
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


    # Delegated rules


 

    FOLLOW_N_StyleSheet_in_styleSheet51 = frozenset([2])
    FOLLOW_charSet_in_styleSheet53 = frozenset([3, 20])
    FOLLOW_imports_in_styleSheet56 = frozenset([3, 20])
    FOLLOW_CHARSET_SYM_in_charSet78 = frozenset([2])
    FOLLOW_STRING_in_charSet80 = frozenset([3])
    FOLLOW_IMPORT_SYM_in_imports107 = frozenset([2])
    FOLLOW_importUrl_in_imports109 = frozenset([3])
    FOLLOW_set_in_importUrl0 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(treelesscss)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
