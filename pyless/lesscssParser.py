# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 lesscss.g 2012-11-17 16:28:57

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=40
STAR=34
EOF=-1
MEDIA_SYM=24
INCLUDES=43
LBRACKET=39
RPAREN=31
NAME=63
GREATER=36
ESCAPE=60
DIMENSION=96
STRINGESC=94
NL=97
COMMENT=91
N_Media=9
D=68
E=69
F=70
G=71
A=65
RBRACE=26
B=66
C=67
L=76
IMPORT_SYM=22
NMCHAR=62
M=77
N=78
O=79
H=72
I=73
J=74
NUMBER=47
K=75
U=85
T=84
W=87
V=86
Q=81
P=80
S=83
CDO=92
R=82
CDC=93
PERCENTAGE=48
URL=64
Y=89
X=88
URI=23
Z=90
PAGE_SYM=33
WS=95
DASHMATCH=44
EMS=50
N_RuleSet=12
NONASCII=58
N_Page=8
N_MediaQuery=10
N_Declarations=14
N_Selector=13
LBRACE=25
N_Import=6
LPAREN=29
LENGTH=49
IMPORTANT_SYM=45
N_Function=16
TIME=53
COMMA=27
N_StyleSheet=4
IDENT=28
PLUS=35
FREQ=54
RBRACKET=41
DOT=38
CHARSET_SYM=19
ANGLE=52
HASH=37
HEXCHAR=57
N_CharSet=5
RESOLUTION=55
MINUS=56
SOLIDUS=46
SEMI=21
UNICODE=59
COLON=30
NMSTART=61
N_Declaration=15
OPEQ=42
FONTFACE_SYM=32
EXS=51
N_Space=18
N_MediaExpr=11
N_Attrib=17
STRING=20
N_FontFace=7

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "N_StyleSheet", "N_CharSet", "N_Import", "N_FontFace", "N_Page", "N_Media", 
    "N_MediaQuery", "N_MediaExpr", "N_RuleSet", "N_Selector", "N_Declarations", 
    "N_Declaration", "N_Function", "N_Attrib", "N_Space", "CHARSET_SYM", 
    "STRING", "SEMI", "IMPORT_SYM", "URI", "MEDIA_SYM", "LBRACE", "RBRACE", 
    "COMMA", "IDENT", "LPAREN", "COLON", "RPAREN", "FONTFACE_SYM", "PAGE_SYM", 
    "STAR", "PLUS", "GREATER", "HASH", "DOT", "LBRACKET", "FUNCTION", "RBRACKET", 
    "OPEQ", "INCLUDES", "DASHMATCH", "IMPORTANT_SYM", "SOLIDUS", "NUMBER", 
    "PERCENTAGE", "LENGTH", "EMS", "EXS", "ANGLE", "TIME", "FREQ", "RESOLUTION", 
    "MINUS", "HEXCHAR", "NONASCII", "UNICODE", "ESCAPE", "NMSTART", "NMCHAR", 
    "NAME", "URL", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
    "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", 
    "Z", "COMMENT", "CDO", "CDC", "STRINGESC", "WS", "DIMENSION", "NL"
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

        self.dfa20 = self.DFA20(
            self, 20,
            eot = self.DFA20_eot,
            eof = self.DFA20_eof,
            min = self.DFA20_min,
            max = self.DFA20_max,
            accept = self.DFA20_accept,
            special = self.DFA20_special,
            transition = self.DFA20_transition
            )

        self.dfa33 = self.DFA33(
            self, 33,
            eot = self.DFA33_eot,
            eof = self.DFA33_eof,
            min = self.DFA33_min,
            max = self.DFA33_max,
            accept = self.DFA33_accept,
            special = self.DFA33_special,
            transition = self.DFA33_transition
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
    # lesscss.g:52:1: styleSheet : ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? ) ;
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
                # lesscss.g:53:5: ( ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? ) )
                # lesscss.g:53:9: ( charSet )? ( imports )* bodylist EOF
                pass 
                # lesscss.g:53:9: ( charSet )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == CHARSET_SYM) :
                    alt1 = 1
                if alt1 == 1:
                    # lesscss.g:53:9: charSet
                    pass 
                    self._state.following.append(self.FOLLOW_charSet_in_styleSheet183)
                    charSet1 = self.charSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_charSet.add(charSet1.tree)



                # lesscss.g:54:9: ( imports )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == IMPORT_SYM) :
                        alt2 = 1


                    if alt2 == 1:
                        # lesscss.g:54:9: imports
                        pass 
                        self._state.following.append(self.FOLLOW_imports_in_styleSheet194)
                        imports2 = self.imports()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_imports.add(imports2.tree)


                    else:
                        break #loop2
                self._state.following.append(self.FOLLOW_bodylist_in_styleSheet205)
                bodylist3 = self.bodylist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_bodylist.add(bodylist3.tree)
                EOF4=self.match(self.input, EOF, self.FOLLOW_EOF_in_styleSheet215) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF4)

                # AST Rewrite
                # elements: imports, charSet, bodylist
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
                    # 57:13: -> ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? )
                    # lesscss.g:57:16: ^( N_StyleSheet ( charSet )? ( imports )* ( bodylist )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_StyleSheet, "N_StyleSheet"), root_1)

                    # lesscss.g:57:31: ( charSet )?
                    if stream_charSet.hasNext():
                        self._adaptor.addChild(root_1, stream_charSet.nextTree())


                    stream_charSet.reset();
                    # lesscss.g:57:40: ( imports )*
                    while stream_imports.hasNext():
                        self._adaptor.addChild(root_1, stream_imports.nextTree())


                    stream_imports.reset();
                    # lesscss.g:57:49: ( bodylist )?
                    if stream_bodylist.hasNext():
                        self._adaptor.addChild(root_1, stream_bodylist.nextTree())


                    stream_bodylist.reset();

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
    # lesscss.g:63:1: charSet : CHARSET_SYM STRING SEMI -> ^( N_CharSet STRING ) ;
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
                # lesscss.g:64:5: ( CHARSET_SYM STRING SEMI -> ^( N_CharSet STRING ) )
                # lesscss.g:64:9: CHARSET_SYM STRING SEMI
                pass 
                CHARSET_SYM5=self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet268) 
                if self._state.backtracking == 0:
                    stream_CHARSET_SYM.add(CHARSET_SYM5)
                STRING6=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet270) 
                if self._state.backtracking == 0:
                    stream_STRING.add(STRING6)
                SEMI7=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_charSet272) 
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
                    # 65:9: -> ^( N_CharSet STRING )
                    # lesscss.g:65:12: ^( N_CharSet STRING )
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
    # lesscss.g:71:1: imports : IMPORT_SYM importUrl ( media_query_list )? SEMI -> ^( N_Import importUrl ( media_query_list )? ) ;
    def imports(self, ):

        retval = self.imports_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORT_SYM8 = None
        SEMI11 = None
        importUrl9 = None

        media_query_list10 = None


        IMPORT_SYM8_tree = None
        SEMI11_tree = None
        stream_IMPORT_SYM = RewriteRuleTokenStream(self._adaptor, "token IMPORT_SYM")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_media_query_list = RewriteRuleSubtreeStream(self._adaptor, "rule media_query_list")
        stream_importUrl = RewriteRuleSubtreeStream(self._adaptor, "rule importUrl")
        try:
            try:
                # lesscss.g:72:5: ( IMPORT_SYM importUrl ( media_query_list )? SEMI -> ^( N_Import importUrl ( media_query_list )? ) )
                # lesscss.g:72:9: IMPORT_SYM importUrl ( media_query_list )? SEMI
                pass 
                IMPORT_SYM8=self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports310) 
                if self._state.backtracking == 0:
                    stream_IMPORT_SYM.add(IMPORT_SYM8)
                self._state.following.append(self.FOLLOW_importUrl_in_imports312)
                importUrl9 = self.importUrl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_importUrl.add(importUrl9.tree)
                # lesscss.g:72:30: ( media_query_list )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((IDENT <= LA3_0 <= LPAREN)) :
                    alt3 = 1
                if alt3 == 1:
                    # lesscss.g:72:30: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_imports314)
                    media_query_list10 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_media_query_list.add(media_query_list10.tree)



                SEMI11=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_imports317) 
                if self._state.backtracking == 0:
                    stream_SEMI.add(SEMI11)

                # AST Rewrite
                # elements: importUrl, media_query_list
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
                    # 73:9: -> ^( N_Import importUrl ( media_query_list )? )
                    # lesscss.g:73:12: ^( N_Import importUrl ( media_query_list )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Import, "N_Import"), root_1)

                    self._adaptor.addChild(root_1, stream_importUrl.nextTree())
                    # lesscss.g:73:33: ( media_query_list )?
                    if stream_media_query_list.hasNext():
                        self._adaptor.addChild(root_1, stream_media_query_list.nextTree())


                    stream_media_query_list.reset();

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
    # lesscss.g:76:1: importUrl : ( STRING | URI );
    def importUrl(self, ):

        retval = self.importUrl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set12 = None

        set12_tree = None

        try:
            try:
                # lesscss.g:77:5: ( STRING | URI )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set12 = self.input.LT(1)
                if self.input.LA(1) == STRING or self.input.LA(1) == URI:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set12))
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
    # lesscss.g:85:1: media : MEDIA_SYM ( media_query_list )? LBRACE ( ruleSet )* RBRACE -> ^( N_Media ( media_query_list )? ( ruleSet )* ) ;
    def media(self, ):

        retval = self.media_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MEDIA_SYM13 = None
        LBRACE15 = None
        RBRACE17 = None
        media_query_list14 = None

        ruleSet16 = None


        MEDIA_SYM13_tree = None
        LBRACE15_tree = None
        RBRACE17_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_MEDIA_SYM = RewriteRuleTokenStream(self._adaptor, "token MEDIA_SYM")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_media_query_list = RewriteRuleSubtreeStream(self._adaptor, "rule media_query_list")
        stream_ruleSet = RewriteRuleSubtreeStream(self._adaptor, "rule ruleSet")
        try:
            try:
                # lesscss.g:86:5: ( MEDIA_SYM ( media_query_list )? LBRACE ( ruleSet )* RBRACE -> ^( N_Media ( media_query_list )? ( ruleSet )* ) )
                # lesscss.g:86:7: MEDIA_SYM ( media_query_list )? LBRACE ( ruleSet )* RBRACE
                pass 
                MEDIA_SYM13=self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media382) 
                if self._state.backtracking == 0:
                    stream_MEDIA_SYM.add(MEDIA_SYM13)
                # lesscss.g:86:17: ( media_query_list )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((IDENT <= LA4_0 <= LPAREN)) :
                    alt4 = 1
                if alt4 == 1:
                    # lesscss.g:86:17: media_query_list
                    pass 
                    self._state.following.append(self.FOLLOW_media_query_list_in_media384)
                    media_query_list14 = self.media_query_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_media_query_list.add(media_query_list14.tree)



                LBRACE15=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_media395) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE15)
                # lesscss.g:88:13: ( ruleSet )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == IDENT or LA5_0 == COLON or LA5_0 == STAR or (HASH <= LA5_0 <= LBRACKET)) :
                        alt5 = 1


                    if alt5 == 1:
                        # lesscss.g:88:13: ruleSet
                        pass 
                        self._state.following.append(self.FOLLOW_ruleSet_in_media409)
                        ruleSet16 = self.ruleSet()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_ruleSet.add(ruleSet16.tree)


                    else:
                        break #loop5
                RBRACE17=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_media420) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE17)

                # AST Rewrite
                # elements: media_query_list, ruleSet
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
                    # 90:9: -> ^( N_Media ( media_query_list )? ( ruleSet )* )
                    # lesscss.g:90:12: ^( N_Media ( media_query_list )? ( ruleSet )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Media, "N_Media"), root_1)

                    # lesscss.g:90:22: ( media_query_list )?
                    if stream_media_query_list.hasNext():
                        self._adaptor.addChild(root_1, stream_media_query_list.nextTree())


                    stream_media_query_list.reset();
                    # lesscss.g:90:40: ( ruleSet )*
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

    class media_query_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_query_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_query_list"
    # lesscss.g:96:1: media_query_list : media_query ( COMMA media_query )* -> ^( N_MediaQuery ( media_query )+ ) ;
    def media_query_list(self, ):

        retval = self.media_query_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA19 = None
        media_query18 = None

        media_query20 = None


        COMMA19_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_media_query = RewriteRuleSubtreeStream(self._adaptor, "rule media_query")
        try:
            try:
                # lesscss.g:97:5: ( media_query ( COMMA media_query )* -> ^( N_MediaQuery ( media_query )+ ) )
                # lesscss.g:97:7: media_query ( COMMA media_query )*
                pass 
                self._state.following.append(self.FOLLOW_media_query_in_media_query_list460)
                media_query18 = self.media_query()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_media_query.add(media_query18.tree)
                # lesscss.g:97:19: ( COMMA media_query )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == COMMA) :
                        alt6 = 1


                    if alt6 == 1:
                        # lesscss.g:97:20: COMMA media_query
                        pass 
                        COMMA19=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_media_query_list463) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA19)
                        self._state.following.append(self.FOLLOW_media_query_in_media_query_list465)
                        media_query20 = self.media_query()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_media_query.add(media_query20.tree)


                    else:
                        break #loop6

                # AST Rewrite
                # elements: media_query
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
                    # 98:9: -> ^( N_MediaQuery ( media_query )+ )
                    # lesscss.g:98:12: ^( N_MediaQuery ( media_query )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_MediaQuery, "N_MediaQuery"), root_1)

                    # lesscss.g:98:27: ( media_query )+
                    if not (stream_media_query.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_media_query.hasNext():
                        self._adaptor.addChild(root_1, stream_media_query.nextTree())


                    stream_media_query.reset()

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

    # $ANTLR end "media_query_list"

    class media_query_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_query_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_query"
    # lesscss.g:101:1: media_query : ( ( IDENT )? media_type ( IDENT media_expr )* | media_expr ( IDENT media_expr )* );
    def media_query(self, ):

        retval = self.media_query_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT21 = None
        IDENT23 = None
        IDENT26 = None
        media_type22 = None

        media_expr24 = None

        media_expr25 = None

        media_expr27 = None


        IDENT21_tree = None
        IDENT23_tree = None
        IDENT26_tree = None

        try:
            try:
                # lesscss.g:102:5: ( ( IDENT )? media_type ( IDENT media_expr )* | media_expr ( IDENT media_expr )* )
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == IDENT) :
                    alt10 = 1
                elif (LA10_0 == LPAREN) :
                    alt10 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # lesscss.g:102:7: ( IDENT )? media_type ( IDENT media_expr )*
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:102:7: ( IDENT )?
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == IDENT) :
                        LA7_1 = self.input.LA(2)

                        if (LA7_1 == IDENT) :
                            LA7_2 = self.input.LA(3)

                            if (LA7_2 == SEMI or LA7_2 == LBRACE or (COMMA <= LA7_2 <= IDENT)) :
                                alt7 = 1
                    if alt7 == 1:
                        # lesscss.g:102:9: IDENT
                        pass 
                        IDENT21=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_query503)
                        if self._state.backtracking == 0:

                            IDENT21_tree = self._adaptor.createWithPayload(IDENT21)
                            self._adaptor.addChild(root_0, IDENT21_tree)




                    self._state.following.append(self.FOLLOW_media_type_in_media_query508)
                    media_type22 = self.media_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_type22.tree)
                    # lesscss.g:102:29: ( IDENT media_expr )*
                    while True: #loop8
                        alt8 = 2
                        LA8_0 = self.input.LA(1)

                        if (LA8_0 == IDENT) :
                            alt8 = 1


                        if alt8 == 1:
                            # lesscss.g:102:31: IDENT media_expr
                            pass 
                            IDENT23=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_query512)
                            if self._state.backtracking == 0:

                                IDENT23_tree = self._adaptor.createWithPayload(IDENT23)
                                root_0 = self._adaptor.becomeRoot(IDENT23_tree, root_0)

                            self._state.following.append(self.FOLLOW_media_expr_in_media_query515)
                            media_expr24 = self.media_expr()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, media_expr24.tree)


                        else:
                            break #loop8


                elif alt10 == 2:
                    # lesscss.g:103:7: media_expr ( IDENT media_expr )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_media_expr_in_media_query526)
                    media_expr25 = self.media_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media_expr25.tree)
                    # lesscss.g:103:18: ( IDENT media_expr )*
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == IDENT) :
                            alt9 = 1


                        if alt9 == 1:
                            # lesscss.g:103:20: IDENT media_expr
                            pass 
                            IDENT26=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_query530)
                            if self._state.backtracking == 0:

                                IDENT26_tree = self._adaptor.createWithPayload(IDENT26)
                                root_0 = self._adaptor.becomeRoot(IDENT26_tree, root_0)

                            self._state.following.append(self.FOLLOW_media_expr_in_media_query533)
                            media_expr27 = self.media_expr()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, media_expr27.tree)


                        else:
                            break #loop9


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

    # $ANTLR end "media_query"

    class media_type_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_type_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_type"
    # lesscss.g:106:1: media_type : IDENT ;
    def media_type(self, ):

        retval = self.media_type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT28 = None

        IDENT28_tree = None

        try:
            try:
                # lesscss.g:107:5: ( IDENT )
                # lesscss.g:107:7: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT28=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_type553)
                if self._state.backtracking == 0:

                    IDENT28_tree = self._adaptor.createWithPayload(IDENT28)
                    self._adaptor.addChild(root_0, IDENT28_tree)




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

    # $ANTLR end "media_type"

    class media_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_expr"
    # lesscss.g:110:1: media_expr : LPAREN media_feature ( COLON expr )? ( COLON )? RPAREN -> ^( N_MediaExpr media_feature ( expr )? ) ;
    def media_expr(self, ):

        retval = self.media_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN29 = None
        COLON31 = None
        COLON33 = None
        RPAREN34 = None
        media_feature30 = None

        expr32 = None


        LPAREN29_tree = None
        COLON31_tree = None
        COLON33_tree = None
        RPAREN34_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_media_feature = RewriteRuleSubtreeStream(self._adaptor, "rule media_feature")
        try:
            try:
                # lesscss.g:111:5: ( LPAREN media_feature ( COLON expr )? ( COLON )? RPAREN -> ^( N_MediaExpr media_feature ( expr )? ) )
                # lesscss.g:111:7: LPAREN media_feature ( COLON expr )? ( COLON )? RPAREN
                pass 
                LPAREN29=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_media_expr570) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN29)
                self._state.following.append(self.FOLLOW_media_feature_in_media_expr572)
                media_feature30 = self.media_feature()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_media_feature.add(media_feature30.tree)
                # lesscss.g:111:28: ( COLON expr )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == COLON) :
                    LA11_1 = self.input.LA(2)

                    if (LA11_1 == STRING or LA11_1 == URI or LA11_1 == IDENT or LA11_1 == PLUS or LA11_1 == HASH or LA11_1 == FUNCTION or (NUMBER <= LA11_1 <= MINUS)) :
                        alt11 = 1
                if alt11 == 1:
                    # lesscss.g:111:30: COLON expr
                    pass 
                    COLON31=self.match(self.input, COLON, self.FOLLOW_COLON_in_media_expr576) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON31)
                    self._state.following.append(self.FOLLOW_expr_in_media_expr578)
                    expr32 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr32.tree)



                # lesscss.g:111:44: ( COLON )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == COLON) :
                    alt12 = 1
                if alt12 == 1:
                    # lesscss.g:111:44: COLON
                    pass 
                    COLON33=self.match(self.input, COLON, self.FOLLOW_COLON_in_media_expr583) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON33)



                RPAREN34=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_media_expr586) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN34)

                # AST Rewrite
                # elements: media_feature, expr
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
                    # 112:9: -> ^( N_MediaExpr media_feature ( expr )? )
                    # lesscss.g:112:12: ^( N_MediaExpr media_feature ( expr )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_MediaExpr, "N_MediaExpr"), root_1)

                    self._adaptor.addChild(root_1, stream_media_feature.nextTree())
                    # lesscss.g:112:40: ( expr )?
                    if stream_expr.hasNext():
                        self._adaptor.addChild(root_1, stream_expr.nextTree())


                    stream_expr.reset();

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

    # $ANTLR end "media_expr"

    class media_feature_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_feature_return, self).__init__()

            self.tree = None




    # $ANTLR start "media_feature"
    # lesscss.g:115:1: media_feature : IDENT ;
    def media_feature(self, ):

        retval = self.media_feature_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT35 = None

        IDENT35_tree = None

        try:
            try:
                # lesscss.g:116:5: ( IDENT )
                # lesscss.g:116:7: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT35=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_media_feature623)
                if self._state.backtracking == 0:

                    IDENT35_tree = self._adaptor.createWithPayload(IDENT35)
                    self._adaptor.addChild(root_0, IDENT35_tree)




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

    # $ANTLR end "media_feature"

    class fontface_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fontface_return, self).__init__()

            self.tree = None




    # $ANTLR start "fontface"
    # lesscss.g:122:1: fontface : FONTFACE_SYM LBRACE declarationset RBRACE -> ^( N_FontFace declarationset ) ;
    def fontface(self, ):

        retval = self.fontface_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FONTFACE_SYM36 = None
        LBRACE37 = None
        RBRACE39 = None
        declarationset38 = None


        FONTFACE_SYM36_tree = None
        LBRACE37_tree = None
        RBRACE39_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_FONTFACE_SYM = RewriteRuleTokenStream(self._adaptor, "token FONTFACE_SYM")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        try:
            try:
                # lesscss.g:123:5: ( FONTFACE_SYM LBRACE declarationset RBRACE -> ^( N_FontFace declarationset ) )
                # lesscss.g:123:7: FONTFACE_SYM LBRACE declarationset RBRACE
                pass 
                FONTFACE_SYM36=self.match(self.input, FONTFACE_SYM, self.FOLLOW_FONTFACE_SYM_in_fontface643) 
                if self._state.backtracking == 0:
                    stream_FONTFACE_SYM.add(FONTFACE_SYM36)
                LBRACE37=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_fontface645) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE37)
                self._state.following.append(self.FOLLOW_declarationset_in_fontface647)
                declarationset38 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset38.tree)
                RBRACE39=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_fontface649) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE39)

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
                    # 124:9: -> ^( N_FontFace declarationset )
                    # lesscss.g:124:12: ^( N_FontFace declarationset )
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
    # lesscss.g:127:1: bodylist : ( bodyset )* ;
    def bodylist(self, ):

        retval = self.bodylist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        bodyset40 = None



        try:
            try:
                # lesscss.g:128:5: ( ( bodyset )* )
                # lesscss.g:128:7: ( bodyset )*
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:128:7: ( bodyset )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == MEDIA_SYM or LA13_0 == IDENT or LA13_0 == COLON or (FONTFACE_SYM <= LA13_0 <= STAR) or (HASH <= LA13_0 <= LBRACKET)) :
                        alt13 = 1


                    if alt13 == 1:
                        # lesscss.g:128:7: bodyset
                        pass 
                        self._state.following.append(self.FOLLOW_bodyset_in_bodylist686)
                        bodyset40 = self.bodyset()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, bodyset40.tree)


                    else:
                        break #loop13



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
    # lesscss.g:131:1: bodyset : ( ruleSet | media | page | fontface );
    def bodyset(self, ):

        retval = self.bodyset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ruleSet41 = None

        media42 = None

        page43 = None

        fontface44 = None



        try:
            try:
                # lesscss.g:132:5: ( ruleSet | media | page | fontface )
                alt14 = 4
                LA14 = self.input.LA(1)
                if LA14 == IDENT or LA14 == COLON or LA14 == STAR or LA14 == HASH or LA14 == DOT or LA14 == LBRACKET:
                    alt14 = 1
                elif LA14 == MEDIA_SYM:
                    alt14 = 2
                elif LA14 == PAGE_SYM:
                    alt14 = 3
                elif LA14 == FONTFACE_SYM:
                    alt14 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae

                if alt14 == 1:
                    # lesscss.g:132:7: ruleSet
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_ruleSet_in_bodyset704)
                    ruleSet41 = self.ruleSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, ruleSet41.tree)


                elif alt14 == 2:
                    # lesscss.g:133:7: media
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_media_in_bodyset712)
                    media42 = self.media()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media42.tree)


                elif alt14 == 3:
                    # lesscss.g:134:7: page
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_page_in_bodyset720)
                    page43 = self.page()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, page43.tree)


                elif alt14 == 4:
                    # lesscss.g:135:7: fontface
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fontface_in_bodyset728)
                    fontface44 = self.fontface()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fontface44.tree)


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
    # lesscss.g:138:1: page : PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE -> ^( N_Page ( pseudoPage )? declarationset ) ;
    def page(self, ):

        retval = self.page_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PAGE_SYM45 = None
        LBRACE47 = None
        RBRACE49 = None
        pseudoPage46 = None

        declarationset48 = None


        PAGE_SYM45_tree = None
        LBRACE47_tree = None
        RBRACE49_tree = None
        stream_PAGE_SYM = RewriteRuleTokenStream(self._adaptor, "token PAGE_SYM")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        stream_pseudoPage = RewriteRuleSubtreeStream(self._adaptor, "rule pseudoPage")
        try:
            try:
                # lesscss.g:139:5: ( PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE -> ^( N_Page ( pseudoPage )? declarationset ) )
                # lesscss.g:139:7: PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE
                pass 
                PAGE_SYM45=self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page748) 
                if self._state.backtracking == 0:
                    stream_PAGE_SYM.add(PAGE_SYM45)
                # lesscss.g:139:16: ( pseudoPage )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == COLON) :
                    alt15 = 1
                if alt15 == 1:
                    # lesscss.g:139:16: pseudoPage
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoPage_in_page750)
                    pseudoPage46 = self.pseudoPage()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_pseudoPage.add(pseudoPage46.tree)



                LBRACE47=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_page753) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE47)
                self._state.following.append(self.FOLLOW_declarationset_in_page755)
                declarationset48 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset48.tree)
                RBRACE49=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_page757) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE49)

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
                    # 140:9: -> ^( N_Page ( pseudoPage )? declarationset )
                    # lesscss.g:140:12: ^( N_Page ( pseudoPage )? declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Page, "N_Page"), root_1)

                    # lesscss.g:140:21: ( pseudoPage )?
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
    # lesscss.g:143:1: pseudoPage : COLON IDENT -> IDENT ;
    def pseudoPage(self, ):

        retval = self.pseudoPage_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON50 = None
        IDENT51 = None

        COLON50_tree = None
        IDENT51_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")

        try:
            try:
                # lesscss.g:144:5: ( COLON IDENT -> IDENT )
                # lesscss.g:144:7: COLON IDENT
                pass 
                COLON50=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudoPage793) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON50)
                IDENT51=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage795) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT51)

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
                    # 144:19: -> IDENT
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
    # lesscss.g:147:1: property : ( IDENT | STAR a= IDENT -> IDENT );
    def property(self, ):

        retval = self.property_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        IDENT52 = None
        STAR53 = None

        a_tree = None
        IDENT52_tree = None
        STAR53_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_STAR = RewriteRuleTokenStream(self._adaptor, "token STAR")

        try:
            try:
                # lesscss.g:148:5: ( IDENT | STAR a= IDENT -> IDENT )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == IDENT) :
                    alt16 = 1
                elif (LA16_0 == STAR) :
                    alt16 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # lesscss.g:148:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT52=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property820)
                    if self._state.backtracking == 0:

                        IDENT52_tree = self._adaptor.createWithPayload(IDENT52)
                        self._adaptor.addChild(root_0, IDENT52_tree)



                elif alt16 == 2:
                    # lesscss.g:152:7: STAR a= IDENT
                    pass 
                    STAR53=self.match(self.input, STAR, self.FOLLOW_STAR_in_property839) 
                    if self._state.backtracking == 0:
                        stream_STAR.add(STAR53)
                    a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property843) 
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
                        # 154:9: -> IDENT
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
    # lesscss.g:158:1: ruleSet : selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) ;
    def ruleSet(self, ):

        retval = self.ruleSet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA55 = None
        LBRACE57 = None
        RBRACE59 = None
        selector54 = None

        selector56 = None

        declarationset58 = None


        COMMA55_tree = None
        LBRACE57_tree = None
        RBRACE59_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_selector = RewriteRuleSubtreeStream(self._adaptor, "rule selector")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        try:
            try:
                # lesscss.g:159:5: ( selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset ) )
                # lesscss.g:159:7: selector ( COMMA selector )* LBRACE declarationset RBRACE
                pass 
                self._state.following.append(self.FOLLOW_selector_in_ruleSet884)
                selector54 = self.selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_selector.add(selector54.tree)
                # lesscss.g:159:16: ( COMMA selector )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == COMMA) :
                        alt17 = 1


                    if alt17 == 1:
                        # lesscss.g:159:17: COMMA selector
                        pass 
                        COMMA55=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_ruleSet887) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA55)
                        self._state.following.append(self.FOLLOW_selector_in_ruleSet889)
                        selector56 = self.selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_selector.add(selector56.tree)


                    else:
                        break #loop17
                LBRACE57=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_ruleSet893) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE57)
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet895)
                declarationset58 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset58.tree)
                RBRACE59=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_ruleSet897) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE59)

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
                    # 160:9: -> ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    # lesscss.g:160:12: ^( N_RuleSet ( ^( N_Selector selector ) )+ declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_RuleSet, "N_RuleSet"), root_1)

                    # lesscss.g:160:24: ( ^( N_Selector selector ) )+
                    if not (stream_selector.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_selector.hasNext():
                        # lesscss.g:160:24: ^( N_Selector selector )
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
    # lesscss.g:163:1: selector : simpleSelector ( combinator simpleSelector )* ;
    def selector(self, ):

        retval = self.selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        simpleSelector60 = None

        combinator61 = None

        simpleSelector62 = None



        try:
            try:
                # lesscss.g:164:5: ( simpleSelector ( combinator simpleSelector )* )
                # lesscss.g:164:7: simpleSelector ( combinator simpleSelector )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_simpleSelector_in_selector937)
                simpleSelector60 = self.simpleSelector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, simpleSelector60.tree)
                # lesscss.g:164:22: ( combinator simpleSelector )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == IDENT or LA18_0 == COLON or (STAR <= LA18_0 <= LBRACKET)) :
                        alt18 = 1


                    if alt18 == 1:
                        # lesscss.g:164:23: combinator simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector940)
                        combinator61 = self.combinator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, combinator61.tree)
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector942)
                        simpleSelector62 = self.simpleSelector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, simpleSelector62.tree)


                    else:
                        break #loop18



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
    # lesscss.g:167:1: combinator : ( PLUS | GREATER | );
    def combinator(self, ):

        retval = self.combinator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS63 = None
        GREATER64 = None

        PLUS63_tree = None
        GREATER64_tree = None

        try:
            try:
                # lesscss.g:168:5: ( PLUS | GREATER | )
                alt19 = 3
                LA19 = self.input.LA(1)
                if LA19 == PLUS:
                    alt19 = 1
                elif LA19 == GREATER:
                    alt19 = 2
                elif LA19 == IDENT or LA19 == COLON or LA19 == STAR or LA19 == HASH or LA19 == DOT or LA19 == LBRACKET:
                    alt19 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # lesscss.g:168:7: PLUS
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS63=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator961)
                    if self._state.backtracking == 0:

                        PLUS63_tree = self._adaptor.createWithPayload(PLUS63)
                        self._adaptor.addChild(root_0, PLUS63_tree)



                elif alt19 == 2:
                    # lesscss.g:169:7: GREATER
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER64=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator969)
                    if self._state.backtracking == 0:

                        GREATER64_tree = self._adaptor.createWithPayload(GREATER64)
                        self._adaptor.addChild(root_0, GREATER64_tree)



                elif alt19 == 3:
                    # lesscss.g:171:5: 
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
    # lesscss.g:173:1: simpleSelector : ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ );
    def simpleSelector(self, ):

        retval = self.simpleSelector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        elementName65 = None

        elementSubsequent66 = None

        elementSubsequent67 = None



        try:
            try:
                # lesscss.g:174:5: ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ )
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == IDENT or LA22_0 == STAR) :
                    alt22 = 1
                elif (LA22_0 == COLON or (HASH <= LA22_0 <= LBRACKET)) :
                    alt22 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # lesscss.g:174:7: elementName ( ( esPred )=> elementSubsequent )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elementName_in_simpleSelector992)
                    elementName65 = self.elementName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, elementName65.tree)
                    # lesscss.g:174:19: ( ( esPred )=> elementSubsequent )*
                    while True: #loop20
                        alt20 = 2
                        alt20 = self.dfa20.predict(self.input)
                        if alt20 == 1:
                            # lesscss.g:174:20: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector999)
                            elementSubsequent66 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent66.tree)


                        else:
                            break #loop20


                elif alt22 == 2:
                    # lesscss.g:175:7: ( ( esPred )=> elementSubsequent )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:175:7: ( ( esPred )=> elementSubsequent )+
                    cnt21 = 0
                    while True: #loop21
                        alt21 = 2
                        LA21 = self.input.LA(1)
                        if LA21 == HASH:
                            LA21_2 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt21 = 1


                        elif LA21 == DOT:
                            LA21_3 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt21 = 1


                        elif LA21 == LBRACKET:
                            LA21_4 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt21 = 1


                        elif LA21 == COLON:
                            LA21_5 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt21 = 1



                        if alt21 == 1:
                            # lesscss.g:175:8: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector1014)
                            elementSubsequent67 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent67.tree)


                        else:
                            if cnt21 >= 1:
                                break #loop21

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(21, self.input)
                            raise eee

                        cnt21 += 1


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
    # lesscss.g:178:1: esPred : ( HASH | DOT | LBRACKET | COLON );
    def esPred(self, ):

        retval = self.esPred_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set68 = None

        set68_tree = None

        try:
            try:
                # lesscss.g:179:5: ( HASH | DOT | LBRACKET | COLON )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set68 = self.input.LT(1)
                if self.input.LA(1) == COLON or (HASH <= self.input.LA(1) <= LBRACKET):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set68))
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
    # lesscss.g:182:1: elementName : ( IDENT | STAR );
    def elementName(self, ):

        retval = self.elementName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set69 = None

        set69_tree = None

        try:
            try:
                # lesscss.g:183:5: ( IDENT | STAR )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set69 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == STAR:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set69))
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
    # lesscss.g:187:1: elementSubsequent : ( HASH | cssClass | attrib | pseudo );
    def elementSubsequent(self, ):

        retval = self.elementSubsequent_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH70 = None
        cssClass71 = None

        attrib72 = None

        pseudo73 = None


        HASH70_tree = None

        try:
            try:
                # lesscss.g:188:5: ( HASH | cssClass | attrib | pseudo )
                alt23 = 4
                LA23 = self.input.LA(1)
                if LA23 == HASH:
                    alt23 = 1
                elif LA23 == DOT:
                    alt23 = 2
                elif LA23 == LBRACKET:
                    alt23 = 3
                elif LA23 == COLON:
                    alt23 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # lesscss.g:188:7: HASH
                    pass 
                    root_0 = self._adaptor.nil()

                    HASH70=self.match(self.input, HASH, self.FOLLOW_HASH_in_elementSubsequent1087)
                    if self._state.backtracking == 0:

                        HASH70_tree = self._adaptor.createWithPayload(HASH70)
                        self._adaptor.addChild(root_0, HASH70_tree)



                elif alt23 == 2:
                    # lesscss.g:189:7: cssClass
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_cssClass_in_elementSubsequent1095)
                    cssClass71 = self.cssClass()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cssClass71.tree)


                elif alt23 == 3:
                    # lesscss.g:190:7: attrib
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_attrib_in_elementSubsequent1103)
                    attrib72 = self.attrib()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, attrib72.tree)


                elif alt23 == 4:
                    # lesscss.g:191:7: pseudo
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pseudo_in_elementSubsequent1111)
                    pseudo73 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudo73.tree)


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
    # lesscss.g:194:1: cssClass : DOT a= IDENT -> IDENT ;
    def cssClass(self, ):

        retval = self.cssClass_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        DOT74 = None

        a_tree = None
        DOT74_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")

        try:
            try:
                # lesscss.g:195:5: ( DOT a= IDENT -> IDENT )
                # lesscss.g:195:7: DOT a= IDENT
                pass 
                DOT74=self.match(self.input, DOT, self.FOLLOW_DOT_in_cssClass1128) 
                if self._state.backtracking == 0:
                    stream_DOT.add(DOT74)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_cssClass1132) 
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
                    # 197:9: -> IDENT
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
    # lesscss.g:200:1: pseudo : ( COLON a= IDENT -> IDENT | COLON FUNCTION expr RPAREN -> ^( N_Function FUNCTION expr ) );
    def pseudo(self, ):

        retval = self.pseudo_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        COLON75 = None
        COLON76 = None
        FUNCTION77 = None
        RPAREN79 = None
        expr78 = None


        a_tree = None
        COLON75_tree = None
        COLON76_tree = None
        FUNCTION77_tree = None
        RPAREN79_tree = None
        stream_FUNCTION = RewriteRuleTokenStream(self._adaptor, "token FUNCTION")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:201:5: ( COLON a= IDENT -> IDENT | COLON FUNCTION expr RPAREN -> ^( N_Function FUNCTION expr ) )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == COLON) :
                    LA24_1 = self.input.LA(2)

                    if (LA24_1 == IDENT) :
                        alt24 = 1
                    elif (LA24_1 == FUNCTION) :
                        alt24 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 24, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # lesscss.g:201:7: COLON a= IDENT
                    pass 
                    COLON75=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1172) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON75)
                    a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo1176) 
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
                        # 203:9: -> IDENT
                        self._adaptor.addChild(root_0, stream_IDENT.nextNode())



                        retval.tree = root_0


                elif alt24 == 2:
                    # lesscss.g:204:7: COLON FUNCTION expr RPAREN
                    pass 
                    COLON76=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1207) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON76)
                    FUNCTION77=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudo1209) 
                    if self._state.backtracking == 0:
                        stream_FUNCTION.add(FUNCTION77)
                    self._state.following.append(self.FOLLOW_expr_in_pseudo1211)
                    expr78 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr78.tree)
                    RPAREN79=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudo1213) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN79)

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
                        # 205:9: -> ^( N_Function FUNCTION expr )
                        # lesscss.g:205:12: ^( N_Function FUNCTION expr )
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
    # lesscss.g:208:1: attrib : LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) ;
    def attrib(self, ):

        retval = self.attrib_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LBRACKET80 = None
        RBRACKET82 = None
        attribBody81 = None


        LBRACKET80_tree = None
        RBRACKET82_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_attribBody = RewriteRuleSubtreeStream(self._adaptor, "rule attribBody")
        try:
            try:
                # lesscss.g:209:5: ( LBRACKET attribBody RBRACKET -> ^( N_Attrib attribBody ) )
                # lesscss.g:209:7: LBRACKET attribBody RBRACKET
                pass 
                LBRACKET80=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_attrib1248) 
                if self._state.backtracking == 0:
                    stream_LBRACKET.add(LBRACKET80)
                self._state.following.append(self.FOLLOW_attribBody_in_attrib1250)
                attribBody81 = self.attribBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_attribBody.add(attribBody81.tree)
                RBRACKET82=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_attrib1252) 
                if self._state.backtracking == 0:
                    stream_RBRACKET.add(RBRACKET82)

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
                    # 210:9: -> ^( N_Attrib attribBody )
                    # lesscss.g:210:13: ^( N_Attrib attribBody )
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
    # lesscss.g:213:1: attribBody : ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) );
    def attribBody(self, ):

        retval = self.attribBody_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT83 = None
        IDENT84 = None
        set85 = None
        set86 = None

        IDENT83_tree = None
        IDENT84_tree = None
        set85_tree = None
        set86_tree = None

        try:
            try:
                # lesscss.g:214:5: ( IDENT | IDENT ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == IDENT) :
                    LA25_1 = self.input.LA(2)

                    if ((OPEQ <= LA25_1 <= DASHMATCH)) :
                        alt25 = 2
                    elif (LA25_1 == RBRACKET) :
                        alt25 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 25, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # lesscss.g:214:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT83=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1287)
                    if self._state.backtracking == 0:

                        IDENT83_tree = self._adaptor.createWithPayload(IDENT83)
                        self._adaptor.addChild(root_0, IDENT83_tree)



                elif alt25 == 2:
                    # lesscss.g:215:7: IDENT ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING )
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT84=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attribBody1295)
                    if self._state.backtracking == 0:

                        IDENT84_tree = self._adaptor.createWithPayload(IDENT84)
                        self._adaptor.addChild(root_0, IDENT84_tree)

                    set85 = self.input.LT(1)
                    set85 = self.input.LT(1)
                    if (OPEQ <= self.input.LA(1) <= DASHMATCH):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set85), root_0)
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    set86 = self.input.LT(1)
                    if self.input.LA(1) == STRING or self.input.LA(1) == IDENT:
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set86))
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
    # lesscss.g:218:1: declarationset : declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ ;
    def declarationset(self, ):

        retval = self.declarationset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI88 = None
        SEMI90 = None
        declaration87 = None

        declaration89 = None


        SEMI88_tree = None
        SEMI90_tree = None
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_declaration = RewriteRuleSubtreeStream(self._adaptor, "rule declaration")
        try:
            try:
                # lesscss.g:219:5: ( declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ )
                # lesscss.g:219:7: declaration ( SEMI declaration )* ( SEMI )?
                pass 
                self._state.following.append(self.FOLLOW_declaration_in_declarationset1335)
                declaration87 = self.declaration()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declaration.add(declaration87.tree)
                # lesscss.g:219:19: ( SEMI declaration )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == SEMI) :
                        LA26_1 = self.input.LA(2)

                        if (LA26_1 == IDENT or LA26_1 == STAR) :
                            alt26 = 1




                    if alt26 == 1:
                        # lesscss.g:219:20: SEMI declaration
                        pass 
                        SEMI88=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1338) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI88)
                        self._state.following.append(self.FOLLOW_declaration_in_declarationset1340)
                        declaration89 = self.declaration()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_declaration.add(declaration89.tree)


                    else:
                        break #loop26
                # lesscss.g:219:39: ( SEMI )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == SEMI) :
                    alt27 = 1
                if alt27 == 1:
                    # lesscss.g:219:39: SEMI
                    pass 
                    SEMI90=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1344) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI90)




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
                    # 219:45: -> ( declaration )+
                    # lesscss.g:219:48: ( declaration )+
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
    # lesscss.g:222:1: declaration : property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) ;
    def declaration(self, ):

        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON92 = None
        property91 = None

        expr93 = None

        prio94 = None


        COLON92_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_property = RewriteRuleSubtreeStream(self._adaptor, "rule property")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_prio = RewriteRuleSubtreeStream(self._adaptor, "rule prio")
        try:
            try:
                # lesscss.g:223:5: ( property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) )
                # lesscss.g:223:7: property COLON expr ( prio )?
                pass 
                self._state.following.append(self.FOLLOW_property_in_declaration1367)
                property91 = self.property()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_property.add(property91.tree)
                COLON92=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1369) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON92)
                self._state.following.append(self.FOLLOW_expr_in_declaration1371)
                expr93 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr93.tree)
                # lesscss.g:223:27: ( prio )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == IMPORTANT_SYM) :
                    alt28 = 1
                if alt28 == 1:
                    # lesscss.g:223:27: prio
                    pass 
                    self._state.following.append(self.FOLLOW_prio_in_declaration1373)
                    prio94 = self.prio()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_prio.add(prio94.tree)




                # AST Rewrite
                # elements: expr, property, prio
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
                    # 223:33: -> ^( N_Declaration property expr ( prio )? )
                    # lesscss.g:223:36: ^( N_Declaration property expr ( prio )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Declaration, "N_Declaration"), root_1)

                    self._adaptor.addChild(root_1, stream_property.nextTree())
                    self._adaptor.addChild(root_1, stream_expr.nextTree())
                    # lesscss.g:223:66: ( prio )?
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
    # lesscss.g:226:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        retval = self.prio_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORTANT_SYM95 = None

        IMPORTANT_SYM95_tree = None

        try:
            try:
                # lesscss.g:227:5: ( IMPORTANT_SYM )
                # lesscss.g:227:7: IMPORTANT_SYM
                pass 
                root_0 = self._adaptor.nil()

                IMPORTANT_SYM95=self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1404)
                if self._state.backtracking == 0:

                    IMPORTANT_SYM95_tree = self._adaptor.createWithPayload(IMPORTANT_SYM95)
                    self._adaptor.addChild(root_0, IMPORTANT_SYM95_tree)




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
    # lesscss.g:230:1: expr : term ( operator term )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        term96 = None

        operator97 = None

        term98 = None



        try:
            try:
                # lesscss.g:231:5: ( term ( operator term )* )
                # lesscss.g:231:7: term ( operator term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_expr1421)
                term96 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term96.tree)
                # lesscss.g:231:12: ( operator term )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == COMMA) :
                        LA29_2 = self.input.LA(2)

                        if (LA29_2 == STRING or LA29_2 == URI or LA29_2 == PLUS or LA29_2 == HASH or LA29_2 == FUNCTION or (NUMBER <= LA29_2 <= MINUS)) :
                            alt29 = 1
                        elif (LA29_2 == IDENT) :
                            LA29_4 = self.input.LA(3)

                            if ((STRING <= LA29_4 <= SEMI) or LA29_4 == URI or (RBRACE <= LA29_4 <= IDENT) or (COLON <= LA29_4 <= RPAREN) or LA29_4 == PLUS or (HASH <= LA29_4 <= DOT) or LA29_4 == FUNCTION or (IMPORTANT_SYM <= LA29_4 <= MINUS)) :
                                alt29 = 1




                    elif (LA29_0 == STRING or LA29_0 == URI or LA29_0 == IDENT or LA29_0 == PLUS or LA29_0 == HASH or LA29_0 == FUNCTION or (SOLIDUS <= LA29_0 <= MINUS)) :
                        alt29 = 1


                    if alt29 == 1:
                        # lesscss.g:231:13: operator term
                        pass 
                        self._state.following.append(self.FOLLOW_operator_in_expr1424)
                        operator97 = self.operator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(operator97.tree, root_0)
                        self._state.following.append(self.FOLLOW_term_in_expr1427)
                        term98 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term98.tree)


                    else:
                        break #loop29



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
    # lesscss.g:234:10: fragment operator : ( SOLIDUS | COMMA | -> N_Space );
    def operator(self, ):

        retval = self.operator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SOLIDUS99 = None
        COMMA100 = None

        SOLIDUS99_tree = None
        COMMA100_tree = None

        try:
            try:
                # lesscss.g:235:5: ( SOLIDUS | COMMA | -> N_Space )
                alt30 = 3
                LA30 = self.input.LA(1)
                if LA30 == SOLIDUS:
                    alt30 = 1
                elif LA30 == COMMA:
                    alt30 = 2
                elif LA30 == STRING or LA30 == URI or LA30 == IDENT or LA30 == PLUS or LA30 == HASH or LA30 == FUNCTION or LA30 == NUMBER or LA30 == PERCENTAGE or LA30 == LENGTH or LA30 == EMS or LA30 == EXS or LA30 == ANGLE or LA30 == TIME or LA30 == FREQ or LA30 == RESOLUTION or LA30 == MINUS:
                    alt30 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae

                if alt30 == 1:
                    # lesscss.g:235:7: SOLIDUS
                    pass 
                    root_0 = self._adaptor.nil()

                    SOLIDUS99=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator1448)
                    if self._state.backtracking == 0:

                        SOLIDUS99_tree = self._adaptor.createWithPayload(SOLIDUS99)
                        self._adaptor.addChild(root_0, SOLIDUS99_tree)



                elif alt30 == 2:
                    # lesscss.g:236:7: COMMA
                    pass 
                    root_0 = self._adaptor.nil()

                    COMMA100=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator1456)
                    if self._state.backtracking == 0:

                        COMMA100_tree = self._adaptor.createWithPayload(COMMA100)
                        self._adaptor.addChild(root_0, COMMA100_tree)



                elif alt30 == 3:
                    # lesscss.g:237:7: 
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
                        # 237:7: -> N_Space
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
    # lesscss.g:240:1: term : ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ | RESOLUTION ) | STRING | IDENT | URI | function | hexColor );
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set102 = None
        STRING103 = None
        IDENT104 = None
        URI105 = None
        unaryOperator101 = None

        function106 = None

        hexColor107 = None


        set102_tree = None
        STRING103_tree = None
        IDENT104_tree = None
        URI105_tree = None

        try:
            try:
                # lesscss.g:241:5: ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ | RESOLUTION ) | STRING | IDENT | URI | function | hexColor )
                alt32 = 6
                LA32 = self.input.LA(1)
                if LA32 == PLUS or LA32 == NUMBER or LA32 == PERCENTAGE or LA32 == LENGTH or LA32 == EMS or LA32 == EXS or LA32 == ANGLE or LA32 == TIME or LA32 == FREQ or LA32 == RESOLUTION or LA32 == MINUS:
                    alt32 = 1
                elif LA32 == STRING:
                    alt32 = 2
                elif LA32 == IDENT:
                    LA32 = self.input.LA(2)
                    if LA32 == STRING or LA32 == SEMI or LA32 == URI or LA32 == RBRACE or LA32 == COMMA or LA32 == IDENT or LA32 == RPAREN or LA32 == PLUS or LA32 == HASH or LA32 == FUNCTION or LA32 == IMPORTANT_SYM or LA32 == SOLIDUS or LA32 == NUMBER or LA32 == PERCENTAGE or LA32 == LENGTH or LA32 == EMS or LA32 == EXS or LA32 == ANGLE or LA32 == TIME or LA32 == FREQ or LA32 == RESOLUTION or LA32 == MINUS:
                        alt32 = 3
                    elif LA32 == COLON:
                        LA32_8 = self.input.LA(3)

                        if (LA32_8 == IDENT or LA32_8 == COLON or LA32_8 == DOT or LA32_8 == FUNCTION) :
                            alt32 = 5
                        elif (LA32_8 == RPAREN) :
                            alt32 = 3
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 32, 8, self.input)

                            raise nvae

                    elif LA32 == DOT:
                        alt32 = 5
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 32, 3, self.input)

                        raise nvae

                elif LA32 == URI:
                    alt32 = 4
                elif LA32 == FUNCTION:
                    alt32 = 5
                elif LA32 == HASH:
                    alt32 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae

                if alt32 == 1:
                    # lesscss.g:241:7: ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ | RESOLUTION )
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:241:20: ( unaryOperator )?
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == PLUS or LA31_0 == MINUS) :
                        alt31 = 1
                    if alt31 == 1:
                        # lesscss.g:241:20: unaryOperator
                        pass 
                        self._state.following.append(self.FOLLOW_unaryOperator_in_term1484)
                        unaryOperator101 = self.unaryOperator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            root_0 = self._adaptor.becomeRoot(unaryOperator101.tree, root_0)



                    set102 = self.input.LT(1)
                    if (NUMBER <= self.input.LA(1) <= RESOLUTION):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set102))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse




                elif alt32 == 2:
                    # lesscss.g:253:7: STRING
                    pass 
                    root_0 = self._adaptor.nil()

                    STRING103=self.match(self.input, STRING, self.FOLLOW_STRING_in_term1658)
                    if self._state.backtracking == 0:

                        STRING103_tree = self._adaptor.createWithPayload(STRING103)
                        self._adaptor.addChild(root_0, STRING103_tree)



                elif alt32 == 3:
                    # lesscss.g:254:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT104=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term1666)
                    if self._state.backtracking == 0:

                        IDENT104_tree = self._adaptor.createWithPayload(IDENT104)
                        self._adaptor.addChild(root_0, IDENT104_tree)



                elif alt32 == 4:
                    # lesscss.g:255:7: URI
                    pass 
                    root_0 = self._adaptor.nil()

                    URI105=self.match(self.input, URI, self.FOLLOW_URI_in_term1674)
                    if self._state.backtracking == 0:

                        URI105_tree = self._adaptor.createWithPayload(URI105)
                        self._adaptor.addChild(root_0, URI105_tree)



                elif alt32 == 5:
                    # lesscss.g:256:7: function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_in_term1682)
                    function106 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function106.tree)


                elif alt32 == 6:
                    # lesscss.g:257:7: hexColor
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_hexColor_in_term1690)
                    hexColor107 = self.hexColor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, hexColor107.tree)


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
    # lesscss.g:260:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        retval = self.unaryOperator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set108 = None

        set108_tree = None

        try:
            try:
                # lesscss.g:261:5: ( MINUS | PLUS )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set108 = self.input.LT(1)
                if self.input.LA(1) == PLUS or self.input.LA(1) == MINUS:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set108))
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
    # lesscss.g:266:1: function : ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) );
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RPAREN111 = None
        RPAREN114 = None
        fnct_name109 = None

        fnct_args110 = None

        fnct_name112 = None

        expr113 = None


        RPAREN111_tree = None
        RPAREN114_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_fnct_name = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_name")
        stream_fnct_args = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_args")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # lesscss.g:267:5: ( fnct_name fnct_args RPAREN -> ^( N_Function fnct_name fnct_args ) | fnct_name expr RPAREN -> ^( N_Function fnct_name expr ) )
                alt33 = 2
                alt33 = self.dfa33.predict(self.input)
                if alt33 == 1:
                    # lesscss.g:267:7: fnct_name fnct_args RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function1735)
                    fnct_name109 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name109.tree)
                    self._state.following.append(self.FOLLOW_fnct_args_in_function1737)
                    fnct_args110 = self.fnct_args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_args.add(fnct_args110.tree)
                    RPAREN111=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1739) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN111)

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
                        # 268:9: -> ^( N_Function fnct_name fnct_args )
                        # lesscss.g:268:12: ^( N_Function fnct_name fnct_args )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Function, "N_Function"), root_1)

                        self._adaptor.addChild(root_1, stream_fnct_name.nextTree())
                        self._adaptor.addChild(root_1, stream_fnct_args.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt33 == 2:
                    # lesscss.g:270:7: fnct_name expr RPAREN
                    pass 
                    self._state.following.append(self.FOLLOW_fnct_name_in_function1766)
                    fnct_name112 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fnct_name.add(fnct_name112.tree)
                    self._state.following.append(self.FOLLOW_expr_in_function1768)
                    expr113 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr113.tree)
                    RPAREN114=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1770) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN114)

                    # AST Rewrite
                    # elements: expr, fnct_name
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
                        # 271:9: -> ^( N_Function fnct_name expr )
                        # lesscss.g:271:12: ^( N_Function fnct_name expr )
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
    # lesscss.g:275:1: fnct_name : ( IDENT ( COLON | DOT )+ )* FUNCTION ;
    def fnct_name(self, ):

        retval = self.fnct_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT115 = None
        set116 = None
        FUNCTION117 = None

        IDENT115_tree = None
        set116_tree = None
        FUNCTION117_tree = None

        try:
            try:
                # lesscss.g:276:5: ( ( IDENT ( COLON | DOT )+ )* FUNCTION )
                # lesscss.g:276:7: ( IDENT ( COLON | DOT )+ )* FUNCTION
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:276:7: ( IDENT ( COLON | DOT )+ )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == IDENT) :
                        alt35 = 1


                    if alt35 == 1:
                        # lesscss.g:276:8: IDENT ( COLON | DOT )+
                        pass 
                        IDENT115=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name1807)
                        if self._state.backtracking == 0:

                            IDENT115_tree = self._adaptor.createWithPayload(IDENT115)
                            self._adaptor.addChild(root_0, IDENT115_tree)

                        # lesscss.g:276:14: ( COLON | DOT )+
                        cnt34 = 0
                        while True: #loop34
                            alt34 = 2
                            LA34_0 = self.input.LA(1)

                            if (LA34_0 == COLON or LA34_0 == DOT) :
                                alt34 = 1


                            if alt34 == 1:
                                # lesscss.g:
                                pass 
                                set116 = self.input.LT(1)
                                if self.input.LA(1) == COLON or self.input.LA(1) == DOT:
                                    self.input.consume()
                                    if self._state.backtracking == 0:
                                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set116))
                                    self._state.errorRecovery = False

                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed

                                    mse = MismatchedSetException(None, self.input)
                                    raise mse




                            else:
                                if cnt34 >= 1:
                                    break #loop34

                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                eee = EarlyExitException(34, self.input)
                                raise eee

                            cnt34 += 1


                    else:
                        break #loop35
                FUNCTION117=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name1819)
                if self._state.backtracking == 0:

                    FUNCTION117_tree = self._adaptor.createWithPayload(FUNCTION117)
                    self._adaptor.addChild(root_0, FUNCTION117_tree)




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
    # lesscss.g:279:10: fragment fnct_args : fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ ;
    def fnct_args(self, ):

        retval = self.fnct_args_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA119 = None
        fnct_arg118 = None

        fnct_arg120 = None


        COMMA119_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_fnct_arg = RewriteRuleSubtreeStream(self._adaptor, "rule fnct_arg")
        try:
            try:
                # lesscss.g:280:5: ( fnct_arg ( COMMA fnct_arg )* -> ( fnct_arg )+ )
                # lesscss.g:280:7: fnct_arg ( COMMA fnct_arg )*
                pass 
                self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1838)
                fnct_arg118 = self.fnct_arg()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_fnct_arg.add(fnct_arg118.tree)
                # lesscss.g:280:16: ( COMMA fnct_arg )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == COMMA) :
                        alt36 = 1


                    if alt36 == 1:
                        # lesscss.g:280:17: COMMA fnct_arg
                        pass 
                        COMMA119=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args1841) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA119)
                        self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1843)
                        fnct_arg120 = self.fnct_arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_fnct_arg.add(fnct_arg120.tree)


                    else:
                        break #loop36

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
                    # 281:9: -> ( fnct_arg )+
                    # lesscss.g:281:12: ( fnct_arg )+
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
    # lesscss.g:284:1: fnct_arg : IDENT OPEQ expr ;
    def fnct_arg(self, ):

        retval = self.fnct_arg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT121 = None
        OPEQ122 = None
        expr123 = None


        IDENT121_tree = None
        OPEQ122_tree = None

        try:
            try:
                # lesscss.g:285:5: ( IDENT OPEQ expr )
                # lesscss.g:285:7: IDENT OPEQ expr
                pass 
                root_0 = self._adaptor.nil()

                IDENT121=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_arg1875)
                if self._state.backtracking == 0:

                    IDENT121_tree = self._adaptor.createWithPayload(IDENT121)
                    self._adaptor.addChild(root_0, IDENT121_tree)

                OPEQ122=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_arg1877)
                if self._state.backtracking == 0:

                    OPEQ122_tree = self._adaptor.createWithPayload(OPEQ122)
                    root_0 = self._adaptor.becomeRoot(OPEQ122_tree, root_0)

                self._state.following.append(self.FOLLOW_expr_in_fnct_arg1880)
                expr123 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr123.tree)



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
    # lesscss.g:288:1: hexColor : HASH ;
    def hexColor(self, ):

        retval = self.hexColor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH124 = None

        HASH124_tree = None

        try:
            try:
                # lesscss.g:289:5: ( HASH )
                # lesscss.g:289:7: HASH
                pass 
                root_0 = self._adaptor.nil()

                HASH124=self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor1897)
                if self._state.backtracking == 0:

                    HASH124_tree = self._adaptor.createWithPayload(HASH124)
                    self._adaptor.addChild(root_0, HASH124_tree)




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
        # lesscss.g:174:20: ( esPred )
        # lesscss.g:174:21: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred1_lesscss996)
        self.esPred()

        self._state.following.pop()


    # $ANTLR end "synpred1_lesscss"



    # $ANTLR start "synpred2_lesscss"
    def synpred2_lesscss_fragment(self, ):
        # lesscss.g:175:8: ( esPred )
        # lesscss.g:175:9: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred2_lesscss1011)
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



    # lookup tables for DFA #20

    DFA20_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA20_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA20_min = DFA.unpack(
        u"\1\31\3\uffff\4\0\3\uffff"
        )

    DFA20_max = DFA.unpack(
        u"\1\47\3\uffff\4\0\3\uffff"
        )

    DFA20_accept = DFA.unpack(
        u"\1\uffff\1\2\10\uffff\1\1"
        )

    DFA20_special = DFA.unpack(
        u"\4\uffff\1\0\1\1\1\2\1\3\3\uffff"
        )

            
    DFA20_transition = [
        DFA.unpack(u"\1\1\1\uffff\2\1\1\uffff\1\7\3\uffff\3\1\1\4\1\5\1\6"),
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

    # class definition for DFA #20

    class DFA20(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA20_4 = input.LA(1)

                 
                index20_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index20_4)
                if s >= 0:
                    return s
            elif s == 1: 
                LA20_5 = input.LA(1)

                 
                index20_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index20_5)
                if s >= 0:
                    return s
            elif s == 2: 
                LA20_6 = input.LA(1)

                 
                index20_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index20_6)
                if s >= 0:
                    return s
            elif s == 3: 
                LA20_7 = input.LA(1)

                 
                index20_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index20_7)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 20, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #33

    DFA33_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA33_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA33_min = DFA.unpack(
        u"\1\34\1\36\1\24\1\34\1\uffff\1\24\1\uffff"
        )

    DFA33_max = DFA.unpack(
        u"\1\50\1\46\1\70\1\50\1\uffff\1\70\1\uffff"
        )

    DFA33_accept = DFA.unpack(
        u"\4\uffff\1\2\1\uffff\1\1"
        )

    DFA33_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA33_transition = [
        DFA.unpack(u"\1\1\13\uffff\1\2"),
        DFA.unpack(u"\1\3\7\uffff\1\3"),
        DFA.unpack(u"\1\4\2\uffff\1\4\4\uffff\1\5\6\uffff\1\4\1\uffff\1"
        u"\4\2\uffff\1\4\6\uffff\12\4"),
        DFA.unpack(u"\1\1\1\uffff\1\3\7\uffff\1\3\1\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\2\uffff\1\4\3\uffff\2\4\1\uffff\2\4\3\uffff\1"
        u"\4\1\uffff\2\4\1\uffff\1\4\1\uffff\1\6\3\uffff\13\4"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #33

    class DFA33(DFA):
        pass


 

    FOLLOW_charSet_in_styleSheet183 = frozenset([22, 24, 28, 30, 32, 33, 34, 37, 38, 39])
    FOLLOW_imports_in_styleSheet194 = frozenset([22, 24, 28, 30, 32, 33, 34, 37, 38, 39])
    FOLLOW_bodylist_in_styleSheet205 = frozenset([])
    FOLLOW_EOF_in_styleSheet215 = frozenset([1])
    FOLLOW_CHARSET_SYM_in_charSet268 = frozenset([20])
    FOLLOW_STRING_in_charSet270 = frozenset([21])
    FOLLOW_SEMI_in_charSet272 = frozenset([1])
    FOLLOW_IMPORT_SYM_in_imports310 = frozenset([20, 23])
    FOLLOW_importUrl_in_imports312 = frozenset([21, 28, 29])
    FOLLOW_media_query_list_in_imports314 = frozenset([21])
    FOLLOW_SEMI_in_imports317 = frozenset([1])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media382 = frozenset([25, 28, 29])
    FOLLOW_media_query_list_in_media384 = frozenset([25])
    FOLLOW_LBRACE_in_media395 = frozenset([26, 28, 30, 34, 37, 38, 39])
    FOLLOW_ruleSet_in_media409 = frozenset([26, 28, 30, 34, 37, 38, 39])
    FOLLOW_RBRACE_in_media420 = frozenset([1])
    FOLLOW_media_query_in_media_query_list460 = frozenset([1, 27])
    FOLLOW_COMMA_in_media_query_list463 = frozenset([28, 29])
    FOLLOW_media_query_in_media_query_list465 = frozenset([1, 27])
    FOLLOW_IDENT_in_media_query503 = frozenset([28])
    FOLLOW_media_type_in_media_query508 = frozenset([1, 28])
    FOLLOW_IDENT_in_media_query512 = frozenset([28, 29])
    FOLLOW_media_expr_in_media_query515 = frozenset([1, 28])
    FOLLOW_media_expr_in_media_query526 = frozenset([1, 28])
    FOLLOW_IDENT_in_media_query530 = frozenset([28, 29])
    FOLLOW_media_expr_in_media_query533 = frozenset([1, 28])
    FOLLOW_IDENT_in_media_type553 = frozenset([1])
    FOLLOW_LPAREN_in_media_expr570 = frozenset([28])
    FOLLOW_media_feature_in_media_expr572 = frozenset([30, 31])
    FOLLOW_COLON_in_media_expr576 = frozenset([20, 23, 28, 35, 37, 40, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56])
    FOLLOW_expr_in_media_expr578 = frozenset([30, 31])
    FOLLOW_COLON_in_media_expr583 = frozenset([31])
    FOLLOW_RPAREN_in_media_expr586 = frozenset([1])
    FOLLOW_IDENT_in_media_feature623 = frozenset([1])
    FOLLOW_FONTFACE_SYM_in_fontface643 = frozenset([25])
    FOLLOW_LBRACE_in_fontface645 = frozenset([28, 34])
    FOLLOW_declarationset_in_fontface647 = frozenset([26])
    FOLLOW_RBRACE_in_fontface649 = frozenset([1])
    FOLLOW_bodyset_in_bodylist686 = frozenset([1, 24, 28, 30, 32, 33, 34, 37, 38, 39])
    FOLLOW_ruleSet_in_bodyset704 = frozenset([1])
    FOLLOW_media_in_bodyset712 = frozenset([1])
    FOLLOW_page_in_bodyset720 = frozenset([1])
    FOLLOW_fontface_in_bodyset728 = frozenset([1])
    FOLLOW_PAGE_SYM_in_page748 = frozenset([25, 30])
    FOLLOW_pseudoPage_in_page750 = frozenset([25])
    FOLLOW_LBRACE_in_page753 = frozenset([28, 34])
    FOLLOW_declarationset_in_page755 = frozenset([26])
    FOLLOW_RBRACE_in_page757 = frozenset([1])
    FOLLOW_COLON_in_pseudoPage793 = frozenset([28])
    FOLLOW_IDENT_in_pseudoPage795 = frozenset([1])
    FOLLOW_IDENT_in_property820 = frozenset([1])
    FOLLOW_STAR_in_property839 = frozenset([28])
    FOLLOW_IDENT_in_property843 = frozenset([1])
    FOLLOW_selector_in_ruleSet884 = frozenset([25, 27])
    FOLLOW_COMMA_in_ruleSet887 = frozenset([28, 30, 34, 37, 38, 39])
    FOLLOW_selector_in_ruleSet889 = frozenset([25, 27])
    FOLLOW_LBRACE_in_ruleSet893 = frozenset([28, 34])
    FOLLOW_declarationset_in_ruleSet895 = frozenset([26])
    FOLLOW_RBRACE_in_ruleSet897 = frozenset([1])
    FOLLOW_simpleSelector_in_selector937 = frozenset([1, 28, 30, 34, 35, 36, 37, 38, 39])
    FOLLOW_combinator_in_selector940 = frozenset([28, 30, 34, 37, 38, 39])
    FOLLOW_simpleSelector_in_selector942 = frozenset([1, 28, 30, 34, 35, 36, 37, 38, 39])
    FOLLOW_PLUS_in_combinator961 = frozenset([1])
    FOLLOW_GREATER_in_combinator969 = frozenset([1])
    FOLLOW_elementName_in_simpleSelector992 = frozenset([1, 28, 30, 34, 37, 38, 39])
    FOLLOW_elementSubsequent_in_simpleSelector999 = frozenset([1, 28, 30, 34, 37, 38, 39])
    FOLLOW_elementSubsequent_in_simpleSelector1014 = frozenset([1, 28, 30, 34, 37, 38, 39])
    FOLLOW_set_in_esPred0 = frozenset([1])
    FOLLOW_set_in_elementName0 = frozenset([1])
    FOLLOW_HASH_in_elementSubsequent1087 = frozenset([1])
    FOLLOW_cssClass_in_elementSubsequent1095 = frozenset([1])
    FOLLOW_attrib_in_elementSubsequent1103 = frozenset([1])
    FOLLOW_pseudo_in_elementSubsequent1111 = frozenset([1])
    FOLLOW_DOT_in_cssClass1128 = frozenset([28])
    FOLLOW_IDENT_in_cssClass1132 = frozenset([1])
    FOLLOW_COLON_in_pseudo1172 = frozenset([28])
    FOLLOW_IDENT_in_pseudo1176 = frozenset([1])
    FOLLOW_COLON_in_pseudo1207 = frozenset([40])
    FOLLOW_FUNCTION_in_pseudo1209 = frozenset([20, 23, 28, 35, 37, 40, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56])
    FOLLOW_expr_in_pseudo1211 = frozenset([31])
    FOLLOW_RPAREN_in_pseudo1213 = frozenset([1])
    FOLLOW_LBRACKET_in_attrib1248 = frozenset([28])
    FOLLOW_attribBody_in_attrib1250 = frozenset([41])
    FOLLOW_RBRACKET_in_attrib1252 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1287 = frozenset([1])
    FOLLOW_IDENT_in_attribBody1295 = frozenset([42, 43, 44])
    FOLLOW_set_in_attribBody1297 = frozenset([20, 28])
    FOLLOW_set_in_attribBody1310 = frozenset([1])
    FOLLOW_declaration_in_declarationset1335 = frozenset([1, 21])
    FOLLOW_SEMI_in_declarationset1338 = frozenset([28, 34])
    FOLLOW_declaration_in_declarationset1340 = frozenset([1, 21])
    FOLLOW_SEMI_in_declarationset1344 = frozenset([1])
    FOLLOW_property_in_declaration1367 = frozenset([30])
    FOLLOW_COLON_in_declaration1369 = frozenset([20, 23, 28, 35, 37, 40, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56])
    FOLLOW_expr_in_declaration1371 = frozenset([1, 45])
    FOLLOW_prio_in_declaration1373 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1404 = frozenset([1])
    FOLLOW_term_in_expr1421 = frozenset([1, 20, 23, 27, 28, 35, 37, 40, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56])
    FOLLOW_operator_in_expr1424 = frozenset([20, 23, 28, 35, 37, 40, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56])
    FOLLOW_term_in_expr1427 = frozenset([1, 20, 23, 27, 28, 35, 37, 40, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56])
    FOLLOW_SOLIDUS_in_operator1448 = frozenset([1])
    FOLLOW_COMMA_in_operator1456 = frozenset([1])
    FOLLOW_unaryOperator_in_term1484 = frozenset([47, 48, 49, 50, 51, 52, 53, 54, 55])
    FOLLOW_set_in_term1496 = frozenset([1])
    FOLLOW_STRING_in_term1658 = frozenset([1])
    FOLLOW_IDENT_in_term1666 = frozenset([1])
    FOLLOW_URI_in_term1674 = frozenset([1])
    FOLLOW_function_in_term1682 = frozenset([1])
    FOLLOW_hexColor_in_term1690 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_fnct_name_in_function1735 = frozenset([28])
    FOLLOW_fnct_args_in_function1737 = frozenset([31])
    FOLLOW_RPAREN_in_function1739 = frozenset([1])
    FOLLOW_fnct_name_in_function1766 = frozenset([20, 23, 28, 35, 37, 40, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56])
    FOLLOW_expr_in_function1768 = frozenset([31])
    FOLLOW_RPAREN_in_function1770 = frozenset([1])
    FOLLOW_IDENT_in_fnct_name1807 = frozenset([30, 38])
    FOLLOW_set_in_fnct_name1809 = frozenset([28, 30, 38, 40])
    FOLLOW_FUNCTION_in_fnct_name1819 = frozenset([1])
    FOLLOW_fnct_arg_in_fnct_args1838 = frozenset([1, 27])
    FOLLOW_COMMA_in_fnct_args1841 = frozenset([28])
    FOLLOW_fnct_arg_in_fnct_args1843 = frozenset([1, 27])
    FOLLOW_IDENT_in_fnct_arg1875 = frozenset([42])
    FOLLOW_OPEQ_in_fnct_arg1877 = frozenset([20, 23, 28, 35, 37, 40, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56])
    FOLLOW_expr_in_fnct_arg1880 = frozenset([1])
    FOLLOW_HASH_in_hexColor1897 = frozenset([1])
    FOLLOW_esPred_in_synpred1_lesscss996 = frozenset([1])
    FOLLOW_esPred_in_synpred2_lesscss1011 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("lesscssLexer", lesscssParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
