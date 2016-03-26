'use strict';
goog.provide('Blockly.JavaScript.variables');
goog.require('Blockly.JavaScript');

Blockly.JavaScript['int_variable'] = function(block) {
  var text_var = block.getFieldValue('VAR');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  if(!value_name) {
    value_name = '0';
  }
  if(value_name.indexOf(".") > -1) {
    var pos = value_name.indexOf(".");
    value_name = value_name.substring(0, pos);
  }
  var code = 'int ' + text_var + ' = ' + value_name + ';\n';
  return code;
};

Blockly.JavaScript['float_variable'] = function(block) {
  var text_var = block.getFieldValue('VAR');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  if(!value_name) {
    value_name = '0.0';
  }
  if(value_name.indexOf(".") < 0) {
    value_name += ".0"
  }
  var code = 'float ' + text_var + ' = ' + value_name + ';\n';
  return code;
};

Blockly.JavaScript['bool_variable'] = function(block) {
  var text_var = block.getFieldValue('VAR');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  if(!value_name) {
    value_name = false;
  }
  var code = 'bool ' + text_var + ' = ' + value_name + ';\n';
  return code;
};

Blockly.JavaScript['char_variable'] = function(block) {
  var text_var = block.getFieldValue('VAR');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  if(value_name.length > 1) {
    value_name = '\'' + value_name[1] + '\'';
  } else {
    value_name = '\'' + '\'';
  }
  var code = 'char ' + text_var + ' = ' + value_name + ';\n';
  return code;
};

Blockly.JavaScript['string_variable'] = function(block) {
  var text_var = block.getFieldValue('VAR');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  value_name = value_name.substring(1, value_name.length-1);
  var code = 'string ' + text_var + ' = ' + '\"' + value_name + '\"' + ';\n';
  return code;
};

Blockly.JavaScript['variable'] = function(block) {
  var text_name = block.getFieldValue('NAME');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  if(!value_name) {
    value_name = '0';
  }
  var code = text_name + ' = ' + value_name + ';\n';
  return code;
};

Blockly.JavaScript['var'] = function(block) {
  var text_var = block.getFieldValue('VAR');
  var code = text_var;
  return [code, Blockly.JavaScript.ORDER_NONE];
};
