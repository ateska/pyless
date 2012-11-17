# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 lesscss.g 2012-11-17 02:33:52

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=36
STAR=35
EOF=-1
MEDIA_SYM=23
INCLUDES=40
LBRACKET=34
RPAREN=37
NAME=59
GREATER=31
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
PLUS=30
FREQ=51
RBRACKET=38
DOT=33
CHARSET_SYM=17
ANGLE=49
HASH=32
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
    "PAGE_SYM", "COLON", "PLUS", "GREATER", "HASH", "DOT", "LBRACKET", "STAR", 
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
                # elements: bodylist, charSet, imports
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
                # elements: medium, importUrl
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

                    if (LA6_0 == IDENT or LA6_0 == COLON or (HASH <= LA6_0 <= STAR)) :
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
                # elements: ruleSet, medium
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

                    if (LA7_0 == MEDIA_SYM or (IDENT <= LA7_0 <= COLON) or (HASH <= LA7_0 <= STAR)) :
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
                if LA8 == IDENT or LA8 == COLON or LA8 == HASH or LA8 == DOT or LA8 == LBRACKET or LA8 == STAR:
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
    # lesscss.g:126:1: property : IDENT ;
    def property(self, ):

        retval = self.property_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT39 = None

        IDENT39_tree = None

        try:
            try:
                # lesscss.g:127:5: ( IDENT )
                # lesscss.g:127:7: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT39=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property658)
                if self._state.backtracking == 0:

                    IDENT39_tree = self._adaptor.createWithPayload(IDENT39)
                    self._adaptor.addChild(root_0, IDENT39_tree)




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
    # lesscss.g:130:1: ruleSet : selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) ;
    def ruleSet(self, ):

        retval = self.ruleSet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA41 = None
        LBRACE43 = None
        RBRACE45 = None
        selector40 = None

        selector42 = None

        declarationset44 = None


        COMMA41_tree = None
        LBRACE43_tree = None
        RBRACE45_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_selector = RewriteRuleSubtreeStream(self._adaptor, "rule selector")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        try:
            try:
                # lesscss.g:131:5: ( selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) )
                # lesscss.g:131:7: selector ( COMMA selector )* LBRACE declarationset RBRACE
                pass 
                self._state.following.append(self.FOLLOW_selector_in_ruleSet675)
                selector40 = self.selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_selector.add(selector40.tree)
                # lesscss.g:131:16: ( COMMA selector )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == COMMA) :
                        alt10 = 1


                    if alt10 == 1:
                        # lesscss.g:131:17: COMMA selector
                        pass 
                        COMMA41=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_ruleSet678) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA41)
                        self._state.following.append(self.FOLLOW_selector_in_ruleSet680)
                        selector42 = self.selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_selector.add(selector42.tree)


                    else:
                        break #loop10
                LBRACE43=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_ruleSet684) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE43)
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet686)
                declarationset44 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset44.tree)
                RBRACE45=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_ruleSet688) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE45)

                # AST Rewrite
                # elements: selector, declarationset
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
                    # 132:9: -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    # lesscss.g:132:12: ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_RuleSet, "N_RuleSet"), root_1)

                    # lesscss.g:132:24: ( ^( N_Selector selector ) )+
                    if not (stream_selector.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_selector.hasNext():
                        # lesscss.g:132:24: ^( N_Selector selector )
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
    # lesscss.g:135:1: selector : simpleSelector ( combinator simpleSelector )* ;
    def selector(self, ):

        retval = self.selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        simpleSelector46 = None

        combinator47 = None

        simpleSelector48 = None



        try:
            try:
                # lesscss.g:136:5: ( simpleSelector ( combinator simpleSelector )* )
                # lesscss.g:136:7: simpleSelector ( combinator simpleSelector )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_simpleSelector_in_selector728)
                simpleSelector46 = self.simpleSelector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, simpleSelector46.tree)
                # lesscss.g:136:22: ( combinator simpleSelector )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == IDENT or (COLON <= LA11_0 <= STAR)) :
                        alt11 = 1


                    if alt11 == 1:
                        # lesscss.g:136:23: combinator simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector731)
                        combinator47 = self.combinator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, combinator47.tree)
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector733)
                        simpleSelector48 = self.simpleSelector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, simpleSelector48.tree)


                    else:
                        break #loop11



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
    # lesscss.g:139:1: combinator : ( PLUS | GREATER | );
    def combinator(self, ):

        retval = self.combinator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS49 = None
        GREATER50 = None

        PLUS49_tree = None
        GREATER50_tree = None

        try:
            try:
                # lesscss.g:140:5: ( PLUS | GREATER | )
                alt12 = 3
                LA12 = self.input.LA(1)
                if LA12 == PLUS:
                    alt12 = 1
                elif LA12 == GREATER:
                    alt12 = 2
                elif LA12 == IDENT or LA12 == COLON or LA12 == HASH or LA12 == DOT or LA12 == LBRACKET or LA12 == STAR:
                    alt12 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # lesscss.g:140:7: PLUS
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS49=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator752)
                    if self._state.backtracking == 0:

                        PLUS49_tree = self._adaptor.createWithPayload(PLUS49)
                        self._adaptor.addChild(root_0, PLUS49_tree)



                elif alt12 == 2:
                    # lesscss.g:141:7: GREATER
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER50=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator760)
                    if self._state.backtracking == 0:

                        GREATER50_tree = self._adaptor.createWithPayload(GREATER50)
                        self._adaptor.addChild(root_0, GREATER50_tree)



                elif alt12 == 3:
                    # lesscss.g:143:5: 
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
    # lesscss.g:145:1: simpleSelector : ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ );
    def simpleSelector(self, ):

        retval = self.simpleSelector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        elementName51 = None

        elementSubsequent52 = None

        elementSubsequent53 = None



        try:
            try:
                # lesscss.g:146:5: ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ )
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
                    # lesscss.g:146:7: elementName ( ( esPred )=> elementSubsequent )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elementName_in_simpleSelector783)
                    elementName51 = self.elementName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, elementName51.tree)
                    # lesscss.g:146:19: ( ( esPred )=> elementSubsequent )*
                    while True: #loop13
                        alt13 = 2
                        alt13 = self.dfa13.predict(self.input)
                        if alt13 == 1:
                            # lesscss.g:146:20: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector790)
                            elementSubsequent52 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent52.tree)


                        else:
                            break #loop13


                elif alt15 == 2:
                    # lesscss.g:147:7: ( ( esPred )=> elementSubsequent )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:147:7: ( ( esPred )=> elementSubsequent )+
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
                            # lesscss.g:147:8: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector805)
                            elementSubsequent53 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent53.tree)


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
    # lesscss.g:150:1: esPred : ( HASH | DOT | LBRACKET | COLON );
    def esPred(self, ):

        retval = self.esPred_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set54 = None

        set54_tree = None

        try:
            try:
                # lesscss.g:151:5: ( HASH | DOT | LBRACKET | COLON )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set54 = self.input.LT(1)
                if self.input.LA(1) == COLON or (HASH <= self.input.LA(1) <= LBRACKET):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set54))
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
    # lesscss.g:154:1: elementName : ( IDENT | STAR );
    def elementName(self, ):

        retval = self.elementName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set55 = None

        set55_tree = None

        try:
            try:
                # lesscss.g:155:5: ( IDENT | STAR )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set55 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == STAR:
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

    # $ANTLR end "elementName"

    class elementSubsequent_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.elementSubsequent_return, self).__init__()

            self.tree = None




    # $ANTLR start "elementSubsequent"
    # lesscss.g:159:1: elementSubsequent : ( HASH | cssClass | attrib | pseudo );
    def elementSubsequent(self, ):

        retval = self.elementSubsequent_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH56 = None
        cssClass57 = None

        attrib58 = None

        pseudo59 = None


        HASH56_tree = None

        try:
            try:
                # lesscss.g:160:5: ( HASH | cssClass | attrib | pseudo )
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
                    # lesscss.g:160:7: HASH
                    pass 
                    root_0 = self._adaptor.nil()

                    HASH56=self.match(self.input, HASH, self.FOLLOW_HASH_in_elementSubsequent878)
                    if self._state.backtracking == 0:

                        HASH56_tree = self._adaptor.createWithPayload(HASH56)
                        self._adaptor.addChild(root_0, HASH56_tree)



                elif alt16 == 2:
                    # lesscss.g:161:7: cssClass
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_cssClass_in_elementSubsequent886)
                    cssClass57 = self.cssClass()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cssClass57.tree)


                elif alt16 == 3:
                    # lesscss.g:162:7: attrib
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_attrib_in_elementSubsequent894)
                    attrib58 = self.attrib()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, attrib58.tree)


                elif alt16 == 4:
                    # lesscss.g:163:7: pseudo
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pseudo_in_elementSubsequent902)
                    pseudo59 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudo59.tree)


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
    # lesscss.g:166:1: cssClass : DOT a= IDENT -> IDENT ;
    def cssClass(self, ):

        retval = self.cssClass_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        DOT60 = None

        a_tree = None
        DOT60_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")

        try:
            try:
                # lesscss.g:167:5: ( DOT a= IDENT -> IDENT )
                # lesscss.g:167:7: DOT a= IDENT
                pass 
                DOT60=self.match(self.input, DOT, self.FOLLOW_DOT_in_cssClass919) 
                if self._state.backtracking == 0:
                    stream_DOT.add(DOT60)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_cssClass923) 
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
                    # 169:9: -> IDENT
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
    # lesscss.g:172:1: pseudo : ( COLON a= IDENT -> IDENT | COLON FUNCTION expr RPAREN -> ^( N_Function FUNCTION expr ) );
    def pseudo(self, ):

        retval = self.pseudo_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        COLON61 = None
        COLON62 = None
        FUNCTION63 = None
        RPAREN65 = None
        expr64 = None


        a_tree = None
        COLON61_tree = None
        COLON62_tree = None
        FUNCTION63_tree = None
        RPAREN65_tree = None
        stream_FUNCTION = RewriteRuleTokenStream(self._adaptor, "token FUNCTION")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:173:5: ( COLON a= IDENT -> IDENT | COLON FUNCTION expr RPAREN -> ^( N_Function FUNCTION expr ) )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == COLON) :
                    LA17_1 = self.input.LA(2)

                    if (LA17_1 == IDENT) :
                        alt17 = 1
                    elif (LA17_1 == FUNCTION) :
                        alt17 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 17, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae

                if alt17 == 1:
                    # lesscss.g:173:7: COLON a= IDENT
                    pass 
                    COLON61=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo963) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON61)
                    a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo967) 
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
                        # 175:9: -> IDENT
                        self._adaptor.addChild(root_0, stream_IDENT.nextNode())



                        retval.tree = root_0


                elif alt17 == 2:
                    # lesscss.g:176:7: COLON FUNCTION expr RPAREN
                    pass 
                    COLON62=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo998) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON62)
                    FUNCTION63=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudo1000) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION63)
                    self._state.following.append(self.FOLLOW_expr_in_pseudo1002)
                    expr64 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr64.tree)
                    RPAREN65=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudo1004) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN65)

                    # AST Rewrite
                    # elements: expr, FUNCTION
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
                        # 177:9: -> ^( N_Function FUNCTION expr )
                        # lesscss.g:177:12: ^( N_Function FUNCTION expr )
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
    # lesscss.g:180:1: attrib : LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) ;
    def attrib(self, ):

        retval = self.attrib_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LBRACKET66 = None
        RBRACKET68 = None
        attribBody67 = None


        LBRACKET66_tree = None
        RBRACKET68_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_attribBody = RewriteRuleSubtreeStream(self._adaptor, "rule attribBody")
        try:
            try:
                # lesscss.g:181:5: ( LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) )
                # lesscss.g:181:7: LBRACKET attribBody RBRACKET
                pass 
                LBRACKET66=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_attrib1039) 
                if self._state.backtracking == 0:
                    stream_LBRACKET.add(LBRACKET66)
                self._state.following.append(self.FOLLOW_attribBody_in_attrib1041)
                attribBody67 = self.attribBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_attribBody.add(attribBody67.tree)
                RBRACKET68=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_attrib1043) 
                if self._state.backtracking == 0:
                    stream_RBRACKET.add(RBRACKET68)

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
                    # 182:9: -> ^( N_Attrib attribBody )
                    # lesscss.g:182:13: ^( N_Attrib attribBody )
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
    # lesscss.g:185:1: attribBody : ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) );
    def attribBody(self, ):

        retval = self.attribBody_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT69 = None
        IDENT70 = None
        set71 = None
        set72 = None

        IDENT69_tree = None
        IDENT70_tree = None
        set71_tree = None
        set72_tree = None

        try:
            try:
                # lesscss.g:186:5: ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == IDENT) :
                    LA18_1 = self.input.LA(2)

                    if ((OPEQ <= LA18_1 <= DASHMATCH)) :
                        alt18 = 2
                    elif (LA18_1 == RBRACKET) :
                        alt18 = 1
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
                    # lesscss.g:186:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT69=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1078)
                    if self._state.backtracking == 0:

                        IDENT69_tree = self._adaptor.createWithPayload(IDENT69)
                        self._adaptor.addChild(root_0, IDENT69_tree)



                elif alt18 == 2:
                    # lesscss.g:187:7: IDENT ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING )
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT70=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1086)
                    if self._state.backtracking == 0:

                        IDENT70_tree = self._adaptor.createWithPayload(IDENT70)
                        self._adaptor.addChild(root_0, IDENT70_tree)

                    set71 = self.input.LT(1)
                    set71 = self.input.LT(1)
                    if (OPEQ <= self.input.LA(1) <= DASHMATCH):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set71), root_0)
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    set72 = self.input.LT(1)
                    if self.input.LA(1) == STRING or self.input.LA(1) == IDENT:
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set72))
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
    # lesscss.g:190:1: declarationset : declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ ;
    def declarationset(self, ):

        retval = self.declarationset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI74 = None
        SEMI76 = None
        declaration73 = None

        declaration75 = None


        SEMI74_tree = None
        SEMI76_tree = None
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_declaration = RewriteRuleSubtreeStream(self._adaptor, "rule declaration")
        try:
            try:
                # lesscss.g:191:5: ( declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ )
                # lesscss.g:191:7: declaration ( SEMI declaration )* ( SEMI )?
                pass 
                self._state.following.append(self.FOLLOW_declaration_in_declarationset1126)
                declaration73 = self.declaration()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declaration.add(declaration73.tree)
                # lesscss.g:191:19: ( SEMI declaration )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == SEMI) :
                        LA19_1 = self.input.LA(2)

                        if (LA19_1 == IDENT) :
                            alt19 = 1




                    if alt19 == 1:
                        # lesscss.g:191:20: SEMI declaration
                        pass 
                        SEMI74=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1129) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI74)
                        self._state.following.append(self.FOLLOW_declaration_in_declarationset1131)
                        declaration75 = self.declaration()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_declaration.add(declaration75.tree)


                    else:
                        break #loop19
                # lesscss.g:191:39: ( SEMI )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == SEMI) :
                    alt20 = 1
                if alt20 == 1:
                    # lesscss.g:191:39: SEMI
                    pass 
                    SEMI76=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1135) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI76)




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
                    # 191:45: -> ( declaration )+
                    # lesscss.g:191:48: ( declaration )+
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
    # lesscss.g:194:1: declaration : property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) ;
    def declaration(self, ):

        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON78 = None
        property77 = None

        expr79 = None

        prio80 = None


        COLON78_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_property = RewriteRuleSubtreeStream(self._adaptor, "rule property")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_prio = RewriteRuleSubtreeStream(self._adaptor, "rule prio")
        try:
            try:
                # lesscss.g:195:5: ( property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) )
                # lesscss.g:195:7: property COLON expr ( prio )?
                pass 
                self._state.following.append(self.FOLLOW_property_in_declaration1158)
                property77 = self.property()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_property.add(property77.tree)
                COLON78=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1160) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON78)
                self._state.following.append(self.FOLLOW_expr_in_declaration1162)
                expr79 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr79.tree)
                # lesscss.g:195:27: ( prio )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == IMPORTANT_SYM) :
                    alt21 = 1
                if alt21 == 1:
                    # lesscss.g:195:27: prio
                    pass 
                    self._state.following.append(self.FOLLOW_prio_in_declaration1164)
                    prio80 = self.prio()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_prio.add(prio80.tree)




                # AST Rewrite
                # elements: prio, property, expr
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
                    # 195:33: -> ^( N_Declaration property expr ( prio )? )
                    # lesscss.g:195:36: ^( N_Declaration property expr ( prio )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Declaration, "N_Declaration"), root_1)

                    self._adaptor.addChild(root_1, stream_property.nextTree())
                    self._adaptor.addChild(root_1, stream_expr.nextTree())
                    # lesscss.g:195:66: ( prio )?
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
    # lesscss.g:198:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        retval = self.prio_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORTANT_SYM81 = None

        IMPORTANT_SYM81_tree = None

        try:
            try:
                # lesscss.g:199:5: ( IMPORTANT_SYM )
                # lesscss.g:199:7: IMPORTANT_SYM
                pass 
                root_0 = self._adaptor.nil()

                IMPORTANT_SYM81=self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1195)
                if self._state.backtracking == 0:

                    IMPORTANT_SYM81_tree = self._adaptor.createWithPayload(IMPORTANT_SYM81)
                    self._adaptor.addChild(root_0, IMPORTANT_SYM81_tree)




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
    # lesscss.g:203:1: expr : term ( operator term )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        term82 = None

        operator83 = None

        term84 = None



        try:
            try:
                # lesscss.g:204:5: ( term ( operator term )* )
                # lesscss.g:204:7: term ( operator term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_expr1213)
                term82 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term82.tree)
                # lesscss.g:204:12: ( operator term )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == COMMA) :
                        LA22_2 = self.input.LA(2)

                        if (LA22_2 == IDENT) :
                            LA22_4 = self.input.LA(3)

                            if ((STRING <= LA22_4 <= SEMI) or (COMMA <= LA22_4 <= URI) or (RBRACE <= LA22_4 <= IDENT) or (COLON <= LA22_4 <= PLUS) or (HASH <= LA22_4 <= DOT) or (FUNCTION <= LA22_4 <= RPAREN) or (IMPORTANT_SYM <= LA22_4 <= MINUS)) :
                                alt22 = 1


                        elif (LA22_2 == STRING or LA22_2 == URI or LA22_2 == PLUS or LA22_2 == HASH or LA22_2 == FUNCTION or (NUMBER <= LA22_2 <= MINUS)) :
                            alt22 = 1


                    elif (LA22_0 == STRING or LA22_0 == URI or LA22_0 == IDENT or LA22_0 == PLUS or LA22_0 == HASH or LA22_0 == FUNCTION or (SOLIDUS <= LA22_0 <= MINUS)) :
                        alt22 = 1


                    if alt22 == 1:
                        # lesscss.g:204:13: operator term
                        pass 
                        self._state.following.append(self.FOLLOW_operator_in_expr1216)
                        operator83 = self.operator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(operator83.tree, root_0)
                        self._state.following.append(self.FOLLOW_term_in_expr1219)
                        term84 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term84.tree)


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

    class operator_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.operator_return, self).__init__()

            self.tree = None




    # $ANTLR start "operator"
    # lesscss.g:207:10: fragment operator : ( SOLIDUS | COMMA | -> N_Space );
    def operator(self, ):

        retval = self.operator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SOLIDUS85 = None
        COMMA86 = None

        SOLIDUS85_tree = None
        COMMA86_tree = None

        try:
            try:
                # lesscss.g:208:5: ( SOLIDUS | COMMA | -> N_Space )
                alt23 = 3
                LA23 = self.input.LA(1)
                if LA23 == SOLIDUS:
                    alt23 = 1
                elif LA23 == COMMA:
                    alt23 = 2
                elif LA23 == STRING or LA23 == URI or LA23 == IDENT or LA23 == PLUS or LA23 == HASH or LA23 == FUNCTION or LA23 == NUMBER or LA23 == PERCENTAGE or LA23 == LENGTH or LA23 == EMS or LA23 == EXS or LA23 == ANGLE or LA23 == TIME or LA23 == FREQ or LA23 == MINUS:
                    alt23 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # lesscss.g:208:7: SOLIDUS
                    pass 
                    root_0 = self._adaptor.nil()

                    SOLIDUS85=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator1240)
                    if self._state.backtracking == 0:

                        SOLIDUS85_tree = self._adaptor.createWithPayload(SOLIDUS85)
                        self._adaptor.addChild(root_0, SOLIDUS85_tree)



                elif alt23 == 2:
                    # lesscss.g:209:7: COMMA
                    pass 
                    root_0 = self._adaptor.nil()

                    COMMA86=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator1248)
                    if self._state.backtracking == 0:

                        COMMA86_tree = self._adaptor.createWithPayload(COMMA86)
                        self._adaptor.addChild(root_0, COMMA86_tree)



                elif alt23 == 3:
                    # lesscss.g:210:7: 
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
                        # 210:7: -> N_Space
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
    # lesscss.g:213:1: term : ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ ) | STRING | IDENT | URI | function | hexColor );
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set88 = None
        STRING89 = None
        IDENT90 = None
        URI91 = None
        unaryOperator87 = None

        function92 = None

        hexColor93 = None


        set88_tree = None
        STRING89_tree = None
        IDENT90_tree = None
        URI91_tree = None

        try:
            try:
                # lesscss.g:214:5: ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ ) | STRING | IDENT | URI | function | hexColor )
                alt25 = 6
                LA25 = self.input.LA(1)
                if LA25 == PLUS or LA25 == NUMBER or LA25 == PERCENTAGE or LA25 == LENGTH or LA25 == EMS or LA25 == EXS or LA25 == ANGLE or LA25 == TIME or LA25 == FREQ or LA25 == MINUS:
                    alt25 = 1
                elif LA25 == STRING:
                    alt25 = 2
                elif LA25 == IDENT:
                    LA25_3 = self.input.LA(2)

                    if (LA25_3 == COLON or LA25_3 == DOT) :
                        alt25 = 5
                    elif ((STRING <= LA25_3 <= SEMI) or (COMMA <= LA25_3 <= URI) or (RBRACE <= LA25_3 <= IDENT) or LA25_3 == PLUS or LA25_3 == HASH or (FUNCTION <= LA25_3 <= RPAREN) or (IMPORTANT_SYM <= LA25_3 <= MINUS)) :
                        alt25 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 25, 3, self.input)

                        raise nvae

                elif LA25 == URI:
                    alt25 = 4
                elif LA25 == FUNCTION:
                    alt25 = 5
                elif LA25 == HASH:
                    alt25 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # lesscss.g:214:7: ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ )
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:214:20: ( unaryOperator )?
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == PLUS or LA24_0 == MINUS) :
                        alt24 = 1
                    if alt24 == 1:
                        # lesscss.g:214:20: unaryOperator
                        pass 
                        self._state.following.append(self.FOLLOW_unaryOperator_in_term1276)
                        unaryOperator87 = self.unaryOperator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(unaryOperator87.tree, root_0)



                    set88 = self.input.LT(1)
                    if (NUMBER <= self.input.LA(1) <= FREQ):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set88))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse




                elif alt25 == 2:
                    # lesscss.g:225:7: STRING
                    pass 
                    root_0 = self._adaptor.nil()

                    STRING89=self.match(self.input, STRING, self.FOLLOW_STRING_in_term1434)
                    if self._state.backtracking == 0:

                        STRING89_tree = self._adaptor.createWithPayload(STRING89)
                        self._adaptor.addChild(root_0, STRING89_tree)



                elif alt25 == 3:
                    # lesscss.g:226:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT90=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term1442)
                    if self._state.backtracking == 0:

                        IDENT90_tree = self._adaptor.createWithPayload(IDENT90)
                        self._adaptor.addChild(root_0, IDENT90_tree)



                elif alt25 == 4:
                    # lesscss.g:227:7: URI
                    pass 
                    root_0 = self._adaptor.nil()

                    URI91=self.match(self.input, URI, self.FOLLOW_URI_in_term1450)
                    if self._state.backtracking == 0:

                        URI91_tree = self._adaptor.createWithPayload(URI91)
                        self._adaptor.addChild(root_0, URI91_tree)



                elif alt25 == 5:
                    # lesscss.g:228:7: function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_in_term1458)
                    function92 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function92.tree)


                elif alt25 == 6:
                    # lesscss.g:229:7: hexColor
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_hexColor_in_term1466)
                    hexColor93 = self.hexColor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, hexColor93.tree)


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
    # lesscss.g:232:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        retval = self.unaryOperator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set94 = None

        set94_tree = None

        try:
            try:
                # lesscss.g:233:5: ( MINUS | PLUS )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set94 = self.input.LT(1)
                if self.input.LA(1) == PLUS or self.input.LA(1) == MINUS:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set94))
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
    # lesscss.g:238:1: function : ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) );
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RPAREN97 = None
        RPAREN100 = None
        fnct_name95 = None

        fnct_args96 = None

        fnct_name98 = None

        expr99 = None


        RPAREN97_tree = None
        RPAREN100_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_fnct_name = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_name")
        stream_fnct_args = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_args")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:239:5: ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) )
                alt26 = 2
                alt26 = self.dfa26.predict(self.input)
                if alt26 == 1:
                    # lesscss.g:239:7: fnct_name fnct_args RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function1511)
                    fnct_name95 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name95.tree)
                    self._state.following.append(self.FOLLOW_fnct_args_in_function1513)
                    fnct_args96 = self.fnct_args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_args.add(fnct_args96.tree)
                    RPAREN97=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1515) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN97)

                    # AST Rewrite
                    # elements: fnct_name, fnct_args
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
                        # 240:9: -> ^( N_Function fnct_name fnct_args )
                        # lesscss.g:240:12: ^( N_Function fnct_name fnct_args )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_fnct_name.nextTree())
                        self._adaptor.addChild(root_1, stream_fnct_args.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt26 == 2:
                    # lesscss.g:242:7: fnct_name expr RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function1542)
                    fnct_name98 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name98.tree)
                    self._state.following.append(self.FOLLOW_expr_in_function1544)
                    expr99 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr99.tree)
                    RPAREN100=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1546) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN100)

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
                        # 243:9: -> ^( N_Function fnct_name expr )
                        # lesscss.g:243:12: ^( N_Function fnct_name expr )
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
    # lesscss.g:247:1: fnct_name : ( IDENT ( COLON | DOT )+ )* FUNCTION ;
    def fnct_name(self, ):

        retval = self.fnct_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT101 = None
        set102 = None
        FUNCTION103 = None

        IDENT101_tree = None
        set102_tree = None
        FUNCTION103_tree = None

        try:
            try:
                # lesscss.g:248:5: ( ( IDENT ( COLON | DOT )+ )* FUNCTION )
                # lesscss.g:248:7: ( IDENT ( COLON | DOT )+ )* FUNCTION
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:248:7: ( IDENT ( COLON | DOT )+ )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == IDENT) :
                        alt28 = 1


                    if alt28 == 1:
                        # lesscss.g:248:8: IDENT ( COLON | DOT )+
                        pass 
                        IDENT101=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name1583)
                        if self._state.backtracking == 0:

                            IDENT101_tree = self._adaptor.createWithPayload(IDENT101)
                            self._adaptor.addChild(root_0, IDENT101_tree)

                        # lesscss.g:248:14: ( COLON | DOT )+
                        cnt27 = 0
                        while True: #loop27
                            alt27 = 2
                            LA27_0 = self.input.LA(1)

                            if (LA27_0 == COLON or LA27_0 == DOT) :
                                alt27 = 1


                            if alt27 == 1:
                                # lesscss.g:
                                pass 
                                set102 = self.input.LT(1)
                                if self.input.LA(1) == COLON or self.input.LA(1) == DOT:
                                    self.input.consume()
                                    if self._state.backtracking == 0:
                                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set102))
                                    self._state.errorRecovery = False

                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed

                                    mse = MismatchedSetException(None, self.input)
                                    raise mse




                            else:
                                if cnt27 >= 1:
                                    break #loop27

                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                eee = EarlyExitException(27, self.input)
                                raise eee

                            cnt27 += 1


                    else:
                        break #loop28
                FUNCTION103=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name1595)
                if self._state.backtracking == 0:

                    FUNCTION103_tree = self._adaptor.createWithPayload(FUNCTION103)
                    self._adaptor.addChild(root_0, FUNCTION103_tree)




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
    # lesscss.g:251:10: fragment fnct_args : fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ ;
    def fnct_args(self, ):

        retval = self.fnct_args_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA105 = None
        fnct_arg104 = None

        fnct_arg106 = None


        COMMA105_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_fnct_arg = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_arg")
        try:
            try:
                # lesscss.g:252:5: ( fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ )
                # lesscss.g:252:7: fnct_arg ( COMMA fnct_arg )*
                pass 
                self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1614)
                fnct_arg104 = self.fnct_arg()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_fnct_arg.add(fnct_arg104.tree)
                # lesscss.g:252:16: ( COMMA fnct_arg )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == COMMA) :
                        alt29 = 1


                    if alt29 == 1:
                        # lesscss.g:252:17: COMMA fnct_arg
                        pass 
                        COMMA105=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args1617) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA105)
                        self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1619)
                        fnct_arg106 = self.fnct_arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_fnct_arg.add(fnct_arg106.tree)


                    else:
                        break #loop29

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
                    # 253:9: -> ( fnct_arg )+
                    # lesscss.g:253:12: ( fnct_arg )+
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
    # lesscss.g:256:1: fnct_arg : IDENT OPEQ expr ;
    def fnct_arg(self, ):

        retval = self.fnct_arg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT107 = None
        OPEQ108 = None
        expr109 = None


        IDENT107_tree = None
        OPEQ108_tree = None

        try:
            try:
                # lesscss.g:257:5: ( IDENT OPEQ expr )
                # lesscss.g:257:7: IDENT OPEQ expr
                pass 
                root_0 = self._adaptor.nil()

                IDENT107=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_arg1651)
                if self._state.backtracking == 0:

                    IDENT107_tree = self._adaptor.createWithPayload(IDENT107)
                    self._adaptor.addChild(root_0, IDENT107_tree)

                OPEQ108=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_arg1653)
                if self._state.backtracking == 0:

                    OPEQ108_tree = self._adaptor.createWithPayload(OPEQ108)
                    root_0 = self._adaptor.becomeRoot(OPEQ108_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_fnct_arg1656)
                expr109 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr109.tree)



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
    # lesscss.g:260:1: hexColor : HASH ;
    def hexColor(self, ):

        retval = self.hexColor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH110 = None

        HASH110_tree = None

        try:
            try:
                # lesscss.g:261:5: ( HASH )
                # lesscss.g:261:7: HASH
                pass 
                root_0 = self._adaptor.nil()

                HASH110=self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor1673)
                if self._state.backtracking == 0:

                    HASH110_tree = self._adaptor.createWithPayload(HASH110)
                    self._adaptor.addChild(root_0, HASH110_tree)




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
        # lesscss.g:146:20: ( esPred )
        # lesscss.g:146:21: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred1_lesscss787)
        self.esPred()

        self._state.following.pop()


    # $ANTLR end "synpred1_lesscss"



    # $ANTLR start "synpred2_lesscss"
    def synpred2_lesscss_fragment(self, ):
        # lesscss.g:147:8: ( esPred )
        # lesscss.g:147:9: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred2_lesscss802)
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
        u"\1\25\3\uffff\4\0\3\uffff"
        )

    DFA13_max = DFA.unpack(
        u"\1\43\3\uffff\4\0\3\uffff"
        )

    DFA13_accept = DFA.unpack(
        u"\1\uffff\1\2\10\uffff\1\1"
        )

    DFA13_special = DFA.unpack(
        u"\4\uffff\1\0\1\1\1\2\1\3\3\uffff"
        )

            
    DFA13_transition = [
        DFA.unpack(u"\1\1\2\uffff\1\1\1\uffff\1\1\2\uffff\1\7\2\1\1\4\1\5"
        u"\1\6\1\1"),
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
    # lookup tables for DFA #26

    DFA26_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA26_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA26_min = DFA.unpack(
        u"\1\32\1\35\1\22\1\32\1\uffff\1\22\1\uffff"
        )

    DFA26_max = DFA.unpack(
        u"\1\44\1\41\1\64\1\44\1\uffff\1\64\1\uffff"
        )

    DFA26_accept = DFA.unpack(
        u"\4\uffff\1\2\1\uffff\1\1"
        )

    DFA26_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA26_transition = [
        DFA.unpack(u"\1\1\11\uffff\1\2"),
        DFA.unpack(u"\1\3\3\uffff\1\3"),
        DFA.unpack(u"\1\4\3\uffff\1\4\3\uffff\1\5\3\uffff\1\4\1\uffff\1"
        u"\4\3\uffff\1\4\7\uffff\11\4"),
        DFA.unpack(u"\1\1\2\uffff\1\3\3\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\2\uffff\2\4\3\uffff\1\4\2\uffff\2\4\1\uffff\2"
        u"\4\2\uffff\2\4\1\uffff\1\6\3\uffff\12\4"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #26

    class DFA26(DFA):
        pass


 

    FOLLOW_charSet_in_styleSheet169 = frozenset([20, 23, 26, 27, 28, 29, 32, 33, 34, 35])
    FOLLOW_imports_in_styleSheet180 = frozenset([20, 23, 26, 27, 28, 29, 32, 33, 34, 35])
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
    FOLLOW_LBRACE_in_media395 = frozenset([25, 26, 29, 32, 33, 34, 35])
    FOLLOW_ruleSet_in_media409 = frozenset([25, 26, 29, 32, 33, 34, 35])
    FOLLOW_RBRACE_in_media420 = frozenset([1])
    FOLLOW_IDENT_in_medium460 = frozenset([1])
    FOLLOW_FONTFACE_SYM_in_fontface481 = frozenset([24])
    FOLLOW_LBRACE_in_fontface483 = frozenset([26])
    FOLLOW_declarationset_in_fontface485 = frozenset([25])
    FOLLOW_RBRACE_in_fontface487 = frozenset([1])
    FOLLOW_bodyset_in_bodylist524 = frozenset([1, 23, 26, 27, 28, 29, 32, 33, 34, 35])
    FOLLOW_ruleSet_in_bodyset542 = frozenset([1])
    FOLLOW_media_in_bodyset550 = frozenset([1])
    FOLLOW_page_in_bodyset558 = frozenset([1])
    FOLLOW_fontface_in_bodyset566 = frozenset([1])
    FOLLOW_PAGE_SYM_in_page586 = frozenset([24, 29])
    FOLLOW_pseudoPage_in_page588 = frozenset([24])
    FOLLOW_LBRACE_in_page591 = frozenset([26])
    FOLLOW_declarationset_in_page593 = frozenset([25])
    FOLLOW_RBRACE_in_page595 = frozenset([1])
    FOLLOW_COLON_in_pseudoPage631 = frozenset([26])
    FOLLOW_IDENT_in_pseudoPage633 = frozenset([1])
    FOLLOW_IDENT_in_property658 = frozenset([1])
    FOLLOW_selector_in_ruleSet675 = frozenset([21, 24])
    FOLLOW_COMMA_in_ruleSet678 = frozenset([26, 29, 32, 33, 34, 35])
    FOLLOW_selector_in_ruleSet680 = frozenset([21, 24])
    FOLLOW_LBRACE_in_ruleSet684 = frozenset([26])
    FOLLOW_declarationset_in_ruleSet686 = frozenset([25])
    FOLLOW_RBRACE_in_ruleSet688 = frozenset([1])
    FOLLOW_simpleSelector_in_selector728 = frozenset([1, 26, 29, 30, 31, 32, 33, 34, 35])
    FOLLOW_combinator_in_selector731 = frozenset([26, 29, 32, 33, 34, 35])
    FOLLOW_simpleSelector_in_selector733 = frozenset([1, 26, 29, 30, 31, 32, 33, 34, 35])
    FOLLOW_PLUS_in_combinator752 = frozenset([1])
    FOLLOW_GREATER_in_combinator760 = frozenset([1])
    FOLLOW_elementName_in_simpleSelector783 = frozenset([1, 26, 29, 32, 33, 34, 35])
    FOLLOW_elementSubsequent_in_simpleSelector790 = frozenset([1, 26, 29, 32, 33, 34, 35])
    FOLLOW_elementSubsequent_in_simpleSelector805 = frozenset([1, 26, 29, 32, 33, 34, 35])
    FOLLOW_set_in_esPred0 = frozenset([1])
    FOLLOW_set_in_elementName0 = frozenset([1])
    FOLLOW_HASH_in_elementSubsequent878 = frozenset([1])
    FOLLOW_cssClass_in_elementSubsequent886 = frozenset([1])
    FOLLOW_attrib_in_elementSubsequent894 = frozenset([1])
    FOLLOW_pseudo_in_elementSubsequent902 = frozenset([1])
    FOLLOW_DOT_in_cssClass919 = frozenset([26])
    FOLLOW_IDENT_in_cssClass923 = frozenset([1])
    FOLLOW_COLON_in_pseudo963 = frozenset([26])
    FOLLOW_IDENT_in_pseudo967 = frozenset([1])
    FOLLOW_COLON_in_pseudo998 = frozenset([36])
    FOLLOW_FUNCTION_in_pseudo1000 = frozenset([18, 22, 26, 30, 32, 36, 44, 45, 46, 47, 48, 49, 50, 51, 52])
    FOLLOW_expr_in_pseudo1002 = frozenset([37])
    FOLLOW_RPAREN_in_pseudo1004 = frozenset([1])
    FOLLOW_LBRACKET_in_attrib1039 = frozenset([26])
    FOLLOW_attribBody_in_attrib1041 = frozenset([38])
    FOLLOW_RBRACKET_in_attrib1043 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1078 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1086 = frozenset([39, 40, 41])
    FOLLOW_set_in_attribBody1088 = frozenset([18, 26])
    FOLLOW_set_in_attribBody1101 = frozenset([1])
    FOLLOW_declaration_in_declarationset1126 = frozenset([1, 19])
    FOLLOW_SEMI_in_declarationset1129 = frozenset([26])
    FOLLOW_declaration_in_declarationset1131 = frozenset([1, 19])
    FOLLOW_SEMI_in_declarationset1135 = frozenset([1])
    FOLLOW_property_in_declaration1158 = frozenset([29])
    FOLLOW_COLON_in_declaration1160 = frozenset([18, 22, 26, 30, 32, 36, 44, 45, 46, 47, 48, 49, 50, 51, 52])
    FOLLOW_expr_in_declaration1162 = frozenset([1, 42])
    FOLLOW_prio_in_declaration1164 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1195 = frozenset([1])
    FOLLOW_term_in_expr1213 = frozenset([1, 18, 21, 22, 26, 30, 32, 36, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52])
    FOLLOW_operator_in_expr1216 = frozenset([18, 22, 26, 30, 32, 36, 44, 45, 46, 47, 48, 49, 50, 51, 52])
    FOLLOW_term_in_expr1219 = frozenset([1, 18, 21, 22, 26, 30, 32, 36, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52])
    FOLLOW_SOLIDUS_in_operator1240 = frozenset([1])
    FOLLOW_COMMA_in_operator1248 = frozenset([1])
    FOLLOW_unaryOperator_in_term1276 = frozenset([44, 45, 46, 47, 48, 49, 50, 51])
    FOLLOW_set_in_term1288 = frozenset([1])
    FOLLOW_STRING_in_term1434 = frozenset([1])
    FOLLOW_IDENT_in_term1442 = frozenset([1])
    FOLLOW_URI_in_term1450 = frozenset([1])
    FOLLOW_function_in_term1458 = frozenset([1])
    FOLLOW_hexColor_in_term1466 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_fnct_name_in_function1511 = frozenset([26])
    FOLLOW_fnct_args_in_function1513 = frozenset([37])
    FOLLOW_RPAREN_in_function1515 = frozenset([1])
    FOLLOW_fnct_name_in_function1542 = frozenset([18, 22, 26, 30, 32, 36, 44, 45, 46, 47, 48, 49, 50, 51, 52])
    FOLLOW_expr_in_function1544 = frozenset([37])
    FOLLOW_RPAREN_in_function1546 = frozenset([1])
    FOLLOW_IDENT_in_fnct_name1583 = frozenset([29, 33])
    FOLLOW_set_in_fnct_name1585 = frozenset([26, 29, 33, 36])
    FOLLOW_FUNCTION_in_fnct_name1595 = frozenset([1])
    FOLLOW_fnct_arg_in_fnct_args1614 = frozenset([1, 21])
    FOLLOW_COMMA_in_fnct_args1617 = frozenset([26])
    FOLLOW_fnct_arg_in_fnct_args1619 = frozenset([1, 21])
    FOLLOW_IDENT_in_fnct_arg1651 = frozenset([39])
    FOLLOW_OPEQ_in_fnct_arg1653 = frozenset([18, 22, 26, 30, 32, 36, 44, 45, 46, 47, 48, 49, 50, 51, 52])
    FOLLOW_expr_in_fnct_arg1656 = frozenset([1])
    FOLLOW_HASH_in_hexColor1673 = frozenset([1])
    FOLLOW_esPred_in_synpred1_lesscss787 = frozenset([1])
    FOLLOW_esPred_in_synpred2_lesscss802 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("lesscssLexer", lesscssParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
