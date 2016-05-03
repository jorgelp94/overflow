// Do not edit this file; automatically generated by build.py.
'use strict';


// Copyright 2012 Google Inc.  Apache License 2.0
Blockly.JavaScript=new Blockly.Generator("JavaScript");Blockly.JavaScript.addReservedWords("Blockly,break,case,catch,continue,debugger,default,delete,do,else,finally,for,function,if,in,instanceof,new,return,switch,this,throw,try,typeof,var,void,while,with,class,enum,export,extends,import,super,implements,interface,let,package,private,protected,public,static,yield,const,null,true,false,Array,ArrayBuffer,Boolean,Date,decodeURI,decodeURIComponent,encodeURI,encodeURIComponent,Error,eval,EvalError,Float32Array,Float64Array,Function,Infinity,Int16Array,Int32Array,Int8Array,isFinite,isNaN,Iterator,JSON,Math,NaN,Number,Object,parseFloat,parseInt,RangeError,ReferenceError,RegExp,StopIteration,String,SyntaxError,TypeError,Uint16Array,Uint32Array,Uint8Array,Uint8ClampedArray,undefined,uneval,URIError,applicationCache,closed,Components,content,_content,controllers,crypto,defaultStatus,dialogArguments,directories,document,frameElement,frames,fullScreen,globalStorage,history,innerHeight,innerWidth,length,location,locationbar,localStorage,menubar,messageManager,mozAnimationStartTime,mozInnerScreenX,mozInnerScreenY,mozPaintCount,name,navigator,opener,outerHeight,outerWidth,pageXOffset,pageYOffset,parent,performance,personalbar,pkcs11,returnValue,screen,screenX,screenY,scrollbars,scrollMaxX,scrollMaxY,scrollX,scrollY,self,sessionStorage,sidebar,status,statusbar,toolbar,top,URL,window,addEventListener,alert,atob,back,blur,btoa,captureEvents,clearImmediate,clearInterval,clearTimeout,close,confirm,disableExternalCapture,dispatchEvent,dump,enableExternalCapture,escape,find,focus,forward,GeckoActiveXObject,getAttention,getAttentionWithCycleCount,getComputedStyle,getSelection,home,matchMedia,maximize,minimize,moveBy,moveTo,mozRequestAnimationFrame,open,openDialog,postMessage,print,prompt,QueryInterface,releaseEvents,removeEventListener,resizeBy,resizeTo,restore,routeEvent,scroll,scrollBy,scrollByLines,scrollByPages,scrollTo,setCursor,setImmediate,setInterval,setResizable,setTimeout,showModalDialog,sizeToContent,stop,unescape,updateCommands,XPCNativeWrapper,XPCSafeJSObjectWrapper,onabort,onbeforeunload,onblur,onchange,onclick,onclose,oncontextmenu,ondevicemotion,ondeviceorientation,ondragdrop,onerror,onfocus,onhashchange,onkeydown,onkeypress,onkeyup,onload,onmousedown,onmousemove,onmouseout,onmouseover,onmouseup,onmozbeforepaint,onpaint,onpopstate,onreset,onresize,onscroll,onselect,onsubmit,onunload,onpageshow,onpagehide,Image,Option,Worker,Event,Range,File,FileReader,Blob,BlobBuilder,Attr,CDATASection,CharacterData,Comment,console,DocumentFragment,DocumentType,DomConfiguration,DOMError,DOMErrorHandler,DOMException,DOMImplementation,DOMImplementationList,DOMImplementationRegistry,DOMImplementationSource,DOMLocator,DOMObject,DOMString,DOMStringList,DOMTimeStamp,DOMUserData,Entity,EntityReference,MediaQueryList,MediaQueryListListener,NameList,NamedNodeMap,Node,NodeFilter,NodeIterator,NodeList,Notation,Plugin,PluginArray,ProcessingInstruction,SharedWorker,Text,TimeRanges,Treewalker,TypeInfo,UserDataHandler,Worker,WorkerGlobalScope,HTMLDocument,HTMLElement,HTMLAnchorElement,HTMLAppletElement,HTMLAudioElement,HTMLAreaElement,HTMLBaseElement,HTMLBaseFontElement,HTMLBodyElement,HTMLBRElement,HTMLButtonElement,HTMLCanvasElement,HTMLDirectoryElement,HTMLDivElement,HTMLDListElement,HTMLEmbedElement,HTMLFieldSetElement,HTMLFontElement,HTMLFormElement,HTMLFrameElement,HTMLFrameSetElement,HTMLHeadElement,HTMLHeadingElement,HTMLHtmlElement,HTMLHRElement,HTMLIFrameElement,HTMLImageElement,HTMLInputElement,HTMLKeygenElement,HTMLLabelElement,HTMLLIElement,HTMLLinkElement,HTMLMapElement,HTMLMenuElement,HTMLMetaElement,HTMLModElement,HTMLObjectElement,HTMLOListElement,HTMLOptGroupElement,HTMLOptionElement,HTMLOutputElement,HTMLParagraphElement,HTMLParamElement,HTMLPreElement,HTMLQuoteElement,HTMLScriptElement,HTMLSelectElement,HTMLSourceElement,HTMLSpanElement,HTMLStyleElement,HTMLTableElement,HTMLTableCaptionElement,HTMLTableCellElement,HTMLTableDataCellElement,HTMLTableHeaderCellElement,HTMLTableColElement,HTMLTableRowElement,HTMLTableSectionElement,HTMLTextAreaElement,HTMLTimeElement,HTMLTitleElement,HTMLTrackElement,HTMLUListElement,HTMLUnknownElement,HTMLVideoElement,HTMLCanvasElement,CanvasRenderingContext2D,CanvasGradient,CanvasPattern,TextMetrics,ImageData,CanvasPixelArray,HTMLAudioElement,HTMLVideoElement,NotifyAudioAvailableEvent,HTMLCollection,HTMLAllCollection,HTMLFormControlsCollection,HTMLOptionsCollection,HTMLPropertiesCollection,DOMTokenList,DOMSettableTokenList,DOMStringMap,RadioNodeList,SVGDocument,SVGElement,SVGAElement,SVGAltGlyphElement,SVGAltGlyphDefElement,SVGAltGlyphItemElement,SVGAnimationElement,SVGAnimateElement,SVGAnimateColorElement,SVGAnimateMotionElement,SVGAnimateTransformElement,SVGSetElement,SVGCircleElement,SVGClipPathElement,SVGColorProfileElement,SVGCursorElement,SVGDefsElement,SVGDescElement,SVGEllipseElement,SVGFilterElement,SVGFilterPrimitiveStandardAttributes,SVGFEBlendElement,SVGFEColorMatrixElement,SVGFEComponentTransferElement,SVGFECompositeElement,SVGFEConvolveMatrixElement,SVGFEDiffuseLightingElement,SVGFEDisplacementMapElement,SVGFEDistantLightElement,SVGFEFloodElement,SVGFEGaussianBlurElement,SVGFEImageElement,SVGFEMergeElement,SVGFEMergeNodeElement,SVGFEMorphologyElement,SVGFEOffsetElement,SVGFEPointLightElement,SVGFESpecularLightingElement,SVGFESpotLightElement,SVGFETileElement,SVGFETurbulenceElement,SVGComponentTransferFunctionElement,SVGFEFuncRElement,SVGFEFuncGElement,SVGFEFuncBElement,SVGFEFuncAElement,SVGFontElement,SVGFontFaceElement,SVGFontFaceFormatElement,SVGFontFaceNameElement,SVGFontFaceSrcElement,SVGFontFaceUriElement,SVGForeignObjectElement,SVGGElement,SVGGlyphElement,SVGGlyphRefElement,SVGGradientElement,SVGLinearGradientElement,SVGRadialGradientElement,SVGHKernElement,SVGImageElement,SVGLineElement,SVGMarkerElement,SVGMaskElement,SVGMetadataElement,SVGMissingGlyphElement,SVGMPathElement,SVGPathElement,SVGPatternElement,SVGPolylineElement,SVGPolygonElement,SVGRectElement,SVGScriptElement,SVGStopElement,SVGStyleElement,SVGSVGElement,SVGSwitchElement,SVGSymbolElement,SVGTextElement,SVGTextPathElement,SVGTitleElement,SVGTRefElement,SVGTSpanElement,SVGUseElement,SVGViewElement,SVGVKernElement,SVGAngle,SVGColor,SVGICCColor,SVGElementInstance,SVGElementInstanceList,SVGLength,SVGLengthList,SVGMatrix,SVGNumber,SVGNumberList,SVGPaint,SVGPoint,SVGPointList,SVGPreserveAspectRatio,SVGRect,SVGStringList,SVGTransform,SVGTransformList,SVGAnimatedAngle,SVGAnimatedBoolean,SVGAnimatedEnumeration,SVGAnimatedInteger,SVGAnimatedLength,SVGAnimatedLengthList,SVGAnimatedNumber,SVGAnimatedNumberList,SVGAnimatedPreserveAspectRatio,SVGAnimatedRect,SVGAnimatedString,SVGAnimatedTransformList,SVGPathSegList,SVGPathSeg,SVGPathSegArcAbs,SVGPathSegArcRel,SVGPathSegClosePath,SVGPathSegCurvetoCubicAbs,SVGPathSegCurvetoCubicRel,SVGPathSegCurvetoCubicSmoothAbs,SVGPathSegCurvetoCubicSmoothRel,SVGPathSegCurvetoQuadraticAbs,SVGPathSegCurvetoQuadraticRel,SVGPathSegCurvetoQuadraticSmoothAbs,SVGPathSegCurvetoQuadraticSmoothRel,SVGPathSegLinetoAbs,SVGPathSegLinetoHorizontalAbs,SVGPathSegLinetoHorizontalRel,SVGPathSegLinetoRel,SVGPathSegLinetoVerticalAbs,SVGPathSegLinetoVerticalRel,SVGPathSegMovetoAbs,SVGPathSegMovetoRel,ElementTimeControl,TimeEvent,SVGAnimatedPathData,SVGAnimatedPoints,SVGColorProfileRule,SVGCSSRule,SVGExternalResourcesRequired,SVGFitToViewBox,SVGLangSpace,SVGLocatable,SVGRenderingIntent,SVGStylable,SVGTests,SVGTextContentElement,SVGTextPositioningElement,SVGTransformable,SVGUnitTypes,SVGURIReference,SVGViewSpec,SVGZoomAndPan");
Blockly.JavaScript.ORDER_ATOMIC=0;Blockly.JavaScript.ORDER_MEMBER=1;Blockly.JavaScript.ORDER_NEW=1;Blockly.JavaScript.ORDER_FUNCTION_CALL=2;Blockly.JavaScript.ORDER_INCREMENT=3;Blockly.JavaScript.ORDER_DECREMENT=3;Blockly.JavaScript.ORDER_LOGICAL_NOT=4;Blockly.JavaScript.ORDER_BITWISE_NOT=4;Blockly.JavaScript.ORDER_UNARY_PLUS=4;Blockly.JavaScript.ORDER_UNARY_NEGATION=4;Blockly.JavaScript.ORDER_TYPEOF=4;Blockly.JavaScript.ORDER_VOID=4;Blockly.JavaScript.ORDER_DELETE=4;
Blockly.JavaScript.ORDER_MULTIPLICATION=5;Blockly.JavaScript.ORDER_DIVISION=5;Blockly.JavaScript.ORDER_MODULUS=5;Blockly.JavaScript.ORDER_ADDITION=6;Blockly.JavaScript.ORDER_SUBTRACTION=6;Blockly.JavaScript.ORDER_BITWISE_SHIFT=7;Blockly.JavaScript.ORDER_RELATIONAL=8;Blockly.JavaScript.ORDER_IN=8;Blockly.JavaScript.ORDER_INSTANCEOF=8;Blockly.JavaScript.ORDER_EQUALITY=9;Blockly.JavaScript.ORDER_BITWISE_AND=10;Blockly.JavaScript.ORDER_BITWISE_XOR=11;Blockly.JavaScript.ORDER_BITWISE_OR=12;
Blockly.JavaScript.ORDER_LOGICAL_AND=13;Blockly.JavaScript.ORDER_LOGICAL_OR=14;Blockly.JavaScript.ORDER_CONDITIONAL=15;Blockly.JavaScript.ORDER_ASSIGNMENT=16;Blockly.JavaScript.ORDER_COMMA=17;Blockly.JavaScript.ORDER_NONE=99;
Blockly.JavaScript.init=function(a){Blockly.JavaScript.definitions_=Object.create(null);Blockly.JavaScript.functionNames_=Object.create(null);Blockly.JavaScript.variableDB_?Blockly.JavaScript.variableDB_.reset():Blockly.JavaScript.variableDB_=new Blockly.Names(Blockly.JavaScript.RESERVED_WORDS_);var b=[];a=Blockly.Variables.allVariables(a);for(var c=0;c<a.length;c++)b[c]="var "+Blockly.JavaScript.variableDB_.getName(a[c],Blockly.Variables.NAME_TYPE)+";";Blockly.JavaScript.definitions_.variables=b.join("\n")};
Blockly.JavaScript.finish=function(a){var b=[],c;for(c in Blockly.JavaScript.definitions_)b.push(Blockly.JavaScript.definitions_[c]);delete Blockly.JavaScript.definitions_;delete Blockly.JavaScript.functionNames_;Blockly.JavaScript.variableDB_.reset();return b.join("\n\n")+"\n\n\n"+a};Blockly.JavaScript.scrubNakedValue=function(a){return a+";\n"};Blockly.JavaScript.quote_=function(a){a=a.replace(/\\/g,"\\\\").replace(/\n/g,"\\\n").replace(/'/g,"\\'");return"'"+a+"'"};
Blockly.JavaScript.scrub_=function(a,b){var c="";if(!a.outputConnection||!a.outputConnection.targetConnection){var d=a.getCommentText();d&&(c+=Blockly.JavaScript.prefixLines(d,"// ")+"\n");for(var e=0;e<a.inputList.length;e++)a.inputList[e].type==Blockly.INPUT_VALUE&&(d=a.inputList[e].connection.targetBlock())&&(d=Blockly.JavaScript.allNestedComments(d))&&(c+=Blockly.JavaScript.prefixLines(d,"// "))}e=a.nextConnection&&a.nextConnection.targetBlock();e=Blockly.JavaScript.blockToCode(e);return c+b+
e};Blockly.JavaScript.functions={};Blockly.JavaScript.function_statement=function(a){var b=a.getFieldValue("TYPE"),c=a.getFieldValue("VAR"),d=Blockly.JavaScript.valueToCode(a,"NAME",Blockly.JavaScript.ORDER_ATOMIC);a=Blockly.JavaScript.statementToCode(a,"BLOCK");return d?b+" func "+c+""+d+" {\n"+a+"}":b+" func "+c+"() {\n"+a+"}"};Blockly.JavaScript.function_param=function(a){var b=a.getFieldValue("TYPE");return[a.getFieldValue("VAR")+" : "+b,Blockly.JavaScript.ORDER_NONE]};
Blockly.JavaScript.function_param_coma=function(a){var b=a.getFieldValue("TYPE"),c=a.getFieldValue("VAR");a=Blockly.JavaScript.valueToCode(a,"NAME",Blockly.JavaScript.ORDER_ATOMIC);-1<a.indexOf("(")&&(a=a.substring(1,a.length-1));return[c+" : "+b+"; "+a,Blockly.JavaScript.ORDER_NONE]};Blockly.JavaScript.function_call=function(a){var b=a.getFieldValue("FNAME");a=Blockly.JavaScript.valueToCode(a,"NAME",Blockly.JavaScript.ORDER_ATOMIC);1>a.length&&(a="()");return["call "+b+a,Blockly.JavaScript.ORDER_NONE]};
Blockly.JavaScript["return"]=function(a){a=Blockly.JavaScript.valueToCode(a,"NAME",Blockly.JavaScript.ORDER_ATOMIC);-1==a.indexOf("(")&&(a="("+a+")");return"return "+a+";\n"};Blockly.JavaScript.lists={};Blockly.JavaScript.lists_create_empty=function(a){return["[]",Blockly.JavaScript.ORDER_ATOMIC]};Blockly.JavaScript.lists_create_with=function(a){for(var b=Array(a.itemCount_),c=0;c<a.itemCount_;c++)b[c]=Blockly.JavaScript.valueToCode(a,"ADD"+c,Blockly.JavaScript.ORDER_COMMA)||"0";b="["+b.join(", ")+"]";return[b,Blockly.JavaScript.ORDER_ATOMIC]};Blockly.JavaScript.logic={};
Blockly.JavaScript.controls_if=function(a){for(var b=0,c=Blockly.JavaScript.valueToCode(a,"IF"+b,Blockly.JavaScript.ORDER_NONE)||"false",d=Blockly.JavaScript.statementToCode(a,"DO"+b),e="if ("+c+") {\n"+d+"}",b=1;b<=a.elseifCount_;b++)c=Blockly.JavaScript.valueToCode(a,"IF"+b,Blockly.JavaScript.ORDER_NONE)||"false",d=Blockly.JavaScript.statementToCode(a,"DO"+b),e+=" else if ("+c+") {\n"+d+"}";a.elseCount_&&(d=Blockly.JavaScript.statementToCode(a,"ELSE"),e+=" else {\n"+d+"}");return e+"\n"};
Blockly.JavaScript.logic_compare=function(a){var b={EQ:"==",NEQ:"!=",LT:"<",LTE:"<=",GT:">",GTE:">="}[a.getFieldValue("OP")],c="=="==b||"!="==b?Blockly.JavaScript.ORDER_EQUALITY:Blockly.JavaScript.ORDER_RELATIONAL,d=Blockly.JavaScript.valueToCode(a,"A",c)||"0";a=Blockly.JavaScript.valueToCode(a,"B",c)||"0";return[d+" "+b+" "+a,c]};
Blockly.JavaScript.logic_operation=function(a){var b="AND"==a.getFieldValue("OP")?"&&":"||",c="&&"==b?Blockly.JavaScript.ORDER_LOGICAL_AND:Blockly.JavaScript.ORDER_LOGICAL_OR,d=Blockly.JavaScript.valueToCode(a,"A",c);a=Blockly.JavaScript.valueToCode(a,"B",c);if(d||a){var e="&&"==b?"true":"false";d||(d=e);a||(a=e)}else a=d="false";return[d+" "+b+" "+a,c]};Blockly.JavaScript.logic_boolean=function(a){return["TRUE"==a.getFieldValue("BOOL")?"true":"false",Blockly.JavaScript.ORDER_ATOMIC]};Blockly.JavaScript.loops={};Blockly.JavaScript.controls_whileUntil=function(a){var b="UNTIL"==a.getFieldValue("MODE"),c=Blockly.JavaScript.valueToCode(a,"BOOL",b?Blockly.JavaScript.ORDER_LOGICAL_NOT:Blockly.JavaScript.ORDER_NONE)||"false",d=Blockly.JavaScript.statementToCode(a,"DO"),d=Blockly.JavaScript.addLoopTrap(d,a.id);b&&(c="!"+c);return"while ("+c+") {\n"+d+"}\n"};Blockly.JavaScript.math={};Blockly.JavaScript.math_number=function(a){return[parseFloat(a.getFieldValue("NUM")),Blockly.JavaScript.ORDER_ATOMIC]};
Blockly.JavaScript.math_arithmetic=function(a){var b={ADD:[" + ",Blockly.JavaScript.ORDER_ADDITION],MINUS:[" - ",Blockly.JavaScript.ORDER_SUBTRACTION],MULTIPLY:[" * ",Blockly.JavaScript.ORDER_MULTIPLICATION],DIVIDE:[" / ",Blockly.JavaScript.ORDER_DIVISION]}[a.getFieldValue("OP")],c=b[0],b=b[1],d=Blockly.JavaScript.valueToCode(a,"A",b)||"0";a=Blockly.JavaScript.valueToCode(a,"B",b)||"0";return c?[d+c+a,b]:["Math.pow("+d+", "+a+")",Blockly.JavaScript.ORDER_FUNCTION_CALL]};Blockly.JavaScript.program={};Blockly.JavaScript.program=function(a){return"program "+a.getFieldValue("ID")+";\n"};Blockly.JavaScript.main=function(a){return"main() {\n"+Blockly.JavaScript.statementToCode(a,"NAME")+"}\nend\n"};Blockly.JavaScript.texts={};Blockly.JavaScript.text=function(a){a=Blockly.JavaScript.quote_(a.getFieldValue("TEXT"));a=a.substring(1,a.length-1);return['"'+a+'"',Blockly.JavaScript.ORDER_ATOMIC]};Blockly.JavaScript.text_print=function(a){return"print("+(Blockly.JavaScript.valueToCode(a,"TEXT",Blockly.JavaScript.ORDER_NONE)||"''")+");\n"};Blockly.JavaScript.char_var=function(a){return["'"+a.getFieldValue("VAR")+"'",Blockly.JavaScript.ORDER_NONE]};Blockly.JavaScript.variables={};Blockly.JavaScript.int_variable=function(a){a=Blockly.JavaScript.valueToCode(a,"NAME",Blockly.JavaScript.ORDER_ATOMIC);-1<a.indexOf("(")&&(a=a.substring(1,a.length-1));return"var "+a+" : int;\n"};Blockly.JavaScript.float_variable=function(a){a=Blockly.JavaScript.valueToCode(a,"NAME",Blockly.JavaScript.ORDER_ATOMIC);-1<a.indexOf("(")&&(a=a.substring(1,a.length-1));return"var "+a+" : float;\n"};
Blockly.JavaScript.bool_variable=function(a){a=Blockly.JavaScript.valueToCode(a,"NAME",Blockly.JavaScript.ORDER_ATOMIC);-1<a.indexOf("(")&&(a=a.substring(1,a.length-1));return"var "+a+" : bool;\n"};Blockly.JavaScript.char_variable=function(a){a=Blockly.JavaScript.valueToCode(a,"NAME",Blockly.JavaScript.ORDER_ATOMIC);-1<a.indexOf("(")&&(a=a.substring(1,a.length-1));return"var "+a+" : char;\n"};
Blockly.JavaScript.int_arr_variable=function(a){a=Blockly.JavaScript.valueToCode(a,"NAME",Blockly.JavaScript.ORDER_ATOMIC);-1<a.indexOf("(")&&(a=a.substring(1,a.length-1));return"arr "+a+" : int;\n"};Blockly.JavaScript.float_arr_variable=function(a){a=Blockly.JavaScript.valueToCode(a,"NAME",Blockly.JavaScript.ORDER_ATOMIC);-1<a.indexOf("(")&&(a=a.substring(1,a.length-1));return"arr "+a+" : float;\n"};
Blockly.JavaScript.char_arr_variable=function(a){a=Blockly.JavaScript.valueToCode(a,"NAME",Blockly.JavaScript.ORDER_ATOMIC);-1<a.indexOf("(")&&(a=a.substring(1,a.length-1));return"arr "+a+" : char;\n"};Blockly.JavaScript.bool_arr_variable=function(a){a=Blockly.JavaScript.valueToCode(a,"NAME",Blockly.JavaScript.ORDER_ATOMIC);-1<a.indexOf("(")&&(a=a.substring(1,a.length-1));return"arr "+a+" : bool;\n"};
Blockly.JavaScript.assignment=function(a){var b=a.getFieldValue("NAME");(a=Blockly.JavaScript.valueToCode(a,"NAME",Blockly.JavaScript.ORDER_ATOMIC))||(a="0");-1<a.indexOf("(")&&(a=a.substring(1,a.length-1));return b+" = "+a+";\n"};Blockly.JavaScript.assignment_arr=function(a){var b=a.getFieldValue("NAME"),c=a.getFieldValue("EXP");a=Blockly.JavaScript.valueToCode(a,"NAME",Blockly.JavaScript.ORDER_ATOMIC);return b+" [ "+c+" ] = "+a+";\n"};
Blockly.JavaScript["var"]=function(a){return[a.getFieldValue("VAR"),Blockly.JavaScript.ORDER_NONE]};Blockly.JavaScript.var_coma=function(a){var b=a.getFieldValue("VAR");a=Blockly.JavaScript.valueToCode(a,"NAME",Blockly.JavaScript.ORDER_ATOMIC);a=a.substring(1,a.length-1);return[b+", "+a,Blockly.JavaScript.ORDER_NONE]};