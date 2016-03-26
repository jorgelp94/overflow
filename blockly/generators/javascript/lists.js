'use strict';

goog.provide('Blockly.JavaScript.lists');
goog.require('Blockly.JavaScript');

Blockly.JavaScript['lists_create_empty'] = function(block) {
  // Create an empty list.
  return ['[]', Blockly.JavaScript.ORDER_ATOMIC];
};

Blockly.JavaScript['lists_create_with'] = function(block) {
  // Create a list with any number of elements of any type.
  var code = new Array(block.itemCount_);
  for (var n = 0; n < block.itemCount_; n++) {
    code[n] = Blockly.JavaScript.valueToCode(block, 'ADD' + n,
        Blockly.JavaScript.ORDER_COMMA) || '0';
  }
  code = '[' + code.join(', ') + ']';
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};
