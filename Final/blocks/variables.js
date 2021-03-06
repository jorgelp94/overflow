'use strict';
goog.provide('Blockly.Blocks.variables');
goog.require('Blockly.Blocks');

Blockly.Blocks['int_variable'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck("Number")
        .appendField("int")
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
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['int_arr_variable'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck("Number")
        .appendField("int")
        .appendField("[")
        .appendField(new Blockly.FieldTextInput("default"), "EXP")
        .appendField("] =");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['float_arr_variable'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck("Number")
        .appendField("float")
        .appendField("[")
        .appendField(new Blockly.FieldTextInput("default"), "EXP")
        .appendField("] =");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['bool_arr_variable'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck("Number")
        .appendField("bool")
        .appendField("[")
        .appendField(new Blockly.FieldTextInput("default"), "EXP")
        .appendField("] =");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['char_arr_variable'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck("Number")
        .appendField("char")
        .appendField("[")
        .appendField(new Blockly.FieldTextInput("default"), "EXP")
        .appendField("] =");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['assignment'] = {
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

Blockly.Blocks['assignment_arr'] = {
  init: function() {
    this.appendValueInput("NAME")
        .appendField("var")
        .appendField(new Blockly.FieldTextInput("default"), "NAME")
        .appendField("[")
        .appendField(new Blockly.FieldTextInput("default"), "EXP")
        .appendField("] =");
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
        .appendField(new Blockly.FieldTextInput("name"), "VAR");
    this.setOutput(true);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['var_coma'] = {
  init: function() {
    this.appendValueInput("NAME")
        .appendField(new Blockly.FieldTextInput("name"), "VAR");
    this.setOutput(true);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};
