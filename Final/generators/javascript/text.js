'use strict';

goog.provide('Blockly.JavaScript.texts');
goog.require('Blockly.JavaScript');


Blockly.JavaScript['text'] = function(block) {
  var code = Blockly.JavaScript.quote_(block.getFieldValue('TEXT'));
  code = code.substring(1, code.length-1);
  code = '\"' + code + '\"';
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};

Blockly.JavaScript['text_print'] = function(block) {
  var argument0 = Blockly.JavaScript.valueToCode(block, 'TEXT',
      Blockly.JavaScript.ORDER_NONE) || '\'\'';
  return 'print(' + argument0 + ');\n';
};

Blockly.JavaScript['char_var'] = function(block) {
  var text_var = block.getFieldValue('VAR');
  var code = '\'' + text_var + '\'';
  return [code, Blockly.JavaScript.ORDER_NONE];
};
