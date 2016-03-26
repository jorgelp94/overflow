'use strict';

goog.provide('Blockly.Blocks.program');
goog.require('Blockly.Blocks');

Blockly.Blocks['program'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Program")
        .appendField(new Blockly.FieldTextInput("id"), "ID");
    this.setNextStatement(true);
    this.setColour(60);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['main'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Main");
    this.appendStatementInput("NAME");
    this.setPreviousStatement(true);
    this.setColour(60);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};
