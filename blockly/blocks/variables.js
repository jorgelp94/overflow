'use strict';
goog.provide('Blockly.Blocks.variables');
goog.require('Blockly.Blocks');

Blockly.Blocks['int_variable'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck("Number")
        .appendField("int")
        .appendField(new Blockly.FieldTextInput("name"), "VAR");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['float_variable'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck("Number")
        .appendField("float")
        .appendField(new Blockly.FieldTextInput("name"), "VAR");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['bool_variable'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck("Boolean")
        .appendField("bool")
        .appendField(new Blockly.FieldTextInput("name"), "VAR");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['char_variable'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck("String")
        .appendField("char")
        .appendField(new Blockly.FieldTextInput("name"), "VAR");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['string_variable'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck("String")
        .appendField("string")
        .appendField(new Blockly.FieldTextInput("name"), "VAR");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['variable'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField(new Blockly.FieldTextInput("var"), "NAME")
        .appendField(" =");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['var'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput("var"), "VAR");
    this.setOutput(true);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['var_coma'] = {
  init: function() {
    this.appendValueInput("NAME")
        .appendField(new Blockly.FieldTextInput("var"), "VAR");
    this.setOutput(true);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};
