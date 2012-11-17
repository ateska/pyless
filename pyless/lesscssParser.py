# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 lesscss.g 2012-11-17 13:38:57

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=36
STAR=30
EOF=-1
MEDIA_SYM=23
INCLUDES=40
LBRACKET=35
RPAREN=37
NAME=59
GREATER=32
ESCAPE=56
DIMENSION=93
STRINGESC=91
NL=94
COMMENT=87
N_Media=9
D=64
E=65
F=66
G=67
A=61
RBRACE=25
B=62
C=63
L=72
IMPORT_SYM=20
NMCHAR=58
M=73
N=74
O=75
H=68
I=69
J=70
NUMBER=44
K=71
U=81
T=80
W=83
V=82
Q=77
P=76
S=79
R=78
CDO=88
CDC=89
PERCENTAGE=45
URL=60
Y=85
X=84
URI=22
Z=86
PAGE_SYM=28
WS=92
DASHMATCH=41
EMS=47
N_RuleSet=10
NONASCII=54
N_Page=8
N_Declarations=12
N_Selector=11
LBRACE=24
N_Import=6
LENGTH=46
LPAREN=90
IMPORTANT_SYM=42
N_Function=14
TIME=50
COMMA=21
N_StyleSheet=4
IDENT=26
PLUS=31
FREQ=51
RBRACKET=38
DOT=34
CHARSET_SYM=17
ANGLE=49
HASH=33
HEXCHAR=53
N_CharSet=5
MINUS=52
SOLIDUS=43
SEMI=19
UNICODE=55
COLON=29
NMSTART=57
N_Declaration=13
OPEQ=39
FONTFACE_SYM=27
EXS=48
N_Space=16
N_Attrib=15
N_FontFace=7
STRING=18

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "N_StyleSheet", "N_CharSet", "N_Import", "N_FontFace", "N_Page", "N_Media", 
    "N_RuleSet", "N_Selector", "N_Declarations", "N_Declaration", "N_Function", 
    "N_Attrib", "N_Space", "CHARSET_SYM", "STRING", "SEMI", "IMPORT_SYM", 
    "COMMA", "URI", "MEDIA_SYM", "LBRACE", "RBRACE", "IDENT", "FONTFACE_SYM", 
    "PAGE_SYM", "COLON", "STAR", "PLUS", "GREATER", "HASH", "DOT", "LBRACKET", 
    "FUNCTION", "RPAREN", "RBRACKET", "OPEQ", "INCLUDES", "DASHMATCH", "IMPORTANT_SYM", 
    "SOLIDUS", "NUMBER", "PERCENTAGE", "LENGTH", "EMS", "EXS", "ANGLE", 
    "TIME", "FREQ", "MINUS", "HEXCHAR", "NONASCII", "UNICODE", "ESCAPE", 
    "NMSTART", "NMCHAR", "NAME", "URL", "A", "B", "C", "D", "E", "F", "G", 
    "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", 
    "V", "W", "X", "Y", "Z", "COMMENT", "CDO", "CDC", "LPAREN", "STRINGESC", 
    "WS", "DIMENSION", "NL"
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

        self.dfa14 = self.DFA14(
            self, 14,
            eot = self.DFA14_eot,
            eof = self.DFA14_eof,
            min = self.DFA14_min,
            max = self.DFA14_max,
            accept = self.DFA14_accept,
            special = self.DFA14_special,
            transition = self.DFA14_transition
            )

        self.dfa27 = self.DFA27(
            self, 27,
            eot = self.DFA27_eot,
            eof = self.DFA27_eof,
            min = self.DFA27_min,
            max = self.DFA27_max,
            accept = self.DFA27_accept,
            special = self.DFA27_special,
            transition = self.DFA27_transition
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
    # lesscss.g:50:1: styleSheet : ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* bodylist ) ;
    def styleSheet(self, ):

        retval = self.styleSheet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF4 = None
        charSet1 = None

        imports2 = None

        bodylist3 = None


        EOF4_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_bodylist = RewriteRuleSubtreeStream(self._adaptor, "rule bodylist")
        stream_charSet = RewriteRuleSubtreeStream(self._adaptor, "rule charSet")
        stream_imports = RewriteRuleSubtreeStream(self._adaptor, "rule imports")
        try:
            try:
                # lesscss.g:51:5: ( ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* bodylist ) )
                # lesscss.g:51:9: ( charSet )? ( imports )* bodylist EOF
                pass 
                # lesscss.g:51:9: ( charSet )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == CHARSET_SYM) :
                    alt1 = 1
                if alt1 == 1:
                    # lesscss.g:51:9: charSet
                    pass 
                    self._state.following.append(self.FOLLOW_charSet_in_styleSheet169)
                    charSet1 = self.charSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_charSet.add(charSet1.tree)



                # lesscss.g:52:9: ( imports )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == IMPORT_SYM) :
                        alt2 = 1


                    if alt2 == 1:
                        # lesscss.g:52:9: imports
                        pass 
                        self._state.following.append(self.FOLLOW_imports_in_styleSheet180)
                        imports2 = self.imports()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_imports.add(imports2.tree)


                    else:
                        break #loop2
                self._state.following.append(self.FOLLOW_bodylist_in_styleSheet191)
                bodylist3 = self.bodylist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_bodylist.add(bodylist3.tree)
                EOF4=self.match(self.input, EOF, self.FOLLOW_EOF_in_styleSheet201) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF4)

                # AST Rewrite
                # elements: bodylist, imports, charSet
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 55:13: -> ^( N_StyleSheet ( charSet )? ( imports )* bodylist )
                    # lesscss.g:55:16: ^( N_StyleSheet ( charSet )? ( imports )* bodylist )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_StyleSheet, "N_StyleSheet"), root_1)

                    # lesscss.g:55:31: ( charSet )?
                    if stream_charSet.hasNext():
                        self._adaptor.addChild(root_1, stream_charSet.nextTree())


                    stream_charSet.reset();
                    # lesscss.g:55:40: ( imports )*
                    while stream_imports.hasNext():
                        self._adaptor.addChild(root_1, stream_imports.nextTree())


                    stream_imports.reset();
                    self._adaptor.addChild(root_1, stream_bodylist.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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
    # lesscss.g:61:1: charSet : CHARSET_SYM STRING SEMI -> ^( N_CharSet STRING ) ;
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
        stream_CHARSET_SYM = RewriteRuleTokenStream(self._adaptor, "token CHARSET_SYM")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")

        try:
            try:
                # lesscss.g:62:5: ( CHARSET_SYM STRING SEMI -> ^( N_CharSet STRING ) )
                # lesscss.g:62:9: CHARSET_SYM STRING SEMI
                pass 
                CHARSET_SYM5=self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet253) 
                if self._state.backtracking == 0:
                    stream_CHARSET_SYM.add(CHARSET_SYM5)
                STRING6=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet255) 
                if self._state.backtracking == 0:
                    stream_STRING.add(STRING6)
                SEMI7=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_charSet257) 
                if self._state.backtracking == 0:
                    stream_SEMI.add(SEMI7)

                # AST Rewrite
                # elements: STRING
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 63:9: -> ^( N_CharSet STRING )
                    # lesscss.g:63:12: ^( N_CharSet STRING )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_CharSet, "N_CharSet"), root_1)

                    self._adaptor.addChild(root_1, stream_STRING.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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
    # lesscss.g:69:1: imports : IMPORT_SYM importUrl ( medium ( COMMA medium )* )? SEMI -> ^( N_Import importUrl ( medium )* ) ;
    def imports(self, ):

        retval = self.imports_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORT_SYM8 = None
        COMMA11 = None
        SEMI13 = None
        importUrl9 = None

        medium10 = None

        medium12 = None


        IMPORT_SYM8_tree = None
        COMMA11_tree = None
        SEMI13_tree = None
        stream_IMPORT_SYM = RewriteRuleTokenStream(self._adaptor, "token IMPORT_SYM")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_importUrl = RewriteRuleSubtreeStream(self._adaptor, "rule importUrl")
        stream_medium = RewriteRuleSubtreeStream(self._adaptor, "rule medium")
        try:
            try:
                # lesscss.g:70:5: ( IMPORT_SYM importUrl ( medium ( COMMA medium )* )? SEMI -> ^( N_Import importUrl ( medium )* ) )
                # lesscss.g:70:9: IMPORT_SYM importUrl ( medium ( COMMA medium )* )? SEMI
                pass 
                IMPORT_SYM8=self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports295) 
                if self._state.backtracking == 0:
                    stream_IMPORT_SYM.add(IMPORT_SYM8)
                self._state.following.append(self.FOLLOW_importUrl_in_imports297)
                importUrl9 = self.importUrl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_importUrl.add(importUrl9.tree)
                # lesscss.g:70:30: ( medium ( COMMA medium )* )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == IDENT) :
                    alt4 = 1
                if alt4 == 1:
                    # lesscss.g:70:31: medium ( COMMA medium )*
                    pass 
                    self._state.following.append(self.FOLLOW_medium_in_imports300)
                    medium10 = self.medium()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_medium.add(medium10.tree)
                    # lesscss.g:70:38: ( COMMA medium )*
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == COMMA) :
                            alt3 = 1


                        if alt3 == 1:
                            # lesscss.g:70:39: COMMA medium
                            pass 
                            COMMA11=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_imports303) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA11)
                            self._state.following.append(self.FOLLOW_medium_in_imports305)
                            medium12 = self.medium()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_medium.add(medium12.tree)


                        else:
                            break #loop3



                SEMI13=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_imports311) 
                if self._state.backtracking == 0:
                    stream_SEMI.add(SEMI13)

                # AST Rewrite
                # elements: importUrl, medium
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 71:9: -> ^( N_Import importUrl ( medium )* )
                    # lesscss.g:71:12: ^( N_Import importUrl ( medium )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Import, "N_Import"), root_1)

                    self._adaptor.addChild(root_1, stream_importUrl.nextTree())
                    # lesscss.g:71:33: ( medium )*
                    while stream_medium.hasNext():
                        self._adaptor.addChild(root_1, stream_medium.nextTree())


                    stream_medium.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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

    class importUrl_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.importUrl_return, self).__init__()

            self.tree = None




    # $ANTLR start "importUrl"
    # lesscss.g:74:1: importUrl : ( STRING | URI );
    def importUrl(self, ):

        retval = self.importUrl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set14 = None

        set14_tree = None

        try:
            try:
                # lesscss.g:75:5: ( STRING | URI )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set14 = self.input.LT(1)
                if self.input.LA(1) == STRING or self.input.LA(1) == URI:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set14))
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

    # $ANTLR end "importUrl"

    class media_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_return, self).__init__()

            self.tree = None




    # $ANTLR start "media"
    # lesscss.g:83:1: media : MEDIA_SYM medium ( COMMA medium )* LBRACE ( ruleSet )* RBRACE -> ^( N_Media ( medium )+ ( ruleSet )* ) ;
    def media(self, ):

        retval = self.media_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MEDIA_SYM15 = None
        COMMA17 = None
        LBRACE19 = None
        RBRACE21 = None
        medium16 = None

        medium18 = None

        ruleSet20 = None


        MEDIA_SYM15_tree = None
        COMMA17_tree = None
        LBRACE19_tree = None
        RBRACE21_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_MEDIA_SYM = RewriteRuleTokenStream(self._adaptor, "token MEDIA_SYM")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_medium = RewriteRuleSubtreeStream(self._adaptor, "rule medium")
        stream_ruleSet = RewriteRuleSubtreeStream(self._adaptor, "rule ruleSet")
        try:
            try:
                # lesscss.g:84:5: ( MEDIA_SYM medium ( COMMA medium )* LBRACE ( ruleSet )* RBRACE -> ^( N_Media ( medium )+ ( ruleSet )* ) )
                # lesscss.g:84:7: MEDIA_SYM medium ( COMMA medium )* LBRACE ( ruleSet )* RBRACE
                pass 
                MEDIA_SYM15=self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media376) 
                if self._state.backtracking == 0:
                    stream_MEDIA_SYM.add(MEDIA_SYM15)
                self._state.following.append(self.FOLLOW_medium_in_media378)
                medium16 = self.medium()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_medium.add(medium16.tree)
                # lesscss.g:84:24: ( COMMA medium )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == COMMA) :
                        alt5 = 1


                    if alt5 == 1:
                        # lesscss.g:84:25: COMMA medium
                        pass 
                        COMMA17=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_media381) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA17)
                        self._state.following.append(self.FOLLOW_medium_in_media383)
                        medium18 = self.medium()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_medium.add(medium18.tree)


                    else:
                        break #loop5
                LBRACE19=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_media395) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE19)
                # lesscss.g:86:13: ( ruleSet )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == IDENT or (COLON <= LA6_0 <= STAR) or (HASH <= LA6_0 <= LBRACKET)) :
                        alt6 = 1


                    if alt6 == 1:
                        # lesscss.g:86:13: ruleSet
                        pass 
                        self._state.following.append(self.FOLLOW_ruleSet_in_media409)
                        ruleSet20 = self.ruleSet()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_ruleSet.add(ruleSet20.tree)


                    else:
                        break #loop6
                RBRACE21=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_media420) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE21)

                # AST Rewrite
                # elements: medium, ruleSet
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 88:9: -> ^( N_Media ( medium )+ ( ruleSet )* )
                    # lesscss.g:88:12: ^( N_Media ( medium )+ ( ruleSet )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Media, "N_Media"), root_1)

                    # lesscss.g:88:22: ( medium )+
                    if not (stream_medium.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_medium.hasNext():
                        self._adaptor.addChild(root_1, stream_medium.nextTree())


                    stream_medium.reset()
                    # lesscss.g:88:30: ( ruleSet )*
                    while stream_ruleSet.hasNext():
                        self._adaptor.addChild(root_1, stream_ruleSet.nextTree())


                    stream_ruleSet.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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

    class medium_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.medium_return, self).__init__()

            self.tree = None




    # $ANTLR start "medium"
    # lesscss.g:94:1: medium : IDENT ;
    def medium(self, ):

        retval = self.medium_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT22 = None

        IDENT22_tree = None

        try:
            try:
                # lesscss.g:95:5: ( IDENT )
                # lesscss.g:95:7: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT22=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_medium460)
                if self._state.backtracking == 0:

                    IDENT22_tree = self._adaptor.createWithPayload(IDENT22)
                    self._adaptor.addChild(root_0, IDENT22_tree)




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

    class fontface_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fontface_return, self).__init__()

            self.tree = None




    # $ANTLR start "fontface"
    # lesscss.g:101:1: fontface : FONTFACE_SYM LBRACE declarationset RBRACE -> ^( N_FontFace declarationset ) ;
    def fontface(self, ):

        retval = self.fontface_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FONTFACE_SYM23 = None
        LBRACE24 = None
        RBRACE26 = None
        declarationset25 = None


        FONTFACE_SYM23_tree = None
        LBRACE24_tree = None
        RBRACE26_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_FONTFACE_SYM = RewriteRuleTokenStream(self._adaptor, "token FONTFACE_SYM")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        try:
            try:
                # lesscss.g:102:5: ( FONTFACE_SYM LBRACE declarationset RBRACE -> ^( N_FontFace declarationset ) )
                # lesscss.g:102:7: FONTFACE_SYM LBRACE declarationset RBRACE
                pass 
                FONTFACE_SYM23=self.match(self.input, FONTFACE_SYM, self.FOLLOW_FONTFACE_SYM_in_fontface481) 
                if self._state.backtracking == 0:
                    stream_FONTFACE_SYM.add(FONTFACE_SYM23)
                LBRACE24=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_fontface483) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE24)
                self._state.following.append(self.FOLLOW_declarationset_in_fontface485)
                declarationset25 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset25.tree)
                RBRACE26=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_fontface487) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE26)

                # AST Rewrite
                # elements: declarationset
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 103:9: -> ^( N_FontFace declarationset )
                    # lesscss.g:103:12: ^( N_FontFace declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_FontFace, "N_FontFace"), root_1)

                    self._adaptor.addChild(root_1, stream_declarationset.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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

    class bodylist_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.bodylist_return, self).__init__()

            self.tree = None




    # $ANTLR start "bodylist"
    # lesscss.g:106:1: bodylist : ( bodyset )* ;
    def bodylist(self, ):

        retval = self.bodylist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        bodyset27 = None



        try:
            try:
                # lesscss.g:107:5: ( ( bodyset )* )
                # lesscss.g:107:7: ( bodyset )*
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:107:7: ( bodyset )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == MEDIA_SYM or (IDENT <= LA7_0 <= STAR) or (HASH <= LA7_0 <= LBRACKET)) :
                        alt7 = 1


                    if alt7 == 1:
                        # lesscss.g:107:7: bodyset
                        pass 
                        self._state.following.append(self.FOLLOW_bodyset_in_bodylist524)
                        bodyset27 = self.bodyset()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, bodyset27.tree)


                    else:
                        break #loop7



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
    # lesscss.g:110:1: bodyset : ( ruleSet | media | page | fontface );
    def bodyset(self, ):

        retval = self.bodyset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ruleSet28 = None

        media29 = None

        page30 = None

        fontface31 = None



        try:
            try:
                # lesscss.g:111:5: ( ruleSet | media | page | fontface )
                alt8 = 4
                LA8 = self.input.LA(1)
                if LA8 == IDENT or LA8 == COLON or LA8 == STAR or LA8 == HASH or LA8 == DOT or LA8 == LBRACKET:
                    alt8 = 1
                elif LA8 == MEDIA_SYM:
                    alt8 = 2
                elif LA8 == PAGE_SYM:
                    alt8 = 3
                elif LA8 == FONTFACE_SYM:
                    alt8 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # lesscss.g:111:7: ruleSet
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_ruleSet_in_bodyset542)
                    ruleSet28 = self.ruleSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, ruleSet28.tree)


                elif alt8 == 2:
                    # lesscss.g:112:7: media
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_media_in_bodyset550)
                    media29 = self.media()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media29.tree)


                elif alt8 == 3:
                    # lesscss.g:113:7: page
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_page_in_bodyset558)
                    page30 = self.page()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, page30.tree)


                elif alt8 == 4:
                    # lesscss.g:114:7: fontface
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fontface_in_bodyset566)
                    fontface31 = self.fontface()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fontface31.tree)


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
    # lesscss.g:117:1: page : PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE -> ^( N_Page ( pseudoPage )? declarationset ) ;
    def page(self, ):

        retval = self.page_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PAGE_SYM32 = None
        LBRACE34 = None
        RBRACE36 = None
        pseudoPage33 = None

        declarationset35 = None


        PAGE_SYM32_tree = None
        LBRACE34_tree = None
        RBRACE36_tree = None
        stream_PAGE_SYM = RewriteRuleTokenStream(self._adaptor, "token PAGE_SYM")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        stream_pseudoPage = RewriteRuleSubtreeStream(self._adaptor, "rule pseudoPage")
        try:
            try:
                # lesscss.g:118:5: ( PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE -> ^( N_Page ( pseudoPage )? declarationset ) )
                # lesscss.g:118:7: PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE
                pass 
                PAGE_SYM32=self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page586) 
                if self._state.backtracking == 0:
                    stream_PAGE_SYM.add(PAGE_SYM32)
                # lesscss.g:118:16: ( pseudoPage )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == COLON) :
                    alt9 = 1
                if alt9 == 1:
                    # lesscss.g:118:16: pseudoPage
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoPage_in_page588)
                    pseudoPage33 = self.pseudoPage()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_pseudoPage.add(pseudoPage33.tree)



                LBRACE34=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_page591) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE34)
                self._state.following.append(self.FOLLOW_declarationset_in_page593)
                declarationset35 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset35.tree)
                RBRACE36=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_page595) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE36)

                # AST Rewrite
                # elements: pseudoPage, declarationset
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 119:9: -> ^( N_Page ( pseudoPage )? declarationset )
                    # lesscss.g:119:12: ^( N_Page ( pseudoPage )? declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Page, "N_Page"), root_1)

                    # lesscss.g:119:21: ( pseudoPage )?
                    if stream_pseudoPage.hasNext():
                        self._adaptor.addChild(root_1, stream_pseudoPage.nextTree())


                    stream_pseudoPage.reset();
                    self._adaptor.addChild(root_1, stream_declarationset.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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
    # lesscss.g:122:1: pseudoPage : COLON IDENT -> IDENT ;
    def pseudoPage(self, ):

        retval = self.pseudoPage_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON37 = None
        IDENT38 = None

        COLON37_tree = None
        IDENT38_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")

        try:
            try:
                # lesscss.g:123:5: ( COLON IDENT -> IDENT )
                # lesscss.g:123:7: COLON IDENT
                pass 
                COLON37=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudoPage631) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON37)
                IDENT38=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage633) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT38)

                # AST Rewrite
                # elements: IDENT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 123:19: -> IDENT
                    self._adaptor.addChild(root_0, stream_IDENT.nextNode())



                    retval.tree = root_0



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

    class property_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.property_return, self).__init__()

            self.tree = None




    # $ANTLR start "property"
    # lesscss.g:126:1: property : ( IDENT | STAR a= IDENT -> IDENT );
    def property(self, ):

        retval = self.property_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        IDENT39 = None
        STAR40 = None

        a_tree = None
        IDENT39_tree = None
        STAR40_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_STAR = RewriteRuleTokenStream(self._adaptor, "token STAR")

        try:
            try:
                # lesscss.g:127:5: ( IDENT | STAR a= IDENT -> IDENT )
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == IDENT) :
                    alt10 = 1
                elif (LA10_0 == STAR) :
                    alt10 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # lesscss.g:127:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT39=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property658)
                    if self._state.backtracking == 0:

                        IDENT39_tree = self._adaptor.createWithPayload(IDENT39)
                        self._adaptor.addChild(root_0, IDENT39_tree)



                elif alt10 == 2:
                    # lesscss.g:131:7: STAR a= IDENT
                    pass 
                    STAR40=self.match(self.input, STAR, self.FOLLOW_STAR_in_property677) 
                    if self._state.backtracking == 0:
                        stream_STAR.add(STAR40)
                    a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property681) 
                    if self._state.backtracking == 0:
                        stream_IDENT.add(a)
                    if self._state.backtracking == 0:
                        a.setText('*' + a.getText()); 


                    # AST Rewrite
                    # elements: IDENT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 133:9: -> IDENT
                        self._adaptor.addChild(root_0, stream_IDENT.nextNode())



                        retval.tree = root_0


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
    # lesscss.g:137:1: ruleSet : selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) ;
    def ruleSet(self, ):

        retval = self.ruleSet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA42 = None
        LBRACE44 = None
        RBRACE46 = None
        selector41 = None

        selector43 = None

        declarationset45 = None


        COMMA42_tree = None
        LBRACE44_tree = None
        RBRACE46_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_selector = RewriteRuleSubtreeStream(self._adaptor, "rule selector")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        try:
            try:
                # lesscss.g:138:5: ( selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) )
                # lesscss.g:138:7: selector ( COMMA selector )* LBRACE declarationset RBRACE
                pass 
                self._state.following.append(self.FOLLOW_selector_in_ruleSet722)
                selector41 = self.selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_selector.add(selector41.tree)
                # lesscss.g:138:16: ( COMMA selector )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == COMMA) :
                        alt11 = 1


                    if alt11 == 1:
                        # lesscss.g:138:17: COMMA selector
                        pass 
                        COMMA42=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_ruleSet725) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA42)
                        self._state.following.append(self.FOLLOW_selector_in_ruleSet727)
                        selector43 = self.selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_selector.add(selector43.tree)


                    else:
                        break #loop11
                LBRACE44=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_ruleSet731) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE44)
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet733)
                declarationset45 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset45.tree)
                RBRACE46=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_ruleSet735) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE46)

                # AST Rewrite
                # elements: declarationset, selector
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 139:9: -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    # lesscss.g:139:12: ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_RuleSet, "N_RuleSet"), root_1)

                    # lesscss.g:139:24: ( ^( N_Selector selector ) )+
                    if not (stream_selector.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_selector.hasNext():
                        # lesscss.g:139:24: ^( N_Selector selector )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Selector, "N_Selector"), root_2)

                        self._adaptor.addChild(root_2, stream_selector.nextTree())

                        self._adaptor.addChild(root_1, root_2)


                    stream_selector.reset()
                    self._adaptor.addChild(root_1, stream_declarationset.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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
    # lesscss.g:142:1: selector : simpleSelector ( combinator simpleSelector )* ;
    def selector(self, ):

        retval = self.selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        simpleSelector47 = None

        combinator48 = None

        simpleSelector49 = None



        try:
            try:
                # lesscss.g:143:5: ( simpleSelector ( combinator simpleSelector )* )
                # lesscss.g:143:7: simpleSelector ( combinator simpleSelector )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_simpleSelector_in_selector775)
                simpleSelector47 = self.simpleSelector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, simpleSelector47.tree)
                # lesscss.g:143:22: ( combinator simpleSelector )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == IDENT or (COLON <= LA12_0 <= LBRACKET)) :
                        alt12 = 1


                    if alt12 == 1:
                        # lesscss.g:143:23: combinator simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector778)
                        combinator48 = self.combinator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, combinator48.tree)
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector780)
                        simpleSelector49 = self.simpleSelector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, simpleSelector49.tree)


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

    class combinator_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.combinator_return, self).__init__()

            self.tree = None




    # $ANTLR start "combinator"
    # lesscss.g:146:1: combinator : ( PLUS | GREATER | );
    def combinator(self, ):

        retval = self.combinator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS50 = None
        GREATER51 = None

        PLUS50_tree = None
        GREATER51_tree = None

        try:
            try:
                # lesscss.g:147:5: ( PLUS | GREATER | )
                alt13 = 3
                LA13 = self.input.LA(1)
                if LA13 == PLUS:
                    alt13 = 1
                elif LA13 == GREATER:
                    alt13 = 2
                elif LA13 == IDENT or LA13 == COLON or LA13 == STAR or LA13 == HASH or LA13 == DOT or LA13 == LBRACKET:
                    alt13 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # lesscss.g:147:7: PLUS
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS50=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator799)
                    if self._state.backtracking == 0:

                        PLUS50_tree = self._adaptor.createWithPayload(PLUS50)
                        self._adaptor.addChild(root_0, PLUS50_tree)



                elif alt13 == 2:
                    # lesscss.g:148:7: GREATER
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER51=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator807)
                    if self._state.backtracking == 0:

                        GREATER51_tree = self._adaptor.createWithPayload(GREATER51)
                        self._adaptor.addChild(root_0, GREATER51_tree)



                elif alt13 == 3:
                    # lesscss.g:150:5: 
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

    class simpleSelector_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.simpleSelector_return, self).__init__()

            self.tree = None




    # $ANTLR start "simpleSelector"
    # lesscss.g:152:1: simpleSelector : ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ );
    def simpleSelector(self, ):

        retval = self.simpleSelector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        elementName52 = None

        elementSubsequent53 = None

        elementSubsequent54 = None



        try:
            try:
                # lesscss.g:153:5: ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == IDENT or LA16_0 == STAR) :
                    alt16 = 1
                elif (LA16_0 == COLON or (HASH <= LA16_0 <= LBRACKET)) :
                    alt16 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # lesscss.g:153:7: elementName ( ( esPred )=> elementSubsequent )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elementName_in_simpleSelector830)
                    elementName52 = self.elementName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, elementName52.tree)
                    # lesscss.g:153:19: ( ( esPred )=> elementSubsequent )*
                    while True: #loop14
                        alt14 = 2
                        alt14 = self.dfa14.predict(self.input)
                        if alt14 == 1:
                            # lesscss.g:153:20: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector837)
                            elementSubsequent53 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent53.tree)


                        else:
                            break #loop14


                elif alt16 == 2:
                    # lesscss.g:154:7: ( ( esPred )=> elementSubsequent )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:154:7: ( ( esPred )=> elementSubsequent )+
                    cnt15 = 0
                    while True: #loop15
                        alt15 = 2
                        LA15 = self.input.LA(1)
                        if LA15 == HASH:
                            LA15_2 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt15 = 1


                        elif LA15 == DOT:
                            LA15_3 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt15 = 1


                        elif LA15 == LBRACKET:
                            LA15_4 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt15 = 1


                        elif LA15 == COLON:
                            LA15_5 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt15 = 1



                        if alt15 == 1:
                            # lesscss.g:154:8: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector852)
                            elementSubsequent54 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent54.tree)


                        else:
                            if cnt15 >= 1:
                                break #loop15

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(15, self.input)
                            raise eee

                        cnt15 += 1


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
    # lesscss.g:157:1: esPred : ( HASH | DOT | LBRACKET | COLON );
    def esPred(self, ):

        retval = self.esPred_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set55 = None

        set55_tree = None

        try:
            try:
                # lesscss.g:158:5: ( HASH | DOT | LBRACKET | COLON )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set55 = self.input.LT(1)
                if self.input.LA(1) == COLON or (HASH <= self.input.LA(1) <= LBRACKET):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set55))
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

    class elementName_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.elementName_return, self).__init__()

            self.tree = None




    # $ANTLR start "elementName"
    # lesscss.g:161:1: elementName : ( IDENT | STAR );
    def elementName(self, ):

        retval = self.elementName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set56 = None

        set56_tree = None

        try:
            try:
                # lesscss.g:162:5: ( IDENT | STAR )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set56 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == STAR:
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

    # $ANTLR end "elementName"

    class elementSubsequent_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.elementSubsequent_return, self).__init__()

            self.tree = None




    # $ANTLR start "elementSubsequent"
    # lesscss.g:166:1: elementSubsequent : ( HASH | cssClass | attrib | pseudo );
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
                # lesscss.g:167:5: ( HASH | cssClass | attrib | pseudo )
                alt17 = 4
                LA17 = self.input.LA(1)
                if LA17 == HASH:
                    alt17 = 1
                elif LA17 == DOT:
                    alt17 = 2
                elif LA17 == LBRACKET:
                    alt17 = 3
                elif LA17 == COLON:
                    alt17 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae

                if alt17 == 1:
                    # lesscss.g:167:7: HASH
                    pass 
                    root_0 = self._adaptor.nil()

                    HASH57=self.match(self.input, HASH, self.FOLLOW_HASH_in_elementSubsequent925)
                    if self._state.backtracking == 0:

                        HASH57_tree = self._adaptor.createWithPayload(HASH57)
                        self._adaptor.addChild(root_0, HASH57_tree)



                elif alt17 == 2:
                    # lesscss.g:168:7: cssClass
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_cssClass_in_elementSubsequent933)
                    cssClass58 = self.cssClass()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cssClass58.tree)


                elif alt17 == 3:
                    # lesscss.g:169:7: attrib
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_attrib_in_elementSubsequent941)
                    attrib59 = self.attrib()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, attrib59.tree)


                elif alt17 == 4:
                    # lesscss.g:170:7: pseudo
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pseudo_in_elementSubsequent949)
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
    # lesscss.g:173:1: cssClass : DOT a= IDENT -> IDENT ;
    def cssClass(self, ):

        retval = self.cssClass_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        DOT61 = None

        a_tree = None
        DOT61_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")

        try:
            try:
                # lesscss.g:174:5: ( DOT a= IDENT -> IDENT )
                # lesscss.g:174:7: DOT a= IDENT
                pass 
                DOT61=self.match(self.input, DOT, self.FOLLOW_DOT_in_cssClass966) 
                if self._state.backtracking == 0:
                    stream_DOT.add(DOT61)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_cssClass970) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(a)
                if self._state.backtracking == 0:
                    a.setText('.' + a.getText()); 


                # AST Rewrite
                # elements: IDENT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 176:9: -> IDENT
                    self._adaptor.addChild(root_0, stream_IDENT.nextNode())



                    retval.tree = root_0



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

    class pseudo_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.pseudo_return, self).__init__()

            self.tree = None




    # $ANTLR start "pseudo"
    # lesscss.g:179:1: pseudo : ( COLON a= IDENT -> IDENT | COLON FUNCTION expr RPAREN -> ^( N_Function FUNCTION expr ) );
    def pseudo(self, ):

        retval = self.pseudo_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        COLON62 = None
        COLON63 = None
        FUNCTION64 = None
        RPAREN66 = None
        expr65 = None


        a_tree = None
        COLON62_tree = None
        COLON63_tree = None
        FUNCTION64_tree = None
        RPAREN66_tree = None
        stream_FUNCTION = RewriteRuleTokenStream(self._adaptor, "token FUNCTION")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:180:5: ( COLON a= IDENT -> IDENT | COLON FUNCTION expr RPAREN -> ^( N_Function FUNCTION expr ) )
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == COLON) :
                    LA18_1 = self.input.LA(2)

                    if (LA18_1 == IDENT) :
                        alt18 = 1
                    elif (LA18_1 == FUNCTION) :
                        alt18 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 18, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae

                if alt18 == 1:
                    # lesscss.g:180:7: COLON a= IDENT
                    pass 
                    COLON62=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1010) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON62)
                    a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo1014) 
                    if self._state.backtracking == 0:
                        stream_IDENT.add(a)
                    if self._state.backtracking == 0:
                        a.setText(':' + a.getText()); 


                    # AST Rewrite
                    # elements: IDENT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 182:9: -> IDENT
                        self._adaptor.addChild(root_0, stream_IDENT.nextNode())



                        retval.tree = root_0


                elif alt18 == 2:
                    # lesscss.g:183:7: COLON FUNCTION expr RPAREN
                    pass 
                    COLON63=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1045) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON63)
                    FUNCTION64=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudo1047) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION64)
                    self._state.following.append(self.FOLLOW_expr_in_pseudo1049)
                    expr65 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr65.tree)
                    RPAREN66=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudo1051) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN66)

                    # AST Rewrite
                    # elements: FUNCTION, expr
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 184:9: -> ^( N_Function FUNCTION expr )
                        # lesscss.g:184:12: ^( N_Function FUNCTION expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_FUNCTION.nextNode())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


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

    class attrib_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.attrib_return, self).__init__()

            self.tree = None




    # $ANTLR start "attrib"
    # lesscss.g:187:1: attrib : LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) ;
    def attrib(self, ):

        retval = self.attrib_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LBRACKET67 = None
        RBRACKET69 = None
        attribBody68 = None


        LBRACKET67_tree = None
        RBRACKET69_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_attribBody = RewriteRuleSubtreeStream(self._adaptor, "rule attribBody")
        try:
            try:
                # lesscss.g:188:5: ( LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) )
                # lesscss.g:188:7: LBRACKET attribBody RBRACKET
                pass 
                LBRACKET67=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_attrib1086) 
                if self._state.backtracking == 0:
                    stream_LBRACKET.add(LBRACKET67)
                self._state.following.append(self.FOLLOW_attribBody_in_attrib1088)
                attribBody68 = self.attribBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_attribBody.add(attribBody68.tree)
                RBRACKET69=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_attrib1090) 
                if self._state.backtracking == 0:
                    stream_RBRACKET.add(RBRACKET69)

                # AST Rewrite
                # elements: attribBody
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 189:9: -> ^( N_Attrib attribBody )
                    # lesscss.g:189:13: ^( N_Attrib attribBody )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Attrib, "N_Attrib"), root_1)

                    self._adaptor.addChild(root_1, stream_attribBody.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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

    class attribBody_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.attribBody_return, self).__init__()

            self.tree = None




    # $ANTLR start "attribBody"
    # lesscss.g:192:1: attribBody : ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) );
    def attribBody(self, ):

        retval = self.attribBody_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT70 = None
        IDENT71 = None
        set72 = None
        set73 = None

        IDENT70_tree = None
        IDENT71_tree = None
        set72_tree = None
        set73_tree = None

        try:
            try:
                # lesscss.g:193:5: ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == IDENT) :
                    LA19_1 = self.input.LA(2)

                    if ((OPEQ <= LA19_1 <= DASHMATCH)) :
                        alt19 = 2
                    elif (LA19_1 == RBRACKET) :
                        alt19 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 19, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # lesscss.g:193:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT70=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1125)
                    if self._state.backtracking == 0:

                        IDENT70_tree = self._adaptor.createWithPayload(IDENT70)
                        self._adaptor.addChild(root_0, IDENT70_tree)



                elif alt19 == 2:
                    # lesscss.g:194:7: IDENT ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING )
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT71=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1133)
                    if self._state.backtracking == 0:

                        IDENT71_tree = self._adaptor.createWithPayload(IDENT71)
                        self._adaptor.addChild(root_0, IDENT71_tree)

                    set72 = self.input.LT(1)
                    set72 = self.input.LT(1)
                    if (OPEQ <= self.input.LA(1) <= DASHMATCH):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set72), root_0)
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    set73 = self.input.LT(1)
                    if self.input.LA(1) == STRING or self.input.LA(1) == IDENT:
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set73))
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

    # $ANTLR end "attribBody"

    class declarationset_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.declarationset_return, self).__init__()

            self.tree = None




    # $ANTLR start "declarationset"
    # lesscss.g:197:1: declarationset : declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ ;
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
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_declaration = RewriteRuleSubtreeStream(self._adaptor, "rule declaration")
        try:
            try:
                # lesscss.g:198:5: ( declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ )
                # lesscss.g:198:7: declaration ( SEMI declaration )* ( SEMI )?
                pass 
                self._state.following.append(self.FOLLOW_declaration_in_declarationset1173)
                declaration74 = self.declaration()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declaration.add(declaration74.tree)
                # lesscss.g:198:19: ( SEMI declaration )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == SEMI) :
                        LA20_1 = self.input.LA(2)

                        if (LA20_1 == IDENT or LA20_1 == STAR) :
                            alt20 = 1




                    if alt20 == 1:
                        # lesscss.g:198:20: SEMI declaration
                        pass 
                        SEMI75=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1176) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI75)
                        self._state.following.append(self.FOLLOW_declaration_in_declarationset1178)
                        declaration76 = self.declaration()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_declaration.add(declaration76.tree)


                    else:
                        break #loop20
                # lesscss.g:198:39: ( SEMI )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == SEMI) :
                    alt21 = 1
                if alt21 == 1:
                    # lesscss.g:198:39: SEMI
                    pass 
                    SEMI77=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1182) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI77)




                # AST Rewrite
                # elements: declaration
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 198:45: -> ( declaration )+
                    # lesscss.g:198:48: ( declaration )+
                    if not (stream_declaration.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_declaration.hasNext():
                        self._adaptor.addChild(root_0, stream_declaration.nextTree())


                    stream_declaration.reset()



                    retval.tree = root_0



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
    # lesscss.g:201:1: declaration : property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) ;
    def declaration(self, ):

        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON79 = None
        property78 = None

        expr80 = None

        prio81 = None


        COLON79_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_property = RewriteRuleSubtreeStream(self._adaptor, "rule property")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_prio = RewriteRuleSubtreeStream(self._adaptor, "rule prio")
        try:
            try:
                # lesscss.g:202:5: ( property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) )
                # lesscss.g:202:7: property COLON expr ( prio )?
                pass 
                self._state.following.append(self.FOLLOW_property_in_declaration1205)
                property78 = self.property()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_property.add(property78.tree)
                COLON79=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1207) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON79)
                self._state.following.append(self.FOLLOW_expr_in_declaration1209)
                expr80 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr80.tree)
                # lesscss.g:202:27: ( prio )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == IMPORTANT_SYM) :
                    alt22 = 1
                if alt22 == 1:
                    # lesscss.g:202:27: prio
                    pass 
                    self._state.following.append(self.FOLLOW_prio_in_declaration1211)
                    prio81 = self.prio()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_prio.add(prio81.tree)




                # AST Rewrite
                # elements: prio, expr, property
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 202:33: -> ^( N_Declaration property expr ( prio )? )
                    # lesscss.g:202:36: ^( N_Declaration property expr ( prio )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Declaration, "N_Declaration"), root_1)

                    self._adaptor.addChild(root_1, stream_property.nextTree())
                    self._adaptor.addChild(root_1, stream_expr.nextTree())
                    # lesscss.g:202:66: ( prio )?
                    if stream_prio.hasNext():
                        self._adaptor.addChild(root_1, stream_prio.nextTree())


                    stream_prio.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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
    # lesscss.g:205:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        retval = self.prio_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORTANT_SYM82 = None

        IMPORTANT_SYM82_tree = None

        try:
            try:
                # lesscss.g:206:5: ( IMPORTANT_SYM )
                # lesscss.g:206:7: IMPORTANT_SYM
                pass 
                root_0 = self._adaptor.nil()

                IMPORTANT_SYM82=self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1242)
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
    # lesscss.g:210:1: expr : term ( operator term )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        term83 = None

        operator84 = None

        term85 = None



        try:
            try:
                # lesscss.g:211:5: ( term ( operator term )* )
                # lesscss.g:211:7: term ( operator term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_expr1260)
                term83 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term83.tree)
                # lesscss.g:211:12: ( operator term )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == COMMA) :
                        LA23_2 = self.input.LA(2)

                        if (LA23_2 == STRING or LA23_2 == URI or LA23_2 == PLUS or LA23_2 == HASH or LA23_2 == FUNCTION or (NUMBER <= LA23_2 <= MINUS)) :
                            alt23 = 1
                        elif (LA23_2 == IDENT) :
                            LA23_4 = self.input.LA(3)

                            if ((STRING <= LA23_4 <= SEMI) or (COMMA <= LA23_4 <= URI) or (RBRACE <= LA23_4 <= IDENT) or LA23_4 == COLON or LA23_4 == PLUS or (HASH <= LA23_4 <= DOT) or (FUNCTION <= LA23_4 <= RPAREN) or (IMPORTANT_SYM <= LA23_4 <= MINUS)) :
                                alt23 = 1




                    elif (LA23_0 == STRING or LA23_0 == URI or LA23_0 == IDENT or LA23_0 == PLUS or LA23_0 == HASH or LA23_0 == FUNCTION or (SOLIDUS <= LA23_0 <= MINUS)) :
                        alt23 = 1


                    if alt23 == 1:
                        # lesscss.g:211:13: operator term
                        pass 
                        self._state.following.append(self.FOLLOW_operator_in_expr1263)
                        operator84 = self.operator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(operator84.tree, root_0)
                        self._state.following.append(self.FOLLOW_term_in_expr1266)
                        term85 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term85.tree)


                    else:
                        break #loop23



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

    class operator_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.operator_return, self).__init__()

            self.tree = None




    # $ANTLR start "operator"
    # lesscss.g:214:10: fragment operator : ( SOLIDUS | COMMA | -> N_Space );
    def operator(self, ):

        retval = self.operator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SOLIDUS86 = None
        COMMA87 = None

        SOLIDUS86_tree = None
        COMMA87_tree = None

        try:
            try:
                # lesscss.g:215:5: ( SOLIDUS | COMMA | -> N_Space )
                alt24 = 3
                LA24 = self.input.LA(1)
                if LA24 == SOLIDUS:
                    alt24 = 1
                elif LA24 == COMMA:
                    alt24 = 2
                elif LA24 == STRING or LA24 == URI or LA24 == IDENT or LA24 == PLUS or LA24 == HASH or LA24 == FUNCTION or LA24 == NUMBER or LA24 == PERCENTAGE or LA24 == LENGTH or LA24 == EMS or LA24 == EXS or LA24 == ANGLE or LA24 == TIME or LA24 == FREQ or LA24 == MINUS:
                    alt24 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # lesscss.g:215:7: SOLIDUS
                    pass 
                    root_0 = self._adaptor.nil()

                    SOLIDUS86=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator1287)
                    if self._state.backtracking == 0:

                        SOLIDUS86_tree = self._adaptor.createWithPayload(SOLIDUS86)
                        self._adaptor.addChild(root_0, SOLIDUS86_tree)



                elif alt24 == 2:
                    # lesscss.g:216:7: COMMA
                    pass 
                    root_0 = self._adaptor.nil()

                    COMMA87=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator1295)
                    if self._state.backtracking == 0:

                        COMMA87_tree = self._adaptor.createWithPayload(COMMA87)
                        self._adaptor.addChild(root_0, COMMA87_tree)



                elif alt24 == 3:
                    # lesscss.g:217:7: 
                    pass 
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 217:7: -> N_Space
                        self._adaptor.addChild(root_0, self._adaptor.createFromType(N_Space, "N_Space"))



                        retval.tree = root_0


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

    class term_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.term_return, self).__init__()

            self.tree = None




    # $ANTLR start "term"
    # lesscss.g:220:1: term : ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ ) | STRING | IDENT | URI | function | hexColor );
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set89 = None
        STRING90 = None
        IDENT91 = None
        URI92 = None
        unaryOperator88 = None

        function93 = None

        hexColor94 = None


        set89_tree = None
        STRING90_tree = None
        IDENT91_tree = None
        URI92_tree = None

        try:
            try:
                # lesscss.g:221:5: ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ ) | STRING | IDENT | URI | function | hexColor )
                alt26 = 6
                LA26 = self.input.LA(1)
                if LA26 == PLUS or LA26 == NUMBER or LA26 == PERCENTAGE or LA26 == LENGTH or LA26 == EMS or LA26 == EXS or LA26 == ANGLE or LA26 == TIME or LA26 == FREQ or LA26 == MINUS:
                    alt26 = 1
                elif LA26 == STRING:
                    alt26 = 2
                elif LA26 == IDENT:
                    LA26_3 = self.input.LA(2)

                    if (LA26_3 == COLON or LA26_3 == DOT) :
                        alt26 = 5
                    elif ((STRING <= LA26_3 <= SEMI) or (COMMA <= LA26_3 <= URI) or (RBRACE <= LA26_3 <= IDENT) or LA26_3 == PLUS or LA26_3 == HASH or (FUNCTION <= LA26_3 <= RPAREN) or (IMPORTANT_SYM <= LA26_3 <= MINUS)) :
                        alt26 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 26, 3, self.input)

                        raise nvae

                elif LA26 == URI:
                    alt26 = 4
                elif LA26 == FUNCTION:
                    alt26 = 5
                elif LA26 == HASH:
                    alt26 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae

                if alt26 == 1:
                    # lesscss.g:221:7: ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ )
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:221:20: ( unaryOperator )?
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == PLUS or LA25_0 == MINUS) :
                        alt25 = 1
                    if alt25 == 1:
                        # lesscss.g:221:20: unaryOperator
                        pass 
                        self._state.following.append(self.FOLLOW_unaryOperator_in_term1323)
                        unaryOperator88 = self.unaryOperator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(unaryOperator88.tree, root_0)



                    set89 = self.input.LT(1)
                    if (NUMBER <= self.input.LA(1) <= FREQ):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set89))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse




                elif alt26 == 2:
                    # lesscss.g:232:7: STRING
                    pass 
                    root_0 = self._adaptor.nil()

                    STRING90=self.match(self.input, STRING, self.FOLLOW_STRING_in_term1481)
                    if self._state.backtracking == 0:

                        STRING90_tree = self._adaptor.createWithPayload(STRING90)
                        self._adaptor.addChild(root_0, STRING90_tree)



                elif alt26 == 3:
                    # lesscss.g:233:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT91=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term1489)
                    if self._state.backtracking == 0:

                        IDENT91_tree = self._adaptor.createWithPayload(IDENT91)
                        self._adaptor.addChild(root_0, IDENT91_tree)



                elif alt26 == 4:
                    # lesscss.g:234:7: URI
                    pass 
                    root_0 = self._adaptor.nil()

                    URI92=self.match(self.input, URI, self.FOLLOW_URI_in_term1497)
                    if self._state.backtracking == 0:

                        URI92_tree = self._adaptor.createWithPayload(URI92)
                        self._adaptor.addChild(root_0, URI92_tree)



                elif alt26 == 5:
                    # lesscss.g:235:7: function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_in_term1505)
                    function93 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function93.tree)


                elif alt26 == 6:
                    # lesscss.g:236:7: hexColor
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_hexColor_in_term1513)
                    hexColor94 = self.hexColor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, hexColor94.tree)


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

    class unaryOperator_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.unaryOperator_return, self).__init__()

            self.tree = None




    # $ANTLR start "unaryOperator"
    # lesscss.g:239:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        retval = self.unaryOperator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set95 = None

        set95_tree = None

        try:
            try:
                # lesscss.g:240:5: ( MINUS | PLUS )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set95 = self.input.LT(1)
                if self.input.LA(1) == PLUS or self.input.LA(1) == MINUS:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set95))
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

    class function_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.function_return, self).__init__()

            self.tree = None




    # $ANTLR start "function"
    # lesscss.g:245:1: function : ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) );
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RPAREN98 = None
        RPAREN101 = None
        fnct_name96 = None

        fnct_args97 = None

        fnct_name99 = None

        expr100 = None


        RPAREN98_tree = None
        RPAREN101_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_fnct_name = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_name")
        stream_fnct_args = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_args")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:246:5: ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) )
                alt27 = 2
                alt27 = self.dfa27.predict(self.input)
                if alt27 == 1:
                    # lesscss.g:246:7: fnct_name fnct_args RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function1558)
                    fnct_name96 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name96.tree)
                    self._state.following.append(self.FOLLOW_fnct_args_in_function1560)
                    fnct_args97 = self.fnct_args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_args.add(fnct_args97.tree)
                    RPAREN98=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1562) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN98)

                    # AST Rewrite
                    # elements: fnct_args, fnct_name
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 247:9: -> ^( N_Function fnct_name fnct_args )
                        # lesscss.g:247:12: ^( N_Function fnct_name fnct_args )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_fnct_name.nextTree())
                        self._adaptor.addChild(root_1, stream_fnct_args.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt27 == 2:
                    # lesscss.g:249:7: fnct_name expr RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function1589)
                    fnct_name99 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name99.tree)
                    self._state.following.append(self.FOLLOW_expr_in_function1591)
                    expr100 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr100.tree)
                    RPAREN101=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1593) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN101)

                    # AST Rewrite
                    # elements: fnct_name, expr
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 250:9: -> ^( N_Function fnct_name expr )
                        # lesscss.g:250:12: ^( N_Function fnct_name expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_fnct_name.nextTree())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


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
    # lesscss.g:254:1: fnct_name : ( IDENT ( COLON | DOT )+ )* FUNCTION ;
    def fnct_name(self, ):

        retval = self.fnct_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT102 = None
        set103 = None
        FUNCTION104 = None

        IDENT102_tree = None
        set103_tree = None
        FUNCTION104_tree = None

        try:
            try:
                # lesscss.g:255:5: ( ( IDENT ( COLON | DOT )+ )* FUNCTION )
                # lesscss.g:255:7: ( IDENT ( COLON | DOT )+ )* FUNCTION
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:255:7: ( IDENT ( COLON | DOT )+ )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == IDENT) :
                        alt29 = 1


                    if alt29 == 1:
                        # lesscss.g:255:8: IDENT ( COLON | DOT )+
                        pass 
                        IDENT102=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name1630)
                        if self._state.backtracking == 0:

                            IDENT102_tree = self._adaptor.createWithPayload(IDENT102)
                            self._adaptor.addChild(root_0, IDENT102_tree)

                        # lesscss.g:255:14: ( COLON | DOT )+
                        cnt28 = 0
                        while True: #loop28
                            alt28 = 2
                            LA28_0 = self.input.LA(1)

                            if (LA28_0 == COLON or LA28_0 == DOT) :
                                alt28 = 1


                            if alt28 == 1:
                                # lesscss.g:
                                pass 
                                set103 = self.input.LT(1)
                                if self.input.LA(1) == COLON or self.input.LA(1) == DOT:
                                    self.input.consume()
                                    if self._state.backtracking == 0:
                                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set103))
                                    self._state.errorRecovery = False

                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed

                                    mse = MismatchedSetException(None, self.input)
                                    raise mse




                            else:
                                if cnt28 >= 1:
                                    break #loop28

                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                eee = EarlyExitException(28, self.input)
                                raise eee

                            cnt28 += 1


                    else:
                        break #loop29
                FUNCTION104=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name1642)
                if self._state.backtracking == 0:

                    FUNCTION104_tree = self._adaptor.createWithPayload(FUNCTION104)
                    self._adaptor.addChild(root_0, FUNCTION104_tree)




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
    # lesscss.g:258:10: fragment fnct_args : fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ ;
    def fnct_args(self, ):

        retval = self.fnct_args_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA106 = None
        fnct_arg105 = None

        fnct_arg107 = None


        COMMA106_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_fnct_arg = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_arg")
        try:
            try:
                # lesscss.g:259:5: ( fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ )
                # lesscss.g:259:7: fnct_arg ( COMMA fnct_arg )*
                pass 
                self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1661)
                fnct_arg105 = self.fnct_arg()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_fnct_arg.add(fnct_arg105.tree)
                # lesscss.g:259:16: ( COMMA fnct_arg )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == COMMA) :
                        alt30 = 1


                    if alt30 == 1:
                        # lesscss.g:259:17: COMMA fnct_arg
                        pass 
                        COMMA106=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args1664) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA106)
                        self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1666)
                        fnct_arg107 = self.fnct_arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_fnct_arg.add(fnct_arg107.tree)


                    else:
                        break #loop30

                # AST Rewrite
                # elements: fnct_arg
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 260:9: -> ( fnct_arg )+
                    # lesscss.g:260:12: ( fnct_arg )+
                    if not (stream_fnct_arg.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_fnct_arg.hasNext():
                        self._adaptor.addChild(root_0, stream_fnct_arg.nextTree())


                    stream_fnct_arg.reset()



                    retval.tree = root_0



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
    # lesscss.g:263:1: fnct_arg : IDENT OPEQ expr ;
    def fnct_arg(self, ):

        retval = self.fnct_arg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT108 = None
        OPEQ109 = None
        expr110 = None


        IDENT108_tree = None
        OPEQ109_tree = None

        try:
            try:
                # lesscss.g:264:5: ( IDENT OPEQ expr )
                # lesscss.g:264:7: IDENT OPEQ expr
                pass 
                root_0 = self._adaptor.nil()

                IDENT108=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_arg1698)
                if self._state.backtracking == 0:

                    IDENT108_tree = self._adaptor.createWithPayload(IDENT108)
                    self._adaptor.addChild(root_0, IDENT108_tree)

                OPEQ109=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_arg1700)
                if self._state.backtracking == 0:

                    OPEQ109_tree = self._adaptor.createWithPayload(OPEQ109)
                    root_0 = self._adaptor.becomeRoot(OPEQ109_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_fnct_arg1703)
                expr110 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr110.tree)



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
    # lesscss.g:267:1: hexColor : HASH ;
    def hexColor(self, ):

        retval = self.hexColor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH111 = None

        HASH111_tree = None

        try:
            try:
                # lesscss.g:268:5: ( HASH )
                # lesscss.g:268:7: HASH
                pass 
                root_0 = self._adaptor.nil()

                HASH111=self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor1720)
                if self._state.backtracking == 0:

                    HASH111_tree = self._adaptor.createWithPayload(HASH111)
                    self._adaptor.addChild(root_0, HASH111_tree)




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
        # lesscss.g:153:20: ( esPred )
        # lesscss.g:153:21: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred1_lesscss834)
        self.esPred()

        self._state.following.pop()


    # $ANTLR end "synpred1_lesscss"



    # $ANTLR start "synpred2_lesscss"
    def synpred2_lesscss_fragment(self, ):
        # lesscss.g:154:8: ( esPred )
        # lesscss.g:154:9: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred2_lesscss849)
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



    # lookup tables for DFA #14

    DFA14_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA14_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA14_min = DFA.unpack(
        u"\1\25\3\uffff\4\0\3\uffff"
        )

    DFA14_max = DFA.unpack(
        u"\1\43\3\uffff\4\0\3\uffff"
        )

    DFA14_accept = DFA.unpack(
        u"\1\uffff\1\2\10\uffff\1\1"
        )

    DFA14_special = DFA.unpack(
        u"\4\uffff\1\0\1\1\1\2\1\3\3\uffff"
        )

            
    DFA14_transition = [
        DFA.unpack(u"\1\1\2\uffff\1\1\1\uffff\1\1\2\uffff\1\7\3\1\1\4\1\5"
        u"\1\6"),
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

    # class definition for DFA #14

    class DFA14(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA14_4 = input.LA(1)

                 
                index14_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index14_4)
                if s >= 0:
                    return s
            elif s == 1: 
                LA14_5 = input.LA(1)

                 
                index14_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index14_5)
                if s >= 0:
                    return s
            elif s == 2: 
                LA14_6 = input.LA(1)

                 
                index14_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index14_6)
                if s >= 0:
                    return s
            elif s == 3: 
                LA14_7 = input.LA(1)

                 
                index14_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index14_7)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 14, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #27

    DFA27_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA27_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA27_min = DFA.unpack(
        u"\1\32\1\35\1\22\1\32\1\uffff\1\22\1\uffff"
        )

    DFA27_max = DFA.unpack(
        u"\1\44\1\42\1\64\1\44\1\uffff\1\64\1\uffff"
        )

    DFA27_accept = DFA.unpack(
        u"\4\uffff\1\2\1\uffff\1\1"
        )

    DFA27_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA27_transition = [
        DFA.unpack(u"\1\1\11\uffff\1\2"),
        DFA.unpack(u"\1\3\4\uffff\1\3"),
        DFA.unpack(u"\1\4\3\uffff\1\4\3\uffff\1\5\4\uffff\1\4\1\uffff\1"
        u"\4\2\uffff\1\4\7\uffff\11\4"),
        DFA.unpack(u"\1\1\2\uffff\1\3\4\uffff\1\3\1\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\2\uffff\2\4\3\uffff\1\4\2\uffff\1\4\1\uffff\1"
        u"\4\1\uffff\2\4\1\uffff\2\4\1\uffff\1\6\3\uffff\12\4"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #27

    class DFA27(DFA):
        pass


 

    FOLLOW_charSet_in_styleSheet169 = frozenset([20, 23, 26, 27, 28, 29, 30, 33, 34, 35])
    FOLLOW_imports_in_styleSheet180 = frozenset([20, 23, 26, 27, 28, 29, 30, 33, 34, 35])
    FOLLOW_bodylist_in_styleSheet191 = frozenset([])
    FOLLOW_EOF_in_styleSheet201 = frozenset([1])
    FOLLOW_CHARSET_SYM_in_charSet253 = frozenset([18])
    FOLLOW_STRING_in_charSet255 = frozenset([19])
    FOLLOW_SEMI_in_charSet257 = frozenset([1])
    FOLLOW_IMPORT_SYM_in_imports295 = frozenset([18, 22])
    FOLLOW_importUrl_in_imports297 = frozenset([19, 26])
    FOLLOW_medium_in_imports300 = frozenset([19, 21])
    FOLLOW_COMMA_in_imports303 = frozenset([26])
    FOLLOW_medium_in_imports305 = frozenset([19, 21])
    FOLLOW_SEMI_in_imports311 = frozenset([1])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media376 = frozenset([26])
    FOLLOW_medium_in_media378 = frozenset([21, 24])
    FOLLOW_COMMA_in_media381 = frozenset([26])
    FOLLOW_medium_in_media383 = frozenset([21, 24])
    FOLLOW_LBRACE_in_media395 = frozenset([25, 26, 29, 30, 33, 34, 35])
    FOLLOW_ruleSet_in_media409 = frozenset([25, 26, 29, 30, 33, 34, 35])
    FOLLOW_RBRACE_in_media420 = frozenset([1])
    FOLLOW_IDENT_in_medium460 = frozenset([1])
    FOLLOW_FONTFACE_SYM_in_fontface481 = frozenset([24])
    FOLLOW_LBRACE_in_fontface483 = frozenset([26, 30])
    FOLLOW_declarationset_in_fontface485 = frozenset([25])
    FOLLOW_RBRACE_in_fontface487 = frozenset([1])
    FOLLOW_bodyset_in_bodylist524 = frozenset([1, 23, 26, 27, 28, 29, 30, 33, 34, 35])
    FOLLOW_ruleSet_in_bodyset542 = frozenset([1])
    FOLLOW_media_in_bodyset550 = frozenset([1])
    FOLLOW_page_in_bodyset558 = frozenset([1])
    FOLLOW_fontface_in_bodyset566 = frozenset([1])
    FOLLOW_PAGE_SYM_in_page586 = frozenset([24, 29])
    FOLLOW_pseudoPage_in_page588 = frozenset([24])
    FOLLOW_LBRACE_in_page591 = frozenset([26, 30])
    FOLLOW_declarationset_in_page593 = frozenset([25])
    FOLLOW_RBRACE_in_page595 = frozenset([1])
    FOLLOW_COLON_in_pseudoPage631 = frozenset([26])
    FOLLOW_IDENT_in_pseudoPage633 = frozenset([1])
    FOLLOW_IDENT_in_property658 = frozenset([1])
    FOLLOW_STAR_in_property677 = frozenset([26])
    FOLLOW_IDENT_in_property681 = frozenset([1])
    FOLLOW_selector_in_ruleSet722 = frozenset([21, 24])
    FOLLOW_COMMA_in_ruleSet725 = frozenset([26, 29, 30, 33, 34, 35])
    FOLLOW_selector_in_ruleSet727 = frozenset([21, 24])
    FOLLOW_LBRACE_in_ruleSet731 = frozenset([26, 30])
    FOLLOW_declarationset_in_ruleSet733 = frozenset([25])
    FOLLOW_RBRACE_in_ruleSet735 = frozenset([1])
    FOLLOW_simpleSelector_in_selector775 = frozenset([1, 26, 29, 30, 31, 32, 33, 34, 35])
    FOLLOW_combinator_in_selector778 = frozenset([26, 29, 30, 33, 34, 35])
    FOLLOW_simpleSelector_in_selector780 = frozenset([1, 26, 29, 30, 31, 32, 33, 34, 35])
    FOLLOW_PLUS_in_combinator799 = frozenset([1])
    FOLLOW_GREATER_in_combinator807 = frozenset([1])
    FOLLOW_elementName_in_simpleSelector830 = frozenset([1, 26, 29, 30, 33, 34, 35])
    FOLLOW_elementSubsequent_in_simpleSelector837 = frozenset([1, 26, 29, 30, 33, 34, 35])
    FOLLOW_elementSubsequent_in_simpleSelector852 = frozenset([1, 26, 29, 30, 33, 34, 35])
    FOLLOW_set_in_esPred0 = frozenset([1])
    FOLLOW_set_in_elementName0 = frozenset([1])
    FOLLOW_HASH_in_elementSubsequent925 = frozenset([1])
    FOLLOW_cssClass_in_elementSubsequent933 = frozenset([1])
    FOLLOW_attrib_in_elementSubsequent941 = frozenset([1])
    FOLLOW_pseudo_in_elementSubsequent949 = frozenset([1])
    FOLLOW_DOT_in_cssClass966 = frozenset([26])
    FOLLOW_IDENT_in_cssClass970 = frozenset([1])
    FOLLOW_COLON_in_pseudo1010 = frozenset([26])
    FOLLOW_IDENT_in_pseudo1014 = frozenset([1])
    FOLLOW_COLON_in_pseudo1045 = frozenset([36])
    FOLLOW_FUNCTION_in_pseudo1047 = frozenset([18, 22, 26, 31, 33, 36, 44, 45, 46, 47, 48, 49, 50, 51, 52])
    FOLLOW_expr_in_pseudo1049 = frozenset([37])
    FOLLOW_RPAREN_in_pseudo1051 = frozenset([1])
    FOLLOW_LBRACKET_in_attrib1086 = frozenset([26])
    FOLLOW_attribBody_in_attrib1088 = frozenset([38])
    FOLLOW_RBRACKET_in_attrib1090 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1125 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1133 = frozenset([39, 40, 41])
    FOLLOW_set_in_attribBody1135 = frozenset([18, 26])
    FOLLOW_set_in_attribBody1148 = frozenset([1])
    FOLLOW_declaration_in_declarationset1173 = frozenset([1, 19])
    FOLLOW_SEMI_in_declarationset1176 = frozenset([26, 30])
    FOLLOW_declaration_in_declarationset1178 = frozenset([1, 19])
    FOLLOW_SEMI_in_declarationset1182 = frozenset([1])
    FOLLOW_property_in_declaration1205 = frozenset([29])
    FOLLOW_COLON_in_declaration1207 = frozenset([18, 22, 26, 31, 33, 36, 44, 45, 46, 47, 48, 49, 50, 51, 52])
    FOLLOW_expr_in_declaration1209 = frozenset([1, 42])
    FOLLOW_prio_in_declaration1211 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1242 = frozenset([1])
    FOLLOW_term_in_expr1260 = frozenset([1, 18, 21, 22, 26, 31, 33, 36, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52])
    FOLLOW_operator_in_expr1263 = frozenset([18, 22, 26, 31, 33, 36, 44, 45, 46, 47, 48, 49, 50, 51, 52])
    FOLLOW_term_in_expr1266 = frozenset([1, 18, 21, 22, 26, 31, 33, 36, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52])
    FOLLOW_SOLIDUS_in_operator1287 = frozenset([1])
    FOLLOW_COMMA_in_operator1295 = frozenset([1])
    FOLLOW_unaryOperator_in_term1323 = frozenset([44, 45, 46, 47, 48, 49, 50, 51])
    FOLLOW_set_in_term1335 = frozenset([1])
    FOLLOW_STRING_in_term1481 = frozenset([1])
    FOLLOW_IDENT_in_term1489 = frozenset([1])
    FOLLOW_URI_in_term1497 = frozenset([1])
    FOLLOW_function_in_term1505 = frozenset([1])
    FOLLOW_hexColor_in_term1513 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_fnct_name_in_function1558 = frozenset([26])
    FOLLOW_fnct_args_in_function1560 = frozenset([37])
    FOLLOW_RPAREN_in_function1562 = frozenset([1])
    FOLLOW_fnct_name_in_function1589 = frozenset([18, 22, 26, 31, 33, 36, 44, 45, 46, 47, 48, 49, 50, 51, 52])
    FOLLOW_expr_in_function1591 = frozenset([37])
    FOLLOW_RPAREN_in_function1593 = frozenset([1])
    FOLLOW_IDENT_in_fnct_name1630 = frozenset([29, 34])
    FOLLOW_set_in_fnct_name1632 = frozenset([26, 29, 34, 36])
    FOLLOW_FUNCTION_in_fnct_name1642 = frozenset([1])
    FOLLOW_fnct_arg_in_fnct_args1661 = frozenset([1, 21])
    FOLLOW_COMMA_in_fnct_args1664 = frozenset([26])
    FOLLOW_fnct_arg_in_fnct_args1666 = frozenset([1, 21])
    FOLLOW_IDENT_in_fnct_arg1698 = frozenset([39])
    FOLLOW_OPEQ_in_fnct_arg1700 = frozenset([18, 22, 26, 31, 33, 36, 44, 45, 46, 47, 48, 49, 50, 51, 52])
    FOLLOW_expr_in_fnct_arg1703 = frozenset([1])
    FOLLOW_HASH_in_hexColor1720 = frozenset([1])
    FOLLOW_esPred_in_synpred1_lesscss834 = frozenset([1])
    FOLLOW_esPred_in_synpred2_lesscss849 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("lesscssLexer", lesscssParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
