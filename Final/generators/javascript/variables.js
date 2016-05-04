'use strict';
goog.provide('Blockly.JavaScript.variables');
goog.require('Blockly.JavaScript');

Blockly.JavaScript['int_variable'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  if(value_name.indexOf("(") > -1) {
    value_name = value_name.substring(1,value_name.length-1);
  }
  var code = 'var ' + value_name + ' : int;\n';
  return code;
};

Blockly.JavaScript['float_variable'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  if(value_name.indexOf("(") > -1) {
    value_name = value_name.substring(1,value_name.length-1);
  }
  var code = 'var ' + value_name + ' : float;\n';
  return code;
};

Blockly.JavaScript['bool_variable'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  if(value_name.indexOf("(") > -1) {
    value_name = value_name.substring(1,value_name.length-1);
  }
  var code = 'var ' + value_name + ' : bool;\n';
  return code;
};

Blockly.JavaScript['char_variable'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  if(value_name.indexOf("(") > -1) {
    value_name = value_name.substring(1,value_name.length-1);
  }
  var code = 'var ' + value_name + ' : char;\n';
  return code;
};

Blockly.JavaScript['int_arr_variable'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  var text_exp = block.getFieldValue('EXP');
  if(value_name.indexOf("(") > -1) {
    value_name = value_name.substring(1,value_name.length-1);
  }
  var code = 'arr '+ value_name + '[' + text_exp + '] : int;\n';
  return code;
};

Blockly.JavaScript['float_arr_variable'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  var text_exp = block.getFieldValue('EXP');
  if(value_name.indexOf("(") > -1) {
    value_name = value_name.substring(1,value_name.length-1);
  }
  var code = 'arr '+ value_name + '[' + text_exp + '] : float;\n';
  return code;
};

Blockly.JavaScript['char_arr_variable'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  var text_exp = block.getFieldValue('EXP');
  if(value_name.indexOf("(") > -1) {
    value_name = value_name.substring(1,value_name.length-1);
  }
  var code = 'arr '+ value_name + '[' + text_exp + '] : char;\n';
  return code;
};

Blockly.JavaScript['bool_arr_variable'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  var text_exp = block.getFieldValue('EXP');
  if(value_name.indexOf("(") > -1) {
    value_name = value_name.substring(1,value_name.length-1);
  }
  var code = 'arr '+ value_name + '[' + text_exp + '] : bool;\n';
  return code;
};

Blockly.JavaScript['assignment'] = function(block) {
  var text_name = block.getFieldValue('NAME');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  if(!value_name) {
    value_name = '0';
  }
  if(value_name.indexOf("(") > -1) {
    value_name = value_name.substring(1,value_name.length-1);
  }
  var code = text_name + ' = ' + value_name + ';\n';
  return code;
};


Blockly.JavaScript['assignment_arr'] = function(block) {
  var text_name = block.getFieldValue('NAME');
  var text_exp = block.getFieldValue('EXP');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  var code = text_name + ' [ ' + text_exp + ' ] = ' + value_name + ';\n';
  return code;
};

Blockly.JavaScript['var'] = function(block) {
  var text_var = block.getFieldValue('VAR');
  var code = text_var;
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['var_coma'] = function(block) {
  var text_var = block.getFieldValue('VAR');
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  value_name = value_name.substring(1,value_name.length-1);
  var code = text_var + ', ' + value_name;
  return [code, Blockly.JavaScript.ORDER_NONE];
};
