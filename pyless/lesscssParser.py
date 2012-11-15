# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 lesscss.g 2012-11-15 21:51:09

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=29
STAR=24
LBRACE=11
EOF=-1
MEDIA_SYM=10
LPAREN=77
LENGTH=34
IMPORTANT_SYM=31
LBRACKET=23
INCLUDES=26
TIME=38
RPAREN=30
NAME=46
GREATER=19
ESCAPE=43
COMMA=9
IDENT=14
DIMENSION=80
PLUS=18
FREQ=39
STRINGESC=78
NL=81
RBRACKET=28
COMMENT=74
DOT=22
D=51
CHARSET_SYM=4
E=52
F=53
G=54
A=48
B=49
RBRACE=12
ANGLE=37
C=50
L=59
M=60
NMCHAR=45
IMPORT_SYM=7
N=61
O=62
H=55
I=56
J=57
K=58
NUMBER=32
U=68
HASH=21
HEXCHAR=40
T=67
W=70
V=69
Q=64
P=63
S=66
CDO=75
R=65
MINUS=20
SOLIDUS=17
SEMI=6
CDC=76
Y=72
URL=47
PERCENTAGE=33
UNICODE=42
X=71
Z=73
URI=8
COLON=16
PAGE_SYM=15
WS=79
NMSTART=44
DASHMATCH=27
FONTFACE_SYM=13
OPEQ=25
EMS=35
EXS=36
NONASCII=41
STRING=5

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "CHARSET_SYM", "STRING", "SEMI", "IMPORT_SYM", "URI", "COMMA", "MEDIA_SYM", 
    "LBRACE", "RBRACE", "FONTFACE_SYM", "IDENT", "PAGE_SYM", "COLON", "SOLIDUS", 
    "PLUS", "GREATER", "MINUS", "HASH", "DOT", "LBRACKET", "STAR", "OPEQ", 
    "INCLUDES", "DASHMATCH", "RBRACKET", "FUNCTION", "RPAREN", "IMPORTANT_SYM", 
    "NUMBER", "PERCENTAGE", "LENGTH", "EMS", "EXS", "ANGLE", "TIME", "FREQ", 
    "HEXCHAR", "NONASCII", "UNICODE", "ESCAPE", "NMSTART", "NMCHAR", "NAME", 
    "URL", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "COMMENT", 
    "CDO", "CDC", "LPAREN", "STRINGESC", "WS", "DIMENSION", "NL"
]




class lesscssParser(Parser):
    grammarFileName = "lesscss.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(lesscssParser, self).__init__(input, state, *args, **kwargs)

        self.dfa13 = self.DFA13(
            self, 13,
            eot = self.DFA13_eot,
            eof = self.DFA13_eof,
            min = self.DFA13_min,
            max = self.DFA13_max,
            accept = self.DFA13_accept,
            special = self.DFA13_special,
            transition = self.DFA13_transition
            )

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






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class styleSheet_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.styleSheet_return, self).__init__()

            self.tree = None




    # $ANTLR start "styleSheet"
    # lesscss.g:34:1: styleSheet : charSet ( imports )* bodylist EOF ;
    def styleSheet(self, ):

        retval = self.styleSheet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF4 = None
        charSet1 = None

        imports2 = None

        bodylist3 = None


        EOF4_tree = None

        try:
            try:
                # lesscss.g:35:5: ( charSet ( imports )* bodylist EOF )
                # lesscss.g:35:9: charSet ( imports )* bodylist EOF
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_charSet_in_styleSheet73)
                charSet1 = self.charSet()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, charSet1.tree)
                # lesscss.g:36:9: ( imports )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == IMPORT_SYM) :
                        alt1 = 1


                    if alt1 == 1:
                        # lesscss.g:36:9: imports
                        pass 
                        self._state.following.append(self.FOLLOW_imports_in_styleSheet83)
                        imports2 = self.imports()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, imports2.tree)


                    else:
                        break #loop1
                self._state.following.append(self.FOLLOW_bodylist_in_styleSheet94)
                bodylist3 = self.bodylist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, bodylist3.tree)
                EOF4=self.match(self.input, EOF, self.FOLLOW_EOF_in_styleSheet101)
                if self._state.backtracking == 0:

                    EOF4_tree = self._adaptor.createWithPayload(EOF4)
                    self._adaptor.addChild(root_0, EOF4_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "styleSheet"

    class charSet_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.charSet_return, self).__init__()

            self.tree = None




    # $ANTLR start "charSet"
    # lesscss.g:44:1: charSet : ( CHARSET_SYM STRING SEMI | );
    def charSet(self, ):

        retval = self.charSet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CHARSET_SYM5 = None
        STRING6 = None
        SEMI7 = None

        CHARSET_SYM5_tree = None
        STRING6_tree = None
        SEMI7_tree = None

        try:
            try:
                # lesscss.g:45:5: ( CHARSET_SYM STRING SEMI | )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == CHARSET_SYM) :
                    alt2 = 1
                elif (LA2_0 == EOF or LA2_0 == IMPORT_SYM or LA2_0 == MEDIA_SYM or (FONTFACE_SYM <= LA2_0 <= COLON) or (HASH <= LA2_0 <= STAR)) :
                    alt2 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # lesscss.g:45:9: CHARSET_SYM STRING SEMI
                    pass 
                    root_0 = self._adaptor.nil()

                    CHARSET_SYM5=self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet127)
                    if self._state.backtracking == 0:

                        CHARSET_SYM5_tree = self._adaptor.createWithPayload(CHARSET_SYM5)
                        self._adaptor.addChild(root_0, CHARSET_SYM5_tree)

                    STRING6=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet129)
                    if self._state.backtracking == 0:

                        STRING6_tree = self._adaptor.createWithPayload(STRING6)
                        self._adaptor.addChild(root_0, STRING6_tree)

                    SEMI7=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_charSet131)
                    if self._state.backtracking == 0:

                        SEMI7_tree = self._adaptor.createWithPayload(SEMI7)
                        self._adaptor.addChild(root_0, SEMI7_tree)



                elif alt2 == 2:
                    # lesscss.g:47:5: 
                    pass 
                    root_0 = self._adaptor.nil()


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "charSet"

    class imports_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.imports_return, self).__init__()

            self.tree = None




    # $ANTLR start "imports"
    # lesscss.g:52:1: imports : IMPORT_SYM ( STRING | URI ) ( medium ( COMMA medium )* )? SEMI ;
    def imports(self, ):

        retval = self.imports_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORT_SYM8 = None
        set9 = None
        COMMA11 = None
        SEMI13 = None
        medium10 = None

        medium12 = None


        IMPORT_SYM8_tree = None
        set9_tree = None
        COMMA11_tree = None
        SEMI13_tree = None

        try:
            try:
                # lesscss.g:53:5: ( IMPORT_SYM ( STRING | URI ) ( medium ( COMMA medium )* )? SEMI )
                # lesscss.g:53:9: IMPORT_SYM ( STRING | URI ) ( medium ( COMMA medium )* )? SEMI
                pass 
                root_0 = self._adaptor.nil()

                IMPORT_SYM8=self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports159)
                if self._state.backtracking == 0:

                    IMPORT_SYM8_tree = self._adaptor.createWithPayload(IMPORT_SYM8)
                    self._adaptor.addChild(root_0, IMPORT_SYM8_tree)

                set9 = self.input.LT(1)
                if self.input.LA(1) == STRING or self.input.LA(1) == URI:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set9))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse


                # lesscss.g:53:33: ( medium ( COMMA medium )* )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == IDENT) :
                    alt4 = 1
                if alt4 == 1:
                    # lesscss.g:53:34: medium ( COMMA medium )*
                    pass 
                    self._state.following.append(self.FOLLOW_medium_in_imports168)
                    medium10 = self.medium()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, medium10.tree)
                    # lesscss.g:53:41: ( COMMA medium )*
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == COMMA) :
                            alt3 = 1


                        if alt3 == 1:
                            # lesscss.g:53:42: COMMA medium
                            pass 
                            COMMA11=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_imports171)
                            if self._state.backtracking == 0:

                                COMMA11_tree = self._adaptor.createWithPayload(COMMA11)
                                self._adaptor.addChild(root_0, COMMA11_tree)

                            self._state.following.append(self.FOLLOW_medium_in_imports173)
                            medium12 = self.medium()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, medium12.tree)


                        else:
                            break #loop3



                SEMI13=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_imports179)
                if self._state.backtracking == 0:

                    SEMI13_tree = self._adaptor.createWithPayload(SEMI13)
                    self._adaptor.addChild(root_0, SEMI13_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "imports"

    class media_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_return, self).__init__()

            self.tree = None




    # $ANTLR start "media"
    # lesscss.g:60:1: media : MEDIA_SYM medium ( COMMA medium )* LBRACE ruleSet RBRACE ;
    def media(self, ):

        retval = self.media_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MEDIA_SYM14 = None
        COMMA16 = None
        LBRACE18 = None
        RBRACE20 = None
        medium15 = None

        medium17 = None

        ruleSet19 = None


        MEDIA_SYM14_tree = None
        COMMA16_tree = None
        LBRACE18_tree = None
        RBRACE20_tree = None

        try:
            try:
                # lesscss.g:61:5: ( MEDIA_SYM medium ( COMMA medium )* LBRACE ruleSet RBRACE )
                # lesscss.g:61:7: MEDIA_SYM medium ( COMMA medium )* LBRACE ruleSet RBRACE
                pass 
                root_0 = self._adaptor.nil()

                MEDIA_SYM14=self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media200)
                if self._state.backtracking == 0:

                    MEDIA_SYM14_tree = self._adaptor.createWithPayload(MEDIA_SYM14)
                    self._adaptor.addChild(root_0, MEDIA_SYM14_tree)

                self._state.following.append(self.FOLLOW_medium_in_media202)
                medium15 = self.medium()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, medium15.tree)
                # lesscss.g:61:24: ( COMMA medium )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == COMMA) :
                        alt5 = 1


                    if alt5 == 1:
                        # lesscss.g:61:25: COMMA medium
                        pass 
                        COMMA16=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_media205)
                        if self._state.backtracking == 0:

                            COMMA16_tree = self._adaptor.createWithPayload(COMMA16)
                            self._adaptor.addChild(root_0, COMMA16_tree)

                        self._state.following.append(self.FOLLOW_medium_in_media207)
                        medium17 = self.medium()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, medium17.tree)


                    else:
                        break #loop5
                LBRACE18=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_media219)
                if self._state.backtracking == 0:

                    LBRACE18_tree = self._adaptor.createWithPayload(LBRACE18)
                    self._adaptor.addChild(root_0, LBRACE18_tree)

                self._state.following.append(self.FOLLOW_ruleSet_in_media233)
                ruleSet19 = self.ruleSet()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, ruleSet19.tree)
                RBRACE20=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_media243)
                if self._state.backtracking == 0:

                    RBRACE20_tree = self._adaptor.createWithPayload(RBRACE20)
                    self._adaptor.addChild(root_0, RBRACE20_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "media"

    class fontface_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fontface_return, self).__init__()

            self.tree = None




    # $ANTLR start "fontface"
    # lesscss.g:71:1: fontface : FONTFACE_SYM LBRACE declarationset RBRACE ;
    def fontface(self, ):

        retval = self.fontface_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FONTFACE_SYM21 = None
        LBRACE22 = None
        RBRACE24 = None
        declarationset23 = None


        FONTFACE_SYM21_tree = None
        LBRACE22_tree = None
        RBRACE24_tree = None

        try:
            try:
                # lesscss.g:72:5: ( FONTFACE_SYM LBRACE declarationset RBRACE )
                # lesscss.g:72:7: FONTFACE_SYM LBRACE declarationset RBRACE
                pass 
                root_0 = self._adaptor.nil()

                FONTFACE_SYM21=self.match(self.input, FONTFACE_SYM, self.FOLLOW_FONTFACE_SYM_in_fontface264)
                if self._state.backtracking == 0:

                    FONTFACE_SYM21_tree = self._adaptor.createWithPayload(FONTFACE_SYM21)
                    self._adaptor.addChild(root_0, FONTFACE_SYM21_tree)

                LBRACE22=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_fontface266)
                if self._state.backtracking == 0:

                    LBRACE22_tree = self._adaptor.createWithPayload(LBRACE22)
                    self._adaptor.addChild(root_0, LBRACE22_tree)

                self._state.following.append(self.FOLLOW_declarationset_in_fontface268)
                declarationset23 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declarationset23.tree)
                RBRACE24=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_fontface270)
                if self._state.backtracking == 0:

                    RBRACE24_tree = self._adaptor.createWithPayload(RBRACE24)
                    self._adaptor.addChild(root_0, RBRACE24_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fontface"

    class medium_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.medium_return, self).__init__()

            self.tree = None




    # $ANTLR start "medium"
    # lesscss.g:78:1: medium : IDENT ;
    def medium(self, ):

        retval = self.medium_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT25 = None

        IDENT25_tree = None

        try:
            try:
                # lesscss.g:79:5: ( IDENT )
                # lesscss.g:79:7: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT25=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_medium290)
                if self._state.backtracking == 0:

                    IDENT25_tree = self._adaptor.createWithPayload(IDENT25)
                    self._adaptor.addChild(root_0, IDENT25_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "medium"

    class bodylist_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.bodylist_return, self).__init__()

            self.tree = None




    # $ANTLR start "bodylist"
    # lesscss.g:83:1: bodylist : ( bodyset )* ;
    def bodylist(self, ):

        retval = self.bodylist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        bodyset26 = None



        try:
            try:
                # lesscss.g:84:5: ( ( bodyset )* )
                # lesscss.g:84:7: ( bodyset )*
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:84:7: ( bodyset )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == MEDIA_SYM or (FONTFACE_SYM <= LA6_0 <= COLON) or (HASH <= LA6_0 <= STAR)) :
                        alt6 = 1


                    if alt6 == 1:
                        # lesscss.g:84:7: bodyset
                        pass 
                        self._state.following.append(self.FOLLOW_bodyset_in_bodylist313)
                        bodyset26 = self.bodyset()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, bodyset26.tree)


                    else:
                        break #loop6



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "bodylist"

    class bodyset_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.bodyset_return, self).__init__()

            self.tree = None




    # $ANTLR start "bodyset"
    # lesscss.g:87:1: bodyset : ( ruleSet | media | page | fontface );
    def bodyset(self, ):

        retval = self.bodyset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ruleSet27 = None

        media28 = None

        page29 = None

        fontface30 = None



        try:
            try:
                # lesscss.g:88:5: ( ruleSet | media | page | fontface )
                alt7 = 4
                LA7 = self.input.LA(1)
                if LA7 == IDENT or LA7 == COLON or LA7 == HASH or LA7 == DOT or LA7 == LBRACKET or LA7 == STAR:
                    alt7 = 1
                elif LA7 == MEDIA_SYM:
                    alt7 = 2
                elif LA7 == PAGE_SYM:
                    alt7 = 3
                elif LA7 == FONTFACE_SYM:
                    alt7 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # lesscss.g:88:7: ruleSet
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_ruleSet_in_bodyset335)
                    ruleSet27 = self.ruleSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, ruleSet27.tree)


                elif alt7 == 2:
                    # lesscss.g:89:7: media
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_media_in_bodyset343)
                    media28 = self.media()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media28.tree)


                elif alt7 == 3:
                    # lesscss.g:90:7: page
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_page_in_bodyset351)
                    page29 = self.page()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, page29.tree)


                elif alt7 == 4:
                    # lesscss.g:91:7: fontface
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fontface_in_bodyset359)
                    fontface30 = self.fontface()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fontface30.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "bodyset"

    class page_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.page_return, self).__init__()

            self.tree = None




    # $ANTLR start "page"
    # lesscss.g:94:1: page : PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE ;
    def page(self, ):

        retval = self.page_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PAGE_SYM31 = None
        LBRACE33 = None
        RBRACE35 = None
        pseudoPage32 = None

        declarationset34 = None


        PAGE_SYM31_tree = None
        LBRACE33_tree = None
        RBRACE35_tree = None

        try:
            try:
                # lesscss.g:95:5: ( PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE )
                # lesscss.g:95:7: PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE
                pass 
                root_0 = self._adaptor.nil()

                PAGE_SYM31=self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page383)
                if self._state.backtracking == 0:

                    PAGE_SYM31_tree = self._adaptor.createWithPayload(PAGE_SYM31)
                    self._adaptor.addChild(root_0, PAGE_SYM31_tree)

                # lesscss.g:95:16: ( pseudoPage )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == COLON) :
                    alt8 = 1
                if alt8 == 1:
                    # lesscss.g:95:16: pseudoPage
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoPage_in_page385)
                    pseudoPage32 = self.pseudoPage()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudoPage32.tree)



                LBRACE33=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_page388)
                if self._state.backtracking == 0:

                    LBRACE33_tree = self._adaptor.createWithPayload(LBRACE33)
                    self._adaptor.addChild(root_0, LBRACE33_tree)

                self._state.following.append(self.FOLLOW_declarationset_in_page390)
                declarationset34 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declarationset34.tree)
                RBRACE35=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_page392)
                if self._state.backtracking == 0:

                    RBRACE35_tree = self._adaptor.createWithPayload(RBRACE35)
                    self._adaptor.addChild(root_0, RBRACE35_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "page"

    class pseudoPage_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.pseudoPage_return, self).__init__()

            self.tree = None




    # $ANTLR start "pseudoPage"
    # lesscss.g:98:1: pseudoPage : COLON IDENT ;
    def pseudoPage(self, ):

        retval = self.pseudoPage_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON36 = None
        IDENT37 = None

        COLON36_tree = None
        IDENT37_tree = None

        try:
            try:
                # lesscss.g:99:5: ( COLON IDENT )
                # lesscss.g:99:7: COLON IDENT
                pass 
                root_0 = self._adaptor.nil()

                COLON36=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudoPage413)
                if self._state.backtracking == 0:

                    COLON36_tree = self._adaptor.createWithPayload(COLON36)
                    self._adaptor.addChild(root_0, COLON36_tree)

                IDENT37=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage415)
                if self._state.backtracking == 0:

                    IDENT37_tree = self._adaptor.createWithPayload(IDENT37)
                    self._adaptor.addChild(root_0, IDENT37_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "pseudoPage"

    class operator_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.operator_return, self).__init__()

            self.tree = None




    # $ANTLR start "operator"
    # lesscss.g:102:1: operator : ( SOLIDUS | COMMA | );
    def operator(self, ):

        retval = self.operator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SOLIDUS38 = None
        COMMA39 = None

        SOLIDUS38_tree = None
        COMMA39_tree = None

        try:
            try:
                # lesscss.g:103:5: ( SOLIDUS | COMMA | )
                alt9 = 3
                LA9 = self.input.LA(1)
                if LA9 == SOLIDUS:
                    alt9 = 1
                elif LA9 == COMMA:
                    alt9 = 2
                elif LA9 == STRING or LA9 == URI or LA9 == IDENT or LA9 == PLUS or LA9 == MINUS or LA9 == HASH or LA9 == FUNCTION or LA9 == NUMBER or LA9 == PERCENTAGE or LA9 == LENGTH or LA9 == EMS or LA9 == EXS or LA9 == ANGLE or LA9 == TIME or LA9 == FREQ:
                    alt9 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae

                if alt9 == 1:
                    # lesscss.g:103:7: SOLIDUS
                    pass 
                    root_0 = self._adaptor.nil()

                    SOLIDUS38=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator436)
                    if self._state.backtracking == 0:

                        SOLIDUS38_tree = self._adaptor.createWithPayload(SOLIDUS38)
                        self._adaptor.addChild(root_0, SOLIDUS38_tree)



                elif alt9 == 2:
                    # lesscss.g:104:7: COMMA
                    pass 
                    root_0 = self._adaptor.nil()

                    COMMA39=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator444)
                    if self._state.backtracking == 0:

                        COMMA39_tree = self._adaptor.createWithPayload(COMMA39)
                        self._adaptor.addChild(root_0, COMMA39_tree)



                elif alt9 == 3:
                    # lesscss.g:106:5: 
                    pass 
                    root_0 = self._adaptor.nil()


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "operator"

    class combinator_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.combinator_return, self).__init__()

            self.tree = None




    # $ANTLR start "combinator"
    # lesscss.g:108:1: combinator : ( PLUS | GREATER | );
    def combinator(self, ):

        retval = self.combinator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS40 = None
        GREATER41 = None

        PLUS40_tree = None
        GREATER41_tree = None

        try:
            try:
                # lesscss.g:109:5: ( PLUS | GREATER | )
                alt10 = 3
                LA10 = self.input.LA(1)
                if LA10 == PLUS:
                    alt10 = 1
                elif LA10 == GREATER:
                    alt10 = 2
                elif LA10 == IDENT or LA10 == COLON or LA10 == HASH or LA10 == DOT or LA10 == LBRACKET or LA10 == STAR:
                    alt10 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # lesscss.g:109:7: PLUS
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS40=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator471)
                    if self._state.backtracking == 0:

                        PLUS40_tree = self._adaptor.createWithPayload(PLUS40)
                        self._adaptor.addChild(root_0, PLUS40_tree)



                elif alt10 == 2:
                    # lesscss.g:110:7: GREATER
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER41=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator479)
                    if self._state.backtracking == 0:

                        GREATER41_tree = self._adaptor.createWithPayload(GREATER41)
                        self._adaptor.addChild(root_0, GREATER41_tree)



                elif alt10 == 3:
                    # lesscss.g:112:5: 
                    pass 
                    root_0 = self._adaptor.nil()


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "combinator"

    class unaryOperator_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.unaryOperator_return, self).__init__()

            self.tree = None




    # $ANTLR start "unaryOperator"
    # lesscss.g:114:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        retval = self.unaryOperator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set42 = None

        set42_tree = None

        try:
            try:
                # lesscss.g:115:5: ( MINUS | PLUS )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set42 = self.input.LT(1)
                if self.input.LA(1) == PLUS or self.input.LA(1) == MINUS:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set42))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "unaryOperator"

    class property_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.property_return, self).__init__()

            self.tree = None




    # $ANTLR start "property"
    # lesscss.g:119:1: property : IDENT ;
    def property(self, ):

        retval = self.property_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT43 = None

        IDENT43_tree = None

        try:
            try:
                # lesscss.g:120:5: ( IDENT )
                # lesscss.g:120:7: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT43=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property537)
                if self._state.backtracking == 0:

                    IDENT43_tree = self._adaptor.createWithPayload(IDENT43)
                    self._adaptor.addChild(root_0, IDENT43_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "property"

    class ruleSet_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.ruleSet_return, self).__init__()

            self.tree = None




    # $ANTLR start "ruleSet"
    # lesscss.g:123:1: ruleSet : selector ( COMMA selector )* LBRACE declarationset RBRACE ;
    def ruleSet(self, ):

        retval = self.ruleSet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA45 = None
        LBRACE47 = None
        RBRACE49 = None
        selector44 = None

        selector46 = None

        declarationset48 = None


        COMMA45_tree = None
        LBRACE47_tree = None
        RBRACE49_tree = None

        try:
            try:
                # lesscss.g:124:5: ( selector ( COMMA selector )* LBRACE declarationset RBRACE )
                # lesscss.g:124:7: selector ( COMMA selector )* LBRACE declarationset RBRACE
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_selector_in_ruleSet558)
                selector44 = self.selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, selector44.tree)
                # lesscss.g:124:16: ( COMMA selector )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == COMMA) :
                        alt11 = 1


                    if alt11 == 1:
                        # lesscss.g:124:17: COMMA selector
                        pass 
                        COMMA45=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_ruleSet561)
                        if self._state.backtracking == 0:

                            COMMA45_tree = self._adaptor.createWithPayload(COMMA45)
                            self._adaptor.addChild(root_0, COMMA45_tree)

                        self._state.following.append(self.FOLLOW_selector_in_ruleSet563)
                        selector46 = self.selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, selector46.tree)


                    else:
                        break #loop11
                LBRACE47=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_ruleSet567)
                if self._state.backtracking == 0:

                    LBRACE47_tree = self._adaptor.createWithPayload(LBRACE47)
                    self._adaptor.addChild(root_0, LBRACE47_tree)

                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet569)
                declarationset48 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declarationset48.tree)
                RBRACE49=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_ruleSet571)
                if self._state.backtracking == 0:

                    RBRACE49_tree = self._adaptor.createWithPayload(RBRACE49)
                    self._adaptor.addChild(root_0, RBRACE49_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "ruleSet"

    class selector_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.selector_return, self).__init__()

            self.tree = None




    # $ANTLR start "selector"
    # lesscss.g:127:1: selector : simpleSelector ( combinator simpleSelector )* ;
    def selector(self, ):

        retval = self.selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        simpleSelector50 = None

        combinator51 = None

        simpleSelector52 = None



        try:
            try:
                # lesscss.g:128:5: ( simpleSelector ( combinator simpleSelector )* )
                # lesscss.g:128:7: simpleSelector ( combinator simpleSelector )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_simpleSelector_in_selector592)
                simpleSelector50 = self.simpleSelector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, simpleSelector50.tree)
                # lesscss.g:128:22: ( combinator simpleSelector )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == IDENT or LA12_0 == COLON or (PLUS <= LA12_0 <= GREATER) or (HASH <= LA12_0 <= STAR)) :
                        alt12 = 1


                    if alt12 == 1:
                        # lesscss.g:128:23: combinator simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector595)
                        combinator51 = self.combinator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, combinator51.tree)
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector597)
                        simpleSelector52 = self.simpleSelector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, simpleSelector52.tree)


                    else:
                        break #loop12



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "selector"

    class simpleSelector_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.simpleSelector_return, self).__init__()

            self.tree = None




    # $ANTLR start "simpleSelector"
    # lesscss.g:131:1: simpleSelector : ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ );
    def simpleSelector(self, ):

        retval = self.simpleSelector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        elementName53 = None

        elementSubsequent54 = None

        elementSubsequent55 = None



        try:
            try:
                # lesscss.g:132:5: ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ )
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == IDENT or LA15_0 == STAR) :
                    alt15 = 1
                elif (LA15_0 == COLON or (HASH <= LA15_0 <= LBRACKET)) :
                    alt15 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae

                if alt15 == 1:
                    # lesscss.g:132:7: elementName ( ( esPred )=> elementSubsequent )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elementName_in_simpleSelector616)
                    elementName53 = self.elementName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, elementName53.tree)
                    # lesscss.g:133:9: ( ( esPred )=> elementSubsequent )*
                    while True: #loop13
                        alt13 = 2
                        alt13 = self.dfa13.predict(self.input)
                        if alt13 == 1:
                            # lesscss.g:133:10: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector632)
                            elementSubsequent54 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent54.tree)


                        else:
                            break #loop13


                elif alt15 == 2:
                    # lesscss.g:135:7: ( ( esPred )=> elementSubsequent )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:135:7: ( ( esPred )=> elementSubsequent )+
                    cnt14 = 0
                    while True: #loop14
                        alt14 = 2
                        LA14 = self.input.LA(1)
                        if LA14 == HASH:
                            LA14_2 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt14 = 1


                        elif LA14 == DOT:
                            LA14_3 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt14 = 1


                        elif LA14 == LBRACKET:
                            LA14_4 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt14 = 1


                        elif LA14 == COLON:
                            LA14_5 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt14 = 1



                        if alt14 == 1:
                            # lesscss.g:135:8: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector656)
                            elementSubsequent55 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent55.tree)


                        else:
                            if cnt14 >= 1:
                                break #loop14

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(14, self.input)
                            raise eee

                        cnt14 += 1


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "simpleSelector"

    class esPred_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.esPred_return, self).__init__()

            self.tree = None




    # $ANTLR start "esPred"
    # lesscss.g:138:1: esPred : ( HASH | DOT | LBRACKET | COLON );
    def esPred(self, ):

        retval = self.esPred_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set56 = None

        set56_tree = None

        try:
            try:
                # lesscss.g:139:5: ( HASH | DOT | LBRACKET | COLON )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set56 = self.input.LT(1)
                if self.input.LA(1) == COLON or (HASH <= self.input.LA(1) <= LBRACKET):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set56))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "esPred"

    class elementSubsequent_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.elementSubsequent_return, self).__init__()

            self.tree = None




    # $ANTLR start "elementSubsequent"
    # lesscss.g:142:1: elementSubsequent : ( HASH | cssClass | attrib | pseudo );
    def elementSubsequent(self, ):

        retval = self.elementSubsequent_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH57 = None
        cssClass58 = None

        attrib59 = None

        pseudo60 = None


        HASH57_tree = None

        try:
            try:
                # lesscss.g:143:5: ( HASH | cssClass | attrib | pseudo )
                alt16 = 4
                LA16 = self.input.LA(1)
                if LA16 == HASH:
                    alt16 = 1
                elif LA16 == DOT:
                    alt16 = 2
                elif LA16 == LBRACKET:
                    alt16 = 3
                elif LA16 == COLON:
                    alt16 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # lesscss.g:143:7: HASH
                    pass 
                    root_0 = self._adaptor.nil()

                    HASH57=self.match(self.input, HASH, self.FOLLOW_HASH_in_elementSubsequent712)
                    if self._state.backtracking == 0:

                        HASH57_tree = self._adaptor.createWithPayload(HASH57)
                        self._adaptor.addChild(root_0, HASH57_tree)



                elif alt16 == 2:
                    # lesscss.g:144:7: cssClass
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_cssClass_in_elementSubsequent720)
                    cssClass58 = self.cssClass()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cssClass58.tree)


                elif alt16 == 3:
                    # lesscss.g:145:7: attrib
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_attrib_in_elementSubsequent728)
                    attrib59 = self.attrib()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, attrib59.tree)


                elif alt16 == 4:
                    # lesscss.g:146:7: pseudo
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pseudo_in_elementSubsequent736)
                    pseudo60 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudo60.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "elementSubsequent"

    class cssClass_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.cssClass_return, self).__init__()

            self.tree = None




    # $ANTLR start "cssClass"
    # lesscss.g:149:1: cssClass : DOT IDENT ;
    def cssClass(self, ):

        retval = self.cssClass_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOT61 = None
        IDENT62 = None

        DOT61_tree = None
        IDENT62_tree = None

        try:
            try:
                # lesscss.g:150:5: ( DOT IDENT )
                # lesscss.g:150:7: DOT IDENT
                pass 
                root_0 = self._adaptor.nil()

                DOT61=self.match(self.input, DOT, self.FOLLOW_DOT_in_cssClass757)
                if self._state.backtracking == 0:

                    DOT61_tree = self._adaptor.createWithPayload(DOT61)
                    self._adaptor.addChild(root_0, DOT61_tree)

                IDENT62=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_cssClass759)
                if self._state.backtracking == 0:

                    IDENT62_tree = self._adaptor.createWithPayload(IDENT62)
                    self._adaptor.addChild(root_0, IDENT62_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "cssClass"

    class elementName_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.elementName_return, self).__init__()

            self.tree = None




    # $ANTLR start "elementName"
    # lesscss.g:153:1: elementName : ( IDENT | STAR );
    def elementName(self, ):

        retval = self.elementName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set63 = None

        set63_tree = None

        try:
            try:
                # lesscss.g:154:5: ( IDENT | STAR )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set63 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == STAR:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set63))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "elementName"

    class attrib_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.attrib_return, self).__init__()

            self.tree = None




    # $ANTLR start "attrib"
    # lesscss.g:158:1: attrib : LBRACKET IDENT ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )? RBRACKET ;
    def attrib(self, ):

        retval = self.attrib_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LBRACKET64 = None
        IDENT65 = None
        set66 = None
        set67 = None
        RBRACKET68 = None

        LBRACKET64_tree = None
        IDENT65_tree = None
        set66_tree = None
        set67_tree = None
        RBRACKET68_tree = None

        try:
            try:
                # lesscss.g:159:5: ( LBRACKET IDENT ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )? RBRACKET )
                # lesscss.g:159:7: LBRACKET IDENT ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )? RBRACKET
                pass 
                root_0 = self._adaptor.nil()

                LBRACKET64=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_attrib809)
                if self._state.backtracking == 0:

                    LBRACKET64_tree = self._adaptor.createWithPayload(LBRACKET64)
                    self._adaptor.addChild(root_0, LBRACKET64_tree)

                IDENT65=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attrib824)
                if self._state.backtracking == 0:

                    IDENT65_tree = self._adaptor.createWithPayload(IDENT65)
                    self._adaptor.addChild(root_0, IDENT65_tree)

                # lesscss.g:163:13: ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if ((OPEQ <= LA17_0 <= DASHMATCH)) :
                    alt17 = 1
                if alt17 == 1:
                    # lesscss.g:164:17: ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING )
                    pass 
                    set66 = self.input.LT(1)
                    if (OPEQ <= self.input.LA(1) <= DASHMATCH):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set66))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    set67 = self.input.LT(1)
                    if self.input.LA(1) == STRING or self.input.LA(1) == IDENT:
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set67))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse





                RBRACKET68=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_attrib1074)
                if self._state.backtracking == 0:

                    RBRACKET68_tree = self._adaptor.createWithPayload(RBRACKET68)
                    self._adaptor.addChild(root_0, RBRACKET68_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "attrib"

    class pseudo_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.pseudo_return, self).__init__()

            self.tree = None




    # $ANTLR start "pseudo"
    # lesscss.g:178:1: pseudo : COLON ( IDENT | FUNCTION expr RPAREN ) ;
    def pseudo(self, ):

        retval = self.pseudo_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON69 = None
        IDENT70 = None
        FUNCTION71 = None
        RPAREN73 = None
        expr72 = None


        COLON69_tree = None
        IDENT70_tree = None
        FUNCTION71_tree = None
        RPAREN73_tree = None

        try:
            try:
                # lesscss.g:179:5: ( COLON ( IDENT | FUNCTION expr RPAREN ) )
                # lesscss.g:179:7: COLON ( IDENT | FUNCTION expr RPAREN )
                pass 
                root_0 = self._adaptor.nil()

                COLON69=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1087)
                if self._state.backtracking == 0:

                    COLON69_tree = self._adaptor.createWithPayload(COLON69)
                    self._adaptor.addChild(root_0, COLON69_tree)

                # lesscss.g:179:13: ( IDENT | FUNCTION expr RPAREN )
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == IDENT) :
                    alt18 = 1
                elif (LA18_0 == FUNCTION) :
                    alt18 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae

                if alt18 == 1:
                    # lesscss.g:179:15: IDENT
                    pass 
                    IDENT70=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo1091)
                    if self._state.backtracking == 0:

                        IDENT70_tree = self._adaptor.createWithPayload(IDENT70)
                        self._adaptor.addChild(root_0, IDENT70_tree)



                elif alt18 == 2:
                    # lesscss.g:179:23: FUNCTION expr RPAREN
                    pass 
                    FUNCTION71=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudo1095)
                    if self._state.backtracking == 0:

                        FUNCTION71_tree = self._adaptor.createWithPayload(FUNCTION71)
                        self._adaptor.addChild(root_0, FUNCTION71_tree)

                    self._state.following.append(self.FOLLOW_expr_in_pseudo1097)
                    expr72 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr72.tree)
                    RPAREN73=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudo1099)
                    if self._state.backtracking == 0:

                        RPAREN73_tree = self._adaptor.createWithPayload(RPAREN73)
                        self._adaptor.addChild(root_0, RPAREN73_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "pseudo"

    class declarationset_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.declarationset_return, self).__init__()

            self.tree = None




    # $ANTLR start "declarationset"
    # lesscss.g:182:1: declarationset : declaration ( SEMI declaration )* ( SEMI )? ;
    def declarationset(self, ):

        retval = self.declarationset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI75 = None
        SEMI77 = None
        declaration74 = None

        declaration76 = None


        SEMI75_tree = None
        SEMI77_tree = None

        try:
            try:
                # lesscss.g:183:5: ( declaration ( SEMI declaration )* ( SEMI )? )
                # lesscss.g:183:7: declaration ( SEMI declaration )* ( SEMI )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_declaration_in_declarationset1118)
                declaration74 = self.declaration()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, declaration74.tree)
                # lesscss.g:183:19: ( SEMI declaration )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == SEMI) :
                        LA19_1 = self.input.LA(2)

                        if (LA19_1 == IDENT) :
                            alt19 = 1




                    if alt19 == 1:
                        # lesscss.g:183:20: SEMI declaration
                        pass 
                        SEMI75=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1121)
                        if self._state.backtracking == 0:

                            SEMI75_tree = self._adaptor.createWithPayload(SEMI75)
                            self._adaptor.addChild(root_0, SEMI75_tree)

                        self._state.following.append(self.FOLLOW_declaration_in_declarationset1123)
                        declaration76 = self.declaration()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, declaration76.tree)


                    else:
                        break #loop19
                # lesscss.g:183:39: ( SEMI )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == SEMI) :
                    alt20 = 1
                if alt20 == 1:
                    # lesscss.g:183:39: SEMI
                    pass 
                    SEMI77=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1127)
                    if self._state.backtracking == 0:

                        SEMI77_tree = self._adaptor.createWithPayload(SEMI77)
                        self._adaptor.addChild(root_0, SEMI77_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "declarationset"

    class declaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.declaration_return, self).__init__()

            self.tree = None




    # $ANTLR start "declaration"
    # lesscss.g:186:1: declaration : property COLON expr ( prio )? ;
    def declaration(self, ):

        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON79 = None
        property78 = None

        expr80 = None

        prio81 = None


        COLON79_tree = None

        try:
            try:
                # lesscss.g:187:5: ( property COLON expr ( prio )? )
                # lesscss.g:187:7: property COLON expr ( prio )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_property_in_declaration1145)
                property78 = self.property()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, property78.tree)
                COLON79=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1147)
                if self._state.backtracking == 0:

                    COLON79_tree = self._adaptor.createWithPayload(COLON79)
                    self._adaptor.addChild(root_0, COLON79_tree)

                self._state.following.append(self.FOLLOW_expr_in_declaration1149)
                expr80 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr80.tree)
                # lesscss.g:187:27: ( prio )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == IMPORTANT_SYM) :
                    alt21 = 1
                if alt21 == 1:
                    # lesscss.g:187:27: prio
                    pass 
                    self._state.following.append(self.FOLLOW_prio_in_declaration1151)
                    prio81 = self.prio()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, prio81.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "declaration"

    class prio_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.prio_return, self).__init__()

            self.tree = None




    # $ANTLR start "prio"
    # lesscss.g:190:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        retval = self.prio_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORTANT_SYM82 = None

        IMPORTANT_SYM82_tree = None

        try:
            try:
                # lesscss.g:191:5: ( IMPORTANT_SYM )
                # lesscss.g:191:7: IMPORTANT_SYM
                pass 
                root_0 = self._adaptor.nil()

                IMPORTANT_SYM82=self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1173)
                if self._state.backtracking == 0:

                    IMPORTANT_SYM82_tree = self._adaptor.createWithPayload(IMPORTANT_SYM82)
                    self._adaptor.addChild(root_0, IMPORTANT_SYM82_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "prio"

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr"
    # lesscss.g:194:1: expr : term ( operator term )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        term83 = None

        operator84 = None

        term85 = None



        try:
            try:
                # lesscss.g:195:5: ( term ( operator term )* )
                # lesscss.g:195:7: term ( operator term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_expr1194)
                term83 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term83.tree)
                # lesscss.g:195:12: ( operator term )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == COMMA) :
                        LA22_2 = self.input.LA(2)

                        if (LA22_2 == IDENT) :
                            LA22_4 = self.input.LA(3)

                            if ((STRING <= LA22_4 <= SEMI) or (URI <= LA22_4 <= COMMA) or LA22_4 == RBRACE or LA22_4 == IDENT or (COLON <= LA22_4 <= PLUS) or (MINUS <= LA22_4 <= DOT) or (FUNCTION <= LA22_4 <= FREQ)) :
                                alt22 = 1


                        elif (LA22_2 == STRING or LA22_2 == URI or LA22_2 == PLUS or (MINUS <= LA22_2 <= HASH) or LA22_2 == FUNCTION or (NUMBER <= LA22_2 <= FREQ)) :
                            alt22 = 1


                    elif (LA22_0 == STRING or LA22_0 == URI or LA22_0 == IDENT or (SOLIDUS <= LA22_0 <= PLUS) or (MINUS <= LA22_0 <= HASH) or LA22_0 == FUNCTION or (NUMBER <= LA22_0 <= FREQ)) :
                        alt22 = 1


                    if alt22 == 1:
                        # lesscss.g:195:13: operator term
                        pass 
                        self._state.following.append(self.FOLLOW_operator_in_expr1197)
                        operator84 = self.operator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, operator84.tree)
                        self._state.following.append(self.FOLLOW_term_in_expr1199)
                        term85 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term85.tree)


                    else:
                        break #loop22



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "expr"

    class term_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.term_return, self).__init__()

            self.tree = None




    # $ANTLR start "term"
    # lesscss.g:198:1: term : ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ ) | STRING | IDENT | URI | function | hexColor );
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set87 = None
        STRING88 = None
        IDENT89 = None
        URI90 = None
        unaryOperator86 = None

        function91 = None

        hexColor92 = None


        set87_tree = None
        STRING88_tree = None
        IDENT89_tree = None
        URI90_tree = None

        try:
            try:
                # lesscss.g:199:5: ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ ) | STRING | IDENT | URI | function | hexColor )
                alt24 = 6
                LA24 = self.input.LA(1)
                if LA24 == PLUS or LA24 == MINUS or LA24 == NUMBER or LA24 == PERCENTAGE or LA24 == LENGTH or LA24 == EMS or LA24 == EXS or LA24 == ANGLE or LA24 == TIME or LA24 == FREQ:
                    alt24 = 1
                elif LA24 == STRING:
                    alt24 = 2
                elif LA24 == IDENT:
                    LA24_3 = self.input.LA(2)

                    if (LA24_3 == COLON or LA24_3 == DOT) :
                        alt24 = 5
                    elif ((STRING <= LA24_3 <= SEMI) or (URI <= LA24_3 <= COMMA) or LA24_3 == RBRACE or LA24_3 == IDENT or (SOLIDUS <= LA24_3 <= PLUS) or (MINUS <= LA24_3 <= HASH) or (FUNCTION <= LA24_3 <= FREQ)) :
                        alt24 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 24, 3, self.input)

                        raise nvae

                elif LA24 == URI:
                    alt24 = 4
                elif LA24 == FUNCTION:
                    alt24 = 5
                elif LA24 == HASH:
                    alt24 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # lesscss.g:199:7: ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ )
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:199:7: ( unaryOperator )?
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == PLUS or LA23_0 == MINUS) :
                        alt23 = 1
                    if alt23 == 1:
                        # lesscss.g:199:7: unaryOperator
                        pass 
                        self._state.following.append(self.FOLLOW_unaryOperator_in_term1222)
                        unaryOperator86 = self.unaryOperator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, unaryOperator86.tree)



                    set87 = self.input.LT(1)
                    if (NUMBER <= self.input.LA(1) <= FREQ):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set87))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse




                elif alt24 == 2:
                    # lesscss.g:210:7: STRING
                    pass 
                    root_0 = self._adaptor.nil()

                    STRING88=self.match(self.input, STRING, self.FOLLOW_STRING_in_term1379)
                    if self._state.backtracking == 0:

                        STRING88_tree = self._adaptor.createWithPayload(STRING88)
                        self._adaptor.addChild(root_0, STRING88_tree)



                elif alt24 == 3:
                    # lesscss.g:211:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT89=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term1387)
                    if self._state.backtracking == 0:

                        IDENT89_tree = self._adaptor.createWithPayload(IDENT89)
                        self._adaptor.addChild(root_0, IDENT89_tree)



                elif alt24 == 4:
                    # lesscss.g:212:7: URI
                    pass 
                    root_0 = self._adaptor.nil()

                    URI90=self.match(self.input, URI, self.FOLLOW_URI_in_term1395)
                    if self._state.backtracking == 0:

                        URI90_tree = self._adaptor.createWithPayload(URI90)
                        self._adaptor.addChild(root_0, URI90_tree)



                elif alt24 == 5:
                    # lesscss.g:213:7: function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_in_term1403)
                    function91 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function91.tree)


                elif alt24 == 6:
                    # lesscss.g:214:7: hexColor
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_hexColor_in_term1411)
                    hexColor92 = self.hexColor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, hexColor92.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "term"

    class function_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.function_return, self).__init__()

            self.tree = None




    # $ANTLR start "function"
    # lesscss.g:218:1: function : ( fnct_name fnct_args RPAREN | fnct_name expr RPAREN );
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RPAREN95 = None
        RPAREN98 = None
        fnct_name93 = None

        fnct_args94 = None

        fnct_name96 = None

        expr97 = None


        RPAREN95_tree = None
        RPAREN98_tree = None

        try:
            try:
                # lesscss.g:219:5: ( fnct_name fnct_args RPAREN | fnct_name expr RPAREN )
                alt25 = 2
                alt25 = self.dfa25.predict(self.input)
                if alt25 == 1:
                    # lesscss.g:219:7: fnct_name fnct_args RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fnct_name_in_function1429)
                    fnct_name93 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fnct_name93.tree)
                    self._state.following.append(self.FOLLOW_fnct_args_in_function1431)
                    fnct_args94 = self.fnct_args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fnct_args94.tree)
                    RPAREN95=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1433)
                    if self._state.backtracking == 0:

                        RPAREN95_tree = self._adaptor.createWithPayload(RPAREN95)
                        self._adaptor.addChild(root_0, RPAREN95_tree)



                elif alt25 == 2:
                    # lesscss.g:220:7: fnct_name expr RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fnct_name_in_function1441)
                    fnct_name96 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fnct_name96.tree)
                    self._state.following.append(self.FOLLOW_expr_in_function1443)
                    expr97 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr97.tree)
                    RPAREN98=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1445)
                    if self._state.backtracking == 0:

                        RPAREN98_tree = self._adaptor.createWithPayload(RPAREN98)
                        self._adaptor.addChild(root_0, RPAREN98_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "function"

    class fnct_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fnct_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "fnct_name"
    # lesscss.g:223:1: fnct_name : ( IDENT ( COLON | DOT )+ )* FUNCTION ;
    def fnct_name(self, ):

        retval = self.fnct_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT99 = None
        set100 = None
        FUNCTION101 = None

        IDENT99_tree = None
        set100_tree = None
        FUNCTION101_tree = None

        try:
            try:
                # lesscss.g:224:5: ( ( IDENT ( COLON | DOT )+ )* FUNCTION )
                # lesscss.g:224:7: ( IDENT ( COLON | DOT )+ )* FUNCTION
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:224:7: ( IDENT ( COLON | DOT )+ )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == IDENT) :
                        alt27 = 1


                    if alt27 == 1:
                        # lesscss.g:224:8: IDENT ( COLON | DOT )+
                        pass 
                        IDENT99=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name1463)
                        if self._state.backtracking == 0:

                            IDENT99_tree = self._adaptor.createWithPayload(IDENT99)
                            self._adaptor.addChild(root_0, IDENT99_tree)

                        # lesscss.g:224:14: ( COLON | DOT )+
                        cnt26 = 0
                        while True: #loop26
                            alt26 = 2
                            LA26_0 = self.input.LA(1)

                            if (LA26_0 == COLON or LA26_0 == DOT) :
                                alt26 = 1


                            if alt26 == 1:
                                # lesscss.g:
                                pass 
                                set100 = self.input.LT(1)
                                if self.input.LA(1) == COLON or self.input.LA(1) == DOT:
                                    self.input.consume()
                                    if self._state.backtracking == 0:
                                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set100))
                                    self._state.errorRecovery = False

                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed

                                    mse = MismatchedSetException(None, self.input)
                                    raise mse




                            else:
                                if cnt26 >= 1:
                                    break #loop26

                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                eee = EarlyExitException(26, self.input)
                                raise eee

                            cnt26 += 1


                    else:
                        break #loop27
                FUNCTION101=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name1475)
                if self._state.backtracking == 0:

                    FUNCTION101_tree = self._adaptor.createWithPayload(FUNCTION101)
                    self._adaptor.addChild(root_0, FUNCTION101_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fnct_name"

    class fnct_args_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fnct_args_return, self).__init__()

            self.tree = None




    # $ANTLR start "fnct_args"
    # lesscss.g:227:10: fragment fnct_args : fnct_arg ( COMMA fnct_arg )* ;
    def fnct_args(self, ):

        retval = self.fnct_args_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA103 = None
        fnct_arg102 = None

        fnct_arg104 = None


        COMMA103_tree = None

        try:
            try:
                # lesscss.g:228:5: ( fnct_arg ( COMMA fnct_arg )* )
                # lesscss.g:228:7: fnct_arg ( COMMA fnct_arg )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1494)
                fnct_arg102 = self.fnct_arg()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fnct_arg102.tree)
                # lesscss.g:228:16: ( COMMA fnct_arg )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == COMMA) :
                        alt28 = 1


                    if alt28 == 1:
                        # lesscss.g:228:17: COMMA fnct_arg
                        pass 
                        COMMA103=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args1497)
                        if self._state.backtracking == 0:

                            COMMA103_tree = self._adaptor.createWithPayload(COMMA103)
                            self._adaptor.addChild(root_0, COMMA103_tree)

                        self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1499)
                        fnct_arg104 = self.fnct_arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, fnct_arg104.tree)


                    else:
                        break #loop28



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fnct_args"

    class fnct_arg_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fnct_arg_return, self).__init__()

            self.tree = None




    # $ANTLR start "fnct_arg"
    # lesscss.g:231:1: fnct_arg : IDENT OPEQ expr ;
    def fnct_arg(self, ):

        retval = self.fnct_arg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT105 = None
        OPEQ106 = None
        expr107 = None


        IDENT105_tree = None
        OPEQ106_tree = None

        try:
            try:
                # lesscss.g:232:5: ( IDENT OPEQ expr )
                # lesscss.g:232:7: IDENT OPEQ expr
                pass 
                root_0 = self._adaptor.nil()

                IDENT105=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_arg1518)
                if self._state.backtracking == 0:

                    IDENT105_tree = self._adaptor.createWithPayload(IDENT105)
                    self._adaptor.addChild(root_0, IDENT105_tree)

                OPEQ106=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_arg1520)
                if self._state.backtracking == 0:

                    OPEQ106_tree = self._adaptor.createWithPayload(OPEQ106)
                    self._adaptor.addChild(root_0, OPEQ106_tree)

                self._state.following.append(self.FOLLOW_expr_in_fnct_arg1522)
                expr107 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr107.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fnct_arg"

    class hexColor_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.hexColor_return, self).__init__()

            self.tree = None




    # $ANTLR start "hexColor"
    # lesscss.g:235:1: hexColor : HASH ;
    def hexColor(self, ):

        retval = self.hexColor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH108 = None

        HASH108_tree = None

        try:
            try:
                # lesscss.g:236:5: ( HASH )
                # lesscss.g:236:7: HASH
                pass 
                root_0 = self._adaptor.nil()

                HASH108=self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor1539)
                if self._state.backtracking == 0:

                    HASH108_tree = self._adaptor.createWithPayload(HASH108)
                    self._adaptor.addChild(root_0, HASH108_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "hexColor"

    # $ANTLR start "synpred1_lesscss"
    def synpred1_lesscss_fragment(self, ):
        # lesscss.g:133:10: ( esPred )
        # lesscss.g:133:11: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred1_lesscss629)
        self.esPred()

        self._state.following.pop()


    # $ANTLR end "synpred1_lesscss"



    # $ANTLR start "synpred2_lesscss"
    def synpred2_lesscss_fragment(self, ):
        # lesscss.g:135:8: ( esPred )
        # lesscss.g:135:9: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred2_lesscss653)
        self.esPred()

        self._state.following.pop()


    # $ANTLR end "synpred2_lesscss"




    # Delegated rules

    def synpred2_lesscss(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred2_lesscss_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred1_lesscss(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_lesscss_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #13

    DFA13_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA13_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA13_min = DFA.unpack(
        u"\1\11\3\uffff\4\0\3\uffff"
        )

    DFA13_max = DFA.unpack(
        u"\1\30\3\uffff\4\0\3\uffff"
        )

    DFA13_accept = DFA.unpack(
        u"\1\uffff\1\2\10\uffff\1\1"
        )

    DFA13_special = DFA.unpack(
        u"\4\uffff\1\0\1\1\1\2\1\3\3\uffff"
        )

            
    DFA13_transition = [
        DFA.unpack(u"\1\1\1\uffff\1\1\2\uffff\1\1\1\uffff\1\7\1\uffff\2\1"
        u"\1\uffff\1\4\1\5\1\6\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #13

    class DFA13(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA13_4 = input.LA(1)

                 
                index13_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index13_4)
                if s >= 0:
                    return s
            elif s == 1: 
                LA13_5 = input.LA(1)

                 
                index13_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index13_5)
                if s >= 0:
                    return s
            elif s == 2: 
                LA13_6 = input.LA(1)

                 
                index13_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index13_6)
                if s >= 0:
                    return s
            elif s == 3: 
                LA13_7 = input.LA(1)

                 
                index13_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index13_7)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 13, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #25

    DFA25_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA25_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA25_min = DFA.unpack(
        u"\1\16\1\20\1\5\1\16\1\5\2\uffff"
        )

    DFA25_max = DFA.unpack(
        u"\1\35\1\26\1\47\1\35\1\47\2\uffff"
        )

    DFA25_accept = DFA.unpack(
        u"\5\uffff\1\2\1\1"
        )

    DFA25_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA25_transition = [
        DFA.unpack(u"\1\1\16\uffff\1\2"),
        DFA.unpack(u"\1\3\5\uffff\1\3"),
        DFA.unpack(u"\1\5\2\uffff\1\5\5\uffff\1\4\3\uffff\1\5\1\uffff\2"
        u"\5\7\uffff\1\5\2\uffff\10\5"),
        DFA.unpack(u"\1\1\1\uffff\1\3\5\uffff\1\3\6\uffff\1\2"),
        DFA.unpack(u"\1\5\2\uffff\2\5\4\uffff\1\5\1\uffff\3\5\1\uffff\3"
        u"\5\2\uffff\1\6\3\uffff\2\5\1\uffff\10\5"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #25

    class DFA25(DFA):
        pass


 

    FOLLOW_charSet_in_styleSheet73 = frozenset([7, 10, 13, 14, 15, 16, 21, 22, 23, 24])
    FOLLOW_imports_in_styleSheet83 = frozenset([7, 10, 13, 14, 15, 16, 21, 22, 23, 24])
    FOLLOW_bodylist_in_styleSheet94 = frozenset([])
    FOLLOW_EOF_in_styleSheet101 = frozenset([1])
    FOLLOW_CHARSET_SYM_in_charSet127 = frozenset([5])
    FOLLOW_STRING_in_charSet129 = frozenset([6])
    FOLLOW_SEMI_in_charSet131 = frozenset([1])
    FOLLOW_IMPORT_SYM_in_imports159 = frozenset([5, 8])
    FOLLOW_set_in_imports161 = frozenset([6, 14])
    FOLLOW_medium_in_imports168 = frozenset([6, 9])
    FOLLOW_COMMA_in_imports171 = frozenset([14])
    FOLLOW_medium_in_imports173 = frozenset([6, 9])
    FOLLOW_SEMI_in_imports179 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media200 = frozenset([14])
    FOLLOW_medium_in_media202 = frozenset([9, 11])
    FOLLOW_COMMA_in_media205 = frozenset([14])
    FOLLOW_medium_in_media207 = frozenset([9, 11])
    FOLLOW_LBRACE_in_media219 = frozenset([14, 16, 21, 22, 23, 24])
    FOLLOW_ruleSet_in_media233 = frozenset([12])
    FOLLOW_RBRACE_in_media243 = frozenset([1])
    FOLLOW_FONTFACE_SYM_in_fontface264 = frozenset([11])
    FOLLOW_LBRACE_in_fontface266 = frozenset([14])
    FOLLOW_declarationset_in_fontface268 = frozenset([12])
    FOLLOW_RBRACE_in_fontface270 = frozenset([1])
    FOLLOW_IDENT_in_medium290 = frozenset([1])
    FOLLOW_bodyset_in_bodylist313 = frozenset([1, 10, 13, 14, 15, 16, 21, 22, 23, 24])
    FOLLOW_ruleSet_in_bodyset335 = frozenset([1])
    FOLLOW_media_in_bodyset343 = frozenset([1])
    FOLLOW_page_in_bodyset351 = frozenset([1])
    FOLLOW_fontface_in_bodyset359 = frozenset([1])
    FOLLOW_PAGE_SYM_in_page383 = frozenset([11, 16])
    FOLLOW_pseudoPage_in_page385 = frozenset([11])
    FOLLOW_LBRACE_in_page388 = frozenset([14])
    FOLLOW_declarationset_in_page390 = frozenset([12])
    FOLLOW_RBRACE_in_page392 = frozenset([1])
    FOLLOW_COLON_in_pseudoPage413 = frozenset([14])
    FOLLOW_IDENT_in_pseudoPage415 = frozenset([1])
    FOLLOW_SOLIDUS_in_operator436 = frozenset([1])
    FOLLOW_COMMA_in_operator444 = frozenset([1])
    FOLLOW_PLUS_in_combinator471 = frozenset([1])
    FOLLOW_GREATER_in_combinator479 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_IDENT_in_property537 = frozenset([1])
    FOLLOW_selector_in_ruleSet558 = frozenset([9, 11])
    FOLLOW_COMMA_in_ruleSet561 = frozenset([14, 16, 21, 22, 23, 24])
    FOLLOW_selector_in_ruleSet563 = frozenset([9, 11])
    FOLLOW_LBRACE_in_ruleSet567 = frozenset([14])
    FOLLOW_declarationset_in_ruleSet569 = frozenset([12])
    FOLLOW_RBRACE_in_ruleSet571 = frozenset([1])
    FOLLOW_simpleSelector_in_selector592 = frozenset([1, 14, 16, 18, 19, 21, 22, 23, 24])
    FOLLOW_combinator_in_selector595 = frozenset([14, 16, 21, 22, 23, 24])
    FOLLOW_simpleSelector_in_selector597 = frozenset([1, 14, 16, 18, 19, 21, 22, 23, 24])
    FOLLOW_elementName_in_simpleSelector616 = frozenset([1, 14, 16, 21, 22, 23, 24])
    FOLLOW_elementSubsequent_in_simpleSelector632 = frozenset([1, 14, 16, 21, 22, 23, 24])
    FOLLOW_elementSubsequent_in_simpleSelector656 = frozenset([1, 14, 16, 21, 22, 23, 24])
    FOLLOW_set_in_esPred0 = frozenset([1])
    FOLLOW_HASH_in_elementSubsequent712 = frozenset([1])
    FOLLOW_cssClass_in_elementSubsequent720 = frozenset([1])
    FOLLOW_attrib_in_elementSubsequent728 = frozenset([1])
    FOLLOW_pseudo_in_elementSubsequent736 = frozenset([1])
    FOLLOW_DOT_in_cssClass757 = frozenset([14])
    FOLLOW_IDENT_in_cssClass759 = frozenset([1])
    FOLLOW_set_in_elementName0 = frozenset([1])
    FOLLOW_LBRACKET_in_attrib809 = frozenset([14])
    FOLLOW_IDENT_in_attrib824 = frozenset([25, 26, 27, 28])
    FOLLOW_set_in_attrib865 = frozenset([5, 14])
    FOLLOW_set_in_attrib973 = frozenset([28])
    FOLLOW_RBRACKET_in_attrib1074 = frozenset([1])
    FOLLOW_COLON_in_pseudo1087 = frozenset([14, 29])
    FOLLOW_IDENT_in_pseudo1091 = frozenset([1])
    FOLLOW_FUNCTION_in_pseudo1095 = frozenset([5, 8, 14, 18, 20, 21, 29, 32, 33, 34, 35, 36, 37, 38, 39])
    FOLLOW_expr_in_pseudo1097 = frozenset([30])
    FOLLOW_RPAREN_in_pseudo1099 = frozenset([1])
    FOLLOW_declaration_in_declarationset1118 = frozenset([1, 6])
    FOLLOW_SEMI_in_declarationset1121 = frozenset([14])
    FOLLOW_declaration_in_declarationset1123 = frozenset([1, 6])
    FOLLOW_SEMI_in_declarationset1127 = frozenset([1])
    FOLLOW_property_in_declaration1145 = frozenset([16])
    FOLLOW_COLON_in_declaration1147 = frozenset([5, 8, 14, 18, 20, 21, 29, 32, 33, 34, 35, 36, 37, 38, 39])
    FOLLOW_expr_in_declaration1149 = frozenset([1, 31])
    FOLLOW_prio_in_declaration1151 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1173 = frozenset([1])
    FOLLOW_term_in_expr1194 = frozenset([1, 5, 8, 9, 14, 17, 18, 20, 21, 29, 32, 33, 34, 35, 36, 37, 38, 39])
    FOLLOW_operator_in_expr1197 = frozenset([5, 8, 14, 18, 20, 21, 29, 32, 33, 34, 35, 36, 37, 38, 39])
    FOLLOW_term_in_expr1199 = frozenset([1, 5, 8, 9, 14, 17, 18, 20, 21, 29, 32, 33, 34, 35, 36, 37, 38, 39])
    FOLLOW_unaryOperator_in_term1222 = frozenset([32, 33, 34, 35, 36, 37, 38, 39])
    FOLLOW_set_in_term1233 = frozenset([1])
    FOLLOW_STRING_in_term1379 = frozenset([1])
    FOLLOW_IDENT_in_term1387 = frozenset([1])
    FOLLOW_URI_in_term1395 = frozenset([1])
    FOLLOW_function_in_term1403 = frozenset([1])
    FOLLOW_hexColor_in_term1411 = frozenset([1])
    FOLLOW_fnct_name_in_function1429 = frozenset([14])
    FOLLOW_fnct_args_in_function1431 = frozenset([30])
    FOLLOW_RPAREN_in_function1433 = frozenset([1])
    FOLLOW_fnct_name_in_function1441 = frozenset([5, 8, 14, 18, 20, 21, 29, 32, 33, 34, 35, 36, 37, 38, 39])
    FOLLOW_expr_in_function1443 = frozenset([30])
    FOLLOW_RPAREN_in_function1445 = frozenset([1])
    FOLLOW_IDENT_in_fnct_name1463 = frozenset([16, 22])
    FOLLOW_set_in_fnct_name1465 = frozenset([14, 16, 22, 29])
    FOLLOW_FUNCTION_in_fnct_name1475 = frozenset([1])
    FOLLOW_fnct_arg_in_fnct_args1494 = frozenset([1, 9])
    FOLLOW_COMMA_in_fnct_args1497 = frozenset([14])
    FOLLOW_fnct_arg_in_fnct_args1499 = frozenset([1, 9])
    FOLLOW_IDENT_in_fnct_arg1518 = frozenset([25])
    FOLLOW_OPEQ_in_fnct_arg1520 = frozenset([5, 8, 14, 18, 20, 21, 29, 32, 33, 34, 35, 36, 37, 38, 39])
    FOLLOW_expr_in_fnct_arg1522 = frozenset([1])
    FOLLOW_HASH_in_hexColor1539 = frozenset([1])
    FOLLOW_esPred_in_synpred1_lesscss629 = frozenset([1])
    FOLLOW_esPred_in_synpred2_lesscss653 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("lesscssLexer", lesscssParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
