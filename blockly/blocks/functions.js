'use strict';

goog.provide('Blockly.Blocks.functions');
goog.require('Blockly.Blocks');

Blockly.Blocks['function_statement'] = {
  init: function() {
    this.appendValueInput("NAME")
        .appendField(new Blockly.FieldDropdown([["int", "int"], ["float", "float"], ["bool", "bool"], ["char", "char"], ["string", "string"], ["void", "void"]]), "TYPE")
        .appendField("function name:")
        .appendField(new Blockly.FieldTextInput("name"), "VAR");
    this.appendStatementInput("BLOCK");
    this.setColour(210);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['function_param'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput("name"), "VAR")
        .appendField(new Blockly.FieldDropdown([["int", "int"], ["float", "float"], ["bool", "bool"], ["char", "char"], ["string", "string"]]), "TYPE");
    this.setOutput(true);
    this.setColour(210);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['function_param_coma'] = {
  init: function() {
    this.appendValueInput("NAME")
        .appendField(new Blockly.FieldTextInput("name"), "VAR")
        .appendField(new Blockly.FieldDropdown([["int", "int"], ["float", "float"], ["bool", "bool"], ["char", "char"], ["string", "string"]]), "TYPE");
    this.setOutput(true);
    this.setColour(210);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['function_call'] = {
  init: function() {
    this.appendValueInput("NAME")
        .appendField("call function")
        .appendField(new Blockly.FieldTextInput("name"), "FNAME");
    this.setOutput(true);
    this.setColour(210);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};
