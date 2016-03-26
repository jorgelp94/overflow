'use strict';

goog.provide('Blockly.JavaScript.functions');
goog.require('Blockly.JavaScript');

Blockly.JavaScript['function_statement'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_var = block.getFieldValue('VAR');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_block = Blockly.JavaScript.statementToCode(block, 'BLOCK');
  if(value_name) {
    var code = dropdown_type + ' function ' + text_var + '' + value_name + ' {\n' + statements_block + '}';
  } else {
    var code = dropdown_type + ' function ' + text_var + '()' + ' {\n' + statements_block + '}';
  }
  return code;
};

Blockly.JavaScript['function_param'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_var = block.getFieldValue('VAR');
  var code = dropdown_type + ' ' + text_var;
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['function_param_coma'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_var = block.getFieldValue('VAR');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  value_name = value_name.substring(1, value_name.length - 1);
  var code = dropdown_type + ' ' + text_var + ', ' + value_name;
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['function_call'] = function(block) {
  var text_fname = block.getFieldValue('FNAME');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  var code = text_fname + value_name;  
  return [code, Blockly.JavaScript.ORDER_NONE];
};
