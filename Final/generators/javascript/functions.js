'use strict';

goog.provide('Blockly.JavaScript.functions');
goog.require('Blockly.JavaScript');

Blockly.JavaScript['function_statement'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_var = block.getFieldValue('VAR');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_block = Blockly.JavaScript.statementToCode(block, 'BLOCK');
  if(value_name) {
    var code = dropdown_type + ' func ' + text_var + '' + value_name + ' {\n' + statements_block + '}';
  } else {
    var code = dropdown_type + ' func ' + text_var + '()' + ' {\n' + statements_block + '}';
  }
  return code;
};

Blockly.JavaScript['function_param'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_var = block.getFieldValue('VAR');
  var code = text_var + ' : ' + dropdown_type;
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['function_param_coma'] = function(block) {
  var dropdown_type = block.getFieldValue('TYPE');
  var text_var = block.getFieldValue('VAR');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  if(value_name.indexOf("(") > -1) {
    value_name = value_name.substring(1,value_name.length-1);
  }
  var code = text_var + ' : ' + dropdown_type + '; ' + value_name;
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['function_call'] = function(block) {
  var text_fname = block.getFieldValue('FNAME');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  if (value_name.length < 1) {
    value_name = "()";
  }

  var code = "call " + text_fname + value_name;
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['return'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  if(value_name.indexOf("(") == -1) {
    value_name = "(" + value_name + ")";
  }
  var code = 'return ' + value_name +';\n';
  return code;
};

Blockly.JavaScript['func_call'] = function(block) {
  var text_name = block.getFieldValue('NAME');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  if (value_name.length < 1) {
    value_name = "()";
  }

  var code = "call " + text_name + value_name +';\n';
  return [code, Blockly.JavaScript.ORDER_NONE];
};
